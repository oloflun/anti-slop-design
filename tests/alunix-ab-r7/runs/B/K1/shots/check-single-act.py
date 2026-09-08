from playwright.sync_api import sync_playwright
import os

OUT = os.path.dirname(os.path.abspath(__file__))
BASE = "http://127.0.0.1:3201/tests/alunix-ab-r7/runs/B/K1/index.html"

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.goto(BASE, wait_until="load")
    page.wait_for_timeout(1200)

    sig = page.evaluate("""() => {
        const api = window.ScrollCraft.instances[0];
        const a = api.acts.find(x => x.el.id === 'signature');
        return { top: a.top, height: a.height };
    }""")
    travel = sig["height"] - 900

    def goto_p(pct):
        y = sig["top"] + travel * pct / 100
        page.evaluate("(y) => window.scrollTo(0, y)", y)
        page.wait_for_timeout(150)

    steps = list(range(0, 58, 2))
    print("FORWARD 0->56%")
    for pct in steps:
        goto_p(pct)
        page.screenshot(path=os.path.join(OUT, f"single-fwd-{pct:02d}.png"))
    print("shots done forward")

    print("BACKWARD 56->0%")
    for pct in reversed(steps):
        goto_p(pct)
        page.screenshot(path=os.path.join(OUT, f"single-bwd-{pct:02d}.png"))
    print("shots done backward")

    b.close()
