"""devices5.py <out.json>: H-24, the four BRIEF device-table tracks motion_probe.py cannot
read (it resolves a pure scale() through atan2(b, a) and falls back to translation, so it
calls them DEAD). Read the computed matrix / geometry directly at real scroll positions
instead and show the value moves. Devices: 7 .giant scale, 4 #threadFill (the ledger's
self-drawing thread), 2 #heroPoolImg (the light pool's translate3d), and the closing rule."""
import json, sys
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
READ = """() => {
  const g = s => document.querySelector(s);
  const m = s => { const e = g(s); return e ? getComputedStyle(e).transform : null; };
  const geo = s => { const e = g(s); if (!e) return null; const r = e.getBoundingClientRect();
    return [Math.round(r.width * 10) / 10, Math.round(r.height * 10) / 10]; };
  const rule = g('.close-rule');
  return {y: Math.round(scrollY),
    giant: m('.giant'), giantSize: geo('.giant'),
    thread: m('#threadFill'), threadGeo: geo('#threadFill'),
    threadSY: g('#threadFill') ? getComputedStyle(g('#threadFill')).scale : null,
    pool: m('#heroPoolImg'),
    closeRule: rule ? [getComputedStyle(rule).transform, getComputedStyle(rule).width, getComputedStyle(rule).scale] : null};
}"""
out = []
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(2000)
    pg.mouse.move(720, 450)
    for y in (0, 400, 900, 1500, 2400, 2900, 3200, 3500, 3800, 4100, 4400, 9000, 9300, 9600, 9682):
        pg.evaluate("y => scrollTo(0, y)", y)
        pg.wait_for_timeout(2200)
        r = pg.evaluate(READ); out.append(r); print(json.dumps(r))
    b.close()
json.dump(out, open(sys.argv[1], "w"), indent=1)
for key in ("giant", "thread", "threadGeo", "pool", "closeRule", "threadSY"):
    vals = {json.dumps(r[key]) for r in out if r.get(key) is not None}
    print(f"{key}: {len(vals)} distinct value(s) across {len(out)} positions -> {'ALIVE' if len(vals) > 1 else 'NO CHANGE'}")
