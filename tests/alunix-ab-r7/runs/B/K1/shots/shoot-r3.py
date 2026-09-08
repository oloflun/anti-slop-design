import os
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3201/tests/alunix-ab-r7/runs/B/K1/index.html"
OUT = os.path.dirname(os.path.abspath(__file__))

def shoot(page, name):
    page.screenshot(path=os.path.join(OUT, name + ".png"))
    print("shot:", name)

def run_motion():
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        msgs = []
        page.on("console", lambda m: msgs.append(f"[{m.type}] {m.text}"))
        page.on("pageerror", lambda e: msgs.append(f"[pageerror] {e}"))
        page.goto(BASE, wait_until="load")
        page.wait_for_timeout(1200)

        shoot(page, "final-fold")

        total = page.evaluate("() => document.documentElement.scrollHeight - window.innerHeight")
        for i in range(0, 101, 8):
            page.evaluate("(y) => window.scrollTo(0, y)", total * i / 100)
            page.wait_for_timeout(280)
            shoot(page, f"final-p{i:03d}")

        # dense 2% steps 34-46% for the scrub->frame handoff
        for pct in range(34, 48, 2):
            page.evaluate("(y) => window.scrollTo(0, y)", total * pct / 100)
            page.wait_for_timeout(200)
            shoot(page, f"final-dense-{pct}")

        for prev in ["window", "horai", "exit", "ledger"]:
            page.goto(BASE + f"?preview={prev}", wait_until="load")
            page.wait_for_timeout(900)
            shoot(page, f"final-preview-{prev}")

        overflow = page.evaluate("() => document.documentElement.scrollWidth - window.innerWidth")
        print("1440 overflow:", overflow)

        with open(os.path.join(OUT, "final-console-motion.log"), "w", encoding="utf-8") as f:
            f.write("\n".join(msgs))
        b.close()

def run_reduced():
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": 1440, "height": 900}, reduced_motion="reduce")
        page = ctx.new_page()
        msgs = []
        page.on("console", lambda m: msgs.append(f"[{m.type}] {m.text}"))
        page.on("pageerror", lambda e: msgs.append(f"[pageerror] {e}"))
        page.goto(BASE, wait_until="load")
        page.wait_for_timeout(1000)
        shoot(page, "final-rm-fold")
        secs = page.query_selector_all(".rm-section")
        for i, s in enumerate(secs):
            s.scroll_into_view_if_needed()
            page.wait_for_timeout(350)
            shoot(page, f"final-rm-{i}")
        overflow = page.evaluate("() => document.documentElement.scrollWidth - window.innerWidth")
        print("1440 reduced overflow:", overflow)
        with open(os.path.join(OUT, "final-console-reduced.log"), "w", encoding="utf-8") as f:
            f.write("\n".join(msgs))
        b.close()

def run_breakpoints():
    with sync_playwright() as p:
        b = p.chromium.launch()
        for w in [320, 390, 768]:
            ctx = b.new_context(viewport={"width": w, "height": 844})
            page = ctx.new_page()
            page.goto(BASE, wait_until="load")
            page.wait_for_timeout(900)
            shoot(page, f"final-m{w}-fold")
            overflow = page.evaluate("() => document.documentElement.scrollWidth - window.innerWidth")
            print(f"{w} overflow:", overflow)
            total = page.evaluate("() => document.documentElement.scrollHeight - window.innerHeight")
            page.evaluate("(y) => window.scrollTo(0, y)", total)
            page.wait_for_timeout(500)
            shoot(page, f"final-m{w}-end")
            ctx2 = b.new_context(viewport={"width": w, "height": 844}, reduced_motion="reduce")
            page2 = ctx2.new_page()
            page2.goto(BASE, wait_until="load")
            page2.wait_for_timeout(700)
            overflow2 = page2.evaluate("() => document.documentElement.scrollWidth - window.innerWidth")
            print(f"{w} reduced overflow:", overflow2)
            ctx.close(); ctx2.close()
        b.close()

if __name__ == "__main__":
    run_motion()
    run_reduced()
    run_breakpoints()
