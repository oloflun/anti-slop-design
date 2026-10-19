"""astra-r18: hjulbilder (20 px sista stegen) i stegbandens bytesfönster, en skärmbild per läge."""
import asyncio, sys
from playwright.async_api import async_playwright
URL = "http://localhost:3090/tests/alunix-r8/runs/V3d/index.html"
JOBS = {1440: (900, [8960, 9000, 9100, 9120, 9960]), 1920: (930, [9260, 9400, 9420, 10300])}


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(ignore_default_args=['--hide-scrollbars'])
        for w, (h, ys) in JOBS.items():
            pg = await b.new_page(viewport={'width': w, 'height': h})
            await pg.goto(URL); await pg.wait_for_timeout(2500); await pg.mouse.move(w / 2, h / 2)
            for y in ys:
                while True:
                    d = y - await pg.evaluate("scrollY")
                    if abs(d) < 2: break
                    await pg.mouse.wheel(0, max(-120, min(120, d)) if abs(d) > 40 else max(-20, min(20, d))); await pg.wait_for_timeout(30)
                await pg.wait_for_timeout(1500)
                await pg.screenshot(path=f"ours/band-{w}-{y}.png")
                print(w, y, await pg.evaluate("scrollY"))
            await pg.close()
        await b.close()

asyncio.run(main())
