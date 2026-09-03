"""A/B numbers harness: run the design + a11y probes against two sites and
diff the results as a markdown table. No visual judgement -- that's human.

    python run_ab.py <test-id> <A-dir|url> <B-dir|url> [--out tests/ab/<id>/]

A/B targets may each be a directory, a direct .html file, or an http(s) URL.
Directories/files are served locally with `python -m http.server`. Because
contrast.py is hardcoded to fetch http://localhost:3055/, a local target is
staged into a temp directory (a full copy, so relative assets keep working)
with the chosen page copied to index.html, then served at the root on that
exact port. Pre-hosted URL targets skip contrast.py (noted in numbers.md).
"""
import argparse
import json
import re
import shutil
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from collections import Counter
from pathlib import Path

# Windows consoles/pipes default child stdout to cp1252, which crashes any
# script (contrast.py, measure.py, ours) the moment it prints Unicode picked
# up from real page content (arrows, curly quotes, ...). Force UTF-8 for
# every subprocess we launch rather than editing scripts we don't own.
CHILD_ENV = dict(os.environ, PYTHONIOENCODING="utf-8")

SCRIPT_DIR = Path(__file__).resolve().parent
DESIGN = Path(r"C:\Users\Anton L\.agents\skills\design\scripts")
A11Y = Path(r"C:\Users\Anton L\OneDrive\Dokument\Obsidian\Knowledge Base\.agents\skills\a11y-audit\scripts")
PORT = 3055
PY = sys.executable


def is_url(s):
    return re.match(r"^https?://", s) is not None


def resolve_target(raw):
    if is_url(raw):
        return "url", raw
    p = Path(raw)
    if p.is_file():
        return "file", p
    if p.is_dir():
        return "dir", p
    raise RuntimeError(f"target not found: {raw}")


def find_index(d):
    top = d / "index.html"
    if top.is_file():
        return top
    matches = list(d.rglob("index.html"))
    if matches:
        return matches[0]
    raise RuntimeError(f"no index.html found under {d}")


def stage(root_dir, name):
    tmp = Path(tempfile.mkdtemp(prefix="a11y_ab_"))
    shutil.copytree(root_dir, tmp, dirs_exist_ok=True)
    if name != "index.html":
        shutil.copyfile(root_dir / name, tmp / "index.html")
    return tmp


