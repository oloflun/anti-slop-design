"""Lead R22: hjulsekvens genom tes -> ritning, enskilda bilder."""
import asyncio, sys
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"

async def main():
    w, h = int(sys.argv[1]), int(sys.argv[2])
    targets = [int(x) for x in sys.argv[3:]]
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        pg = await b.new_page(viewport={'width': w, 'height': h})
        await pg.goto(URL); await pg.wait_for_timeout(3000)
        await pg.mouse.move(w // 2, h // 2)
        cur = 0
        for t in targets:
            while cur < t:
                step = min(20, t - cur)
                await pg.mouse.wheel(0, step); cur += step
                await pg.wait_for_timeout(4)
            await pg.wait_for_timeout(1200)
            y = await pg.evaluate("window.scrollY")
            await pg.screenshot(path=f"wheel-{w}-{t}.png")
            print(f"{t} -> scrollY {y}", flush=True)
        await b.close()

asyncio.run(main())
