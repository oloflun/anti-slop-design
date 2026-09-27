#!/usr/bin/env python3
"""Pinned-showcase motion probe (V3f "Exempelcase" -> "#showcase").
Measures rAF frame pacing + scrollY traces around clicking the Hoerai
case-choice button, and through the whole pinned showcase scroll.

Serve the repo root first, e.g.:
  python "C:/Users/Anton L/.agents/skills/design/scripts/serve.py" --port 3305 --root .

Usage:
  python showcase_probe.py <url> <outdir> [--width 1440] [--headed] [--busy-loop-check]

--busy-loop-check injects a 40ms busy-wait into every rAF callback (via
page.add_init_script) before loading the page, as a falsification check:
frame pacing over the click window must then show p95 > 33ms. It does not
write screenshots/sheet.png/result.json to <outdir> -- only prints stats.
"""
import argparse
import json
import os
import statistics
import sys
import time

from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

CLICK_SHOT_TIMES_MS = [60, 150, 250, 400, 800, 1400]
CLICK_WINDOW_MS = 1500
THROUGH_STEP_PX = 450
WHEEL_STEP_PX = 120
WHEEL_DELAY_MS = 16

BUSY_LOOP_INIT_SCRIPT = """
(() => {
  const origRAF = window.requestAnimationFrame.bind(window);
  window.requestAnimationFrame = function(cb) {
    return origRAF(function(t) {
      const end = performance.now() + 40;
      while (performance.now() < end) { /* ponytail: deliberate busy-wait for falsification check */ }
      cb(t);
    });
  };
})();
"""

RECORDER_INIT_SCRIPT = """
(() => {
  window.__probe = { frameDeltas: [], scrollYs: [], iframeYs: [], recording: false };
  let last = performance.now();
  function frame(t) {
    if (window.__probe.recording) {
      window.__probe.frameDeltas.push(t - last);
      window.__probe.scrollYs.push(window.scrollY);
      let iy = null;
      try {
        // R5: the active/inactive contract moved from an inline
        // display:none string (V3g R4) to opacity/visibility (V3g R5 -
        // both iframes stay laid out and painted so a switch never forces
        // a fresh layout/decode mid-scroll). A selector keyed to the old
        // "display: none" string always matched the FIRST iframe in DOM
        // order once neither iframe carried that string, silently
        // recording the wrong (inactive) iframe's scrollY. Select by
        // actual rendered opacity instead, which still tracks whichever
        // case is really being shown regardless of the hiding mechanism.
        const frames = Array.prototype.slice.call(document.querySelectorAll('#showcase iframe'));
        const f = frames.find(function(fr){ return parseFloat(getComputedStyle(fr).opacity) > 0.5; }) || frames[0];
        iy = f && f.contentWindow ? f.contentWindow.scrollY : null;
      } catch (e) { iy = null; }
      window.__probe.iframeYs.push(iy);
    }
    last = t;
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
"""


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("outdir")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--headed", action="store_true")
    ap.add_argument("--no-shots", action="store_true",
                    help="Timing-only pass: no screenshots, so page.screenshot() stalls (~0.5 s each) never enter the frame trace.")
    ap.add_argument("--busy-loop-check", action="store_true",
                     help="Falsification check: inject a 40ms rAF busy-loop, print click-window frame stats, exit.")
    return ap.parse_args()


def shot(page, path, retries=3):
    for i in range(retries):
        try:
            page.screenshot(path=path)
            return True
        except Exception as e:
            if "Unable to capture screenshot" in str(e) and i < retries - 1:
                page.wait_for_timeout(200)
                continue
            raise
    return False


def start_recording(page):
    page.evaluate("() => { window.__probe.frameDeltas = []; window.__probe.scrollYs = []; window.__probe.iframeYs = []; window.__probe.recording = true; }")


def stop_recording(page):
    page.evaluate("() => { window.__probe.recording = false; }")
    return page.evaluate("() => ({ frameDeltas: window.__probe.frameDeltas, scrollYs: window.__probe.scrollYs, iframeYs: window.__probe.iframeYs })")


