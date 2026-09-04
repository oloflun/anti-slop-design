import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

URL = "file:///C:/Users/Anton L/anti-slop-design/tests/alunix-concepts/cells/K2-chain/index.html"
OUT = Path(__file__).parent
WIDTHS = [320, 375, 414, 768]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for w in WIDTHS:
            page = await browser.new_page(viewport={"width": w, "height": 900}, device_scale_factor=1, reduced_motion="no-preference")
            await page.goto(URL, wait_until="networkidle", timeout=60000)
            await page.wait_for_timeout(900)
            await page.screenshot(path=str(OUT / f"mobile-{w}-fold.png"))
            await page.screenshot(path=str(OUT / f"mobile-{w}-full.png"), full_page=True)
            sw = await page.evaluate("document.documentElement.scrollWidth")
            cw = await page.evaluate("document.documentElement.clientWidth")
            print(f"{w}px -> scrollWidth={sw} clientWidth={cw} overflow={'YES' if sw>cw else 'no'}")
            await page.close()
        # also check reduced-motion mode at desktop width
        page = await browser.new_page(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
        await page.goto(URL, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(900)
        await page.screenshot(path=str(OUT / "reduced-motion-full.png"), full_page=True)
        await page.close()
        await browser.close()

asyncio.run(main())
