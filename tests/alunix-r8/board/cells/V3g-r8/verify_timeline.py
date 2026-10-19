#!/usr/bin/env python3
"""R6 fas 2, punkt 3 (devices.md's timeline-regel): hoppa till varje steg i
bada casen (forward-jump direkt via progress) och skrolla bakat till tre av
dem; kontrollera att textens och figurens opacity ar 1 pa det aktiva steget
och 0 pa alla andra, och att tile-opaciteten (medel over rutnatet) ar nara 0
i vilofonstrets slut (bilden fardigst upplost) och nara 1 vid introningen
(nyss intonad, fortfarande rastrerad)."""
import os
from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:3307/tests/alunix-r8/runs/V3g/index.html"


def get_pin_range(page):
    return page.evaluate("""() => {
        const st = ScrollTrigger.getAll().find(s => s.trigger && s.trigger.id === 'showcase');
        return st ? {start: st.start, end: st.end} : null;
    }""")


def jump_to(page, start, end, p):
    y = start + p * (end - start)
    page.evaluate(f"() => window.__lenis.scrollTo({y}, {{immediate:true}})")
    page.wait_for_timeout(120)


def read_state(page, case_key, n):
    return page.evaluate(f"""() => {{
        const C = window.__CASES['{case_key}'];
        const textOps = C.textEls.map(el => parseFloat(getComputedStyle(el).opacity));
        const figOps = C.figures.map(el => parseFloat(getComputedStyle(el).opacity));
        const tileMeans = C.figureTiles.map(tiles => {{
            if (!tiles || !tiles.length) return null;
            const sum = tiles.reduce((a, t) => a + parseFloat(getComputedStyle(t).opacity), 0);
            return sum / tiles.length;
        }});
        return {{textOps, figOps, tileMeans, lastStep: C.lastStep}};
    }}""")


def check_case(page, case_key, n, start, end, rows):
    print(f"\n=== {case_key} (n={n}) ===")
    header = f"{'step':>4} | {'mode':>6} | {'lastStep':>8} | {'textOps (want 1 at active, 0 else)':>40} | {'figOps (want 1 at active, 0 else)':>36} | {'tileMean@rest (want ~0)':>10} | {'tileMean@intoo (want ~1)':>10}"
    print(header)
    for k in range(n):
        p_rest = (k + 0.95) / n
        jump_to(page, start, end, p_rest)
        st_rest = read_state(page, case_key, n)
        p_intoo = (k + 0.20) / n if k > 0 else 0.05 / n
        jump_to(page, start, end, p_intoo)
        st_intoo = read_state(page, case_key, n)
        text_ok = all(abs(v - (1 if i == k else 0)) < 0.05 for i, v in enumerate(st_rest["textOps"]))
        fig_ok = all(abs(v - (1 if i == k else 0)) < 0.05 for i, v in enumerate(st_rest["figOps"]))
        tile_rest = st_rest["tileMeans"][k]
        tile_intoo = st_intoo["tileMeans"][k]
        rows.append({
            "case": case_key, "step": k, "lastStep_rest": st_rest["lastStep"],
            "textOps_rest": [round(v, 2) for v in st_rest["textOps"]],
            "figOps_rest": [round(v, 2) for v in st_rest["figOps"]],
            "text_ok": text_ok, "fig_ok": fig_ok,
            "tile_mean_at_rest_end": round(tile_rest, 3) if tile_rest is not None else None,
            "tile_mean_at_intoo": round(tile_intoo, 3) if tile_intoo is not None else None,
        })
        print(f"{k:>4} | {'jump':>6} | {st_rest['lastStep']:>8} | "
              f"{str([round(v,2) for v in st_rest['textOps']]):>40} | "
              f"{str([round(v,2) for v in st_rest['figOps']]):>36} | "
              f"{tile_rest:>10.3f} | {tile_intoo:>10.3f}"
              if tile_rest is not None and tile_intoo is not None else "n/a")


def check_back(page, case_key, n, start, end, ks, rows):
    for k in ks:
        jump_to(page, start, end, 0.98)
        p_rest = (k + 0.95) / n
        jump_to(page, start, end, p_rest)
        st = read_state(page, case_key, n)
        text_ok = all(abs(v - (1 if i == k else 0)) < 0.05 for i, v in enumerate(st["textOps"]))
        fig_ok = all(abs(v - (1 if i == k else 0)) < 0.05 for i, v in enumerate(st["figOps"]))
        tile_rest = st["tileMeans"][k]
        rows.append({
            "case": case_key, "step": k, "mode": "back",
            "lastStep": st["lastStep"], "text_ok": text_ok, "fig_ok": fig_ok,
            "tile_mean_at_rest_end": round(tile_rest, 3) if tile_rest is not None else None,
        })
        print(f"BACK -> {case_key} step {k}: lastStep={st['lastStep']} text_ok={text_ok} fig_ok={fig_ok} tile_mean={tile_rest}")


def main():
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1440, "height": 900}, device_scale_factor=1)
            errors = []
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(URL, wait_until="load")
            page.wait_for_timeout(500)
            rng = get_pin_range(page)
            start, end = rng["start"], rng["end"]

            check_case(page, "calyx", 5, start, end, rows)
            check_back(page, "calyx", 5, start, end, [1, 2, 4], rows)

            btn = page.query_selector('.case-choice[data-case="horai"]')
            btn.click()
            page.wait_for_timeout(1200)
            rng2 = get_pin_range(page)
            start2, end2 = rng2["start"], rng2["end"]
            check_case(page, "horai", 6, start2, end2, rows)
            check_back(page, "horai", 6, start2, end2, [1, 3, 5], rows)

            print("\npage errors:", errors)

            all_text_ok = all(r.get("text_ok", True) for r in rows)
            all_fig_ok = all(r.get("fig_ok", True) for r in rows)
            print("\nALL text_ok:", all_text_ok, " ALL fig_ok:", all_fig_ok)
        finally:
            browser.close()


if __name__ == "__main__":
    main()
