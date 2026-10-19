"""previews.py <out-dir> <base-url>: every ?preview= mode at 1440x900 and 390x844."""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe"
MODES = ["front", "mid", "back", "ledger", "bleed"] + [f"process-0{i}" for i in range(1, 8)]

async def main(out_dir, base):
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        for w, h, tag in ((1440, 900, "1440"), (390, 844, "390")):
            pg = await b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1,
                                  reduced_motion="reduce")
            for m in MODES:
                await pg.goto(f"{base}?preview={m}", wait_until="load", timeout=60000)
                await pg.wait_for_timeout(1500)
                await pg.screenshot(path=str(out / f"preview-{tag}-{m}.png"))
                print(f"preview-{tag}-{m}.png")
            await pg.close()
        await b.close()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
