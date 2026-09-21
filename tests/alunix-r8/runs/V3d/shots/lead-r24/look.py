"""R24: titta pa sidan. Fullskarmsbild vid ett givet skrollage.

Domar skriptet gor inte - det ar min uppgift. Det har verktyget tar bilden.

  python look.py <namn> <bredd> <hojd> <mål> [--y=N] [--wheel=N] [--noscroll]

<mål> ar ett CSS-valjare (skrolla dit) eller 'y=<tal>' eller 'none'.
--wheel=N skickar N px hju l EFTER positioneringen, sa att akten drivs av
riktiga scroll-handelser och inte av scrollTo.
"""
import asyncio, sys
from playwright.async_api import async_playwright

URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"


async def main():
    name = sys.argv[1]
    w, h = int(sys.argv[2]), int(sys.argv[3])
    target = sys.argv[4]
    extra_wheel = 0
    plain = '--plain' in sys.argv
    crop = None
    for a in sys.argv[5:]:
        if a.startswith('--wheel='):
            extra_wheel = int(a.split('=')[1])
        if a.startswith('--crop='):
            crop = a.split('=', 1)[1]
    async with async_playwright() as p:
        b = await p.chromium.launch(
            ignore_default_args=['--hide-scrollbars'],
            args=['--disable-dev-shm-usage', '--disable-gpu',
                  '--disable-extensions', '--disable-background-networking',
                  '--js-flags=--max-old-space-size=192'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto(URL)
        await pg.wait_for_timeout(2500)
        await pg.mouse.move(w // 2, h // 2)
        if target.startswith('y='):
            y = int(target[2:])
        elif target == 'none':
            y = 0
        else:
            y = await pg.evaluate(
                """(s) => { const e = document.querySelector(s);
                     if (!e) return 0;
                     const r = e.getBoundingClientRect();
                     return Math.round(r.top + scrollY - 40); }""", target)
        cur = await pg.evaluate("() => scrollY")
        step = 80 if y > cur else -80
        while (step > 0 and cur < y) or (step < 0 and cur > y):
            d = min(abs(step), abs(y - cur))
            await pg.mouse.wheel(0, d * (1 if step > 0 else -1))
            cur += d * (1 if step > 0 else -1)
        if extra_wheel:
            await pg.mouse.wheel(0, extra_wheel)
        if plain:
            # Tar bort background-clip:text-klippet. Skiljer bleckets
            # underkant mot den byggda bilden ar det klippet - samma
            # differential som fel5.py raknar, har som bild i stallet.
            await pg.add_style_tag(content=(
                ".process-title,.process-step-title{background-image:none !important;"
                "-webkit-text-fill-color:currentColor !important;"
                "color:var(--ink) !important;}"))
        if crop:
            r = await pg.evaluate(
                """(s) => { const e = document.querySelector(s);
                     const b = e.getBoundingClientRect();
                     return {x: b.left, y: b.top, width: b.width, height: b.height}; }""",
                crop)
            pad = 24
            r = {'x': max(0, r['x'] - pad), 'y': max(0, r['y'] - pad),
                 'width': r['width'] + 2 * pad, 'height': r['height'] + 2 * pad}
            await pg.wait_for_timeout(500)
            await pg.screenshot(path=f"{name}-{w}.png", clip=r)
            print(f"{name}-{w}.png  beskuren till {crop}")
            await b.close()
            return
        await pg.wait_for_timeout(900)
        info = await pg.evaluate("() => ({y: Math.round(scrollY),"
                                 " h: document.documentElement.scrollHeight,"
                                 " vh: innerHeight})")
        await pg.screenshot(path=f"{name}-{w}.png")
        print(f"{name}-{w}.png  y={info['y']}  sidhöjd={info['h']}  vh={info['vh']}")
        await b.close()


asyncio.run(main())
