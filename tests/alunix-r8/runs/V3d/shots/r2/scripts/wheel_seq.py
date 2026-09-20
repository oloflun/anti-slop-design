import asyncio, sys
from playwright.async_api import async_playwright
from pathlib import Path

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://127.0.0.1:8791/tests/alunix-r8/runs/V3d/index.html"

async def run(width, height, out_dir, proc_top, proc_bottom):
    out_dir.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        pg = await browser.new_page(viewport={"width": width, "height": height})
        for attempt in range(6):
            try:
                await pg.goto(URL, wait_until="load", timeout=15000)
                break
            except Exception:
                if attempt == 5: raise
        await pg.wait_for_timeout(600)
        # scroll to just above the process act using wheel ticks (not scrollTo)
        # move mouse to center first
        await pg.mouse.move(width/2, height/2)
        target_start = max(0, proc_top - 200)
        cur = 0
        while cur < target_start:
            step = min(600, target_start - cur)
            await pg.mouse.wheel(0, step)
            cur += step
            await pg.wait_for_timeout(15)
        await pg.wait_for_timeout(500)
        i = 0
        last_y = await pg.evaluate("window.scrollY")
        stall = 0
        while last_y < proc_bottom + 300:
            await pg.mouse.wheel(0, 150)
            await pg.wait_for_timeout(180)
            y = await pg.evaluate("window.scrollY")
            if y == last_y:
                stall += 1
                if stall >= 4:
                    break
                continue
            stall = 0
            await pg.screenshot(path=str(out_dir / f"w{i:03d}-y{int(y)}.png"))
            last_y = y
            i += 1
            if i > 120:
                break
        await browser.close()
        print("done", width, "frames:", i)

async def main():
    # 390: process 5522..10092
    await run(390, 844, BASE/"tests/alunix-r8/runs/V3d/shots/r2/wheel-390", 5522, 10092)

asyncio.run(main())
