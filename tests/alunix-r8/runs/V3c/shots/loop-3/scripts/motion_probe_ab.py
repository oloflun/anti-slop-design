#!/usr/bin/env python3
"""motion_probe.py - does the motion actually glide, or does it step?

The gap this closes
-------------------
Nothing in the chain measured frame time or value continuity. scroll_verify.py
proves a page CHANGES between scroll positions; upstream's own verify.md says
so in as many words: "the harness cannot tell you whether the motion is
smooth." That left F-012 ("scrolleffekten renderade som den skulle, men det
sag hackigt och billigt gjort ut") with no instrument at all, only hypotheses.

What it measures, per tracked property, while driving the page with a scripted
wheel at a fixed cadence:

  frame_p95_ms     95th percentile frame time
  frames_over_20ms / frames_over_33ms
  max_step         largest single-frame change, as % of the value's own range.
                   Gated (> 3 % fails) only on the damped playhead --sc-ps; on a
                   derived track it is reported, because a smoothstepped value
                   peaks at ~4.4 %/frame by its own derivative and `staircase`
                   is what catches a real step there. Never track raw --sc-p.
  staircase        frames where the value did NOT move and the next frame
                   jumped more than 3% of the range. This is the number that
                   names the F-012 failure: a page can hold 60fps and still
                   step, because the steps are in the VALUE, not the clock.
  reversals        sign flips that do not match the scroll direction

A page that renders correctly and still looks cheap shows a low frame_p95 and a
high staircase. That combination is the whole point of the script.

    python motion_probe.py --url URL --track "sel:prop,sel:prop" [--cpu 4]
                           [--wheel 100:60] [--out DIR] [--json]

`--track` takes CSS-selector:property pairs. A property starting with `--` is
read as a custom property; `transform` is decomposed into its translate and
rotation so a matrix does not read as noise.
"""
from __future__ import annotations

import argparse
import json
import math
import statistics
import sys
from pathlib import Path

PROBE_JS = r"""
(function (specs) {
  window.__mp = { frames: [], t0: performance.now() };
  function readOne(el, prop) {
    var cs = getComputedStyle(el);
    if (prop.slice(0, 2) === '--') {
      var v = parseFloat(cs.getPropertyValue(prop));
      return isNaN(v) ? null : v;
    }
    if (prop === 'transform') {
      var m = cs.transform;
      if (!m || m === 'none') return 0;
      var n = m.match(/matrix3?d?\(([^)]+)\)/);
      if (!n) return 0;
      var p = n[1].split(',').map(parseFloat);
      // 2D matrix(a,b,c,d,e,f): rotation from (a,b), translation from (e,f).
      if (p.length === 6) {
        var rot = Math.atan2(p[1], p[0]) * 180 / Math.PI;
        return rot !== 0 ? rot : p[5];
      }
      if (p.length === 16) {
        // Column-major matrix3d. A rotateY lives in m11/m31, NOT in the
        // translation column - reading p[13] returned a constant 0 for a
        // flipping card and made the probe blind to the very motion it was
        // pointed at (found 2026-09-08 on tests/motion/staircase.html).
        var ry = Math.atan2(-p[8], p[0]) * 180 / Math.PI;
        if (Math.abs(ry) > 1e-6) return ry;
        var rx = Math.atan2(p[9], p[10]) * 180 / Math.PI;
        if (Math.abs(rx) > 1e-6) return rx;
        return p[13];
      }
      return 0;
    }
    var f = parseFloat(cs.getPropertyValue(prop));
    return isNaN(f) ? null : f;
  }
  function frame(now) {
    var row = { t: now, y: window.scrollY, v: [] };
    for (var i = 0; i < specs.length; i++) {
      var el = document.querySelector(specs[i].sel);
      row.v.push(el ? readOne(el, specs[i].prop) : null);
    }
    window.__mp.frames.push(row);
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})(SPECS);
"""


