import asyncio
from playwright.async_api import async_playwright
from pathlib import Path

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://127.0.0.1:8791/tests/alunix-r8/runs/V3d/index.html"
OUT = BASE / "tests/alunix-r8/runs/V3d/shots/r2/ours"
OUT.mkdir(parents=True, exist_ok=True)

# (id, kind, arg, filename-stub)
# kind "preview" -> ?preview=<arg>; kind "scroll" -> scrollTo(0, arg); kind "center" -> scrollIntoView center on selector
ROWS_1440 = [
    ("P01", "preview", "front", "front"),
    ("P02", "preview", "back", "back"),
    ("P03", "center", ".thesis-figure", "thesis"),
    ("P04", "preview", "ledger", "ledger"),
    ("P05", "center", ".horai-fig", "horai-band"),
    ("P06", "scrollto-sel", "#process", "process-chapter"),
    ("P07", "preview", "process-01", "process-01"),
    ("P08", "preview", "process-02", "process-02"),
    ("P09", "preview", "process-03", "process-03"),
    ("P10", "preview", "process-04", "process-04"),
    ("P11", "preview", "process-05", "process-05"),
    ("P12", "preview", "process-06", "process-06"),
    ("P13", "preview", "process-07", "process-07"),
    ("P14", "center", "#principer", "principer"),
]

async def shoot(pg, kind, arg, path):
    if path.exists():
        return
    if kind == "preview":
        await pg.goto(URL + f"?preview={arg}", wait_until="domcontentloaded", timeout=60000)
        await pg.wait_for_timeout(900)
    elif kind == "center":
        await pg.goto(URL, wait_until="domcontentloaded")
        await pg.wait_for_timeout(700)
        await pg.evaluate(f"document.querySelector('{arg}').scrollIntoView({{block:'center'}})")
        await pg.wait_for_timeout(700)
    elif kind == "scrollto-sel":
        await pg.goto(URL, wait_until="domcontentloaded")
        await pg.wait_for_timeout(700)
        await pg.evaluate(f"document.querySelector('{arg}').scrollIntoView({{block:'start'}})")
        await pg.wait_for_timeout(700)
    await pg.screenshot(path=str(path))

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # 1440
        pg = await browser.new_page(viewport={"width":1440,"height":900})
        for rid, kind, arg, stub in ROWS_1440:
            out = OUT / f"{stub}-1440.png"
            await shoot(pg, kind, arg, out)
            print("1440", rid, stub, "done")
        await pg.close()
        # 390
        pg = await browser.new_page(viewport={"width":390,"height":844})
        for rid, kind, arg, stub in ROWS_1440:
            out = OUT / f"{stub}-390.png"
            await shoot(pg, kind, arg, out)
            print("390", rid, stub, "done")
        await pg.close()

        # P15: two separate rows, no stitching. "sista viewporten" and "en viewport före".
        pg = await browser.new_page(viewport={"width":1440,"height":900})
        await pg.goto(URL)
        await pg.wait_for_timeout(500)
        full_h = await pg.evaluate("document.body.scrollHeight")
        await pg.evaluate(f"window.scrollTo(0,{full_h})")
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=str(OUT / "pris-end-1440.png"))
        await pg.evaluate(f"window.scrollTo(0,{full_h}-900)")
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=str(OUT / "pris-before-1440.png"))
        await pg.close()

        pg = await browser.new_page(viewport={"width":390,"height":844})
        await pg.goto(URL)
        await pg.wait_for_timeout(500)
        full_h = await pg.evaluate("document.body.scrollHeight")
        await pg.evaluate(f"window.scrollTo(0,{full_h})")
        await pg.wait_for_timeout(600)
        await pg.screenshot(path=str(OUT / "pris-end-390.png"))
        await pg.close()

        await browser.close()

asyncio.run(main())
