#!/usr/bin/env python3
"""extract_batch.py [--only slug,slug] [--flags "..."] [--timeout 300]

Runs designlang for every entries/<slug>/entry.md that has a live http(s) url and
`extract: none` (or `failed:`), writes into entries/<slug>/extract/, and rewrites the
frontmatter `extract:` line to `ok` or `failed: <last stderr line>`. Sequential on purpose:
one Chromium at a time keeps the machine usable while agents work.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
ENTRIES = ROOT / "design-catalogue" / "entries"
# ponytail: --full hung (responsive + deep-interact); --screenshots --interactions took 269s and
# 4.8MB per site for screenshots we already take with capture.py. Base extraction: 61s, 300K,
# and it still carries Motion Language / Component Anatomy / Brand Voice. Add
# `designlang replay <url>` per entry when a scroll clip is wanted.
DEFAULT_FLAGS = "--wait 2000 --ignore-widgets -q"


def fm_get(text, key):
    m = re.search(rf"^{key}:\s*(.*)$", text, re.M)
    return m.group(1).strip().strip('"') if m else ""


def fm_set(text, key, value):
    if re.search(rf"^{key}:", text, re.M):
        return re.sub(rf"^{key}:.*$", f"{key}: {value}", text, count=1, flags=re.M)
    return text.replace("\n---\n", f"\n{key}: {value}\n---\n", 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--flags", default=DEFAULT_FLAGS)
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--redo", action="store_true", help="also redo entries already marked ok")
    ap.add_argument("--workers", type=int, default=3, help="parallel Chromiums")
    a = ap.parse_args()
    only = {s.strip() for s in a.only.split(",") if s.strip()}

    jobs = []
    for d in sorted(ENTRIES.iterdir()):
        p = d / "entry.md"
        if not p.exists() or (only and d.name not in only):
            continue
        t = p.read_text(encoding="utf-8")
        url = fm_get(t, "url")
        if not url.startswith("http"):
            continue
        if fm_get(t, "extract") == "ok" and not a.redo:
            continue
        jobs.append((d, url))

    def run(job):
        d, url = job
        out = d / "extract"
        out.mkdir(exist_ok=True)
        cmd = ["designlang", url, *a.flags.split(), "-o", str(out)]
        print(f"[{d.name}] {url}", flush=True)
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=a.timeout, shell=(sys.platform == "win32"))
            if r.returncode == 0 and list(out.glob("*design-language.md")):
                new = "ok"
            else:
                last = (r.stderr.strip().splitlines() or r.stdout.strip().splitlines() or ["no output"])[-1][:160]
                new = f"failed: {last}"
        except subprocess.TimeoutExpired:
            new = f"failed: timeout {a.timeout}s"
        p = d / "entry.md"
        p.write_text(fm_set(p.read_text(encoding="utf-8"), "extract", new), encoding="utf-8")
        print(f"   [{d.name}] -> {new}", flush=True)
        return new == "ok"

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=max(1, a.workers)) as ex:
        results = list(ex.map(run, jobs))
    print(f"extract_batch: {len(results)} run, {sum(results)} ok")


if __name__ == "__main__":
    main()
