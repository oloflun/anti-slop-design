#!/usr/bin/env python3
"""a11y-audit's three scripts plus contrast.py: on the known-broken fixture first (CARL rule),
then on V4. Run through tests/alunix-r8/browser_lock.py so one browser runs at a time."""
import subprocess, sys
from pathlib import Path

HOME = Path.home()
S = HOME / ".claude/skills/a11y-audit/scripts"
C = HOME / ".claude/skills/design/scripts"
O = Path(__file__).parent / "shots" / "a11y"
O.mkdir(parents=True, exist_ok=True)
URLS = {"broken": "http://127.0.0.1:3308/tests/a11y/broken.html",
        "v4": "http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"}
JOBS = [("scan", [S / "a11y_scan.py"]), ("tab", [S / "tab_walk.py", "--max", "120"]),
        ("reflow", [S / "reflow.py"]), ("contrast", [C / "contrast.py"])]
for name, url in URLS.items():
    for job, cmd in JOBS:
        args = [sys.executable, str(cmd[0]), url] + [str(a) for a in cmd[1:]]
        r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
        (O / f"{name}-{job}.out").write_text(r.stdout, encoding="utf-8")
        (O / f"{name}-{job}.err").write_text(r.stderr, encoding="utf-8")
        print(name, job, "exit", r.returncode, "bytes", len(r.stdout))
