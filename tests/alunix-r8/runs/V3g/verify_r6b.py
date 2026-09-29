#!/usr/bin/env python3
"""R6 runda 6, fas 1b-3: samma 22 + 3 bakat som verify_r6.py, men i
shots/r6-steps-b/ (efter de nya bilderna/texterna) och med stegbytesbilden
tagen vid p=(k+0.22)/n i stallet for (k+0.15)/n - (k+0.15)/n ar den exakta
nollpunkten mellan text k-1:s uttoning och text k:s introning (bada
INTE_FRAC/UT_FRAC ar 0.15/n, sa vid precis 0.15/n har uttoningen just
avslutats och introningen just paborjats - cellen star tom det ogonblicket).
0.22/n ligger halvvags in i introningsfonstret (0.15-0.30 av segmentet)."""
import os
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3307/tests/alunix-r8/runs/V3g/index.html"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shots", "r6-steps-b")


def get_pin_range(page):
    return page.evaluate("""() => {
        const st = ScrollTrigger.getAll().find(s => s.trigger && s.trigger.id === 'showcase');
        return st ? {start: st.start, end: st.end} : null;
    }""")


def jump_to(page, start, end, p):
    y = start + p * (end - start)
    page.evaluate(f"() => window.__lenis.scrollTo({y}, {{immediate:true}})")
    page.wait_for_timeout(120)


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(URL, wait_until="load")
            page.wait_for_timeout(500)

            rng = get_pin_range(page)
            print("pin range:", rng)
            start, end = rng["start"], rng["end"]

            n = 5
            box_heights = []
            for k in range(n):
                p_rest = (k + 0.95) / n
                jump_to(page, start, end, p_rest)
                box = page.query_selector("#showcase-calyx .showcase-steps").bounding_box()
                detail = page.query_selector("#showcase-calyx .showcase-detail").bounding_box()
                box_heights.append(round(box["height"], 2))
                page.screenshot(path=os.path.join(OUT, f"calyx-{k}-rest.png"),
                                 clip={"x": 0, "y": 0, "width": 1440, "height": 900})
                p_change = (k + 0.22) / n
                jump_to(page, start, end, p_change)
                page.screenshot(path=os.path.join(OUT, f"calyx-{k}-change.png"),
                                 clip={"x": 0, "y": 0, "width": 1440, "height": 900})
            print("calyx steps-cell heights per step (rest):", box_heights,
                  "constant:", (max(box_heights) - min(box_heights) < 1))
            print("calyx detail cell bbox (last measured):", detail)

            for k in [1, 2, 4]:
                jump_to(page, start, end, 0.98)
                p_rest = (k + 0.95) / n
                jump_to(page, start, end, p_rest)
                page.screenshot(path=os.path.join(OUT, f"calyx-{k}-back.png"),
                                 clip={"x": 0, "y": 0, "width": 1440, "height": 900})

            btn = page.query_selector('.case-choice[data-case="horai"]')
            btn.click()
            page.wait_for_timeout(1200)
            rng2 = get_pin_range(page)
            start2, end2 = rng2["start"], rng2["end"]

            n = 6
            box_heights_h = []
            for k in range(n):
                p_rest = (k + 0.95) / n
                jump_to(page, start2, end2, p_rest)
                box = page.query_selector("#showcase-horai .showcase-steps").bounding_box()
                detail = page.query_selector("#showcase-horai .showcase-detail").bounding_box()
                box_heights_h.append(round(box["height"], 2))
                page.screenshot(path=os.path.join(OUT, f"horai-{k}-rest.png"),
                                 clip={"x": 0, "y": 0, "width": 1440, "height": 900})
                p_change = (k + 0.22) / n
                jump_to(page, start2, end2, p_change)
                page.screenshot(path=os.path.join(OUT, f"horai-{k}-change.png"),
                                 clip={"x": 0, "y": 0, "width": 1440, "height": 900})
            print("horai steps-cell heights per step (rest):", box_heights_h,
                  "constant:", (max(box_heights_h) - min(box_heights_h) < 1))
            print("horai detail cell bbox (last measured):", detail)

            for k in [1, 3, 5]:
                jump_to(page, start2, end2, 0.98)
                p_rest = (k + 0.95) / n
                jump_to(page, start2, end2, p_rest)
                page.screenshot(path=os.path.join(OUT, f"horai-{k}-back.png"),
                                 clip={"x": 0, "y": 0, "width": 1440, "height": 900})

            gap_info = page.evaluate("""() => {
                const bh = document.querySelector('#showcase-horai .showcase-box-head').getBoundingClientRect();
                const st = document.querySelector('#showcase-horai .showcase-steps').getBoundingClientRect();
                const dt = document.querySelector('#showcase-horai .showcase-detail').getBoundingClientRect();
                return {
                    boxHeadBottom: bh.bottom, stepsTop: st.top, stepsBottom: st.bottom, detailTop: dt.top,
                    gap1: st.top - bh.bottom, gap2: dt.top - st.bottom
                };
            }""")
            print("gap check (should be ~1px each):", gap_info)
            print("page errors:", errors)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
