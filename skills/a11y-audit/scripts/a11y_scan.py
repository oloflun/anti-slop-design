"""axe-core accessibility scan at desktop + mobile viewports.

    python a11y_scan.py <url|file> [--out f]

Loads the page in Chromium, injects axe-core (resolved from the npm
package, installing a local cached copy under ./.deps if needed), runs
axe.run() at 1440x900 and 390x844, and merges the two result sets.

Exit 0 with findings in the JSON (findings are data, not failure).
Exit 2 only if the tool itself failed (browser/axe/navigation error).
"""
import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Windows consoles/pipes often default stdout/stderr to cp1252, which
# crashes on ordinary Unicode (arrows, curly quotes, etc.) picked up from
# scanned page content. Force UTF-8 so a print() never blows up mid-run.
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

SCRIPT_DIR = Path(__file__).resolve().parent
DEPS_DIR = SCRIPT_DIR / ".deps"
TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice"]
VIEWPORTS = [("1440x900", 1440, 900), ("390x844", 390, 844)]

RUN_JS = """async () => {
  return await axe.run(document, {runOnly: {type: 'tag', values: %s}});
}""" % json.dumps(TAGS)


def resolve_axe_path():
    cached = DEPS_DIR / "node_modules" / "axe-core" / "axe.min.js"
    if cached.is_file():
        return str(cached)
    try:
        cmd = subprocess.list2cmdline(
            ["node", "-e", "console.log(require.resolve('axe-core/axe.min.js'))"]
        )
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=15)
        if r.returncode == 0 and r.stdout.strip() and os.path.isfile(r.stdout.strip()):
            return r.stdout.strip()
    except Exception:
        pass
    DEPS_DIR.mkdir(parents=True, exist_ok=True)
    cmd = subprocess.list2cmdline(
        ["npm", "install", "--no-save", "axe-core", "--prefix", str(DEPS_DIR)]
    )
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=180)
    if r.returncode != 0:
        raise RuntimeError(f"npm install axe-core failed: {r.stderr.strip()}")
    if not cached.is_file():
        raise RuntimeError(f"axe-core install did not produce {cached}")
    return str(cached)


def to_url(arg):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://", arg):
        return arg
    return Path(arg).resolve().as_uri()


def target_str(target):
    return " ".join(target) if isinstance(target, list) else str(target)


def merge_results(per_viewport):
    merged = {}
    for vp_label, result in per_viewport:
        for v in result["violations"]:
            vid = v["id"]
            entry = merged.setdefault(vid, {
                "id": vid,
                "impact": v.get("impact"),
                "wcag": v.get("tags", []),
                "help": v.get("help"),
                "nodes": [],
                "viewports": [],
                "_seen": set(),
            })
            if vp_label not in entry["viewports"]:
                entry["viewports"].append(vp_label)
            for n in v["nodes"]:
                t = target_str(n.get("target"))
                if t in entry["_seen"]:
                    continue
                entry["_seen"].add(t)
                entry["nodes"].append({"target": t, "html": (n.get("html") or "")[:160]})
    violations = []
    for v in merged.values():
        del v["_seen"]
        violations.append(v)
    passed_ids = set()
    incomplete_ids = set()
    for _, result in per_viewport:
        passed_ids.update(r["id"] for r in result.get("passes", []))
        incomplete_ids.update(r["id"] for r in result.get("incomplete", []))
    return violations, len(passed_ids), len(incomplete_ids)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--out")
    args = ap.parse_args()

    try:
        url = to_url(args.target)
        axe_path = resolve_axe_path()
        per_viewport = []
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for label, w, h in VIEWPORTS:
                page = browser.new_page(viewport={"width": w, "height": h})
                page.goto(url, wait_until="networkidle", timeout=60000)
                page.wait_for_timeout(500)
                page.add_script_tag(path=axe_path)
                res = page.evaluate(RUN_JS)
                per_viewport.append((label, res))
                page.close()
            browser.close()
        violations, passes, incomplete = merge_results(per_viewport)
        out = {"url": url, "violations": violations, "passes": passes, "incomplete": incomplete}
    except Exception as e:
        sys.stderr.write(f"a11y_scan tool failure: {e}\n")
        sys.exit(2)

    text = json.dumps(out, indent=2, ensure_ascii=False)
    print(text)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    sys.exit(0)


if __name__ == "__main__":
    main()
