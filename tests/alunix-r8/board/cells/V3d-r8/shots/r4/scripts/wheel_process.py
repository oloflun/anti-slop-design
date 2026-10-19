import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = Path(r"C:\Users\Anton L\anti-slop-design")
URL = "http://127.0.0.1:8795/tests/alunix-r8/runs/V3d/index.html"

async def run(width, height, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        pg = await browser.new_page(viewport={"width": width, "height": height})
        for attempt in range(8):
            try:
                await pg.goto(URL, wait_until="load", timeout=20000)
                break
            except Exception:
                if attempt == 7: raise
        await pg.wait_for_timeout(500)
        await pg.mouse.move(width/2, height/2)
        target_start, target_end = await pg.evaluate("""() => {
            const el = document.querySelector('#process');
            const r = el.getBoundingClientRect();
            return [window.scrollY + r.top - 50, window.scrollY + r.bottom + 100];
        }""")
        cur = 0
        while cur < target_start:
            step = min(400, target_start - cur)
            await pg.mouse.wheel(0, step)
            cur += step
            await pg.wait_for_timeout(15)
        await pg.wait_for_timeout(400)
        i = 0
        last_y = await pg.evaluate("window.scrollY")
        stall = 0
        while last_y < target_end:
            await pg.mouse.wheel(0, 150)
            await pg.wait_for_timeout(140)
            y = await pg.evaluate("window.scrollY")
            if y == last_y:
                stall += 1
                if stall >= 5: break
                continue
            stall = 0
            await pg.screenshot(path=str(out_dir / f"w{i:03d}-y{int(y)}.png"))
            last_y = y
            i += 1
            if i > 90: break
        await browser.close()
        print(width, "frames:", i)

async def main():
    await run(1440, 900, BASE/"tests/alunix-r8/runs/V3d/shots/r4/wheel-1440")
    await run(390, 844, BASE/"tests/alunix-r8/runs/V3d/shots/r4/wheel-390")

asyncio.run(main())
