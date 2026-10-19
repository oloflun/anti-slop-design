#!/usr/bin/env python3
"""Tab to each iframe in V4 and screenshot it: is the focus ring visible?"""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
O = Path(__file__).parent / "shots" / "a11y"
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto("http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"); time.sleep(1.0)
    for i in range(1, 9):
        pg.keyboard.press("Tab"); time.sleep(0.9)
        info = pg.evaluate("""() => { const a=document.activeElement; const f=a.closest && a.closest('.frame');
          return {tag:a.tagName, title:a.title||a.textContent.trim().slice(0,30), ring: f ? getComputedStyle(f).outlineStyle+' '+getComputedStyle(f).outlineWidth+' '+f.className : getComputedStyle(a).outlineStyle} }""")
        print(i, info)
        if info["tag"] == "IFRAME":
            pg.screenshot(path=str(O / f"focus-{i}.png"))
    b.close()
