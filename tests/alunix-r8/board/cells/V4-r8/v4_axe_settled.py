#!/usr/bin/env python3
"""axe on V4 after the intro has settled (a11y_scan waits only 500 ms after load, inside the
3.8 s intro fade). Same axe build and tags as a11y_scan.py. Also runs at 0.6 s as the control:
the fade-in state must reproduce the color-contrast hits, or this check proves nothing."""
import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path.home() / ".claude/skills/a11y-audit/scripts"))
import a11y_scan as A
axe = A.resolve_axe_path()
URL = "http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"
out = {}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    for W, H in [(1440, 900), (390, 844)]:
        for label, wait in [("mid-fade-3.1s", 3.1), ("settled-6s", 6.0)]:
            pg = b.new_page(viewport={"width": W, "height": H})
            pg.goto(URL, wait_until="load"); time.sleep(wait)
            pg.add_script_tag(path=axe)
            r = pg.evaluate(A.RUN_JS)
            out[f"{W}-{label}"] = [(v["id"], len(v["nodes"])) for v in r["violations"]]
            pg.close()
    b.close()
print(json.dumps(out, indent=1))
(Path(__file__).parent / "shots/a11y/axe-settled.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
