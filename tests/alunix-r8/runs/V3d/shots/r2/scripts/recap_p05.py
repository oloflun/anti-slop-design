import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://127.0.0.1:8791/tests/alunix-r8/runs/V3d/index.html"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/r2/ours"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for width, height, suffix in [(390,844,"390")]:
            pg = await browser.new_page(viewport={"width":width,"height":height})
            await pg.goto(URL, wait_until="load", timeout=60000)
            await pg.wait_for_timeout(500)
            # incremental scroll in steps to let lazy images trigger naturally
            target = await pg.evaluate("""() => {
                const h = document.querySelector('.horai-fig');
                const r = h.getBoundingClientRect();
                return window.scrollY + r.top + r.height/2 - window.innerHeight/2;
            }""")
            steps = 12
            for i in range(1, steps+1):
                y = target * i / steps
                await pg.evaluate(f"window.scrollTo(0,{y})")
                await pg.wait_for_timeout(150)
            await pg.wait_for_timeout(1200)
            await pg.screenshot(path=str(OUT / f"horai-band-{suffix}.png"))
            print(width, "done")
            await pg.close()
        await browser.close()

asyncio.run(main())
