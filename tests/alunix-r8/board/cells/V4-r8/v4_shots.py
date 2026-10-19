#!/usr/bin/env python3
"""V4 capture: real wheel walk through the whole page, headless, one browser.

    python tests/alunix-r8/browser_lock.py -- python tests/alunix-r8/runs/V4/v4_shots.py WxH [step_px] [every_n]

Writes shots/walk-<W>/NNN.png every `every_n` wheel steps plus walk.json (console errors,
iframe loads, scrollY per frame, document height). Wheel = 100 px per event (Lenis x0.6),
250 ms apart so Lenis settles between captures.
"""
import json, sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3308/tests/alunix-r8/runs/V4/index.html"
size = sys.argv[1] if len(sys.argv) > 1 else "1440x900"
step = int(sys.argv[2]) if len(sys.argv) > 2 else 100
every = int(sys.argv[3]) if len(sys.argv) > 3 else 4
W, H = map(int, size.split("x"))
out = Path(__file__).parent / "shots" / f"walk-{W}"
out.mkdir(parents=True, exist_ok=True)
for f in out.glob("*.png"):
    f.unlink()

log = {"size": size, "errors": [], "frames": [], "requests": {}}
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    pg.on("console", lambda m: m.type in ("error", "warning") and log["errors"].append(f"{m.type}: {m.text}"))
    pg.on("pageerror", lambda e: log["errors"].append(f"pageerror: {e}"))
    def onreq(r):
        if "/sites/" in r.url and r.resource_type == "document":
            log["requests"][r.url] = log["requests"].get(r.url, 0) + 1
    pg.on("request", onreq)
    pg.goto(URL, wait_until="load")
    time.sleep(0.4)
    pg.screenshot(path=str(out / "intro-0.4s.png"))
    time.sleep(1.3)
    pg.screenshot(path=str(out / "intro-1.7s.png"))
    time.sleep(1.0)
    pg.screenshot(path=str(out / "intro-2.7s.png"))
    time.sleep(1.6)
    pg.mouse.move(W * 0.5, H * 0.5)
    i = 0
    last = -1
    stuck = 0
    while True:
        y = pg.evaluate("window.scrollY")
        if i % every == 0:
            pg.screenshot(path=str(out / f"{i:03d}.png"))
            log["frames"].append({"i": i, "y": round(y)})
        pg.mouse.wheel(0, step)
        time.sleep(0.25)
        i += 1
        ny = pg.evaluate("window.scrollY")
        stuck = stuck + 1 if abs(ny - last) < 1 else 0
        last = ny
        if stuck > 6 or i > 900:
            break
    time.sleep(1.2)
    pg.screenshot(path=str(out / "end.png"))
    log["docHeight"] = pg.evaluate("document.documentElement.scrollHeight")
    log["vh"] = H
    log["steps"] = i
    b.close()
(out / "walk.json").write_text(json.dumps(log, indent=1), encoding="utf-8")
print(json.dumps({k: log[k] for k in ("size", "errors", "requests", "docHeight", "steps")}, indent=1))