def scroll_until_visible(page, selector, max_steps=200):
    for _ in range(max_steps):
        vis = page.evaluate(
            """(sel) => {
                const el = document.querySelector(sel);
                if (!el) return false;
                const r = el.getBoundingClientRect();
                return r.top < window.innerHeight && r.bottom > 0;
            }""",
            selector,
        )
        if vis:
            return True
        page.mouse.wheel(0, WHEEL_STEP_PX)
        page.wait_for_timeout(WHEEL_DELAY_MS)
    return False


def wait_for_lenis_settle(page, max_wait_ms=2000, poll_ms=50, velocity_eps=0.05):
    """Lenis (lerp:0.1) keeps easing toward its target for a while after the
    last wheel event. page.click()'s own actionability check repeatedly
    fails while the target element's box is still moving under that ease,
    which silently inflates click() latency by seconds (measured: ~3.1s
    settling vs ~0.3s once actually still) -- exactly the kind of delay
    that would corrupt "ms after click" screenshot timing. Poll real Lenis
    velocity instead of guessing a fixed wait."""
    waited = 0
    while waited < max_wait_ms:
        v = page.evaluate("() => window.__lenis ? Math.abs(window.__lenis.velocity) : 0")
        if v < velocity_eps:
            return
        page.wait_for_timeout(poll_ms)
        waited += poll_ms


def frame_stats(deltas):
    deltas = sorted(d for d in deltas if d and d > 0)
    n = len(deltas)
    if not n:
        return {"count": 0, "median_ms": None, "p95_ms": None, "p99_ms": None, "max_ms": None, "over_33ms_count": 0}

    def pct(p):
        return deltas[min(n - 1, int(n * p))]

    return {
        "count": n,
        "median_ms": round(statistics.median(deltas), 2),
        "p95_ms": round(pct(0.95), 2),
        "p99_ms": round(pct(0.99), 2),
        "max_ms": round(deltas[-1], 2),
        "over_33ms_count": sum(1 for d in deltas if d > 33),
    }


def biggest_scrolly_jump(scroll_ys):
    max_jump = 0
    for i in range(1, len(scroll_ys)):
        a, b = scroll_ys[i - 1], scroll_ys[i]
        if a is None or b is None:
            continue
        max_jump = max(max_jump, abs(b - a))
    return round(max_jump, 2)


def iframe_scroll_stats(iframe_ys):
    max_delta = 0.0
    stall_then_lurch = 0
    stall_run = 0
    for i in range(1, len(iframe_ys)):
        a, b = iframe_ys[i - 1], iframe_ys[i]
        if a is None or b is None:
            stall_run = 0
            continue
        d = abs(b - a)
        max_delta = max(max_delta, d)
        if d < 0.5:
            stall_run += 1
        else:
            if stall_run >= 8 and d > 20:
                stall_then_lurch += 1
            stall_run = 0
    return {
        "max_single_frame_delta_px": round(max_delta, 2),
        "stall_then_lurch_events": stall_then_lurch,
        "total_frames": len(iframe_ys),
    }


def pin_active(page):
    """ScrollTrigger pins '.showcase-stage' -> its own pin-spacer wraps that
    element (not #showcase). Present only on desktop (>=768px); absent by
    design on mobile (no pin there, see index.html matchMedia isMobile)."""
    return page.evaluate(
        """() => {
            const stage = document.querySelector('.showcase-stage');
            const p = stage && stage.parentElement;
            return !!(p && p.classList && p.classList.contains('pin-spacer'));
        }"""
    )


