"""R24 Fel 5: processektionerna. Fyra matt, alla pa RENDERADE pixlar (V2).

1. Ordantal per steg, last ur renderad textContent (inte ur filen), och
   antal rader - en radbrytning over husets matt ar ett matt fel, och
   32px text i en 441px kolumn ger ~7 rader for en 33-ordig mening.

2. Avstand .ledger-num <-> .process-p. Siffran har line-height .8 och
   font-size 168px vid 1920: hennes BOX ar 134px hog, hennes BLECK ar
   ~168px. En bounding-box-matning ser darfor antingen en kollision som
   inte finns eller missar en som finns. Matt metod: siffran fargas rent
   rod, stycket rent bla, rubriken goms - da ar bleckgraderna tva
   separata masker och avstandet exakt aven om de overlappar.

3. Rubrikens underkant mot klippet. .js satter background-clip:text +
   color:transparent pa .process-title och .process-step-title.
   Background malas BARA inom paddingboxen, och line-height .95 ar
   kortare an glyfboxen - sa glyfens overhang (foljande 'g' i
   Planering/Lansering/Utveckling/Förvaltning, rundstavingarnas
   underkant i "lanserad sida") far ingen bakgrund och blir osynligt.
   Differential: samma sida tva ganger, en med -webkit-text-fill-color:
   currentColor + background-image:none (oklippt bleck). Skiljer
   underkanterna ar det klippet, och skillnaden ar antalet pixlar.

4. Rubrikens box mot sin container (kraver ingen injektion).

M3: --inject-broken lagger tillbaka den trasiga raden (padding-block:0)
sa kontrollen kan bevisa att den SER klippet innan den anvands pa lagt
lage. Byggt lage ar just nu det trasiga for punkt 3, sa den forsta
korningen ar den trasiga - differentialen ar beviset.
"""
import asyncio, json, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
SIZES = [(1920, 930), (1440, 900), (390, 844)]

MEASURE_CSS = """
.process-steps li .ledger-num{color:#ff0000 !important;}
.process-steps li .process-p{color:#0000ff !important;}
.process-steps li .process-step-title{visibility:hidden !important;}
"""
# Bara det aktuella bandet far vara malt. Vid 390 ar .step-band sticky pa
# top:var(--sheet-h) och FLERA band star samtidigt i bild - en granne med
# bla text hamnade i fonstret och gav gap = -100px dar det i sjalva verket
# ar 32. Samma skydd behovs vid 768-1023 och vid varje bredd dar ett släppt
# band overlappar ett fastnaglat.
# visibility:hidden pa hela li:t - layouten star kvar (--band-h mats
# oforandrat av measureAct), men inget av grannen kan hamna i fonstret.
ONLY_CSS = """
.process-steps li:not(.probe-on){visibility:hidden !important;}
"""
PLAIN_CSS = """
.process-title,.process-step-title{
  background-image:none !important;
  -webkit-text-fill-color:currentColor !important;
  color:var(--ink) !important;}
"""
BROKEN_CSS = """
@media (min-width:768px){
  .process-title,.process-step-title{
    padding-block:0 !important; margin-block:0 !important;}}
"""
# Klippet mats med FARGNYCKEL, inte med "allt som inte ar bakgrund". En
# sadan mask fastnar pa stämpelrutans kant och pa stycket under rubriken sa
# fort fonstret vidgas, och vidgas det inte sitter det exakt pa overhanget
# och mattar ingenting (forsta korningen: pad 56 = overhang 56, bada
# lagena lasta samma tal). Rent rott i bada lagena ar otvetydigt:
#   CLIP  - gradienten bytt mot en platt roda, background-clip:text star
#           kvar, alltsa exakt byggets klipp men en matbar farg.
#   PLAIN - ingen bakgrund alls, texten fylld med samma roda: oklippt bleck.
RED_CLIP_CSS = """
.process-title,.process-step-title{
  background-image:linear-gradient(#ff0000,#ff0000) !important;}
"""
RED_PLAIN_CSS = """
.process-title,.process-step-title{
  background-image:none !important;
  -webkit-text-fill-color:#ff0000 !important;
  color:#ff0000 !important;}
"""