def analyse(frames, spec_index, label):
    ts = [f["t"] for f in frames]
    deltas = [b - a for a, b in zip(ts, ts[1:]) if b > a]
    vals = [f["v"][spec_index] for f in frames]
    ys = [f["y"] for f in frames]

    pairs = [(v, y) for v, y in zip(vals, ys) if v is not None]
    if len(pairs) < 8:
        return {"track": label, "error": "for fa mätpunkter (elementet hittades inte?)"}
    vals = [p[0] for p in pairs]
    ys = [p[1] for p in pairs]

    # Unwrap an angle series. atan2 returns (-180, 180], so a rotateY passing
    # 90 degrees produces a 360-degree jump that is a coordinate artifact, not
    # motion - it reported max_step 100% on a perfectly smooth flip.
    if label.endswith(":transform") and any(abs(b - a) > 180 for a, b in zip(vals, vals[1:])):
        unwrapped, off = [vals[0]], 0.0
        for a, b in zip(vals, vals[1:]):
            d = b - a
            if d > 180:
                off -= 360
            elif d < -180:
                off += 360
            unwrapped.append(b + off)
        vals = unwrapped

    lo, hi = min(vals), max(vals)
    rng = (hi - lo) or 1.0
    dv = [b - a for a, b in zip(vals, vals[1:])]
    dy = [b - a for a, b in zip(ys, ys[1:])]

    # A staircase frame: the value did not move, and the very next frame jumped
    # more than 3% of its range.
    #
    # The first version also required scrollY to have changed on the flat
    # frame (`dy[i] != 0`) and therefore counted nothing: in a real staircase
    # BOTH are frozen between wheel notches and then both jump together. That
    # is the failure, not an exception to it. The run-level guard is that the
    # wheel is being driven at all, which the caller guarantees, plus a
    # requirement that the page actually moved somewhere during the window.
    scrolled = (max(ys) - min(ys)) > 1
    stair = 0
    if scrolled:
        for i in range(len(dv) - 1):
            if abs(dv[i]) <= 1e-9 and abs(dv[i + 1]) > 0.03 * rng:
                stair += 1

    rev = 0
    for i in range(1, len(dv)):
        if dv[i] * dv[i - 1] < 0 and dy[i] * dy[i - 1] > 0:
            rev += 1

    # DEAD: the value never moved while the page was driven. A property that
    # never changes is perfectly smooth by every other measure here, so without
    # this check the probe PASSES a completely dead animation - measured
    # 2026-09-08, when a wrongly registered custom property stopped inheriting
    # and the card stopped rotating entirely: staircase 0, max_step 0.00%, PASS.
    # A probe that green-lights a page where nothing happens is worse than no
    # probe. scroll_verify.py has the same check at the page level; this is it
    # per tracked property.
    dead = scrolled and (hi - lo) < 1e-6

    p95 = statistics.quantiles(deltas, n=20)[-1] if len(deltas) >= 20 else (max(deltas) if deltas else 0)
    return {
        "track": label,
        "dead": dead,
        "frames": len(frames),
        "frame_p95_ms": round(p95, 2),
        "frames_over_20ms": sum(1 for d in deltas if d > 20),
        "frames_over_33ms": sum(1 for d in deltas if d > 33),
        "value_range": [round(lo, 4), round(hi, 4)],
        "max_step_pct": round(100 * (max((abs(x) for x in dv), default=0) / rng), 2),
        "staircase": stair,
        "reversals": rev,
    }


