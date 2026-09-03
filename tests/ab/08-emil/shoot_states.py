"""Capture the interactive states of the settings surface for A and B."""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

async def shoot(variant: str, reduced: bool):
    d = Path(__file__).parent / variant
    url = (d / "index.html").resolve().as_uri()
    out = d / ("shots-rm" if reduced else "shots"); out.mkdir(exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1440, "height": 900},
                              reduced_motion="reduce" if reduced else "no-preference")
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        await pg.goto(url, wait_until="networkidle"); await pg.wait_for_timeout(800)
        await pg.screenshot(path=str(out / "01-fold.png"))
        # tabs
        tabs = pg.get_by_role("tab")
        n = await tabs.count()
        if n >= 2:
            await tabs.nth(1).click(); await pg.wait_for_timeout(120)
            await pg.screenshot(path=str(out / "02-tab-mid.png"))
            await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(out / "03-tab-aviseringar.png"))
        # drawer (back to first tab so the trigger is visible)
        if n >= 2:
            await tabs.nth(0).click(); await pg.wait_for_timeout(400)
        btn = pg.locator("button:has-text('API'):visible")
        if await btn.count():
            await btn.first.click(); await pg.wait_for_timeout(120)
            await pg.screenshot(path=str(out / "04-drawer-mid.png"))
            await pg.wait_for_timeout(600)
            await pg.screenshot(path=str(out / "05-drawer-open.png"))
            # hold to delete: mouse down on first Radera for 900ms
            rad = pg.locator("button:has-text('Radera'):visible, button[data-hold-delete]:visible, button.hold-delete:visible")
            if await rad.count():
                box = await rad.first.bounding_box()
                if box:
                    await pg.mouse.move(box["x"]+box["width"]/2, box["y"]+box["height"]/2)
                    await pg.mouse.down(); await pg.wait_for_timeout(900)
                    await pg.screenshot(path=str(out / "06-hold-mid.png"))
                    await pg.mouse.up(); await pg.wait_for_timeout(300)
                    await pg.screenshot(path=str(out / "07-hold-released.png"))
            await pg.keyboard.press("Escape"); await pg.wait_for_timeout(600)
        # toast
        save = pg.locator("button:has-text('Spara'):visible")
        if await save.count():
            await save.first.click(); await pg.wait_for_timeout(150)
            await pg.screenshot(path=str(out / "08-toast-enter.png"))
            await pg.wait_for_timeout(600)
            await save.first.click(); await pg.wait_for_timeout(700)
            await pg.screenshot(path=str(out / "09-toast-stack.png"))
        # mobile fold
        await pg.set_viewport_size({"width": 390, "height": 844}); await pg.wait_for_timeout(300)
        await pg.screenshot(path=str(out / "10-mobile.png"))
        await b.close()
        (out / "errors.txt").write_text("\n".join(errs), encoding="utf-8")
        print(variant, "reduced" if reduced else "normal", "errors:", len(errs))

async def main():
    for v in ("A-baseline", "B-with"):
        if (Path(__file__).parent / v / "index.html").exists():
            await shoot(v, False); await shoot(v, True)

asyncio.run(main())
