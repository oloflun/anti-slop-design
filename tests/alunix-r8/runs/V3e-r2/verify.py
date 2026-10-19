"""Verify V3e-r2: console, overflow, iframe mount, hero fold, works' colors."""
import json, re
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3305/tests/alunix-r8/runs/V3e-r2/index.html"
WIDTHS = [390, 414, 768, 1440, 1920]

def main():
    results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        # --- overflow + console at every width
        for w in WIDTHS:
            page = browser.new_page(viewport={"width": w, "height": 900})
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.goto(URL, wait_until="load")
            page.wait_for_timeout(1200)
            sw = page.evaluate("document.documentElement.scrollWidth")
            cw = page.evaluate("document.documentElement.clientWidth")
            results[f"overflow_{w}"] = sw - cw
            results[f"console_{w}"] = [e for e in errors if "cdn.tailwindcss" not in e]
            page.close()

        # --- detailed 1440x900
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(1500)

        # hero fold
        hero = page.evaluate("""() => {
            const h1 = document.querySelector('.hero-h1');
            const r = h1.getBoundingClientRect();
            const hero = document.querySelector('#hero').getBoundingClientRect();
            const wm = document.querySelector('.hero-wordmark');
            const wmcs = getComputedStyle(wm);
            const label = document.querySelector('.hero-label').getBoundingClientRect();
            return {
                h1Top: r.top, h1Bottom: r.bottom, heroTop: hero.top, heroBottom: hero.bottom,
                h1Font: getComputedStyle(h1).fontFamily.split(',')[0].trim(),
                h1Weight: getComputedStyle(h1).fontWeight,
                h1Size: getComputedStyle(h1).fontSize,
                wordmarkStroke: wmcs.webkitTextStrokeWidth || wmcs.webkitTextStroke,
                wordmarkFill: wmcs.webkitTextFillColor,
                labelBottom: label.bottom,
                viewport: innerHeight,
            };
        }""")
        results["hero"] = hero

        # works' colors
        colors = page.evaluate("""() => {
            const calyxNum = document.querySelector('.work--calyx .work-strip .num');
            const horaiNum = document.querySelector('.work--horai .work-strip .num');
            const calyxRule = document.querySelector('.work--calyx .work-rule');
            return {
                calyxW: getComputedStyle(document.querySelector('.work--calyx')).getPropertyValue('--w').trim(),
                horaiW: getComputedStyle(document.querySelector('.work--horai')).getPropertyValue('--w').trim(),
                calyxNumColor: getComputedStyle(calyxNum).color,
                horaiNumColor: getComputedStyle(horaiNum).color,
                calyxRuleBg: getComputedStyle(calyxRule).backgroundColor,
                plateBg: getComputedStyle(document.querySelector('.work--calyx')).backgroundColor,
                groundBg: getComputedStyle(document.body).backgroundColor,
            };
        }""")
        results["colors"] = colors

        # iframe mount: scroll to case, wait, check
        page.evaluate("window.scrollTo(0, 3300)")
        page.wait_for_timeout(6000)
        frames = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('iframe')).map(f => ({
                src: f.getAttribute('src'), dataSrc: f.getAttribute('data-src'),
                title: f.getAttribute('title'), loading: f.getAttribute('loading'),
                nodes: f.contentDocument ? f.contentDocument.body.querySelectorAll('*').length : 0,
                sticky: getComputedStyle(f.parentElement).position,
            }));
        }""")
        results["frames"] = frames

        # full page height
        results["pageHeight"] = page.evaluate("document.body.scrollHeight")
        results["console1440"] = [e for e in errors if "cdn.tailwindcss" not in e]

        # screenshots
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(800)
        page.screenshot(path="tests/alunix-r8/runs/V3e-r2/_shot-hero.png")
        page.screenshot(path="tests/alunix-r8/runs/V3e-r2/_shot-full.png", full_page=True)
        page.close()

        # mobile screenshot
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(URL, wait_until="load")
        page.wait_for_timeout(1000)
        page.evaluate("window.scrollTo(0, 3200)")
        page.wait_for_timeout(5000)
        page.screenshot(path="tests/alunix-r8/runs/V3e-r2/_shot-mobile-case.png")
        page.close()

        browser.close()

    with open("tests/alunix-r8/runs/V3e-r2/_verify.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("wrote _verify.json")

if __name__ == "__main__":
    main()
