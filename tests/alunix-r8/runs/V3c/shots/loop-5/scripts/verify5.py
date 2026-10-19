"""verify_astra4.py <out-dir>: Astra loop-4 fix 2 (Calyx reveal is a no-op) and fix 3 (drift
handoff jumps at thesis raw = 1). 1440x900, frames mounted and awake."""
import json, sys, io
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
URL = "http://127.0.0.1:3301/tests/alunix-r8/runs/V3c/index.html"
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
res = {}
def ch(p): return max(p) - min(p)
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(1500)
    # --- fix 3: drift handoff. Sample the wood pixel (720,180 is behind the band here; use the
    # right margin ground strip x=1420 and the gutter x=720 at y=100) across scrollY 3400..3800.
    pg.evaluate("document.querySelectorAll('iframe[data-src]').forEach(f => { if (!f.src) f.src = f.getAttribute('data-src'); })"); pg.wait_for_timeout(3000)
    drift = []
    for y in (3400, 3500, 3580, 3600, 3620, 3700, 3800, 4000):
        pg.evaluate("y => scrollTo(0, y)", y); pg.wait_for_timeout(600)
        canvas = pg.evaluate("getComputedStyle(document.querySelector('.ground')).getPropertyValue('--sc-canvas')")
        img = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
        px = {f"{x},{yy}": (img.getpixel((x, yy)), ch(img.getpixel((x, yy)))) for x, yy in ((1420, 850), (720, 40), (1420, 400))}
        drift.append({"scrollY": y, "canvas": canvas, "px": px})
        print(y, canvas, px)
        if y in (3580, 3620): img.save(OUT / f"drift-{y}.png")
    res["drift"] = drift
    # --- fix 2: Calyx reveal. Put the wrapper fully in view, force --rv, screenshot the wrapper.
    top = pg.evaluate("document.querySelector('.calyx-wrap').getBoundingClientRect().top + scrollY")
    pg.evaluate("y => scrollTo(0, y)", top - 40); pg.wait_for_timeout(2500)
    cal = []
    for rv in ("0", "0.25", "0.5", "1"):
        pg.evaluate("v => document.querySelector('.calyx-wrap').style.setProperty('--rv', v)", rv); pg.wait_for_timeout(400)
        box = pg.evaluate("""() => { const w = document.querySelector('.calyx-wrap').getBoundingClientRect(); const r = document.querySelector('.calyx-wrap .rv').getBoundingClientRect(); const f = document.querySelector('.calyx-wrap iframe').getBoundingClientRect();
          return {wrap: [Math.round(w.top), Math.round(w.height)], rv: [Math.round(r.top), Math.round(r.height)], iframe: [Math.round(f.top), Math.round(f.height)], rvOverflow: getComputedStyle(document.querySelector('.calyx-wrap .rv')).overflow}; }""")
        img = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
        crop = img.crop((40, 40, 691, 40 + min(810, 860)))
        crop.save(OUT / f"calyx-rv{rv}.png")
        # how much of the wrapper area is non-background (not the wrapper's own #e9e5da)?
        data = list(crop.getdata()); n = len(data)
        bg = sum(1 for p in data if abs(p[0] - 233) < 6 and abs(p[1] - 229) < 6 and abs(p[2] - 218) < 6)
        cal.append({"rv": rv, "box": box, "bgFraction": round(bg / n, 3)})
        print("calyx", rv, box, "bg fraction", round(bg / n, 3))
    res["calyx"] = cal
    # Horai for comparison
    top = pg.evaluate("document.querySelector('.horai-wrap').getBoundingClientRect().top + scrollY")
    pg.evaluate("y => scrollTo(0, y)", top - 40); pg.wait_for_timeout(2500)
    hor = []
    for rv in ("0", "0.5", "1"):
        pg.evaluate("v => document.querySelector('.horai-wrap').style.setProperty('--rv', v)", rv); pg.wait_for_timeout(400)
        img = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
        crop = img.crop((749, 40, 1400, 860)); crop.save(OUT / f"horai-rv{rv}.png")
        data = list(crop.getdata()); n = len(data)
        dark = sum(1 for p in data if p[0] < 30 and p[1] < 30 and p[2] < 30)
        hor.append({"rv": rv, "darkFraction": round(dark / n, 3)}); print("horai", rv, "dark fraction", round(dark / n, 3))
    res["horai"] = hor
    b.close()
json.dump(res, open(OUT / "verify_astra4.json", "w"), indent=1)
