import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://127.0.0.1:8795/tests/alunix-r8/runs/V3d/index.html"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/r4/ours"

# (stub, kind, arg)
ROWS = [
    ("back", "preview", "back"),
    ("thesis", "center", ".thesis-figure"),
    ("ledger", "preview", "ledger"),
    ("process-chapter", "top", "#process"),
    ("process-04", "preview", "process-04"),
    ("process-06", "preview", "process-06"),
    ("process-07", "preview", "process-07"),
]

async def shoot(pg, kind, arg, path):
    if kind == "preview":
        for attempt in range(8):
            try:
                await pg.goto(URL + f"?preview={arg}", wait_until="domcontentloaded", timeout=20000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(900)
    elif kind == "center":
        for attempt in range(8):
            try:
                await pg.goto(URL, wait_until="domcontentloaded", timeout=20000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(700)
        await pg.evaluate(f"document.querySelector('{arg}').scrollIntoView({{block:'center'}})")
        await pg.wait_for_timeout(700)
    elif kind == "top":
        for attempt in range(8):
            try:
                await pg.goto(URL, wait_until="domcontentloaded", timeout=20000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(700)
        top = await pg.evaluate(f"document.querySelector('{arg}').getBoundingClientRect().top + window.scrollY")
        await pg.evaluate(f"window.scrollTo(0,{top})")
        await pg.wait_for_timeout(500)
    await pg.screenshot(path=str(path))

async def main():
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for width, height in [(1440,900),(390,844)]:
            pg = await browser.new_page(viewport={"width":width,"height":height})
            for stub, kind, arg in ROWS:
                path = OUT / f"{stub}-{width}.png"
                if path.exists():
                    continue
                await shoot(pg, kind, arg, path)
                print(width, stub, "done")
            await pg.close()

        # P16: full-page contact sheet at 1440
        pg = await browser.new_page(viewport={"width":1440,"height":900})
        for attempt in range(8):
            try:
                await pg.goto(URL, wait_until="load", timeout=20000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(700)
        await pg.screenshot(path=str(OUT / "sheet-1440.png"), full_page=True)
        print("sheet done")
        await browser.close()

asyncio.run(main())
