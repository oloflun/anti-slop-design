from playwright.sync_api import sync_playwright
BASE = "http://127.0.0.1:3202/tests/alunix-ab-r7/runs/B/K2/index.html"
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.goto(BASE + "?preview=open", wait_until="networkidle")
    page.wait_for_timeout(500)
    clip = page.evaluate("""
        () => {
            const row1 = document.getElementById('row1').getBoundingClientRect();
            const stage = document.getElementById('stage').getBoundingClientRect();
            return {row1Top: row1.top, stageTop: stage.top, clipped: row1.top < stage.top, margin: row1.top - stage.top};
        }
    """)
    print("ALU_CLIP_CHECK", clip)
    page.screenshot(path="r6-preview-open-1440-clipcheck.png")
    ctx.close()
    browser.close()
