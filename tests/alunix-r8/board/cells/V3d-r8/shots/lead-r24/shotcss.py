"""Samma bilder som shot.py men med en injicerad CSS-override, sa att
plattans roll kan bedomas utan att filen rors."""
import asyncio, sys, os
from playwright.async_api import async_playwright

URL = "http://localhost:3304/tests/alunix-r8/runs/V3d/index.html"
OUT = os.path.dirname(os.path.abspath(__file__))


async def read_cx(pg):
    return await pg.evaluate(
        """() => { const e = document.querySelector('.cases-chapter');
             const v = parseFloat(getComputedStyle(e).getPropertyValue('--cx'));
             return isNaN(v) ? null : v; }""")


async def scroll_until(pg, target_cx):
    vh = await pg.evaluate("() => innerHeight")
    top = await pg.evaluate(
        """() => { const e = document.querySelector('.cases-chapter');
             const r = e.getBoundingClientRect();
             return Math.round(r.top + scrollY); }""")
    best = (None, 1e9)
    for step in (48, 12, 3):
        lo = top - int(1.4 * vh) if best[0] is None else best[0] - 3 * step
        hi = top + int(0.7 * vh) if best[0] is None else best[0] + 3 * step
        for y in range(lo, hi + 1, step):
            await pg.evaluate("(y) => window.scrollTo(0, y)", y)
            await pg.wait_for_timeout(90)
            cx = await read_cx(pg)
            if cx is None:
                continue
            if abs(cx - target_cx) < best[1]:
                best = (y, abs(cx - target_cx))
        if best[1] <= 0.004:
            break
    if best[0] is not None:
        await pg.evaluate("(y) => window.scrollTo(0, y)", best[0])
        await pg.wait_for_timeout(120)
    return best[0]


async def main():
    w = int(sys.argv[1]); h = int(sys.argv[2])
    cxs = [float(x) for x in sys.argv[3].split(',')]
    tag = sys.argv[4]
    css = sys.argv[5] if len(sys.argv) > 5 else ''
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto(URL)
        await pg.wait_for_timeout(2200)
        if css:
            await pg.add_style_tag(content=css)
            await pg.wait_for_timeout(300)
        await pg.mouse.move(w // 2, h // 2)
        for target in cxs:
            await scroll_until(pg, target)
            await pg.wait_for_timeout(420)
            got = await pg.evaluate(
                """() => { const e = document.querySelector('.cases-chapter');
                     const v = parseFloat(getComputedStyle(e).getPropertyValue('--cx'));
                     return {cx: isNaN(v) ? null : v, y: Math.round(window.scrollY)}; }""")
            name = f"{tag}-{w}x{h}-cx{target:.2f}.png"
            await pg.screenshot(path=os.path.join(OUT, name))
            print(f"{name}  y={got['y']} cx={got['cx']}")
        await b.close()


asyncio.run(main())