def start_server(root, port):
    proc = subprocess.Popen(
        [PY, "-m", "http.server", str(port), "--bind", "127.0.0.1", "--directory", str(root)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=CHILD_ENV,
    )
    deadline = time.time() + 10
    while time.time() < deadline:
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/", timeout=1)
            return proc
        except Exception:
            time.sleep(0.2)
    proc.terminate()
    raise RuntimeError(f"http.server on port {port} did not become ready")


def prep(raw):
    """Returns (base_url, server_proc_or_None, staged_tmp_dir_or_None)."""
    mode, val = resolve_target(raw)
    if mode == "url":
        return val.rstrip("/") + "/", None, None
    root_dir, name = (val.parent, val.name) if mode == "file" else (find_index(val).parent, find_index(val).name)
    tmp = stage(root_dir, name)
    proc = start_server(tmp, PORT)
    return f"http://127.0.0.1:{PORT}/", proc, tmp


def run(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, encoding="utf-8", env=CHILD_ENV)
    if r.returncode != 0:
        sys.stderr.write(f"WARN failed: {' '.join(str(c) for c in cmd)}\n{r.stderr[-2000:]}\n")
    return r


def load_json(path, default):
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default


def run_side(label, raw_target, side_dir):
    side_dir.mkdir(parents=True, exist_ok=True)
    base_url, proc, tmp = prep(raw_target)
    try:
        run([PY, DESIGN / "shoot.py", side_dir, base_url])
        run([PY, DESIGN / "shoot_slices.py", side_dir, base_url, label])

        r = run([PY, DESIGN / "measure.py", base_url])
        try:
            measure_all = json.loads(r.stdout)
        except Exception:
            measure_all = {}
        (side_dir / "measure.json").write_text(json.dumps(measure_all, indent=2, ensure_ascii=False), encoding="utf-8")

        if proc is not None:
            r = run([PY, DESIGN / "contrast.py"])
            contrast_text = r.stdout
        else:
            contrast_text = "SKIPPED: contrast.py is hardcoded to http://localhost:3055/; target was a pre-hosted URL."
        (side_dir / "contrast.txt").write_text(contrast_text, encoding="utf-8")

        run([PY, A11Y / "a11y_scan.py", base_url, "--out", side_dir / "a11y.json"])
        run([PY, A11Y / "tab_walk.py", base_url, "--out", side_dir / "tabwalk.json"])
        run([PY, A11Y / "reflow.py", base_url, "--out", side_dir / "reflow.json"])
    finally:
        if proc is not None:
            proc.terminate()
            proc.wait(timeout=10)
        if tmp is not None:
            shutil.rmtree(tmp, ignore_errors=True)

    return {
        "measure": measure_all.get(base_url, {}),
        "contrast_text": contrast_text,
        "a11y": load_json(side_dir / "a11y.json", {"violations": [], "passes": 0, "incomplete": 0}),
        "tabwalk": load_json(side_dir / "tabwalk.json", {"stops": [], "issues": []}),
        "reflow": load_json(side_dir / "reflow.json", {"overflow320": [], "overflowZoom200": [], "hiddenUnderReducedMotion": 0}),
    }


def contrast_summary(text):
    m = re.search(r"(\d+) tokenbakgrunder, (\d+) under golvet", text or "")
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def build_numbers_md(test_id, a_raw, b_raw, a_res, b_res):
    L = [f"# A/B numbers: {test_id}", "", f"- A (baseline): `{a_raw}`", f"- B (with): `{b_raw}`", "",
         "No visual judgement here -- raw numbers only. Screenshots are in A-baseline/ and B-with/.", ""]

    L += ["## measure.py", "", "| metric | A | B |", "|---|---|---|"]
    for k in ["height", "textElements", "distinctFontSizes", "distinctTextColors", "distinctWeights",
              "hairlineRules", "distinctBackgrounds", "contentWidthUsed", "images"]:
        L.append(f"| {k} | {a_res['measure'].get(k, '-')} | {b_res['measure'].get(k, '-')} |")
    L.append("")

    a_tot, a_fail = contrast_summary(a_res["contrast_text"])
    b_tot, b_fail = contrast_summary(b_res["contrast_text"])
    L += ["## contrast.py", "", "| | A | B |", "|---|---|---|",
          f"| token backgrounds checked | {a_tot if a_tot is not None else 'n/a'} | {b_tot if b_tot is not None else 'n/a'} |",
          f"| below floor (fails) | {a_fail if a_fail is not None else 'n/a'} | {b_fail if b_fail is not None else 'n/a'} |", ""]

    a_imp = Counter(v.get("impact") or "unknown" for v in a_res["a11y"].get("violations", []))
    b_imp = Counter(v.get("impact") or "unknown" for v in b_res["a11y"].get("violations", []))
    L += ["## a11y_scan.py (axe-core violations by impact)", "", "| impact | A | B |", "|---|---|---|"]
    for imp in ["critical", "serious", "moderate", "minor", "unknown"]:
        if a_imp.get(imp) or b_imp.get(imp):
            L.append(f"| {imp} | {a_imp.get(imp, 0)} | {b_imp.get(imp, 0)} |")
    L.append(f"| **total** | **{len(a_res['a11y'].get('violations', []))}** | **{len(b_res['a11y'].get('violations', []))}** |")
    L.append("")

    L += ["## tab_walk.py", "", "| | A | B |", "|---|---|---|",
          f"| tab stops | {len(a_res['tabwalk'].get('stops', []))} | {len(b_res['tabwalk'].get('stops', []))} |",
          f"| issues | {len(a_res['tabwalk'].get('issues', []))} | {len(b_res['tabwalk'].get('issues', []))} |", ""]

    L += ["## reflow.py", "", "| | A | B |", "|---|---|---|",
          f"| overflow @320px | {len(a_res['reflow'].get('overflow320', []))} | {len(b_res['reflow'].get('overflow320', []))} |",
          f"| overflow @200% zoom | {len(a_res['reflow'].get('overflowZoom200', []))} | {len(b_res['reflow'].get('overflowZoom200', []))} |",
          f"| hidden under reduced motion | {a_res['reflow'].get('hiddenUnderReducedMotion', 0)} | {b_res['reflow'].get('hiddenUnderReducedMotion', 0)} |", ""]

    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("test_id")
    ap.add_argument("a_target")
    ap.add_argument("b_target")
    ap.add_argument("--out")
    args = ap.parse_args()

    out_root = Path(args.out) if args.out else SCRIPT_DIR / args.test_id
    out_root.mkdir(parents=True, exist_ok=True)

    a_res = run_side("A-baseline", args.a_target, out_root / "A-baseline")
    b_res = run_side("B-with", args.b_target, out_root / "B-with")

    md = build_numbers_md(args.test_id, args.a_target, args.b_target, a_res, b_res)
    numbers_path = out_root / "numbers.md"
    numbers_path.write_text(md, encoding="utf-8")
    print(str(numbers_path))


if __name__ == "__main__":
    main()
