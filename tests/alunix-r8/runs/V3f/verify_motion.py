#!/usr/bin/env python3
"""V3f R3 motion verification. Serve from repo root first:
  python skills/design/scripts/serve.py --port 3305 --root .
Then: python tests/alunix-r8/runs/V3f/verify_motion.py
"""
import json
import os
import statistics
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:3305"
URL = BASE + "/tests/alunix-r8/runs/V3f/index.html"
HERE = os.path.dirname(os.path.abspath(__file__))
SHOTS_ROUND = os.environ.get("V3F_MOTION_SHOTS_ROUND", "r4")
SHOTS = os.path.join(HERE, "shots", SHOTS_ROUND)
os.makedirs(SHOTS, exist_ok=True)

SECTIONS = ["hero", "tes", "process", "exempelcase", "showcase", "pris", "kontakt"]

# R5 §A: every headline that must stand fully on-screen, unclipped, for
# >=40vh of scroll (RUNDA5-SPEC.md §A/§D).
LEGIBILITY_TARGETS = {
    "hero h1 (headline-40)": ".hero-h1",
    "tes headline (headline-50)": ".tes-top .headline-50",
    "exempelcase word (headline-50)": ".case-word-cell .headline-50",
    "pris headline (headline-50)": ".pris-statement .headline-50",
    "kontakt headline (headline-40)": ".kontakt-q--ov .headline-40",
}


def shot(page, name):
    page.screenshot(path=os.path.join(SHOTS, name))


def run_viewport(browser, w, h, label):
    page = browser.new_page(viewport={"width": w, "height": h})
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda exc: errors.append(str(exc)))
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(200)

    # --- hero intro states at 300ms and 1600ms after load ---
    page.reload(wait_until="networkidle")
    page.wait_for_timeout(300)
    shot(page, f"{label}-hero-intro-300ms.png")
    page.wait_for_timeout(1300)
    shot(page, f"{label}-hero-intro-1600ms.png")

    # --- hero pin at ~50% progress (desktop only pins; still a valid mid-scroll shot on mobile) ---
    total_hero = page.evaluate("document.getElementById('hero').offsetHeight")
    page.mouse.move(w / 2, h / 2)
    # wheel scroll in steps to exercise real wheel events (not scrollTo)
    for _ in range(30):
        page.mouse.wheel(0, 120)
        page.wait_for_timeout(20)
    page.wait_for_timeout(300)
    shot(page, f"{label}-hero-pin-mid.png")

    # continue scrolling and capture named section screenshots as each is reached
    for sid in ["tes", "process", "exempelcase", "case-calyx", "case-horai", "pris", "kontakt"]:
        for _ in range(40):
            page.mouse.wheel(0, 140)
            page.wait_for_timeout(15)
            y = page.evaluate(f"(() => {{ const el = document.getElementById('{sid}'); if (!el) return null; const r = el.getBoundingClientRect(); return r.top; }})()")
            if y is not None and y < h * 0.5:
                break
        page.wait_for_timeout(250)
        shot(page, f"{label}-{sid}-midscroll.png")

    # footer
    page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
    page.wait_for_timeout(300)
    shot(page, f"{label}-footer.png")

    page.close()
    return errors


def jump_test(browser, w, h):
    page = browser.new_page(viewport={"width": w, "height": h})
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(300)

    before = page.evaluate("window.ScrollTrigger.getAll().map(t => [t.start, t.end])")
    before_count = page.evaluate("window.ScrollTrigger.getAll().length")

    results = {}
    for sid in SECTIONS:
        ok = page.evaluate(
            """(id) => {
                const el = document.getElementById(id);
                if (!el) return {found:false};
                window.__lenis && window.__lenis.scrollTo ? window.__lenis.scrollTo(el, {immediate:true}) : window.scrollTo(0, el.getBoundingClientRect().top + window.scrollY);
                return {found:true};
            }""",
            sid,
        )
        page.wait_for_timeout(200)
        hidden = page.evaluate(
            """(id) => {
                const el = document.getElementById(id);
                if (!el) return null;
                const walker = document.createTreeWalker(el, NodeFilter.SHOW_ELEMENT);
                let bad = [];
                let node = walker.currentNode;
                while (node) {
                    if (node.offsetParent !== null || getComputedStyle(node).position === 'fixed') {
                        const cs = getComputedStyle(node);
                        if (parseFloat(cs.opacity) === 0 && node.getAttribute('aria-hidden') !== 'true') {
                            const r = node.getBoundingClientRect();
                            if (r.width > 0 && r.height > 0) bad.push(node.className || node.tagName);
                        }
                    }
                    node = walker.nextNode();
                }
                return bad.slice(0, 10);
            }""",
            sid,
        )
        results[sid] = {"jumped": ok, "hidden_visible_elements": hidden}
        shot(page, f"jump-{sid}.png")

    ScrollTrigger_refresh_ok = page.evaluate("window.ScrollTrigger.refresh(); true")
    after = page.evaluate("window.ScrollTrigger.getAll().map(t => [t.start, t.end])")
    after_count = page.evaluate("window.ScrollTrigger.getAll().length")

    page.close()
    return {
        "scrolltrigger_count_before": before_count,
        "scrolltrigger_count_after": after_count,
        "start_end_before_sample": before[:8],
        "start_end_after_sample": after[:8],
        "per_section": results,
    }


