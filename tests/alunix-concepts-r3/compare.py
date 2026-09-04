# -*- coding: utf-8 -*-
"""Render build/index.html at 1440, measure column section boundaries (fractions of column
width) and stitch reference | build into compare.png. Usage: python compare.py [url]"""
import sys, numpy as np
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:3090/tests/alunix-concepts-r3/build/index.html"

with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1440, "height": 900})
    pg.goto(url, wait_until="networkidle"); pg.wait_for_timeout(1200)
    H = pg.evaluate("document.documentElement.scrollHeight")
    for y in range(0, H, 300):
        pg.evaluate(f"window.scrollTo(0,{y})"); pg.wait_for_timeout(120)
    pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(600)
    pg.screenshot(path=str(HERE / "build-full-1440.png"), full_page=True)
    b.close()

def boundaries(img, x0, x1, w, thr=30):
    a = np.asarray(img.convert("RGB")).astype(int)
    col = a[:, x0:x1].mean(axis=(1, 2)); out = []; last = -99
    for y in range(1, a.shape[0]):
        if abs(col[y] - col[y - 1]) > thr and y - last > 8:
            out.append(round(y / w, 3)); last = y
    return out

ref = Image.open(HERE / "reference-mosaic.png"); bld = Image.open(HERE / "build-full-1440.png")
wr, wb = ref.width / 2, bld.width / 2
print("build height in w:", round(bld.height / wb, 3), "(reference 2.69 target)")
print("REF  left :", boundaries(ref, 60, 540, wr));  print("BLD  left :", boundaries(bld, 70, 650, wb))
print("REF  right:", boundaries(ref, 623, 1183, wr)); print("BLD  right:", boundaries(bld, 790, 1370, wb))

# stitch at equal column width
scale = wr / wb
bs = bld.resize((int(bld.width * scale), int(bld.height * scale)))
h = max(ref.height, bs.height)
out = Image.new("RGB", (ref.width + bs.width + 24, h), (128, 128, 128))
out.paste(ref, (0, 0)); out.paste(bs, (ref.width + 24, 0))
out.save(HERE / "compare.png"); print("compare.png", out.size)
