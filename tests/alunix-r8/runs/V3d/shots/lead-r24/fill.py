"""R24 Fel 2: halls .tes-plane pa accenten till tx 0,75?

Kontrollen mater RENDERADE pixlar, inte computed style (V2). Metod: element-
skarmbild av .tes-plane (tomt element - bara fyllning) och av .thesis-stage
(plat bla yta med text ovanpa - modalfargen ar fyllningen). Delta-E i oklab
mellan de tva modalerna.

Krav: dE <= 1 vid tx 0,10 / 0,40 / 0,70 pa 1920/1440/390.
      dE >= 12 mellan tx 0,70 och tx 1,0 (C8:s vandning).

--tx satts via scroll (--sc-ps), aldrig genom att skriva --tx direkt: det ar
sa akten faktiskt drivs, och sedan Fel 1:s registrering ar --tx ocksa lastbar.
"""
import asyncio, io, json, sys
import numpy as np
from PIL import Image
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
SIZES = [(1920, 930), (1440, 900), (390, 844)]

# M3: kontrollen maste bevisa sig mot en TRANSPARENT trasig variant forst.
# Det har ar ordagrant den gamla raden - --c-accent i stallet for
# --c-accent-band, alltsa den overskrivna token inifran #process.
BROKEN_CSS = """
.tes-plane{background:color-mix(in oklab,var(--c-accent),var(--c-drafting)
  calc(clamp(0,calc((var(--tx) - .75) / .25),1) * 100%)) !important;}
"""


def mode_rgb(png_bytes):
    """Vanligaste fargen i en PNG - den platta fyllningen, inte texten."""
    im = Image.open(io.BytesIO(png_bytes)).convert('RGB')
    a = np.asarray(im).reshape(-1, 3)
    # kvantisera latt sa att antialias-kanten inte splittrar modalen
    q = (a // 2) * 2
    uniq, counts = np.unique(q, axis=0, return_counts=True)
    win = uniq[counts.argmax()]
    # medelvardet av de pixlar som ligger i modal-bunken
    m = (np.abs(q.astype(int) - win.astype(int)).sum(axis=1) <= 2)
    return a[m].mean(axis=0)


def srgb_to_oklab(rgb):
    c = np.asarray(rgb, dtype=float) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = c
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = np.cbrt([l, m, s])
    return np.array([
        0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
        1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
        0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s,
    ])


def de(a, b):
    return float(np.linalg.norm(srgb_to_oklab(a) - srgb_to_oklab(b)))


async def stage_rgb(pg):
    """Tesbandets fyllning - referensen. #tes ligger ovanfor akten."""
    st = pg.locator('.thesis-stage')
    await st.scroll_into_view_if_needed()
    await pg.wait_for_timeout(400)
    return mode_rgb(await st.screenshot())


async def plane_at(pg, target_tx):
    """Skrolla tills --tx nar target_tx och las planets fyllning."""
    el = pg.locator('.process-chapter')
    box = await el.bounding_box()
    top = await el.evaluate("e => e.getBoundingClientRect().top + window.scrollY")
    height = await el.evaluate("e => e.offsetHeight")
    vh = await pg.evaluate("() => innerHeight")
    # grov gissning: tx ror sig over --tx-a..--tx-a+--tx-b i aktens liv
    for _ in range(26):
        tx = await pg.evaluate(
            "() => { const e=document.querySelector('.process-chapter');"
            " return parseFloat(getComputedStyle(e).getPropertyValue('--tx')); }")
        if tx is not None and not (tx != tx):
            if abs(tx - target_tx) <= 0.01:
                break
            # d/dy: tx vaxer med y; stega proportionellt men dampat
            y = await pg.evaluate("() => window.scrollY")
            step = int(np.clip((target_tx - tx) * (height + vh) * 0.6, -600, 600))
            await pg.mouse.wheel(0, step)
            await pg.wait_for_timeout(60)
        else:
            # tx ar NaN (trasigt lage) - fall tillbaka pa --sc-ps-formeln
            await pg.evaluate(
                "(y) => window.scrollTo(0, y)",
                int(top + (0.2258 + target_tx * 0.1613) * (height + vh) - vh))
            await pg.wait_for_timeout(120)
    await pg.wait_for_timeout(350)
    tx = await pg.evaluate(
        "() => { const e=document.querySelector('.process-chapter');"
        " return parseFloat(getComputedStyle(e).getPropertyValue('--tx')); }")
    png = await pg.locator('.tes-plane').screenshot()
    return tx, mode_rgb(png)


async def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else "now"
    inject = '--inject-broken' in sys.argv
    out = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for (w, h) in SIZES:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(URL)
            await pg.wait_for_timeout(2500)
            if inject:
                await pg.add_style_tag(content=BROKEN_CSS)
                await pg.wait_for_timeout(300)
            await pg.mouse.move(w // 2, h // 2)
            ref = await stage_rgb(pg)
            row = {'stage': [round(float(x), 1) for x in ref], 'tx': {}}
            for t in (0.10, 0.40, 0.70, 1.00):
                tx, rgb = await plane_at(pg, t)
                row['tx'][t] = {
                    'tx': None if tx != tx else round(tx, 3),
                    'rgb': [round(float(x), 1) for x in rgb],
                    'dE_vs_stage': round(de(rgb, ref), 2),
                }
            row['dE_070_100'] = round(
                de(np.array(row['tx'][0.70]['rgb']), np.array(row['tx'][1.00]['rgb'])), 2)
            out[f"{w}x{h}"] = row
            await pg.close()
        await b.close()

    for k, r in out.items():
        print(f"=== {k} ===  tesband rgb{tuple(r['stage'])}")
        for t in (0.10, 0.40, 0.70, 1.00):
            d = r['tx'][t]
            mark = ''
            if t < 1.0:
                mark = ' OK' if d['dE_vs_stage'] <= 1 else '  <-- OVER 1'
            print(f"  tx~{t:<4} (last {d['tx']})  rgb{tuple(d['rgb'])}  "
                  f"dE mot bandet = {d['dE_vs_stage']}{mark}")
        print(f"  dE tx0,70 -> tx1,00 = {r['dE_070_100']}"
              f"{' OK' if r['dE_070_100'] >= 12 else '  <-- UNDER 12'}")
    print(f"\n  lage: {'INJICERAT TRASIG (--c-accent)' if inject else 'byggt lage (--c-accent-band)'}")
    open(f"fill-{tag}.json", 'w').write(json.dumps(out, indent=1))


asyncio.run(main())