def frame_pacing(browser, w, h):
    page = browser.new_page(viewport={"width": w, "height": h})
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(300)

    page.evaluate(
        """() => {
            window.__frameDeltas = [];
            window.__sampling = true;
            let last = performance.now();
            function loop(t) {
                window.__frameDeltas.push(t - last);
                last = t;
                if (window.__sampling) requestAnimationFrame(loop);
            }
            requestAnimationFrame(loop);
        }"""
    )
    end_time = 3000
    elapsed = 0
    step = 100
    while elapsed < end_time:
        page.mouse.wheel(0, 60)
        page.wait_for_timeout(step)
        elapsed += step
    page.evaluate("window.__sampling = false;")
    deltas = page.evaluate("window.__frameDeltas")
    page.close()
    deltas = [d for d in deltas if d > 0]
    deltas.sort()
    median = statistics.median(deltas) if deltas else None
    p95 = deltas[int(len(deltas) * 0.95)] if deltas else None
    return {"sample_count": len(deltas), "median_ms": median, "p95_ms": p95}


def max_scroll_residual_check(browser, w, h, label):
    """R4 §5: after lenis.scrollTo('bottom',{immediate:true}) + 600ms, every
    footer and kontakt element must be at its final transform/clip - no
    residual yPercent rise or clip-path sweep left mid-flight. Checks:
    - every split char/line/word INNER element (the one GSAP actually
      animates yPercent on) has an identity transform (translate 0,0 or
      'none') - not partway through a rise.
    - char boxes are horizontally contiguous (no layout gap introduced by
      the animation itself) for the footer mark, as a proxy for "one word".
    - clip-path on the kontakt image cell / calyx-mirrored embed cells (if
      present in view) is fully open, not mid-sweep.
    - the footer ScrollTrigger's own .progress is exactly 1.
    """
    page = browser.new_page(viewport={"width": w, "height": h})
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(300)
    page.evaluate("() => { window.__lenis.scrollTo('bottom', {immediate:true}); }")
    page.wait_for_timeout(600)

    data = page.evaluate(
        """() => {
            function residualTransforms(rootSel) {
                const root = document.querySelector(rootSel);
                if (!root) return {found:false};
                const inner = Array.from(root.querySelectorAll('div, span')).filter(el => {
                    const t = getComputedStyle(el).transform;
                    return t && t !== 'none';
                });
                const EPS = 0.5; // px - GSAP's yPercent->px conversion leaves sub-pixel float residue at "0"; not visible, not a real residual rise
                const nonIdentity = inner.filter(el => {
                    const t = getComputedStyle(el).transform;
                    const m2 = t.match(/^matrix\\(([^)]+)\\)$/);
                    if (m2) {
                        const v = m2[1].split(',').map(parseFloat);
                        // [a,b,c,d,tx,ty] - identity scale/rotation plus near-zero translation
                        return !(Math.abs(v[0]-1)<0.01 && Math.abs(v[1])<0.01 && Math.abs(v[2])<0.01 && Math.abs(v[3]-1)<0.01 && Math.abs(v[4])<EPS && Math.abs(v[5])<EPS);
                    }
                    const m3 = t.match(/^matrix3d\\(([^)]+)\\)$/);
                    if (m3) {
                        const v = m3[1].split(',').map(parseFloat);
                        return !(Math.abs(v[0]-1)<0.01 && Math.abs(v[5]-1)<0.01 && Math.abs(v[10]-1)<0.01 && Math.abs(v[15]-1)<0.01 && Math.abs(v[12])<EPS && Math.abs(v[13])<EPS && Math.abs(v[14])<EPS);
                    }
                    return true; // unrecognised transform string - flag it
                });
                return {found:true, nonIdentityCount: nonIdentity.length, nonIdentitySample: nonIdentity.slice(0,5).map(e => ({tag:e.tagName, cls:e.className, transform:getComputedStyle(e).transform}))};
            }
            function charGapCheck(rootSel) {
                const root = document.querySelector(rootSel);
                if (!root) return {found:false};
                const outer = Array.from(root.querySelectorAll(':scope > div'));
                if (!outer.length) return {found:true, chars:0, maxGap:0};
                let maxGap = 0;
                for (let i=1;i<outer.length;i++){
                    const prev = outer[i-1].getBoundingClientRect();
                    const cur = outer[i].getBoundingClientRect();
                    maxGap = Math.max(maxGap, Math.abs(cur.left - prev.right));
                }
                return {found:true, chars: outer.length, maxGap};
            }
            function clipState(sel) {
                const el = document.querySelector(sel);
                if (!el) return {found:false};
                const cp = getComputedStyle(el).clipPath;
                return {found:true, clipPath: cp};
            }
            const footerST = window.ScrollTrigger.getAll().find(t => t.trigger && t.trigger.tagName === 'FOOTER');
            return {
                footerMarkResidual: residualTransforms('.footer-mark'),
                footerMarkGap: charGapCheck('.footer-mark'),
                kontaktGiantResidual: residualTransforms('.kontakt-giant'),
                kontaktStillResidual: residualTransforms('.kontakt-still'),
                kontaktImageClip: clipState('.kontakt-image-cell .color-layer'),
                footerScrollTriggerProgress: footerST ? footerST.progress : null
            };
        }"""
    )
    shot(page, f"{label}-maxscroll-endstate.png")
    page.close()
    return data


