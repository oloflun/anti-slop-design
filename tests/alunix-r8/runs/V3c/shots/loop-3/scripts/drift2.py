"""drift2.py: ground-drift variants sampled on MID-TONE ground pixels (the wood panel and
the desk), not only the near-black margin. `color` blending moves chroma in proportion
to luminance, so a 12-step floor on a L=20 pixel forces a wash on the L=80 wood.
Points at 1440x900, thesis centred (scrollY 2961): left column above the thesis panel,
the gutter and the right margin, all raw ground. Fold: right of the card (wood)."""
import json, sys, io
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUTD = Path(sys.argv[1]); OUTD.mkdir(parents=True, exist_ok=True)
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
V = {n: f".ground::after{{background:color-mix(in srgb,var(--sc-canvas) {n}%,transparent)!important;mix-blend-mode:color!important;}}" for n in (44, 30, 24, 18)}
V["0"] = ".ground::after{display:none!important;}"
PTS_THESIS = [(300,180),(720,180),(1000,180),(1420,850),(1300,100)]
PTS_FOLD = [(1300,700),(1420,850),(1200,450)]
def ch(p): return max(p)-min(p)
res = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME)
    for name, css in V.items():
        ctx = b.new_context(viewport={"width":1440,"height":900}, reduced_motion="reduce")
        pg = ctx.new_page(); pg.goto(URL, wait_until="load"); pg.wait_for_timeout(1500)
        pg.add_style_tag(content=css); pg.wait_for_timeout(300)
        yT = pg.evaluate("() => { const t = document.querySelector('.panel-thesis').getBoundingClientRect(); return Math.round(t.top + scrollY + t.height/2 - innerHeight/2); }")
        yG = pg.evaluate("() => { const g = document.querySelector('.panel-giant').getBoundingClientRect(); return Math.round(g.top + scrollY - 200); }")
        r = {}
        for label, y, pts in (("fold", 0, PTS_FOLD), ("thesis", yT, PTS_THESIS), ("giant", yG, PTS_THESIS)):
            pg.evaluate("y => scrollTo(0,y)", y); pg.wait_for_timeout(700)
            img = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
            img.save(OUTD / f"d{name}-{label}.png")
            r[label] = {f"{x},{y_}": (img.getpixel((x,y_)), ch(img.getpixel((x,y_)))) for x,y_ in pts}
        res[name] = r
        print(name, json.dumps(r))
        ctx.close()
    b.close()
json.dump(res, open(OUTD/"drift2.json","w"), indent=1)
