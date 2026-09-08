import sys, os
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3201/tests/alunix-ab-r7/runs/B/K1/index.html"
OUT = os.path.dirname(os.path.abspath(__file__))

def shoot(page, name):
    page.screenshot(path=os.path.join(OUT, name + ".png"))
    print("shot:", name)

def hero_scroll_positions(page, frac):
    # returns pixel scrollY for a fraction of #hero's own scroll span
    return page.evaluate("""(frac) => {
        const el = document.getElementById('hero');
        const r = el.getBoundingClientRect();
        const top = r.top + window.scrollY;
        const travel = el.offsetHeight - window.innerHeight;
        return top + travel * frac;
    }""", frac)

def console_errors(page, label):
    msgs = []
    page.on("console", lambda m: msgs.append(f"[{m.type}] {m.text}") if m.type in ("error","warning") else None)
    return msgs

def run_mode(reduced, tag):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width":1440,"height":900}, reduced_motion=("reduce" if reduced else "no-preference"))
        page = ctx.new_page()
        console_msgs = []
        page.on("console", lambda m: console_msgs.append(f"[{m.type}] {m.text}"))
        page.on("pageerror", lambda e: console_msgs.append(f"[pageerror] {e}"))
        page.goto(BASE, wait_until="load")
        page.wait_for_timeout(600)

        shoot(page, f"{tag}-fold")

        if not reduced:
            fracs = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7]
            for f in fracs:
                y = hero_scroll_positions(page, f)
                page.evaluate("(y) => window.scrollTo(0, y)", y)
                page.wait_for_timeout(250)
                shoot(page, f"{tag}-hero-p{int(f*100):02d}")

            for prev in ["window","horai","exit"]:
                page.goto(BASE + f"?preview={prev}", wait_until="load")
                page.wait_for_timeout(900)
                shoot(page, f"{tag}-preview-{prev}")
        else:
            page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(300)
            page.evaluate("() => window.scrollTo(0, 0)")
            secs = page.query_selector_all(".rm-section")
            for i, s in enumerate(secs):
                s.scroll_into_view_if_needed()
                page.wait_for_timeout(300)
                shoot(page, f"{tag}-rm-{i}")

        with open(os.path.join(OUT, f"console-{tag}.log"), "w", encoding="utf-8") as f:
            f.write("\n".join(console_msgs))
        browser.close()

def run_mobile():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width":390,"height":844})
        page = ctx.new_page()
        page.goto(BASE, wait_until="load")
        page.wait_for_timeout(500)
        shoot(page, "m390-fold")
        overflow = page.evaluate("() => document.documentElement.scrollWidth - window.innerWidth")
        print("m390 horizontal overflow px:", overflow)
        browser.close()

if __name__ == "__main__":
    run_mode(False, "motion")
    run_mode(True, "reduced")
    run_mobile()
