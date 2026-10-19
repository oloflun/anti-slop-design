"""drift_diag.py: the ground drift at N % of --sc-canvas under mix-blend-mode:color.

For each variant, capture the band screen (scrollY where .panel-thesis is centred) and the
giant screen, and sample ground pixels: fold right margin (1420,850) at scrollY 0, the same
point at the thesis, the gutter behind the giant (720,450), and the lamp's light pool
(brightest ground pixel in a window). Variants override .ground::after via injected CSS.
"""
import json, sys, io
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

URL = "http://localhost:3090/tests/alunix-r8/runs/V3c/index.html"
OUTD = Path(sys.argv[1] if len(sys.argv) > 1 else "drift")
OUTD.mkdir(parents=True, exist_ok=True)
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"

VARIANTS = {
  "c44": ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 44%,transparent)!important;mix-blend-mode:color!important;}",
  "c30": ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 30%,transparent)!important;mix-blend-mode:color!important;}",
  "c22": ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 22%,transparent)!important;mix-blend-mode:color!important;}",
  "c16": ".ground::after{background:color-mix(in srgb,var(--sc-canvas) 16%,transparent)!important;mix-blend-mode:color!important;}",
  "c00": ".ground::after{display:none!important;}",
}

def px(img, x, y):
    return img.getpixel((x, y))[:3]

def brightest(img, x0, y0, x1, y1):
    best = (0, 0, 0); bl = -1
    for y in range(y0, y1, 4):
        for x in range(x0, x1, 4):
            p = img.getpixel((x, y))[:3]; l = sum(p)
            if l > bl: bl, best = l, p
    return best

def chroma(p): return max(p) - min(p)

res = {}
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME, headless=True)
    for name, css in VARIANTS.items():
        ctx = b.new_context(viewport={"width":1440,"height":900}, reduced_motion="reduce")
        page = ctx.new_page()
        page.goto(URL, wait_until="load"); page.wait_for_timeout(1500)
        page.add_style_tag(content=css)
        page.wait_for_timeout(300)
        ys = page.evaluate("""() => {
          const t = document.querySelector('.panel-thesis').getBoundingClientRect();
          const g = document.querySelector('.panel-giant').getBoundingClientRect();
          return {thesis: Math.round(t.top + scrollY + t.height/2 - innerHeight/2),
                  giant: Math.round(g.top + scrollY - 200)};
        }""")
        r = {}
        for label, y in (("fold", 0), ("thesis", ys["thesis"]), ("giant", ys["giant"])):
            page.evaluate("y => scrollTo(0,y)", y); page.wait_for_timeout(700)
            buf = page.screenshot(full_page=False)
            img = Image.open(io.BytesIO(buf)).convert("RGB")
            img.save(OUTD / f"{name}-{label}.png")
            r[label] = {"y": y, "margin_1420_850": px(img, 1420, 850),
                        "gutter_720_450": px(img, 720, 450),
                        "left_60_450": px(img, 20, 450),
                        "brightest_lamp": brightest(img, 0, 100, 740, 700)}
        # summary numbers
        f, t, g = r["fold"]["margin_1420_850"], r["thesis"]["margin_1420_850"], r["giant"]
        r["delta_fold_thesis_margin"] = max(abs(f[i]-t[i]) for i in range(3))
        r["chroma_thesis_margin"] = chroma(t)
        r["chroma_thesis_gutter"] = chroma(r["thesis"]["gutter_720_450"])
        r["chroma_thesis_lamp"] = chroma(r["thesis"]["brightest_lamp"])
        r["chroma_giant_gutter"] = chroma(g["gutter_720_450"])
        r["b_minus_r_thesis_lamp"] = r["thesis"]["brightest_lamp"][2] - r["thesis"]["brightest_lamp"][0]
        res[name] = r
        print(name, json.dumps({k: r[k] for k in r if not isinstance(r[k], dict)}),
              "fold", f, "thesis", t, "gutter", r["thesis"]["gutter_720_450"], "lamp", r["thesis"]["brightest_lamp"])
        ctx.close()
    b.close()
json.dump(res, open(OUTD / "drift_diag.json", "w"), indent=1)