ONLY_JS = """(i) => { document.querySelectorAll('.process-steps li')
  .forEach((el, k) => el.classList.toggle('probe-on', k === i)); }"""


def _arr(png):
    from PIL import Image
    import io
    im = Image.open(io.BytesIO(png)).convert('RGB')
    import numpy as np
    return np.frombuffer(im.tobytes(), dtype=np.uint8).reshape(
        im.height, im.width, 3).astype(np.int16), im.width, im.height


def _bbox(mask, x0, y0):
    import numpy as np
    if not mask.any():
        return None
    ys = np.where(mask.any(axis=1))[0]
    xs = np.where(mask.any(axis=0))[0]
    return {'top': y0 + int(ys.min()), 'bottom': y0 + int(ys.max()),
            'left': x0 + int(xs.min()), 'right': x0 + int(xs.max()),
            'h': int(ys.max() - ys.min() + 1)}


async def window_shot(pg, rect, pad=64):
    vw = await pg.evaluate("() => innerWidth")
    vh = await pg.evaluate("() => innerHeight")
    y = await pg.evaluate("() => window.scrollY")
    x = max(0, rect['x'] - pad)
    top = max(0, rect['y'] - pad)
    w = min(vw - x, rect['w'] + 2 * pad)
    h = min(vh - top, rect['h'] + 2 * pad)
    if w <= 2 or h <= 2:
        return None
    png = await pg.screenshot(clip={'x': x, 'y': top, 'width': w, 'height': h})
    a, _, _ = _arr(png)
    return a, int(x), int(top + y)


async def ink(pg, rect, pad=64):
    """Tataste bleckrektangel (allt som inte ar bakgrund) for ett element."""
    import numpy as np
    got = await window_shot(pg, rect, pad)
    if got is None:
        return None
    a, x0, y0 = got
    # .astype(int16): np.median ger float64, och int16 - float64 promoverar
    # hela bilden till float64 (6,3 MB for ett 370x749-fonster). Maskinen
    # ligger nara commit-taket och numpy vagsrar aven det.
    bg = np.median(a.reshape(-1, 3), axis=0).astype(np.int16)
    mask = np.abs(a - bg).sum(axis=2) > 60
    # kasta hairlines (stämpelrutans kant, .step-bands border) - de tacker
    # hela fonstret och skulle annars bli "rubrikens underkant".
    cov = mask.mean(axis=1)
    keep = cov <= 0.9
    if keep.any():
        mask = mask & keep[:, None]
    return _bbox(mask, x0, y0)


async def red_ink(pg, rect, pad=150):
    """Bleck matt som RENT ROTT i ett fylligt fonster - ingen hairline, inget
    grannstycke, bara rubrikens egen glyf."""
    import numpy as np
    got = await window_shot(pg, rect, pad)
    if got is None:
        return None
    a, x0, y0 = got
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    mask = (r > 140) & (g < 90) & (b < 90)
    return _bbox(mask, x0, y0)


async def colour_ink(pg, rect, pad=64):
    """Bleck i rent rodt och rent blatt, ur SAMMA fonster."""
    import numpy as np
    got = await window_shot(pg, rect, pad)
    if got is None:
        return None, None
    a, x0, y0 = got
    r, g, b = a[:, :, 0], a[:, :, 1], a[:, :, 2]
    red = (r > 150) & (g < 110) & (b < 110)
    blue = (b > 150) & (r < 110) & (g < 110)
    return _bbox(red, x0, y0), _bbox(blue, x0, y0)


