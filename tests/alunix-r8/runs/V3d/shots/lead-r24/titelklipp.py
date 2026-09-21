"""R24 Fel 5.3: klipps rubrikens glyfer av background-clip:text?

Kontrollen ar en PIXELDIFFERENTIAL, inte en bounding box. Bounding-box-vagen
har tva fallgropar som jag gick i bada:
  - ar fonstret precis sa stort som overhanget mattar bada lagena samma tal
    (forsta korningen: pad 56 = overhang 56, "OK" pa ett klipp som syns);
  - vidgas fonstret fastnar masken pa stämpelrutans kant och pa stycket
    under rubriken i stallet.

Metod: samma element, samma fonster, samma skrollage, tva injektioner som
BADA ger rent roda glyfer men bara den ena gar genom klippet.
  KLIPP  background-image:linear-gradient(#ff0000,#ff0000)  (clip:text kvar)
  OKLIPPT background-image:none + -webkit-text-fill-color:#ff0000
Antalet pixlar som ar roda i OKLIPPT men inte i KLIPP ar exakt det antal
pixlar klippet at. Noll = ingen kladd. Bilderna sparas sa att jag kan se
dem, inte bara lita pa talet.

Kor:  python titelklipp.py <tag> [--only=WxH] [--inject-broken]
"""
import asyncio, io, json, sys
import numpy as np
from PIL import Image
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
SIZES = [(1920, 930), (1440, 900), (390, 844)]

RED_CLIP = """
.process-title,.process-step-title{
  background-image:linear-gradient(#ff0000,#ff0000) !important;}
"""
RED_PLAIN = """
.process-title,.process-step-title{
  background-image:none !important;
  -webkit-text-fill-color:#ff0000 !important;
  color:#ff0000 !important;}
"""
BROKEN = """
@media (min-width:768px){
  .process-title,.process-step-title{
    padding-block:0 !important; margin-block:0 !important;}}
"""


async def redmask(pg, rect, pad=130):
    vw = await pg.evaluate("() => innerWidth")
    vh = await pg.evaluate("() => innerHeight")
    x = max(0, rect['x'] - pad)
    top = max(0, rect['y'] - pad)
    w = min(vw - x, rect['w'] + 2 * pad)
    h = min(vh - top, rect['h'] + 2 * pad)
    if w <= 2 or h <= 2:
        return None, None
    clip = {'x': x, 'y': top, 'width': w, 'height': h}
    png = await pg.screenshot(clip=clip)
    im = Image.open(io.BytesIO(png)).convert('RGB')
    a = np.frombuffer(im.tobytes(), dtype=np.uint8).reshape(
        im.height, im.width, 3).astype(np.int16)
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    return (r > 140) & (g < 90) & (b < 90), png


async def place(pg, sel, idx):
    """Skrolla sa elementet star i bild, returnera dess viewport-rektangel."""
    return await pg.evaluate(
        """([s, i]) => { const els = document.querySelectorAll(s);
             const e = els[i]; if (!e) return null;
             const b = e.getBoundingClientRect();
             return {x: b.left, y: b.top, w: b.width, h: b.height,
                     txt: e.textContent.trim().slice(0, 24)}; }""", [sel, idx])


async def wheel_to(pg, y):
    cur = await pg.evaluate("() => scrollY")
    step = 80 if y > cur else -80
    while (step > 0 and cur < y) or (step < 0 and cur > y):
        d = min(abs(step), abs(y - cur))
        await pg.mouse.wheel(0, d * (1 if step > 0 else -1))
        cur += d * (1 if step > 0 else -1)


