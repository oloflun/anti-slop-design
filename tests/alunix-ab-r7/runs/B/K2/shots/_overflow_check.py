import pathlib
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html"
OUT = pathlib.Path(__file__).parent

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    for w, h in [(320, 700), (768, 1024)]:
        ctx = browser.new_context(viewport={"width": w, "height": h})
        page = ctx.new_page()
        logs = []
        page.on("console", lambda m: logs.append(f"{m.type}: {m.text}") if m.type in ("error", "warning") else None)
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(400)
        sw = page.evaluate("document.documentElement.scrollWidth")
        cw = page.evaluate("document.documentElement.clientWidth")
        print(f"{w}px viewport: scrollWidth={sw} clientWidth={cw} overflow={'YES' if sw > cw else 'no'}")
        page.screenshot(path=str(OUT / f"fold-{w}.png"), full_page=False)
        if logs:
            print(f"  console: {logs}")
        ctx.close()
    for w, h in [(1440, 900)]:
        ctx = browser.new_context(viewport={"width": w, "height": h})
        page = ctx.new_page()
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(400)
        sw = page.evaluate("document.documentElement.scrollWidth")
        cw = page.evaluate("document.documentElement.clientWidth")
        print(f"{w}px viewport: scrollWidth={sw} clientWidth={cw} overflow={'YES' if sw > cw else 'no'}")
        ctx.close()
    browser.close()