def stitch_sheet(paths, out_path, cols=4, tile_w=480):
    paths = [p for p in paths if os.path.exists(p)]
    if not paths:
        return
    imgs = [Image.open(p) for p in paths]
    tile_h = int(tile_w * imgs[0].height / imgs[0].width)
    label_h = 22
    rows = (len(imgs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile_w, rows * (tile_h + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, (path, img) in enumerate(zip(paths, imgs)):
        col, row = i % cols, i // cols
        x, y = col * tile_w, row * (tile_h + label_h)
        draw.rectangle([x, y, x + tile_w, y + label_h], fill=(20, 20, 20))
        draw.text((x + 4, y + 4), os.path.basename(path), fill="white")
        sheet.paste(img.resize((tile_w, tile_h)), (x, y + label_h))
    sheet.save(out_path)


def launch_browser(p, headed):
    """Always headless: no window ever lands on Anton's desktop (2026-09-25,
    headed probes piled up and crashed the machine). `headed` is kept for CLI
    compatibility and now means "headless with GPU" -- the new-headless
    Chromium channel with the GPU forced on, which renders like a real window
    and gives frame timing close to headed (the old headless shell has no GPU
    and inflates frame times 5-10x)."""
    if headed:
        try:
            return p.chromium.launch(headless=True, channel="chromium",
                                     args=["--enable-gpu", "--ignore-gpu-blocklist",
                                           "--use-angle=d3d11", "--enable-unsafe-swiftshader"]), "headless-gpu"
        except Exception as e:
            print(f"[showcase_probe] headless-gpu launch failed ({e}); falling back to headless shell", file=sys.stderr)
    return p.chromium.launch(headless=True), "headless-shell"


def capture_click_window(page, outdir=None):
    """Click the Hoerai case-choice button, record rAF frame/scroll traces
    for CLICK_WINDOW_MS, and (if outdir given) grab screenshots at the
    spec'd offsets. Returns (trace_dict, shot_paths, actual_duration_ms).
    actual_duration_ms can exceed the nominal 1.5s when the page's main
    thread stalls (e.g. the Hoerai iframe's own navigation/layout) long
    enough to overrun a wait_for_timeout call -- that overrun is itself
    real, observable jank, not a measurement bug, so it's reported rather
    than silently clipped."""
    start_recording(page)
    page.click('button.case-choice[data-case="horai"]')
    # t0 = when the click actually landed, not when we called click() -- see
    # wait_for_lenis_settle: click() itself can block for seconds waiting
    # for Playwright's actionability/stability check, so timing "ms after
    # click" screenshots from before the call would be off by that delay.
    t0 = time.time()

    shot_paths = []
    for ms in CLICK_SHOT_TIMES_MS:
        wait = ms - (time.time() - t0) * 1000
        if wait > 0:
            page.wait_for_timeout(wait)
        if outdir is not None:
            path = os.path.join(outdir, f"click-{ms:04d}ms.png")
            shot(page, path)
            shot_paths.append(path)

    remaining = CLICK_WINDOW_MS - (time.time() - t0) * 1000
    if remaining > 0:
        page.wait_for_timeout(remaining)

    trace = stop_recording(page)
    actual_duration_ms = round((time.time() - t0) * 1000, 1)
    return trace, shot_paths, actual_duration_ms


def run_busy_loop_check(url, width):
    height = 844 if width < 500 else 900
    with sync_playwright() as p:
        browser, headed_used = launch_browser(p, headed=False)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.add_init_script(BUSY_LOOP_INIT_SCRIPT)
        page.add_init_script(RECORDER_INIT_SCRIPT)
        page.goto(url, wait_until="load", timeout=30000)
        page.wait_for_timeout(1500)
        scroll_until_visible(page, "#exempelcase")
        wait_for_lenis_settle(page)
        trace, _, actual_ms = capture_click_window(page, outdir=None)
        browser.close()
    stats = frame_stats(trace["frameDeltas"])
    stats["actual_duration_ms"] = actual_ms
    print("[falsification] busy-loop click-window frame_stats:", json.dumps(stats))
    return stats


def run(url, outdir, width, headed, no_shots=False):
    os.makedirs(outdir, exist_ok=True)
    height = 844 if width < 500 else 900
    result = {"url": url, "width": width, "height": height}

    with sync_playwright() as p:
        browser, headed_used = launch_browser(p, headed)
        result["headed"] = headed_used
        page = browser.new_page(viewport={"width": width, "height": height})
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.add_init_script(RECORDER_INIT_SCRIPT)
        page.goto(url, wait_until="load", timeout=30000)
        page.wait_for_timeout(1500)

        # 1. scroll with real wheel until the picker is in view
        scroll_until_visible(page, "#exempelcase")
        wait_for_lenis_settle(page)

        # 2+3. click Hoerai, record + screenshot the transition window
        click_trace, click_shots, click_actual_ms = capture_click_window(page, None if no_shots else outdir)
        result["click_window"] = {
            "nominal_duration_ms": CLICK_WINDOW_MS,
            "actual_duration_ms": click_actual_ms,
            "frame_stats": frame_stats(click_trace["frameDeltas"]),
            "biggest_window_scrollY_jump_px": biggest_scrolly_jump(click_trace["scrollYs"]),
            "iframe_scroll": iframe_scroll_stats(click_trace["iframeYs"]),
        }
        result["pin_active_after_click"] = pin_active(page)

        # 4. wheel-scroll through the whole pin + 1 viewport beyond
        pin = page.evaluate(
            """() => {
                const st = window.ScrollTrigger && window.ScrollTrigger.getAll().find(t => t.trigger && t.trigger.id === 'showcase');
                return st ? { start: st.start, end: st.end } : null;
            }"""
        )
        cur_y = page.evaluate("() => window.scrollY")
        if pin:
            total_through_px = max(height, (pin["end"] - cur_y) + height)
        else:
            # mobile: no pin (matchMedia isMobile branch) - fall back to the
            # section's own natural height + 1 viewport.
            sec_h = page.evaluate("() => { const el = document.getElementById('showcase'); return el ? el.offsetHeight : 0; }")
            total_through_px = sec_h + height
        result["through_scroll_target_px"] = round(total_through_px)

        start_recording(page)
        through_shots = []
        scrolled = 0
        next_shot_at = 0
        idx = 0
        while scrolled < total_through_px:
            page.mouse.wheel(0, WHEEL_STEP_PX)
            page.wait_for_timeout(WHEEL_DELAY_MS)
            scrolled += WHEEL_STEP_PX
            if not no_shots and scrolled >= next_shot_at:
                path = os.path.join(outdir, f"through-{idx:02d}.png")
                shot(page, path)
                through_shots.append(path)
                idx += 1
                next_shot_at += THROUGH_STEP_PX
        through_trace = stop_recording(page)
        result["through_scroll"] = {
            "frame_stats": frame_stats(through_trace["frameDeltas"]),
            "iframe_scroll": iframe_scroll_stats(through_trace["iframeYs"]),
        }

        result["console_errors"] = errors
        browser.close()

    result["no_shots"] = no_shots
    if click_shots or through_shots:
        stitch_sheet(click_shots + through_shots, os.path.join(outdir, "sheet.png"))

    with open(os.path.join(outdir, "result.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


LOCK = os.path.join(os.environ.get("TEMP", "/tmp"), "alunix-browser.lock")


def single_flight():
    """One browser run at a time across every probe/verify process: wait for
    the lock file (stale after 15 min), then hold it until exit."""
    if os.environ.get("ALUNIX_BROWSER_LOCK_HELD"):
        return  # held by browser_lock.py around us
    import atexit
    deadline = time.time() + 1800
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode()); os.close(fd)
            atexit.register(lambda: os.path.exists(LOCK) and os.remove(LOCK))
            return
        except FileExistsError:
            if time.time() - os.path.getmtime(LOCK) > 900:
                os.remove(LOCK); continue
            if time.time() > deadline:
                sys.exit("[showcase_probe] browser lock held too long: " + LOCK)
            time.sleep(2)


if __name__ == "__main__":
    single_flight()
    args = parse_args()
    if args.busy_loop_check:
        run_busy_loop_check(args.url, args.width)
    else:
        run(args.url, args.outdir, args.width, args.headed, args.no_shots)
