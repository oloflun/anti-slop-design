#!/usr/bin/env python3
"""R6b: stillbilder av rutan vid varje steg, 1440x900, båda casen.

Per steg tre lägen i den skrubbade tidslinjen (segment k av n):
  in   (k+0.22)/n  mitt i intoningen, figuren rastrerad
  mid  (k+0.40)/n  mitt i upplösningen raster -> färg (0.30-0.50)
  rest (k+0.75)/n  vilotillståndet, ska vara ren färg
Plus bakåtscroll till rest för tre steg per case (devices.md, timeline-längd).
Mäter rutornas största opacitet och aktiv text/figur per läge, och sparar
rutans utsnitt (panelen) i shots/r6b-steps/ samt tre ark.
"""
import json
import os

from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

URL = os.environ.get("R6B_URL", "http://127.0.0.1:3307/tests/alunix-r8/runs/V3g/index.html")
OUT = os.environ.get("R6B_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "shots", "r6b-steps"))
PHASES = {"in": 0.22, "mid": 0.40, "rest": 0.75}

STATE_JS = """(key) => {
  const P = document.getElementById('showcase-' + key);
  const figs = [...P.querySelectorAll('.showcase-figure')];
  const txt = [...P.querySelectorAll('.showcase-row-text')];
  return {
    fig: figs.map(f => +getComputedStyle(f).opacity),
    text: txt.map(t => +getComputedStyle(t).opacity),
    tilesMax: figs.map(f => Math.max(0, ...[...f.querySelectorAll('.tile-grid span')].map(s => +getComputedStyle(s).opacity))),
    counter: P.querySelector('.showcase-counter').textContent.trim()
  };
}"""


def pin(page):
    return page.evaluate("""() => { const st = ScrollTrigger.getAll().find(s => s.trigger && s.trigger.id === 'showcase');
        return {start: st.start, end: st.end}; }""")


def jump(page, r, p):
    page.evaluate(f"() => window.__lenis.scrollTo({r['start'] + p * (r['end'] - r['start'])}, {{immediate:true}})")
    page.wait_for_timeout(160)


def main():
    os.makedirs(OUT, exist_ok=True)
    log = {"errors": []}
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        try:
            page = b.new_page(viewport={"width": 1440, "height": 900})
            page.on("pageerror", lambda e: log["errors"].append(str(e)))
            page.goto(URL, wait_until="load")
            page.wait_for_timeout(800)
            for key, n in (("calyx", 5), ("horai", 6)):
                if key == "horai":
                    page.click('.case-choice[data-case="horai"]')
                    page.wait_for_timeout(1500)
                r = pin(page)
                jump(page, r, 0.5 / n)
                box = page.query_selector(f"#showcase-{key} .showcase-rows").bounding_box()
                clip = {"x": box["x"], "y": box["y"] - 110, "width": box["width"], "height": box["height"] + 110}
                for k in range(n):
                    for ph, f in PHASES.items():
                        if k == 0 and ph == "in":
                            continue
                        jump(page, r, (k + f) / n)
                        page.wait_for_timeout(250)   # let every image decode before the shot
                        page.screenshot(path=os.path.join(OUT, f"{key}-{k + 1}-{ph}.png"), clip=clip)
                        log[f"{key}-{k + 1}-{ph}"] = page.evaluate(STATE_JS, key)
                for k in (1, n // 2, n - 1):
                    jump(page, r, 0.99)
                    jump(page, r, (k + PHASES["rest"]) / n)
                    page.wait_for_timeout(250)
                    page.screenshot(path=os.path.join(OUT, f"{key}-{k + 1}-back.png"), clip=clip)
                    log[f"{key}-{k + 1}-back"] = page.evaluate(STATE_JS, key)
        finally:
            b.close()
    with open(os.path.join(OUT, "state.json"), "w", encoding="utf-8") as fh:
        json.dump(log, fh, ensure_ascii=False, indent=1)
    # the check: at rest and on the way back only the active step is visible,
    # and its raster is gone; mid-resolve is between; fade-in is fully rastered
    bad = []
    for name, s in log.items():
        if name == "errors":
            continue
        key, k, ph = name.split("-")
        i = int(k) - 1
        on = [j for j, v in enumerate(s["text"]) if v > 0.99]
        if ph in ("rest", "back"):
            if on != [i] or s["fig"][i] < 0.99 or s["tilesMax"][i] > 0.01:
                bad.append((name, on, s["fig"][i], s["tilesMax"][i]))
        if ph == "in" and s["tilesMax"][i] < 0.99:
            bad.append((name, "raster not full at fade-in", s["tilesMax"][i]))
    print("checks failing:", bad or "none", "| page errors:", log["errors"] or "none")
    for ph in ("rest", "mid", "in"):
        names = [f"{c}-{k}-{ph}" for c, n in (("calyx", 5), ("horai", 6)) for k in range(1, n + 1)
                 if os.path.exists(os.path.join(OUT, f"{c}-{k}-{ph}.png"))]
        ims = [Image.open(os.path.join(OUT, x + ".png")) for x in names]
        w, h = ims[0].size
        cols = 6
        sheet = Image.new("RGB", (cols * (w + 8), ((len(ims) + cols - 1) // cols) * (h + 22)), "white")
        d = ImageDraw.Draw(sheet)
        for j, (nm, im) in enumerate(zip(names, ims)):
            x, y = (j % cols) * (w + 8), (j // cols) * (h + 22)
            sheet.paste(im, (x, y + 18)); d.text((x + 2, y + 3), nm, fill="black")
        sheet.save(os.path.join(OUT, f"sheet-{ph}.png"))


if __name__ == "__main__":
    main()
