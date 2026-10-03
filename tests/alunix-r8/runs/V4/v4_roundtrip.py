#!/usr/bin/env python3
"""F-027 owner check: wheel to the bottom, wheel back to the top, then measure every animated
property at scrollY 0 and compare with the values measured right after the intro.
M3: the same comparison runs on a deliberately broken state (axis x forced to 120px) and must flag."""
import json, time
from pathlib import Path
from playwright.sync_api import sync_playwright
O = Path(__file__).parent / "shots"
READ = r"""() => {
  const g = (s, p) => { const e = document.querySelector(s); return e ? getComputedStyle(e)[p] : null; };
  const tr = s => { const e = document.querySelector(s); return e ? new DOMMatrix(getComputedStyle(e).transform).m41.toFixed(1) + ',' + new DOMMatrix(getComputedStyle(e).transform).m42.toFixed(1) : null; };
  return { y: scrollY, axisX: tr('.hero-axis'), axisClip: g('.hero-axis','clipPath'), axisVis: g('.hero-axis','visibility'),
    sel: g('.hero-sel','clipPath'), tTop: tr('.t-top'), tBot: tr('.t-bot'), track: tr('.p-track'),
    flood: g('.p-flood','clipPath'), narrow: g('.narrow','clipPath'),
    rsel: [...document.querySelectorAll('.rsel')].map(e => new DOMMatrix(getComputedStyle(e).transform).a.toFixed(2)).join(' '),
    heroH: [...document.querySelectorAll('.hero-h .row')].map(e => Math.round(e.getBoundingClientRect().top)).join(' '),
    typed: [...document.querySelectorAll('.typed .ch')].filter(c => c.style.visibility === 'visible').length };
}"""
with sync_playwright() as p:
    b = p.chromium.launch(headless=True); pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto("http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"); time.sleep(4.8)
    before = pg.evaluate(READ)
    pg.mouse.move(1400, 450)
    for _ in range(320): pg.mouse.wheel(0, 120); time.sleep(0.03)
    time.sleep(2.5); bottom = pg.evaluate("scrollY")
    for _ in range(360): pg.mouse.wheel(0, -120); time.sleep(0.03)
    time.sleep(3.0)
    after = pg.evaluate(READ)
    pg.screenshot(path=str(O / "roundtrip-top.png"))
    pg.evaluate("document.querySelector('.hero-axis').style.translate = '120px 0'")
    broken = pg.evaluate(READ.replace("new DOMMatrix(getComputedStyle(e).transform).m41.toFixed(1)", "(new DOMMatrix(getComputedStyle(e).transform).m41 + (parseFloat(getComputedStyle(e).translate)||0)).toFixed(1)"))
    b.close()
diff = {k: (before[k], after[k]) for k in before if k != "y" and before[k] != after[k]}
bdiff = {k: (before[k], broken[k]) for k in before if k != "y" and before[k] != broken[k]}
res = {"bottomY": bottom, "before": before, "after": after, "diff": diff, "brokenDiff": bdiff}
(O / "roundtrip.json").write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
print(json.dumps({"bottomY": bottom, "diff": diff, "brokenDiff": bdiff}, indent=1, ensure_ascii=False))
