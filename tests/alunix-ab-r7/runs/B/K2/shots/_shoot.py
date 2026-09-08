"""Round-2 K2 screenshot pass. Run with: python _shoot.py"""
import pathlib
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html"
OUT = pathlib.Path(__file__).parent
OUT.mkdir(exist_ok=True)

console_log = []


def attach_console(page, tag):
    def on_console(msg):
        if msg.type in ("error", "warning") or "[scrollcraft]" in msg.text:
            console_log.append(f"[{tag}] {msg.type}: {msg.text}")
    page.on("console", on_console)
    page.on("pageerror", lambda e: console_log.append(f"[{tag}] pageerror: {e}"))


def scroll_to_progress(page, p):
    page.evaluate(
        """(p) => {
            const act = document.getElementById('heroAct');
            const top = act.offsetTop;
            const travel = Math.max(act.offsetHeight - innerHeight, 1);
            window.scrollTo(0, top + travel * p);
        }""",
        p,
    )
    page.wait_for_timeout(500)  # let the lerp settle


with sync_playwright() as pw:
    browser = pw.chromium.launch()

    # ---- motion mode, 1440x900 ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach_console(page, "motion-1440")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "fold-1440.png"))

    for pct in [0, 15, 30, 45, 60, 80]:
        scroll_to_progress(page, pct / 100)
        page.screenshot(path=str(OUT / f"act-{pct:02d}.png"))
    ctx.close()

    # ---- preview modes ----
    for name in ["calyx", "horai", "hyperborea", "open"]:
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
        page = ctx.new_page()
        attach_console(page, f"preview-{name}")
        page.goto(BASE + f"?preview={name}", wait_until="networkidle")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / f"preview-{name}.png"))
        ctx.close()

    # ---- reduced motion ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    attach_console(page, "rm-1440")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "rm-fold-1440.png"))
    page.evaluate("window.scrollTo(0, document.body.scrollHeight * 0.5)")
    page.wait_for_timeout(300)
    page.screenshot(path=str(OUT / "rm-50pct-1440.png"))
    ctx.close()

    # ---- mobile fold ----
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach_console(page, "motion-390")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "fold-390.png"))
    ctx.close()

    browser.close()

print("\n".join(console_log) if console_log else "no console errors/warnings")