def sparkline(path: Path, series, title):
    try:
        from PIL import Image, ImageDraw
    except Exception:
        return None
    w, h, pad = 900, 160, 12
    img = Image.new("RGB", (w, h), (253, 251, 244))
    d = ImageDraw.Draw(img)
    vals = [v for v in series if v is not None]
    if len(vals) < 2:
        return None
    lo, hi = min(vals), max(vals)
    rng = (hi - lo) or 1.0
    pts = []
    n = len(series)
    for i, v in enumerate(series):
        if v is None:
            continue
        x = pad + (w - 2 * pad) * i / max(n - 1, 1)
        y = h - pad - (h - 2 * pad) * (v - lo) / rng
        pts.append((x, y))
    d.line(pts, fill=(30, 94, 156), width=2)
    d.text((pad, 4), title, fill=(20, 23, 26))
    img.save(path)
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", required=True)
    ap.add_argument("--track", required=True,
                    help='comma-separated "selector:property" pairs, e.g. '
                         '"#hero:--sc-p,#hero:--sc-ps,.plate-card:transform"')
    ap.add_argument("--cpu", type=float, default=4.0, help="CPU throttling rate (1 = none)")
    ap.add_argument("--wheel", default="100:60", help="px per tick : ms between ticks")
    ap.add_argument("--ticks", type=int, default=40)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--out", default="")
    ap.add_argument("--start", default=None)
    ap.add_argument("--pre", default=None, help="JS to evaluate after load (A/B ablation), then 5 s settle")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    specs = []
    for part in args.track.split(","):
        part = part.strip()
        if not part:
            continue
        sel, _, prop = part.rpartition(":")
        if not sel or not prop:
            print("motion_probe: kan inte tolka '" + part + "' (vantar selektor:egenskap)",
                  file=sys.stderr)
            return 2
        specs.append({"sel": sel, "prop": prop})

    px, _, gap = args.wheel.partition(":")
    px, gap = int(px), int(gap or 60)

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print("motion_probe: playwright saknas (" + str(e) + ")", file=sys.stderr)
        return 2

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe")
        ctx = browser.new_context(viewport={"width": args.width, "height": args.height},
                                  device_scale_factor=1)
        page = ctx.new_page()
        if args.cpu and args.cpu > 1:
            cdp = ctx.new_cdp_session(page)
            cdp.send("Emulation.setCPUThrottlingRate", {"rate": args.cpu})
        page.add_init_script(PROBE_JS.replace("SPECS", json.dumps(specs)))
        try:
            page.goto(args.url, wait_until="networkidle", timeout=45000)
        except Exception:
            page.goto(args.url, wait_until="load", timeout=45000)
        page.wait_for_timeout(700)
        if args.pre:
            page.evaluate(args.pre)
            page.wait_for_timeout(5000)

        if args.start:
            page.evaluate("window.scrollTo(0, %s)" % ("document.documentElement.scrollHeight" if args.start=="bottom" else args.start))
            page.wait_for_timeout(2500)
        page.mouse.move(args.width // 2, args.height // 2)
        # Frames recorded before the first wheel tick belong to page load, not to
        # the scroll. Counting them made the known-good fixture (tests/motion/
        # smooth.html) fail the "0 frames > 33 ms" bar on its own load spike, and
        # a gate the reference build cannot pass measures nothing (gates.md,
        # "Both directions"). Mark the drag and drop everything before it.
        page.evaluate("window.__mp && (window.__mp.dragStart = performance.now())")
        for _ in range(args.ticks):
            page.mouse.wheel(0, px)
            page.wait_for_timeout(gap)
        page.wait_for_timeout(600)          # let any lerp land before we stop

        frames = page.evaluate("window.__mp ? window.__mp.frames : []")
        drag_start = page.evaluate("window.__mp ? (window.__mp.dragStart || 0) : 0")
        frames = [f for f in frames if f["t"] >= drag_start]
        browser.close()

    out = {"url": args.url, "wheel": args.wheel, "cpu": args.cpu, "tracks": []}
    for i, s in enumerate(specs):
        out["tracks"].append(analyse(frames, i, s["sel"] + ":" + s["prop"]))

    # Pass criteria (references/performance.md § 4).
    fails = []
    for t in out["tracks"]:
        if "error" in t:
            fails.append(t["track"] + ": " + t["error"]); continue
        if t.get("dead"):
            fails.append(t["track"] + ": DEAD - vardet rorde sig inte alls medan sidan "
                                      "scrollades (kontrollera att elementet arver "
                                      "egenskapen och att akten faktiskt driver den)")
            continue
        if t["frame_p95_ms"] > 20:
            fails.append(t["track"] + ": frame_p95 " + str(t["frame_p95_ms"]) + " ms > 20")
        if t["frames_over_33ms"]:
            fails.append(t["track"] + ": " + str(t["frames_over_33ms"]) + " frames > 33 ms")
        if t["staircase"]:
            fails.append(t["track"] + ": staircase " + str(t["staircase"]))
        # max_step is a continuity bar for the PLAYHEAD (--sc-p / --sc-ps): a
        # smoothed playhead that jumps more than 3 % of its range in one frame
        # is not smoothed. It is not a bar for derived properties: a value that
        # is deliberately eased (smoothstep on a card flip, a 1.2 s cubic-bezier
        # reveal) has a per-frame slope that exceeds 3 % at flawless 60 fps by
        # construction, so the bar failed every eased act and passed only linear
        # ones (r8 R2, 2026-09-10: V3c 4.12 % on the flip with staircase 0 and
        # p95 16.7 ms; the calyx reveal 8.47 % at 60 fps). For derived tracks
        # the F-013 faults are already caught above: staircase and frame time.
        is_playhead = t["track"].rsplit(":", 1)[-1].startswith("--sc-p")
        if is_playhead and t["max_step_pct"] > 3.0:
            fails.append(t["track"] + ": max_step " + str(t["max_step_pct"]) + " % > 3 (spelhuvud)")
    out["pass"] = not fails
    out["failures"] = fails

    if args.out:
        d = Path(args.out); d.mkdir(parents=True, exist_ok=True)
        (d / "motion_probe.json").write_text(json.dumps(out, indent=2, ensure_ascii=False),
                                             encoding="utf-8")
        for i, s in enumerate(specs):
            series = [f["v"][i] for f in frames]
            sparkline(d / ("track-%d.png" % i), series, s["sel"] + " " + s["prop"])
        sparkline(d / "frame-times.png",
                  [b["t"] - a["t"] for a, b in zip(frames, frames[1:])], "frame time (ms)")

    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print("motion_probe " + ("PASS" if out["pass"] else "FAIL") + "  " + args.url)
        for t in out["tracks"]:
            if "error" in t:
                print("  " + t["track"] + ": " + t["error"]); continue
            print("  %-34s p95 %5.1f ms | >33ms %2d | max_step %5.2f%% | staircase %3d | rev %2d%s"
                  % (t["track"], t["frame_p95_ms"], t["frames_over_33ms"],
                     t["max_step_pct"], t["staircase"], t["reversals"],
                     "  DEAD" if t.get("dead") else ""))
        for f in fails:
            print("  FAIL " + f)
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
