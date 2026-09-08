"""Measure #proof-horai-media's viewport rect at the scroll position where
#exit's own act ends (i.e. where #proof begins), so #exit's shrink transform
can target it exactly. Run once, lock the printed CSS vars into style.css."""
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3201/tests/alunix-ab-r7/runs/B/K1/index.html"

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1440, "height": 900})
    page = ctx.new_page()
    page.goto(BASE, wait_until="load")
    page.wait_for_timeout(500)

    # First check: is the Hōrai row visible right at the #exit/#proof seam
    # (the last scroll position where #exit's pinned stage still fills the
    # viewport)? If not (row 2 sits deep in #proof's own flow, below intro +
    # row 1), a pixel-continuous handoff across that document-flow boundary
    # is not physically possible -- fall back to measuring the row at its own
    # natural resting position (centered in the viewport once scrolled to),
    # which is what the shrink can actually aim at.
    seam_y = page.evaluate("""() => {
        const exit = document.getElementById('exit');
        const r = exit.getBoundingClientRect();
        return r.top + window.scrollY + exit.offsetHeight - window.innerHeight;
    }""")
    page.evaluate("(y) => window.scrollTo(0, y)", seam_y)
    page.wait_for_timeout(200)
    seam_rect = page.evaluate("""() => {
        const img = document.querySelector('#proof-horai-media img');
        const r = img.getBoundingClientRect();
        return { top: r.top, bottom: r.bottom, vh: window.innerHeight };
    }""")
    print("rect at exit/proof seam:", seam_rect)
    visible_at_seam = seam_rect["bottom"] > 0 and seam_rect["top"] < seam_rect["vh"]
    print("Hōrai row visible at seam:", visible_at_seam)

    if visible_at_seam:
        y = seam_y
    else:
        # Natural resting position: scroll until the row's own center lines
        # up with the viewport's center.
        y = page.evaluate("""() => {
            const img = document.querySelector('#proof-horai-media img');
            const r = img.getBoundingClientRect();
            const centerNow = r.top + r.height / 2 + window.scrollY;
            return centerNow - window.innerHeight / 2;
        }""")
        page.evaluate("(y) => window.scrollTo(0, y)", y)
        page.wait_for_timeout(300)

    rect = page.evaluate("""() => {
        const img = document.querySelector('#proof-horai-media img');
        const r = img.getBoundingClientRect();
        return { left: r.left, top: r.top, width: r.width, height: r.height,
                 vw: window.innerWidth, vh: window.innerHeight };
    }""")
    print("raw rect:", rect)

    tx_pct = (rect["left"] + rect["width"] / 2) / rect["vw"] * 100
    ty_pct = (rect["top"] + rect["height"] / 2) / rect["vh"] * 100
    sx = rect["width"] / rect["vw"]
    sy = rect["height"] / rect["vh"]

    print(f"--exit-tx: {tx_pct:.1f}%;")
    print(f"--exit-ty: {ty_pct:.1f}%;")
    print(f"--exit-sx: {sx:.3f};")
    print(f"--exit-sy: {sy:.3f};")

    page.screenshot(path="tests/alunix-ab-r7/runs/B/K1/shots/measure-boundary.png")
    b.close()
