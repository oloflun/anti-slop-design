import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://127.0.0.1:8792/tests/alunix-r8/runs/V3d/index.html"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/r3/ours"

ROWS = [
    ("back", "?preview=back", "preview"),
    ("thesis", ".thesis-figure", "center"),
]

async def shoot(pg, kind, arg, path):
    if kind == "preview":
        for attempt in range(8):
            try:
                await pg.goto(URL + arg, wait_until="domcontentloaded", timeout=15000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(900)
    elif kind == "center":
        for attempt in range(8):
            try:
                await pg.goto(URL, wait_until="domcontentloaded", timeout=15000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(700)
        await pg.evaluate(f"document.querySelector('{arg}').scrollIntoView({{block:'center'}})")
        await pg.wait_for_timeout(700)
    await pg.screenshot(path=str(path))

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for width, height in [(1440,900),(390,844)]:
            pg = await browser.new_page(viewport={"width":width,"height":height})
            for stub, arg, kind in ROWS:
                await shoot(pg, kind, arg, OUT / f"{stub}-{width}.png")
                print(width, stub, "done")
            await pg.close()
        await browser.close()

asyncio.run(main())
