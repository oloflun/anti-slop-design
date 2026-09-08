"""Round-6 K2 verification: 18-finding fixes across both motion modes + mobile."""
import pathlib
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html"
OUT = pathlib.Path(__file__).parent
console_log = []


def attach(page, tag):
    def on_console(msg):
        if msg.type == "error" or "[scrollcraft]" in msg.text:
            console_log.append(f"[{tag}] {msg.type}: {msg.text}")
    page.on("console", on_console)
    page.on("pageerror", lambda e: console_log.append(f"[{tag}] pageerror: {e}"))


with sync_playwright() as pw:
    browser = pw.chromium.launch()

    # ---- desktop motion, fold + 2%-series 20-40% + whole-page percentages ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "motion-1440")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "r6-fold-1440.png"))
    total_h = page.evaluate("document.body.scrollHeight - innerHeight")
    for pct in [0, 12, 25, 37, 50, 62, 75, 100]:
        page.evaluate(f"window.scrollTo(0, {total_h} * {pct} / 100)")
        page.wait_for_timeout(450)
        page.screenshot(path=str(OUT / f"r6-page-{pct:03d}.png"))
    ctx.close()

    # ---- preview=open desktop ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "preview-open")
    page.goto(BASE + "?preview=open", wait_until="networkidle")
    page.wait_for_timeout(500)
    page.screenshot(path=str(OUT / "r6-preview-open-1440.png"))
    ctx.close()

    # ---- preview=open + reduced motion (fynd 9) ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    attach(page, "preview-open-rm")
    page.goto(BASE + "?preview=open", wait_until="networkidle")
    page.wait_for_timeout(500)
    page.screenshot(path=str(OUT / "r6-preview-open-rm-1440.png"))
    ctx.close()

    # ---- reduced motion: fold + each act ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    attach(page, "rm-1440")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "r6-rm-fold.png"))
    h = page.evaluate("document.body.scrollHeight")
    for frac, name in [(0.14, "rm-opened"), (0.30, "rm-calyx"), (0.45, "rm-horai"), (0.58, "rm-hyperborea"),
                        (0.70, "rm-services"), (0.85, "rm-price"), (1.0, "rm-close")]:
        page.evaluate(f"window.scrollTo(0, {h} * {frac})")
        page.wait_for_timeout(400)
        page.screenshot(path=str(OUT / f"r6-{name}.png"))
    ctx.close()

    # ---- rm transition check hero -> .opened (fynd: rm-övergången) ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
    page = ctx.new_page()
    attach(page, "rm-transition")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    h = page.evaluate("document.body.scrollHeight")
    for frac, name in [(0.0, "rm-trans-00-hero"), (0.06, "rm-trans-06-seam"), (0.12, "rm-trans-12-opened")]:
        page.evaluate(f"window.scrollTo(0, {h} * {frac})")
        page.wait_for_timeout(350)
        page.screenshot(path=str(OUT / f"r6-{name}.png"))
    ctx.close()

    # ---- close section: Tab-walk to kontakt@alunix.se, focus screenshot (fynd 1) ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "tab-close")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(300)
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(500)
    # Tab through until the mail-link in .close is focused, or cap at 40 tabs.
    for i in range(40):
        page.keyboard.press("Tab")
        focused = page.evaluate("document.activeElement ? document.activeElement.outerHTML.slice(0,120) : null")
        if focused and "mail-link" in focused:
            print(f"reached mail-link after {i+1} tabs")
            break
    page.wait_for_timeout(150)
    page.screenshot(path=str(OUT / "r6-tab-close-focus.png"))
    ctx.close()

    # ---- contrast sweep through the close drift (fynd 2): 5 steps ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "contrast-sweep")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(300)
    h = page.evaluate("document.body.scrollHeight")
    close_top = page.evaluate("document.getElementById('closeAct').offsetTop")
    vh = 900
    # act range for a flow act: raw goes 0->1 over (y+vh-top) in [0, height+vh]; sample around the raw 0-0.35 ramp.
    close_height = page.evaluate("document.getElementById('closeAct').offsetHeight")
    span = close_height + vh
    results = []
    for frac in [0.0, 0.25, 0.5, 0.75, 1.0]:
        # target a raw value from 0 to ~0.45 (covers the 0-0.35 ramp plus a bit past)
        raw = frac * 0.45
        y = close_top - vh + raw * span
        page.evaluate(f"window.scrollTo(0, {max(y,0)})")
        page.wait_for_timeout(300)
        data = page.evaluate("""
            () => {
                const el = document.getElementById('closeAct');
                const cs = getComputedStyle(el);
                const bg = getComputedStyle(document.body).backgroundColor;
                const fg = cs.color;
                const textmix = cs.getPropertyValue('--textmix');
                return {bg, fg, textmix, scrollY: window.scrollY};
            }
        """)
        results.append({"raw_target": raw, **data})
        page.screenshot(path=str(OUT / f"r6-contrast-{int(frac*100):03d}.png"))
    ctx.close()
    print("CONTRAST_SWEEP", results)

    # ---- mobile: fold + full transition through hero, plus preview=open (fynd 10/12/14) ----
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "motion-390")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "r6-fold-390.png"))
    hero_top = page.evaluate("document.getElementById('heroAct').offsetTop")
    hero_h = page.evaluate("document.getElementById('heroAct').offsetHeight")
    print(f"mobile heroAct: top={hero_top} height={hero_h}")
    vh_m = 844
    span_m = hero_h + vh_m
    for frac, name in [(0.0, "390-hero-00"), (0.3, "390-hero-30"), (0.62, "390-hero-62"),
                        (0.84, "390-hero-84"), (1.0, "390-hero-100")]:
        y = hero_top - vh_m + frac * span_m
        page.evaluate(f"window.scrollTo(0, {max(y,0)})")
        page.wait_for_timeout(350)
        page.screenshot(path=str(OUT / f"r6-{name}.png"))
    sw = page.evaluate("document.documentElement.scrollWidth")
    cw = page.evaluate("document.documentElement.clientWidth")
    print(f"overflow 390: scrollWidth={sw} clientWidth={cw}")
    h2 = page.evaluate("document.body.scrollHeight")
    for frac, name in [(0.35, "390-proof"), (0.72, "390-services"), (0.82, "390-price"), (1.0, "390-close")]:
        page.evaluate(f"window.scrollTo(0, {h2} * {frac})")
        page.wait_for_timeout(350)
        page.screenshot(path=str(OUT / f"r6-{name}.png"))
    ctx.close()

    # ---- mobile preview=open (fynd 10, 16) ----
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="no-preference")
    page = ctx.new_page()
    attach(page, "preview-open-390")
    page.goto(BASE + "?preview=open", wait_until="networkidle")
    page.wait_for_timeout(500)
    page.screenshot(path=str(OUT / "r6-preview-open-390.png"))
    ctx.close()

    # ---- mobile reduced motion (still static .opened) ----
    ctx = browser.new_context(viewport={"width": 390, "height": 844}, reduced_motion="reduce")
    page = ctx.new_page()
    attach(page, "rm-390")
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(400)
    page.screenshot(path=str(OUT / "r6-rm-390-fold.png"))
    ctx.close()

    # ---- ALU top-clip check at desktop preview=open (fynd 16) ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    page.goto(BASE + "?preview=open", wait_until="networkidle")
    page.wait_for_timeout(500)
    clip = page.evaluate("""
        () => {
            const row1 = document.getElementById('row1').getBoundingClientRect();
            const stage = document.getElementById('stage').getBoundingClientRect();
            return {row1Top: row1.top, stageTop: stage.top, clipped: row1.top < stage.top};
        }
    """)
    print("ALU_CLIP_CHECK", clip)
    ctx.close()

    # ---- close section height check (fynd 8) ----
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="no-preference")
    page = ctx.new_page()
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_timeout(300)
    close_h = page.evaluate("""
        () => {
            const el = document.getElementById('closeAct');
            return {clientHeight: el.clientHeight, vh: innerHeight, ratio: el.clientHeight / innerHeight};
        }
    """)
    print("CLOSE_HEIGHT_CHECK", close_h)
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
