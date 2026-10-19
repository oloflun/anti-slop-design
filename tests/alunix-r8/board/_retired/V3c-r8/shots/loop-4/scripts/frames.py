"""frames.py <mode> <out-dir> <url> <slug> <width> <height> [n]

mode = flip    : 12 frames, --flip 0 -> 1 on #plateCard via page.evaluate (as r4-pre),
                 window.__scFreezeMotion = true so the shim tracks raw.
mode = act     : 12 frames scrolled in equal steps through the element given by
                 the 8th argument (a CSS selector), from its top to bottom - vh.
mode = pin     : 12 frames through a pinned act: scroll from act.top to act.top +
                 (act.height - vh) in equal steps (selector in 8th argument).
"""
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"


async def main(mode, out_dir, url, slug, width, height, n, sel):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=CHROME)
        page = await browser.new_page(viewport={"width": width, "height": height},
                                      device_scale_factor=1, reduced_motion="reduce")
        await page.goto(url, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(1500)
        if mode == "flip":
            await page.evaluate("window.__scFreezeMotion = true")
            for i in range(n):
                f = i / (n - 1)
                await page.evaluate(
                    "(f)=>{const c=document.getElementById('plateCard');"
                    "c.style.setProperty('--flip', String(f));"
                    "const hero=document.getElementById('hero-section');"
                    "hero.classList.remove('is-turning');}", f)
                await page.wait_for_timeout(250)
                await page.screenshot(path=str(out / f"{slug}-flip-{i:02d}-{int(round(f*100)):03d}.png"))
        else:
            box = await page.evaluate(
                "(s)=>{const e=document.querySelector(s);const r=e.getBoundingClientRect();"
                "return {top:r.top+scrollY,h:r.height}}", sel)
            top, h = box["top"], box["h"]
            if mode == "life":
                start, travel = top - height, h + height
            else:
                start, travel = top, max(h - height, 1)
            for i in range(n):
                y = start + travel * i / (n - 1)
                await page.evaluate(f"window.scrollTo(0, {y})")
                await page.wait_for_timeout(700)
                await page.screenshot(path=str(out / f"{slug}-{mode}-{i:02d}.png"))
            print(f"{slug}: {sel} top={top:.0f} h={h:.0f} travel={travel:.0f}")
        await browser.close()
        print(f"{slug}: {n} frames -> {out}")


if __name__ == "__main__":
    a = sys.argv
    asyncio.run(main(a[1], a[2], a[3], a[4], int(a[5]), int(a[6]),
                     int(a[7]) if len(a) > 7 else 12, a[8] if len(a) > 8 else None))
