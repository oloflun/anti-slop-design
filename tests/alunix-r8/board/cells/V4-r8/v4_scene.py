#!/usr/bin/env python3
"""Calyx scene in V4 at 1440: the closed state (both words together over the shut frame),
mid-part and open, by real wheel steps from just above the scene."""
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
O = Path(__file__).parent / "shots" / "scene"; O.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto("http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"); time.sleep(4.8)
    pg.evaluate("window.__v4.lenis.scrollTo(document.querySelector('#exempel'), {immediate:true, force:true, offset:-700})"); time.sleep(1.0)
    pg.mouse.move(1400, 450)
    for i in range(14):
        pg.mouse.wheel(0, 100); time.sleep(0.18)
        pg.screenshot(path=str(O / f"s{i:02d}.png"))
    b.close()
