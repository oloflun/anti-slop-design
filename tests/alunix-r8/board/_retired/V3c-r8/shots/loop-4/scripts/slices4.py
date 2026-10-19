"""slices4.py <out-dir> <url> <slug> <w> <h> [max]
Loop-4 slice capture on the R9 state: plain scrollTo (no injected sampler; plan 035 is
built), wait_until="load", 3 s settle per slice so live frames get to render, and the
inline --rv of both wrappers logged per slice (H-27)."""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright
CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
RV = "[document.querySelector('.calyx-wrap').style.getPropertyValue('--rv'), document.querySelector('.horai-wrap').style.getPropertyValue('--rv'), document.querySelector('.calyx-wrap').classList.contains('is-asleep'), document.querySelector('.horai-wrap').classList.contains('is-asleep')]"
async def main(out_dir, url, slug, w, h, mx):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        page = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1, reduced_motion="reduce")
        await page.goto(url, wait_until="load", timeout=60000)
        await page.wait_for_timeout(1500)
        total = await page.evaluate("document.documentElement.scrollHeight")
        n = min(mx, -(-total // h))
        for i in range(n):
            await page.evaluate(f"window.scrollTo(0, {i*h})")
            await page.wait_for_timeout(3000)
            rv = await page.evaluate(RV)
            await page.screenshot(path=str(out / f"{slug}--s{i:02d}.png"))
            print(f"{slug}--s{i:02d}.png rv calyx={rv[0]} horai={rv[1]} asleep={rv[2]}/{rv[3]}")
        print(f"{slug}: total height {total}px = {total/h:.2f} vh, {n} slices")
        await b.close()
a = sys.argv
asyncio.run(main(a[1], a[2], a[3], int(a[4]), int(a[5]), int(a[6]) if len(a) > 6 else 16))
