"""R6 lead fix: re-crop horai-3 (quote, all three lines) and horai-4 (menu I whole,
fixed site header hidden). Crop = element box in viewport + margin, GROWN to the
detail cell's aspect (1.4058), never shrunk. Dither via V3f dither_variant."""
import sys, io
sys.path.insert(0, r"C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3f")
from dither import dither_variant, WHITE, BLACK
from PIL import Image
from playwright.sync_api import sync_playwright
OUT = r"C:/Users/Anton L/anti-slop-design/tests/alunix-r8/runs/V3g/assets/steps/"
ASPECT = 1.4058
def grow(x0, y0, x1, y1, m, W, H):
    x0 -= m; y0 -= m; x1 += m; y1 += m
    w, h = x1 - x0, y1 - y0
    if w / h < ASPECT: d = (h * ASPECT - w) / 2; x0 -= d; x1 += d
    else: d = (w / ASPECT - h) / 2; y0 -= d; y1 += d
    if x0 < 0: x1 -= x0; x0 = 0
    if y0 < 0: y1 -= y0; y0 = 0
    if x1 > W: x0 -= x1 - W; x1 = W
    if y1 > H: y0 -= y1 - H; y1 = H
    return max(0, x0), max(0, y0), x1, y1
def save(img, name):
    img = img.convert("RGB")
    img.resize((1200, round(1200 / ASPECT)), Image.LANCZOS).save(OUT + name + ".webp", "WEBP", quality=82)
    s = img.resize((900, round(900 / ASPECT)), Image.LANCZOS)
    dither_variant(s, WHITE, BLACK).save(OUT + name + "-dither.webp", "WEBP", lossless=True, quality=100, method=6)
with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    try:
        pg = b.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
        pg.set_default_timeout(15000)
        pg.goto("http://127.0.0.1:3307/sites/horai.html?preview=quote", wait_until="load")
        pg.add_style_tag(content="header.fixed{display:none!important}")
        pg.evaluate("document.getElementById('quote-text').scrollIntoView({block:'center'})")
        pg.wait_for_timeout(2500)
        r = pg.evaluate("(()=>{const q=document.getElementById('quote-text');const s=q.parentElement.getBoundingClientRect();const b=q.getBoundingClientRect();return [Math.min(b.left,s.left),Math.min(b.top,s.top),Math.max(b.right,s.right),Math.max(b.bottom,s.bottom)]})()")
        shot = Image.open(io.BytesIO(pg.screenshot()))
        # tighten to actual light pixels (text) inside the quote container
        box = [int(v * 2) for v in r]
        region = shot.crop(box).convert("L").point(lambda v: 255 if v > 120 else 0)
        bb = region.getbbox()
        x0, y0, x1, y1 = box[0] + bb[0], box[1] + bb[1], box[0] + bb[2], box[1] + bb[3]
        print("quote text bbox", x0, y0, x1, y1)
        save(shot.crop(tuple(round(v) for v in grow(x0, y0, x1, y1, 90, 2880, 1800))), "horai-3")
        pg.evaluate("document.querySelector('article').scrollIntoView({block:'start'})")
        pg.evaluate("window.scrollBy(0,-60)")
        pg.wait_for_timeout(1500)
        r = pg.evaluate("(()=>{const a=document.querySelector('article');const kids=[...a.querySelectorAll('div,h3,p')].map(e=>e.getBoundingClientRect()).filter(x=>x.width&&x.height);const rr=a.getBoundingClientRect();return [rr.left,rr.top,rr.right,Math.min(rr.bottom, Math.max(...kids.map(k=>k.bottom)))]})()")
        print("menu I rect", r)
        shot = Image.open(io.BytesIO(pg.screenshot()))
        save(shot.crop(tuple(round(v) for v in grow(*[v * 2 for v in r], 40, 2880, 1800))), "horai-4")
    finally:
        b.close()
