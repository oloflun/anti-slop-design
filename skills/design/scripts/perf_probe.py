#!/usr/bin/env python3
"""perf_probe.py - the performance budget, measured instead of assumed.

The gap this closes
-------------------
The chain had one line about performance ("Production build, then LCP and
CLS") and no script, no budget and no gate. Meanwhile r7 shipped a page with
three live iframes, ~100 WebP frames and a permanent `will-change: transform`,
and the only symptom anyone could name was "it looks cheap" - the same words
F-012 used for a different fault. This measures the things that produce that
sentence.

Checks, at one viewport per run:
  LCP, CLS, long tasks (>50ms), long tasks DURING a scripted scroll
  transfer weight by type, DOM node count
  <img> without width/height, without decoding, LCP image without
    fetchpriority, below-fold image without loading=lazy
  <iframe> without loading=lazy
  @font-face without font-display, missing preload for the display face
  elements with a resting `will-change` (nothing is animating, so nothing
    should be promoted)
  filter / backdrop-filter on a surface larger than half the viewport
  `transition: all`, `height: 100vh` without a dvh fallback

    python perf_probe.py --url URL [--cpu 4] [--width 1440] [--height 900]
                         [--budget budget.json] [--out DIR] [--json]

Exit 0 when every measured value is inside budget, 1 when something is out,
2 only on tool failure. Findings are data; the exit code is the verdict.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_BUDGET = {
    "lcp_ms": 1800,           # local, 4x CPU ~ 2.5s field (the CWV floor)
    "cls": 0.05,
    "long_tasks_during_scroll": 0,
    "frame_p95_ms": 20,
    "total_bytes": 2_500_000,
    "hero_image_bytes": 250_000,
    "font_files": 3,
    "font_bytes": 300_000,
    "dom_nodes": 1500,
    "resting_will_change": 0,
    "large_blur_surfaces": 0,
}

COLLECT_JS = r"""
(() => {
  const vw = innerWidth, vh = innerHeight;
  const big = (r) => (r.width * r.height) > (vw * vh * 0.5);
  const sel = (el) => {
    if (el.id) return '#' + el.id;
    const c = (el.className && el.className.baseVal !== undefined)
      ? el.className.baseVal : (el.className || '');
    const cls = String(c).trim().split(/\s+/).filter(Boolean).slice(0, 2).join('.');
    return el.tagName.toLowerCase() + (cls ? '.' + cls : '');
  };

  const imgs = [...document.images].map(im => {
    const r = im.getBoundingClientRect();
    return {
      sel: sel(im), src: (im.currentSrc || im.src || '').slice(-80),
      hasDims: im.hasAttribute('width') && im.hasAttribute('height'),
      decoding: im.getAttribute('decoding') || '',
      loading: im.getAttribute('loading') || '',
      fetchpriority: im.getAttribute('fetchpriority') || '',
      area: Math.round(r.width * r.height),
      aboveFold: r.top < vh && r.bottom > 0,
    };
  });

  const iframes = [...document.querySelectorAll('iframe')].map(f => ({
    sel: sel(f), loading: f.getAttribute('loading') || '',
    src: (f.getAttribute('src') || '').slice(-60),
  }));

  const restingWillChange = [];
  const bigBlur = [];
  const transitionAll = [];
  let nodes = 0;
  for (const el of document.querySelectorAll('*')) {
    nodes++;
    const cs = getComputedStyle(el);
    if (cs.willChange && cs.willChange !== 'auto') {
      restingWillChange.push({ sel: sel(el), value: cs.willChange });
    }
    const f = (cs.filter || 'none') + ' ' + (cs.backdropFilter || 'none');
    if (f.includes('blur(') && big(el.getBoundingClientRect())) {
      bigBlur.push({ sel: sel(el), filter: f.trim() });
    }
    // `transition-property` computes to `all` by DEFAULT, so testing it alone
    // flags every element on a page with no transitions at all - it fired on
    // 10 nodes of the clean fixture (2026-09-08). A real `transition: all`
    // also has a non-zero duration.
    if ((cs.transitionProperty || '') === 'all'
        && (cs.transitionDuration || '0s') !== '0s') {
      transitionAll.push({ sel: sel(el), dur: cs.transitionDuration });
    }
  }

  const faces = [];
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch (e) { continue; }
    for (const r of rules || []) {
      if (r.constructor && r.constructor.name === 'CSSFontFaceRule') {
        faces.push({
          family: r.style.getPropertyValue('font-family'),
          display: r.style.getPropertyValue('font-display') || '',
          sizeAdjust: r.style.getPropertyValue('size-adjust') || '',
        });
      }
    }
  }
  const preloads = [...document.querySelectorAll('link[rel=preload][as=font]')]
    .map(l => (l.getAttribute('href') || '').slice(-60));

  const vhNoDvh = [...document.querySelectorAll('*')].filter(el => {
    const s = el.getAttribute('style') || '';
    return /height:\s*100vh/.test(s);
  }).map(sel);

  return { imgs, iframes, restingWillChange, bigBlur, transitionAll,
           nodes, faces, preloads, vhNoDvh, vw, vh };
})()
"""

OBSERVER_JS = r"""
window.__perf = { lcp: 0, cls: 0, long: [], scrollLong: [], scrolling: false, frames: [] };
try {
  new PerformanceObserver((l) => {
    const e = l.getEntries();
    window.__perf.lcp = e[e.length - 1].startTime;
  }).observe({ type: 'largest-contentful-paint', buffered: true });
} catch (e) {}
try {
  new PerformanceObserver((l) => {
    for (const entry of l.getEntries()) {
      if (!entry.hadRecentInput) window.__perf.cls += entry.value;
    }
  }).observe({ type: 'layout-shift', buffered: true });
} catch (e) {}
try {
  new PerformanceObserver((l) => {
    for (const entry of l.getEntries()) {
      const rec = { start: Math.round(entry.startTime), dur: Math.round(entry.duration) };
      window.__perf.long.push(rec);
      if (window.__perf.scrolling) window.__perf.scrollLong.push(rec);
    }
  }).observe({ type: 'longtask', buffered: true });
} catch (e) {}
(function f(t){ window.__perf.frames.push(t); requestAnimationFrame(f); })(0);
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--url", required=True)
    ap.add_argument("--cpu", type=float, default=4.0)
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--height", type=int, default=900)
    ap.add_argument("--budget", default="")
    ap.add_argument("--out", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    budget = dict(DEFAULT_BUDGET)
    if args.budget:
        try:
            budget.update(json.loads(Path(args.budget).read_text(encoding="utf-8")))
        except Exception as e:
            print("perf_probe: kan inte lasa budget (" + str(e) + ")", file=sys.stderr)
            return 2

    try:
        from playwright.sync_api import sync_playwright
    except Exception as e:
        print("perf_probe: playwright saknas (" + str(e) + ")", file=sys.stderr)
        return 2

    transfer = {}

    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": args.width, "height": args.height},
                                  device_scale_factor=1)
        page = ctx.new_page()
        if args.cpu and args.cpu > 1:
            cdp = ctx.new_cdp_session(page)
            cdp.send("Emulation.setCPUThrottlingRate", {"rate": args.cpu})

        def on_response(resp):
            try:
                ct = (resp.headers.get("content-type") or "").split(";")[0]
                cl = int(resp.headers.get("content-length") or 0)
            except Exception:
                return
            kind = ("image" if ct.startswith("image/") else
                    "font" if "font" in ct else
                    "script" if "javascript" in ct else
                    "style" if "css" in ct else
                    "video" if ct.startswith("video/") else "other")
            e = transfer.setdefault(kind, {"bytes": 0, "count": 0, "largest": 0, "largest_url": ""})
            e["bytes"] += cl
            e["count"] += 1
            if cl > e["largest"]:
                e["largest"] = cl
                e["largest_url"] = resp.url[-90:]

        page.on("response", on_response)
        page.add_init_script(OBSERVER_JS)
        try:
            page.goto(args.url, wait_until="networkidle", timeout=45000)
        except Exception:
            page.goto(args.url, wait_until="load", timeout=45000)
        page.wait_for_timeout(800)

        static = page.evaluate(COLLECT_JS)

        page.evaluate("window.__perf.scrolling = true")
        page.mouse.move(args.width // 2, args.height // 2)
        for _ in range(20):
            page.mouse.wheel(0, 100)
            page.wait_for_timeout(60)
        page.wait_for_timeout(400)
        page.evaluate("window.__perf.scrolling = false")

        perf = page.evaluate("({lcp: window.__perf.lcp, cls: window.__perf.cls, "
                             "long: window.__perf.long, scrollLong: window.__perf.scrollLong})")
        browser.close()

    total_bytes = sum(v["bytes"] for v in transfer.values())
    img_bytes = transfer.get("image", {}).get("largest", 0)
    font = transfer.get("font", {"bytes": 0, "count": 0})

    findings = []

    def fail(rule, detail):
        findings.append({"rule": rule, "detail": detail})

    if not perf["lcp"]:
        # Never silently pass an unmeasured metric. A page whose LCP entry
        # never arrives (blocked main thread, no qualifying paint) is not a
        # page with a good LCP.
        fail("lcp-not-measured", "ingen largest-contentful-paint-post - "
                                 "huvudtraden blockerad eller ingen kvalificerande malning")
    elif perf["lcp"] > budget["lcp_ms"]:
        fail("lcp", "%.0f ms > %d" % (perf["lcp"], budget["lcp_ms"]))
    if perf["cls"] > budget["cls"]:
        fail("cls", "%.3f > %.3f" % (perf["cls"], budget["cls"]))
    if len(perf["scrollLong"]) > budget["long_tasks_during_scroll"]:
        fail("long-task-under-scroll", str(len(perf["scrollLong"])) + " tasks > 50 ms under scroll")
    if total_bytes > budget["total_bytes"]:
        fail("transfer", "%d B > %d" % (total_bytes, budget["total_bytes"]))
    if img_bytes > budget["hero_image_bytes"]:
        fail("hero-image", "%d B > %d (%s)" % (img_bytes, budget["hero_image_bytes"],
                                               transfer.get("image", {}).get("largest_url", "")))
    if font["count"] > budget["font_files"]:
        fail("font-files", str(font["count"]) + " > " + str(budget["font_files"]))
    if font["bytes"] > budget["font_bytes"]:
        fail("font-bytes", "%d B > %d" % (font["bytes"], budget["font_bytes"]))
    if static["nodes"] > budget["dom_nodes"]:
        fail("dom-nodes", str(static["nodes"]) + " > " + str(budget["dom_nodes"]))

    for im in static["imgs"]:
        if not im["hasDims"]:
            fail("img-without-dimensions", im["sel"] + "  " + im["src"])
        if im["aboveFold"] and not im["fetchpriority"] and im["area"] > 40000:
            fail("lcp-image-without-fetchpriority", im["sel"])
        if not im["aboveFold"] and im["loading"] != "lazy":
            fail("below-fold-image-not-lazy", im["sel"])
        if not im["decoding"]:
            fail("img-without-decoding", im["sel"])
    for f in static["iframes"]:
        if f["loading"] != "lazy":
            fail("iframe-not-lazy", f["sel"] + "  " + f["src"])
    for face in static["faces"]:
        if not face["display"]:
            fail("font-face-without-display", face["family"])
    if static["faces"] and not static["preloads"]:
        fail("no-font-preload", "en @font-face finns men ingen <link rel=preload as=font>")
    if len(static["restingWillChange"]) > budget["resting_will_change"]:
        fail("resting-will-change",
             ", ".join(w["sel"] for w in static["restingWillChange"][:6]))
    if len(static["bigBlur"]) > budget["large_blur_surfaces"]:
        fail("blur-on-large-surface", ", ".join(b["sel"] for b in static["bigBlur"][:4]))
    for t in static["transitionAll"]:
        fail("transition-all", t["sel"])
    for s in static["vhNoDvh"]:
        fail("100vh-without-dvh", s)

    out = {
        "url": args.url, "viewport": [args.width, args.height], "cpu": args.cpu,
        "lcp_ms": round(perf["lcp"]), "cls": round(perf["cls"], 4),
        "long_tasks": len(perf["long"]), "long_tasks_under_scroll": len(perf["scrollLong"]),
        "transfer": transfer, "total_bytes": total_bytes, "dom_nodes": static["nodes"],
        "findings": findings, "pass": not findings,
    }

    if args.out:
        d = Path(args.out); d.mkdir(parents=True, exist_ok=True)
        (d / "perf_probe.json").write_text(json.dumps(out, indent=2, ensure_ascii=False),
                                           encoding="utf-8")
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print("perf_probe " + ("PASS" if out["pass"] else "FAIL") + "  " + args.url)
        print("  LCP %d ms | CLS %.3f | long tasks %d (%d under scroll) | %.0f kB | %d noder"
              % (out["lcp_ms"], out["cls"], out["long_tasks"],
                 out["long_tasks_under_scroll"], total_bytes / 1000, static["nodes"]))
        seen = {}
        for f in findings:
            seen.setdefault(f["rule"], []).append(f["detail"])
        for rule in sorted(seen):
            rows = seen[rule]
            print("  FAIL %-32s %s" % (rule, rows[0]))
            if len(rows) > 1:
                print("       + %d till" % (len(rows) - 1))
    return 0 if out["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