async def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "now"
    inject = '--inject-broken' in sys.argv
    only = [s for s in sys.argv if s.startswith('--only=')]
    sizes = SIZES
    if only:
        want = only[0].split('=', 1)[1]
        sizes = [s for s in SIZES if f"{s[0]}x{s[1]}" == want]
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(
            ignore_default_args=['--hide-scrollbars'],
            args=['--disable-dev-shm-usage', '--disable-gpu',
                  '--disable-extensions', '--disable-background-networking',
                  '--js-flags=--max-old-space-size=192'])
        for (w, h) in sizes:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(URL)
            await pg.wait_for_timeout(2500)
            await pg.mouse.move(w // 2, h // 2)
            if inject:
                await pg.add_style_tag(content=BROKEN)
                await pg.wait_for_timeout(300)

            targets = [('.process-title', 0, 'kapitel')]
            n = await pg.evaluate(
                "() => document.querySelectorAll('.process-step-title').length")
            for i in range(n):
                targets.append(('.process-step-title', i, f'steg{i+1:02d}'))

            rows = []
            anchor = await pg.evaluate(
                """() => [...document.querySelectorAll('.process-steps li')]
                     .map(li => Math.round(li.getBoundingClientRect().top + scrollY))""")
            chapy = await pg.evaluate(
                """() => { const e = document.querySelector('.chapter-stamp');
                     return Math.round(e.getBoundingClientRect().top + scrollY - 120); }""")

            for sel, idx, name in targets:
                y = chapy if name == 'kapitel' else anchor[idx]
                await wheel_to(pg, y)
                await pg.wait_for_timeout(450)
                hc = await pg.add_style_tag(content=RED_CLIP)
                await pg.wait_for_timeout(350)
                rect = await place(pg, sel, idx)
                if rect is None or rect['w'] < 2:
                    await pg.evaluate("el => el.remove()", hc)
                    rows.append({'name': name, 'skip': True})
                    continue
                mc, png_c = await redmask(pg, rect)
                await pg.evaluate("el => el.remove()", hc)
                hp = await pg.add_style_tag(content=RED_PLAIN)
                await pg.wait_for_timeout(350)
                mp, png_p = await redmask(pg, rect)
                await pg.evaluate("el => el.remove()", hp)
                if mc is None or mp is None:
                    rows.append({'name': name, 'skip': True})
                    continue
                lost = int((mp & ~mc).sum())
                gained = int((mc & ~mp).sum())
                # var sitter de forlorade pixlarna? overst eller nederst?
                ys = np.where((mp & ~mc).any(axis=1))[0]
                ys2 = np.where(mc.any(axis=1))[0]
                rows.append({
                    'name': name, 'text': rect['txt'],
                    'clip_px': int(mc.sum()), 'plain_px': int(mp.sum()),
                    'lost_px': lost, 'gained_px': gained,
                    'clip_rows': [int(ys2.min()), int(ys2.max())] if len(ys2) else None,
                    'lost_rows': [int(ys.min()), int(ys.max())] if len(ys) else None,
                })
                open(f"titelklipp-{tag}-{w}-{name}-klippt.png", 'wb').write(png_c)
                open(f"titelklipp-{tag}-{w}-{name}-oklippt.png", 'wb').write(png_p)
            out[f"{w}x{h}"] = rows
            await pg.close()
        await b.close()

    for k, rows in out.items():
        print(f"=== {k} ===")
        for r in rows:
            if r.get('skip'):
                print(f"  {r['name']:<9} hoppad")
                continue
            status = 'OK' if r['lost_px'] == 0 else f"KLIPPT {r['lost_px']}px"
            print(f"  {r['name']:<9} {r['text']:<22} "
                  f"klippt {r['clip_px']:>6}  oklippt {r['plain_px']:>6}  "
                  f"forlorat {r['lost_px']:>6}  vunnet {r['gained_px']:>5}  {status}")
            if r['lost_px']:
                print(f"            klippets rader {r['clip_rows']}, "
                      f"forlorade rader {r['lost_rows']}")
    print(f"\n  lage: {'INJICERAT TRASIG' if inject else 'byggt lage'}")
    fn = f"titelklipp-{tag}.json"
    try:
        prev = json.load(open(fn))
    except Exception:
        prev = {}
    prev.update(out)
    open(fn, 'w').write(json.dumps(prev, indent=1))


asyncio.run(main())