async def scroll_to(pg, y, cur):
    step = 60 if y > cur else -60
    while (step > 0 and cur < y) or (step < 0 and cur > y):
        d = min(abs(step), abs(y - cur))
        await pg.mouse.wheel(0, d * (1 if step > 0 else -1))
        cur += d * (1 if step > 0 else -1)
    return cur


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
                  '--disable-features=Translate,BackForwardCache',
                  '--js-flags=--max-old-space-size=192'])
        for (w, h) in sizes:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(URL)
            await pg.wait_for_timeout(2500)
            await pg.mouse.move(w // 2, h // 2)

            # 1. ordantal och radbrytning, ur renderad text
            words = await pg.evaluate(
                "() => [...document.querySelectorAll('.process-p')]"
                ".map(e => e.textContent.trim().split(/\\s+/).length)")
            lines = await pg.evaluate(
                """() => [...document.querySelectorAll('.process-p')].map(e => {
                     const r = document.createRange(); r.selectNodeContents(e);
                     return new Set([...r.getClientRects()]
                       .filter(x => x.width > 1).map(x => Math.round(x.top))).size;
                   })""")
            colw = await pg.evaluate(
                """() => { const e=document.querySelector('.process-p');
                     const b=e.getBoundingClientRect();
                     return {col: Math.round(b.width),
                             fs: getComputedStyle(e).fontSize,
                             maxw: getComputedStyle(e).maxWidth}; }""")

            lis = await pg.evaluate(
                """() => [...document.querySelectorAll('.process-steps li')].map(li => {
                     const b = li.getBoundingClientRect();
                     return Math.round(b.top + window.scrollY); })""")

            # 2. avstand siffra <-> stycke, fargkodat
            h_meas = await pg.add_style_tag(content=MEASURE_CSS)
            h_only = await pg.add_style_tag(content=ONLY_CSS)
            await pg.wait_for_timeout(300)
            gaps = []
            cur = await pg.evaluate("() => window.scrollY")
            for i, liy in enumerate(lis):
                await pg.evaluate(ONLY_JS, i)
                cur = await scroll_to(pg, liy, cur)
                await pg.wait_for_timeout(320)
                box = await pg.evaluate(
                    """(i) => { const li=document.querySelectorAll('.process-steps li')[i];
                         const n=li.querySelector('.ledger-num'), q=li.querySelector('.process-p');
                         const a=n.getBoundingClientRect(), c=q.getBoundingClientRect();
                         const sy = window.scrollY;
                         return {x:Math.min(a.left,c.left), y:Math.min(a.top,c.top),
                                 r:Math.max(a.right,c.right), b:Math.max(a.bottom,c.bottom),
                                 nbox:[Math.round(a.top+sy), Math.round(a.bottom+sy)],
                                 qbox:[Math.round(c.top+sy), Math.round(c.bottom+sy)],
                                 nfs:getComputedStyle(n).fontSize,
                                 nlh:getComputedStyle(n).lineHeight}; }""", i)
                rect = {'x': box['x'], 'y': box['y'],
                        'w': box['r'] - box['x'], 'h': box['b'] - box['y']}
                nr, qb = await colour_ink(pg, rect)
                if not nr or not qb:
                    gaps.append({'i': i + 1, 'gap': None})
                    continue
                if qb['top'] >= nr['bottom']:
                    gp = qb['top'] - nr['bottom']
                elif qb['left'] >= nr['right']:
                    gp = qb['left'] - nr['right']
                else:
                    gp = -min(nr['bottom'] - qb['top'], nr['right'] - qb['left'])
                gaps.append({'i': i + 1, 'gap': int(gp), 'num': nr, 'p': qb,
                             'nbox': box['nbox'], 'qbox': box['qbox'],
                             'nfs': box['nfs'], 'nlh': box['nlh'],
                             'num_overhang': nr['bottom'] - box['nbox'][1]})
            await pg.evaluate("el => el.remove()", h_meas)
            await pg.wait_for_timeout(300)

            # 3. rubrikens underkant, klippt vs oklippt, per steg
            async def step_bottoms():
                res = []
                c2 = await pg.evaluate("() => window.scrollY")
                for i, liy in enumerate(lis):
                    await pg.evaluate(ONLY_JS, i)
                    c2 = await scroll_to(pg, liy, c2)
                    await pg.wait_for_timeout(300)
                    r = await pg.evaluate(
                        """(i) => { const e=document.querySelectorAll('.process-steps li')[i]
                                     .querySelector('.process-step-title');
                             if (!e) return null;
                             const b=e.getBoundingClientRect();
                             return {x:b.left,y:b.top,w:b.width,h:b.height,
                                     t:e.textContent,
                                     band_b: (() => { const k=e.closest('.step-band')
                                       .getBoundingClientRect(); return k.top + window.scrollY + k.height; })(),
                                     band_ovf: getComputedStyle(e.closest('.step-band')).overflow}; }""", i)
                    if not r or r['w'] < 2:
                        res.append(None)
                        continue
                    k = await red_ink(pg, r)
                    sy = await pg.evaluate("() => window.scrollY")
                    res.append({'text': r['t'],
                                'box_top': int(r['y'] + sy),
                                'box_bottom': int(r['y'] + r['h'] + sy),
                                'band_bottom': int(r['band_b']),
                                'band_overflow': r['band_ovf'],
                                'ink_top': k['top'] if k else None,
                                'ink_bottom': k['bottom'] if k else None})
                return res

            if inject:
                h_broken = await pg.add_style_tag(content=BROKEN_CSS)
                await pg.wait_for_timeout(300)
            h_clip = await pg.add_style_tag(content=RED_CLIP_CSS)
            await pg.wait_for_timeout(300)
            clipped = await step_bottoms()
            await pg.evaluate("el => el.remove()", h_clip)
            h_plain = await pg.add_style_tag(content=RED_PLAIN_CSS)
            await pg.wait_for_timeout(300)
            plain = await step_bottoms()
            await pg.evaluate("el => el.remove()", h_plain)
            if inject:
                await pg.evaluate("el => el.remove()", h_broken)
            await pg.evaluate("el => el.remove()", h_only)
            await pg.evaluate(
                "() => document.querySelectorAll('.process-steps li')"
                ".forEach(el => el.classList.remove('probe-on'))")
            await pg.wait_for_timeout(200)

            # kapitelrubriken, samma differential
            chapter = []
            c3 = await pg.evaluate("() => window.scrollY")
            chy = await pg.evaluate(
                """() => { const e=document.querySelector('.chapter-stamp');
                     return Math.round(e.getBoundingClientRect().top + window.scrollY - 200); }""")
            c3 = await scroll_to(pg, chy, c3)
            await pg.wait_for_timeout(400)

            async def chap_bottom():
                r = await pg.evaluate(
                    """() => { const e=document.querySelector('.process-title');
                         const b=e.getBoundingClientRect();
                         const s=e.closest('.chapter-stamp').getBoundingClientRect();
                         return {x:b.left,y:b.top,w:b.width,h:b.height,
                                 stamp_b: s.top + window.scrollY + s.height,
                                 stamp_ovf: getComputedStyle(e.closest('.chapter-stamp')).overflow,
                                 stamp_clip: getComputedStyle(e.closest('.chapter-stamp')).clipPath}; }""")
                k = await red_ink(pg, r)
                sy = await pg.evaluate("() => window.scrollY")
                return {'box_top': int(r['y'] + sy),
                        'box_bottom': int(r['y'] + r['h'] + sy),
                        'stamp_bottom': int(r['stamp_b']),
                        'stamp_overflow': r['stamp_ovf'],
                        'stamp_clip': r['stamp_clip'],
                        'ink_top': k['top'] if k else None,
                        'ink_bottom': k['bottom'] if k else None}

            h_clip2 = await pg.add_style_tag(content=RED_CLIP_CSS)
            await pg.wait_for_timeout(300)
            chapter.append(await chap_bottom())
            await pg.evaluate("el => el.remove()", h_clip2)
            h_plain2 = await pg.add_style_tag(content=RED_PLAIN_CSS)
            await pg.wait_for_timeout(400)
            chapter.append(await chap_bottom())
            await pg.evaluate("el => el.remove()", h_plain2)

            out[f"{w}x{h}"] = {'words': words, 'lines': lines, 'col': colw,
                               'gaps': gaps, 'steps': {'clipped': clipped,
                                                       'plain': plain},
                               'chapter': chapter, 'injected': inject}
            await pg.close()
        await b.close()

    for k, r in out.items():
        print(f"=== {k} ===   kolumn {r['col']['col']}px, "
              f"font {r['col']['fs']}, max-width {r['col']['maxw']}")
        print(f"  ordantal: {r['words']}   (krav 28-34)")
        bad = [(i + 1, n) for i, n in enumerate(r['words']) if not 28 <= n <= 34]
        print(f"  utanfor bandet: {bad or '-'}")
        print(f"  rader per stycke: {r['lines']}")
        print("  avstand siffra<->stycke (bleck mot bleck):")
        for g in r['gaps']:
            if g['gap'] is None:
                print(f"    {g['i']:02d}  ingen matning")
                continue
            mark = ' OK' if g['gap'] >= 16 else '  <-- UNDER 16'
            n, q = g['num'], g['p']
            # siffrans bleck skjuter ut nedanfor sin egen box (line-height .8)
            print(f"    {g['i']:02d}  gap={g['gap']:>5}px{mark}"
                  f"   siffran box {g['nbox'][0]}..{g['nbox'][1]}"
                  f" (font {g['nfs']}, lh {g['nlh']}), bleck till {n['bottom']}"
                  f" -> overhang {g['num_overhang']}px"
                  f";  stycket {q['top']}..")
        print("  stegrubrikerna:")
        for i, (c, pl) in enumerate(zip(r['steps']['clipped'], r['steps']['plain'])):
            if not c or not pl or c['ink_bottom'] is None:
                print(f"    {i+1:02d}  ingen matning")
                continue
            cut = c['ink_bottom'] - pl['ink_bottom']
            mark = ' OK' if cut == 0 else f'  <-- KLIPPT {cut}px'
            # oversta bleckraden: line-height .95 kan ocksa skara ascnedrarna
            topcut = c['ink_top'] - pl['ink_top']
            tmark = '' if topcut == 0 else f'  <-- KLIPPT I OVERKANT {topcut}px'
            out_of_band = c['ink_bottom'] - c['band_bottom']
            bmark = '' if out_of_band <= 0 else f'  <-- {out_of_band}px UNDER BANDET'
            print(f"    {i+1:02d} {c['text']:<12} box {c['box_top']}..{c['box_bottom']}"
                  f"  bleck {c['ink_top']}..{c['ink_bottom']}"
                  f"  bandets botten {c['band_bottom']} ({c['band_overflow']})"
                  f"{mark}{tmark}{bmark}")
        c0, c1 = r['chapter']
        print(f"  kapitelrubriken \"Från samtal till lanserad sida.\":")
        if c0['ink_bottom'] is None or c1['ink_bottom'] is None:
            print(f"    ingen bleckmatning (klippt {c0['ink_bottom']}, "
                  f"oklippt {c1['ink_bottom']}) - box {c0['box_top']}..{c0['box_bottom']}")
        else:
            cut = c0['ink_bottom'] - c1['ink_bottom']
            topcut = c0['ink_top'] - c1['ink_top']
            mark = ' OK' if cut == 0 else f'  <-- KLIPPT {cut}px'
            tmark = '' if topcut == 0 else f'  <-- KLIPPT I OVERKANT {topcut}px'
            print(f"    box {c0['box_top']}..{c0['box_bottom']}  "
                  f"bleck {c0['ink_top']}..{c0['ink_bottom']}{mark}{tmark}")
        print(f"    stämpelrutan slutar {c0['stamp_bottom']}, "
              f"overflow {c0['stamp_overflow']}, clip-path {c0['stamp_clip']}")
    print(f"\n  lage: {'INJICERAT TRASIG' if inject else 'byggt lage'}")
    fn = f"fel5-{tag}.json"
    try:
        prev = json.load(open(fn))
    except Exception:
        prev = {}
    prev.update(out)
    open(fn, 'w').write(json.dumps(prev, indent=1))


asyncio.run(main())
