"""Round-3 K2 full-page screenshot pass."""
import pathlib
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html"
OUT = pathlib.Path(__file__).parent
OUT.mkdir(exist_ok=True)
console_log = []


def attach(page, tag):
    def on_console(msg):
        if msg.type == "error" or "[scrollcraft]" in msg.text:
            console_log.append(f"[{tag}] {msg.type}: {msg.text}")
    page.on("console", on_console)
    page.on("pageerror", lambda e: console_log.append(f"[{tag}] pageerror: {e}"))


with sync_playwright() as pw:
    browser = pw.chromium.launch()

    # ---- motion mode, 1440x900, fold + 8 whole-page percentages ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "motion-1440")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "fold-1440.png"))
    total_h = page.evaluate("document.body.scrollHeight - innerHeight")
    for pct in [0, 12, 25, 37, 50, 62, 75, 100]:
        page.evaluate(f"window.scrollTo(0, {total_h} * {pct} / 100)")
        page.wait_for_timeout(450)
        page.screenshot(path=str(OUT / f"page-{pct:03d}.png"))
    ctx.close()

    # ---- preview=open ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "preview-open")
    page.goto(BASE + "?preview=open", wait_until="networkidle")
    page.wait_for_timeout(500)
    page.screenshot(path=str(OUT / "preview-open.png"))
    ctx.close()

    # ---- reduced motion: fold + each act, full page ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    attach(page, "rm-1440")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "rm-full-1440.png"), full_page=True)
    print("rm scrollHeight:", page.evaluate("document.body.scrollHeight"))
    ctx.close()

    # ---- mobile: fold + full page ----
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "motion-390")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "fold-390.png"))
    sw = page.evaluate("document.documentElement.scrollWidth")
    cw = page.evaluate("document.documentElement.clientWidth")
    print(f"overflow 390: scrollWidth={sw} clientWidth={cw}")
    page.screenshot(path=str(OUT / "full-390.png"), full_page=True)
    ctx.close()

    # ---- overflow check at 320/768/1440 ----
    for w, h in [(320, 700), (768, 1024), (1440, 900)]:
        ctx = browser.new_context(viewport={"width": w, "height": h})
        page = ctx.new_page()
        page.goto(BASE, wait_until="networkidle")
        page.wait_for_timeout(300)
        sw = page.evaluate("document.documentElement.scrollWidth")
        cw = page.evaluate("document.documentElement.clientWidth")
        print(f"overflow {w}px: scrollWidth={sw} clientWidth={cw} {'OVERFLOW' if sw>cw else 'ok'}")
        ctx.close()

    browser.close()

print("\n".join(console_log) if console_log else "no console errors/[scrollcraft] warnings")
