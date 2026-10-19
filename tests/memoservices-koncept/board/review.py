"""Granskningsbilder för en boardcell: varje ?preview=-krok vid 1440x900 och mobil 390x844,
plus mobilmenyn öppen. Skriver PNG till <cell>/.review/. Leaden läser bilderna själv.

    python review.py <cell-url> <out-dir> hero passage ...
"""
import sys, time
from pathlib import Path
from playwright.sync_api import sync_playwright

url, out = sys.argv[1], Path(sys.argv[2]); hooks = sys.argv[3:]
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch()
    for name, w, h in (("desk", 1440, 900), ("mob", 390, 844)):
        pg = b.new_page(viewport={"width": w, "height": h})
        errs = []
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        for hk in hooks:
            pg.goto(f"{url}?preview={hk}", wait_until="load"); time.sleep(3.5)
            pg.screenshot(path=str(out / f"{name}-{hk}.png"))
            # verkligt hjul: 12 hack á 100 px från krokens läge, sedan en bild till
            for _ in range(12): pg.mouse.wheel(0, 100); time.sleep(0.05)
            time.sleep(1.2); pg.screenshot(path=str(out / f"{name}-{hk}-plus12.png"))
        if name == "mob":
            pg.goto(url, wait_until="load"); time.sleep(3)
            btn = pg.query_selector("button[aria-expanded]")
            if btn:
                btn.click(); time.sleep(1); pg.screenshot(path=str(out / "mob-meny.png"))
        print(name, "konsolfel:", len(errs), errs[:5])
        pg.close()
    b.close()
print("skrev", len(list(out.glob("*.png"))), "bilder till", out)