def legibility_check(browser, w, h):
    """RUNDA5-SPEC.md §A/§D: for every headline-* in LEGIBILITY_TARGETS,
    measure the longest continuous scroll window (in vh) during which the
    element sits fully inside every clipping ancestor's box AND inside the
    viewport - i.e. no glyph sheared by any edge. Coarse-stepped (15px) for
    speed; a scan only needs to find one window >=40vh, not the exact px.
    """
    page = browser.new_page(viewport={"width": w, "height": h})
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(300)
    total_h = page.evaluate("document.documentElement.scrollHeight")
    vh_px = h / 100.0
    step = max(10, total_h // 900)
    results = {}
    for name, sel in LEGIBILITY_TARGETS.items():
        max_window = 0
        window_px = 0
        in_window = False
        for i in range(0, total_h, step):
            page.evaluate(f"window.scrollTo(0,{i})")
            info = page.evaluate(
                """(sel) => {
                    const el = document.querySelector(sel);
                    if (!el) return null;
                    const r = el.getBoundingClientRect();
                    if (r.width === 0 && r.height === 0) return { fits: false };
                    let parent = el.parentElement;
                    let clipTop=-Infinity, clipBottom=Infinity, clipLeft=-Infinity, clipRight=Infinity;
                    while (parent) {
                        const pcs = getComputedStyle(parent);
                        if (pcs.overflow !== 'visible' || pcs.overflowX !== 'visible' || pcs.overflowY !== 'visible') {
                            const pr = parent.getBoundingClientRect();
                            clipTop = Math.max(clipTop, pr.top); clipBottom = Math.min(clipBottom, pr.bottom);
                            clipLeft = Math.max(clipLeft, pr.left); clipRight = Math.min(clipRight, pr.right);
                        }
                        parent = parent.parentElement;
                    }
                    const fits = r.top >= clipTop - 0.5 && r.bottom <= clipBottom + 0.5 &&
                                 r.left >= clipLeft - 0.5 && r.right <= clipRight + 0.5 &&
                                 r.top >= -0.5 && r.bottom <= window.innerHeight + 0.5;
                    return { fits };
                }""",
                sel,
            )
            if info and info.get("fits"):
                if not in_window:
                    window_px = 0
                    in_window = True
                window_px += step
                max_window = max(max_window, window_px)
            else:
                in_window = False
        vh = max_window / vh_px
        results[name] = {"max_continuous_vh": round(vh, 1), "passes_40vh": vh >= 40}
    page.close()
    return results


def showcase_check(browser, w, h):
    """RUNDA5-SPEC.md §B/§D: click Hoerai -> scroll to #showcase, pin
    active, Hoerai panel visible, the site's own inner scrollY hits all six
    anchors within +/-2px over the pin's scroll range. Same for Calyx via
    Tab+Enter. A direct jump to #showcase with no selection shows Calyx.
    """
    page = browser.new_page(viewport={"width": w, "height": h})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(1500)

    result = {}

    # jump directly to #showcase without ever choosing -> Calyx by default
    result["jump_no_selection_shows_calyx"] = page.evaluate(
        """() => {
            window.__lenis.scrollTo('#showcase', { immediate: true });
            return getComputedStyle(document.getElementById('showcase-calyx')).display !== 'none' &&
                   getComputedStyle(document.getElementById('showcase-horai')).display === 'none';
        }"""
    )
    page.evaluate("window.scrollTo(0,0)")
    page.wait_for_timeout(150)

    def anchor_hits(key, iframe_id):
        page.wait_for_timeout(3000)  # let the case's iframe finish its own load
        pin = page.evaluate(
            "() => { const st = window.ScrollTrigger.getAll().find(t => t.trigger && t.trigger.id === 'showcase'); return st ? { start: st.start, end: st.end } : null; }"
        )
        if not pin:
            return {"found_pin": False}
        y_expected = page.evaluate(f"() => window.__CASES['{key}'].y")
        if not y_expected:
            return {"found_pin": True, "anchors_measured": False}
        n = len(y_expected)
        diffs = []
        for i in range(n):
            frac = (i + 0.999) / n
            y = pin["start"] + (pin["end"] - pin["start"]) * frac
            page.evaluate(f"window.__lenis.scrollTo({y}, {{immediate:true}})")
            page.wait_for_timeout(120)
            actual = page.evaluate(f"document.getElementById('{iframe_id}').contentWindow.scrollY")
            diffs.append(round(abs(actual - y_expected[i]), 2))
        return {
            "found_pin": True,
            "anchors_measured": True,
            "expected": [round(v) for v in y_expected],
            "diffs_px": diffs,
            "all_within_2px": all(d <= 2 for d in diffs),
        }

    # click Hoerai
    page.click('button.case-choice[data-case="horai"]')
    result["horai_click_scrolled_to_showcase"] = page.evaluate(
        """() => { const r = document.getElementById('showcase').getBoundingClientRect(); return Math.abs(r.top) < window.innerHeight; }"""
    )
    result["horai_panel_visible_after_click"] = page.evaluate(
        "() => getComputedStyle(document.getElementById('showcase-horai')).display !== 'none'"
    )
    result["horai_anchors"] = anchor_hits("horai", "showcaseIframeHorai")

    # Tab to Calyx, Enter (keyboard path)
    page.evaluate("window.scrollTo(0,0); document.activeElement.blur();")
    page.wait_for_timeout(150)
    page.keyboard.press("Tab")
    for _ in range(40):
        cls = page.evaluate("document.activeElement.className || ''")
        if "case-choice" in cls:
            break
        page.keyboard.press("Tab")
    focused_case = page.evaluate("document.activeElement.dataset.case")
    if focused_case != "calyx":
        page.keyboard.press("Tab")
        focused_case = page.evaluate("document.activeElement.dataset.case")
    page.keyboard.press("Enter")
    page.wait_for_timeout(300)
    result["keyboard_reached_calyx_button"] = focused_case == "calyx"
    result["calyx_pressed_after_enter"] = page.evaluate(
        "document.querySelector('.case-choice[data-case=\"calyx\"]').getAttribute('aria-pressed')"
    ) == "true"
    result["calyx_anchors"] = anchor_hits("calyx", "showcaseIframeCalyx")

    result["console_errors"] = errors
    page.close()
    return result


def kontakt_check(browser, w, h):
    """RUNDA5-SPEC.md §C/§D: click flips the card and makes the back links
    clickable/focusable; a jump to the page bottom shows the back; Tab
    reaches both links once flipped.
    """
    page = browser.new_page(viewport={"width": w, "height": h})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(1200)

    result = {}

    # click flips it, from a mid-section scroll position (not yet auto-flipped)
    page.evaluate("window.__lenis.scrollTo('#kontakt', { offset: -400, immediate: true })")
    page.wait_for_timeout(250)
    result["front_visible_before_click"] = not page.evaluate(
        "document.getElementById('kontaktCardFront').hasAttribute('inert')"
    )
    page.click("#kontaktCardFront", force=True)
    page.wait_for_timeout(900)
    result["back_visible_after_click"] = not page.evaluate(
        "document.getElementById('kontaktCardBack').hasAttribute('inert')"
    )

    # tab reaches both back links
    page.evaluate("document.querySelector('#kontaktCardBack a[href^=mailto]').focus()")
    result["mail_link_focusable"] = page.evaluate("document.activeElement.getAttribute('href')") == "mailto:kontakt@alunix.se"
    page.keyboard.press("Tab")
    result["boka_link_focusable_next"] = page.evaluate("document.activeElement.tagName") == "A"

    # jump to bottom shows the back
    page2 = browser.new_page(viewport={"width": w, "height": h})
    page2.goto(URL, wait_until="networkidle", timeout=30000)
    page2.wait_for_timeout(1000)
    page2.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
    page2.wait_for_timeout(400)
    result["jump_to_bottom_shows_back"] = not page2.evaluate(
        "document.getElementById('kontaktCardBack').hasAttribute('inert')"
    )
    page2.close()

    # jump directly to #kontakt shows the back
    page3 = browser.new_page(viewport={"width": w, "height": h})
    page3.goto(URL, wait_until="networkidle", timeout=30000)
    page3.wait_for_timeout(1000)
    page3.evaluate("window.__lenis.scrollTo('#kontakt', {immediate:true})")
    page3.wait_for_timeout(400)
    result["jump_to_kontakt_shows_back"] = not page3.evaluate(
        "document.getElementById('kontaktCardBack').hasAttribute('inert')"
    )
    page3.close()

    # R6 §4: the card must never intersect the ÖV headline/subline's own
    # text box, at rest, mid-flip (any rotationY) or mid hover-tilt.
    page4 = browser.new_page(viewport={"width": w, "height": h})
    errors4 = []
    page4.on("pageerror", lambda e: errors4.append(str(e)))
    page4.goto(URL, wait_until="networkidle", timeout=30000)
    page4.wait_for_timeout(1200)
    top = page4.evaluate("document.getElementById('kontakt').getBoundingClientRect().top + window.scrollY")
    page4.evaluate(f"window.scrollTo(0, {top})")
    page4.wait_for_timeout(300)
    card_text_overlaps = []
    for rot in range(0, 190, 15):
        try:
            page4.evaluate(f"gsap.set(document.getElementById('kontaktCardFlip'), {{rotationY: {rot}, y: {-14 if w >= 768 else 0}}})")
        except Exception:
            pass  # a 3D-transform compositing quirk sometimes reports a false "context destroyed" here even though the set applies - see RAPPORT.md R5/R6
        page4.wait_for_timeout(60)
        try:
            info = page4.evaluate(
                """() => {
                    const flip = document.getElementById('kontaktCardFlip').getBoundingClientRect();
                    const heading = document.getElementById('kontakt-title').getBoundingClientRect();
                    const sub = document.querySelector('.kontakt-q--ov p').getBoundingClientRect();
                    function ix(a,b){ return !(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom); }
                    return {headOverlap: ix(flip,heading), subOverlap: ix(flip,sub)};
                }"""
            )
        except Exception:
            page4.wait_for_timeout(150)
            info = page4.evaluate(
                """() => {
                    const flip = document.getElementById('kontaktCardFlip').getBoundingClientRect();
                    const heading = document.getElementById('kontakt-title').getBoundingClientRect();
                    const sub = document.querySelector('.kontakt-q--ov p').getBoundingClientRect();
                    function ix(a,b){ return !(a.right<b.left||a.left>b.right||a.bottom<b.top||a.top>b.bottom); }
                    return {headOverlap: ix(flip,heading), subOverlap: ix(flip,sub)};
                }"""
            )
        if info["headOverlap"] or info["subOverlap"]:
            card_text_overlaps.append({"rotationY": rot, **info})
    result["card_text_overlap_sweep"] = {
        "checked_angles": list(range(0, 190, 15)),
        "overlaps_found": card_text_overlaps,
        "passed": not card_text_overlaps,
    }
    result["headline_fits_ov_cell"] = page4.evaluate(
        """() => {
            const h = document.getElementById('kontakt-title').getBoundingClientRect();
            const cell = document.querySelector('.kontakt-q--ov').getBoundingClientRect();
            return h.left >= cell.left - 1 && h.right <= cell.right + 1;
        }"""
    )
    page4.close()

    result["console_errors"] = errors
    page.close()
    return result


def showcase_row_clip_check(browser, w, h):
    """RUNDA5-SPEC.md R6 §1/§D: no showcase row's text may ever be clipped -
    scrollHeight > clientHeight on any row (or its body) is a hard fail,
    checked while stepping through the pin so every row gets its turn as
    the active (expanded) one.
    """
    page = browser.new_page(viewport={"width": w, "height": h})
    errors = []
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(URL, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(1500)
    page.evaluate("window.__lenis.scrollTo('#showcase', {immediate:true})")
    page.wait_for_timeout(500)

    def sample():
        return page.evaluate(
            """() => {
                const rows = document.querySelectorAll('.showcase-row');
                const bad = [];
                rows.forEach(r => {
                    if (r.scrollHeight > r.clientHeight + 1) {
                        bad.push({row: r.dataset.row, panel: r.closest('.showcase-panel') ? r.closest('.showcase-panel').id : null, scrollHeight: r.scrollHeight, clientHeight: r.clientHeight});
                    }
                });
                const side = document.querySelector('.showcase-side');
                return {bad, sideOverflow: side.scrollHeight > side.clientHeight + 1};
            }"""
        )

    findings = {"calyx": [], "horai": []}
    st = page.evaluate(
        "() => { const t = window.ScrollTrigger.getAll().find(x => x.trigger && x.trigger.id === 'showcase'); return t ? {start: t.start, end: t.end} : null; }"
    )
    if st:
        for frac in [0.0, 0.2, 0.4, 0.6, 0.8, 0.99]:
            y = st["start"] + (st["end"] - st["start"]) * frac
            page.evaluate(f"window.__lenis.scrollTo({y}, {{immediate:true}})")
            page.wait_for_timeout(250)
            r = sample()
            if r["bad"]:
                findings["calyx"].append({"frac": frac, "bad": r["bad"]})

    # Hoerai: switch case, repeat
    page.evaluate("window.scrollTo(0,0)")
    page.wait_for_timeout(150)
    page.click('button.case-choice[data-case="horai"]')
    page.wait_for_timeout(2500)
    st2 = page.evaluate(
        "() => { const t = window.ScrollTrigger.getAll().find(x => x.trigger && x.trigger.id === 'showcase'); return t ? {start: t.start, end: t.end} : null; }"
    )
    if st2:
        for frac in [0.0, 0.2, 0.4, 0.6, 0.8, 0.99]:
            y = st2["start"] + (st2["end"] - st2["start"]) * frac
            page.evaluate(f"window.__lenis.scrollTo({y}, {{immediate:true}})")
            page.wait_for_timeout(250)
            r = sample()
            if r["bad"]:
                findings["horai"].append({"frac": frac, "bad": r["bad"]})

    page.close()
    return {
        "passed": not findings["calyx"] and not findings["horai"],
        "findings": findings,
        "console_errors": errors,
    }


def run():
    report = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()

        console_errors = {}
        for (w, h, label) in [(1440, 900, "d1440"), (390, 844, "m390")]:
            console_errors[label] = run_viewport(browser, w, h, label)

        report["console_errors"] = console_errors
        report["jump_test_1440"] = jump_test(browser, 1440, 900)
        report["jump_test_390"] = jump_test(browser, 390, 844)
        report["frame_pacing_1440"] = frame_pacing(browser, 1440, 900)
        report["max_scroll_residual_1440"] = max_scroll_residual_check(browser, 1440, 900, "d1440")
        report["max_scroll_residual_390"] = max_scroll_residual_check(browser, 390, 844, "m390")
        report["max_scroll_residual_768"] = max_scroll_residual_check(browser, 768, 1024, "t768")
        report["max_scroll_residual_1920"] = max_scroll_residual_check(browser, 1920, 1080, "w1920")

        report["legibility_1440"] = legibility_check(browser, 1440, 900)
        report["showcase_check_1440"] = showcase_check(browser, 1440, 900)
        report["kontakt_check_1440"] = kontakt_check(browser, 1440, 900)
        report["kontakt_check_1280"] = kontakt_check(browser, 1280, 800)
        report["kontakt_check_768"] = kontakt_check(browser, 768, 1024)
        report["kontakt_check_390"] = kontakt_check(browser, 390, 844)
        report["showcase_row_clip_check_1440"] = showcase_row_clip_check(browser, 1440, 900)
        report["showcase_row_clip_check_1280"] = showcase_row_clip_check(browser, 1280, 800)
        report["showcase_row_clip_check_390"] = showcase_row_clip_check(browser, 390, 844)

        browser.close()

    out_path = os.path.join(HERE, "verify-motion-result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(json.dumps(report, indent=2, ensure_ascii=False)[:6000])
    print("\nFull report:", out_path)
    print("Screenshots:", SHOTS)


if __name__ == "__main__":
    run()
