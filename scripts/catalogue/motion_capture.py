#!/usr/bin/env python3
"""motion_capture.py - what a page DOES as it is scrolled, for the catalogue.

capture.py takes a full-page screenshot, which on a Lenis/ScrollTrigger site is
a lie: pinned sections collapse, scrubbed reveals sit at progress 0, WebGL
canvases come out black. This drives the page the way a visitor does (real
wheel events, 4x120 px bursts, the lead's method from tests/alunix-r8) and
keeps what that produces:

  entries/<slug>/fold.webp          first viewport after the intro settles (only if absent)
  entries/<slug>/shot.webp          the scroll frames stacked, longest edge <= 2200 (only if absent)
  entries/<slug>/slices/NN.webp     scroll frames, max 12 (only if absent)
  entries/<slug>/motion/sheet.webp  intro strip (300/1200/2500 ms) + every scroll frame, one image to read
  entries/<slug>/motion/probe.json  stack detection + scroll metrics (below)

probe.json carries what can be measured rather than guessed: gsapVersions
(GSAP writes window.gsapVersions), ScrollTrigger count when it is global,
pin-spacers (one per pinned section), Lenis (html.lenis), ScrollSmoother
(#smooth-wrapper), Locomotive, Barba/Swup/Taxi page transitions, WebGL
canvases, videos, split-text density, fonts, scroll height and how far the
page moved per wheel burst (smoothing shows as lag between wheel and scrollY).

    python scripts/catalogue/motion_capture.py --list sites.json [--only host,host] [--redo]
    python scripts/catalogue/motion_capture.py --url https://x.com --slug x

Headless only, one browser at a time (memory: headless-browsers-only), with the
GPU flags that were calibrated to headed frame timing.
"""
import argparse
import json
import os
import re
import sys
import time
from io import BytesIO
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent.parent
ENTRIES = ROOT / "design-catalogue" / "entries"
LOCK = os.path.join(os.environ.get("TEMP", "/tmp"), "alunix-browser.lock")
W, H = 1440, 900
MAX_FRAMES = 20
SITE_BUDGET_S = 90

DETECT = r"""
() => {
  const q = s => document.querySelectorAll(s).length;
  const html = document.documentElement;
  const st = window.ScrollTrigger || (window.gsap && window.gsap.core && window.gsap.plugins && window.gsap.plugins.scrollTrigger);
  let triggers = null;
  try { if (window.ScrollTrigger && ScrollTrigger.getAll) triggers = ScrollTrigger.getAll().length; } catch(e) {}
  let webgl = 0;
  for (const c of document.querySelectorAll('canvas')) {
    try { if (c.getContext('webgl2') || c.getContext('webgl')) webgl++; } catch(e) {}
  }
  const inlineBlocks = q('div[style*="inline-block"], span[style*="inline-block"]');
  const scripts = [...document.scripts].map(s => s.src).filter(Boolean);
  const fonts = new Set();
  try { document.fonts.forEach(f => f.status === 'loaded' && fonts.add(f.family.replace(/["']/g,''))); } catch(e) {}
  const bg = getComputedStyle(document.body).backgroundColor;
  return {
    title: document.title,
    gsapVersions: window.gsapVersions || null,
    gsapGlobal: !!window.gsap,
    scrollTriggers: triggers,
    pinSpacers: q('.pin-spacer'),
    lenis: html.classList.contains('lenis') || !!window.lenis || !!window.__lenis || q('[data-lenis-prevent]') > 0,
    lenisClasses: [...html.classList].filter(c => c.startsWith('lenis')),
    scrollSmoother: q('#smooth-wrapper') > 0 || q('#smooth-content') > 0,
    locomotive: html.classList.contains('has-scroll-smooth') || q('[data-scroll-container]') > 0,
    barba: q('[data-barba]') > 0 || !!window.barba,
    swup: q('#swup, [data-swup]') > 0 || !!window.swup,
    taxi: q('[data-taxi]') > 0,
    three: !!window.__THREE__ || !!window.THREE,
    webglCanvases: webgl,
    canvases: q('canvas'),
    videos: q('video'),
    splitTextSuspect: inlineBlocks,
    lazyImages: q('img[loading="lazy"]'),
    scriptHosts: [...new Set(scripts.map(s => { try { return new URL(s).host } catch(e) { return '' } }))].slice(0, 25),
    libHints: scripts.filter(s => /gsap|scrolltrigger|lenis|locomotive|barba|swup|three|ogl|pixi|lottie|rive|framer|motion|splitting|swiper|curtains/i.test(s)).slice(0, 25),
    fonts: [...fonts].slice(0, 12),
    bg,
    docHeight: Math.max(document.body.scrollHeight, html.scrollHeight),
    reducedMotionQuery: matchMedia('(prefers-reduced-motion: reduce)').matches,
  };
}
"""


def single_flight():
    """Same lock as tests/alunix-r8/showcase_probe.py: one browser run at a time."""
    import atexit
    deadline = time.time() + 3600
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode())
            os.close(fd)
            atexit.register(lambda: os.path.exists(LOCK) and os.remove(LOCK))
            return
        except FileExistsError:
            if time.time() - os.path.getmtime(LOCK) > 900:
                os.remove(LOCK)
                continue
            if time.time() > deadline:
                sys.exit("[motion_capture] browser lock held too long: " + LOCK)
            time.sleep(2)


def slugify(host: str) -> str:
    s = host.lower().replace("www.", "")
    s = re.sub(r"\.(com|co|io|dev|studio|design|net|org|app|xyz|fr|nl|it|de|ro|at|uk|es|se|jp|tech|world|online|works|agency|vercel\.app)$", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "site"


def shot(pg):
    for i in range(3):
        try:
            return Image.open(BytesIO(pg.screenshot(timeout=12000, type="jpeg", quality=88))).convert("RGB")
        except Exception:
            pg.wait_for_timeout(400)
    return None


def webp(img, path, width=None, q=72):
    path.parent.mkdir(parents=True, exist_ok=True)
    if width and img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    img.save(path, "WEBP", quality=q, method=4)


def sheet(intro, frames):
    tw, th, gap = 360, 225, 4
    cols = 5 if len(intro) > 4 else 4
    rows_f = (len(frames) + cols - 1) // cols
    s = Image.new("RGB", (cols * (tw + gap), (1 + rows_f) * (th + gap)), (255, 0, 64))
    for i, im in enumerate(intro[:cols]):
        s.paste(im.resize((tw, th)), (i * (tw + gap), 0))
    for i, im in enumerate(frames):
        s.paste(im.resize((tw, th)), ((i % cols) * (tw + gap), (1 + i // cols) * (th + gap)))
    return s


def diff(a, b):
    """Mean absolute pixel change, 0-255, on a 96 px thumbnail - how much moved."""
    from PIL import ImageChops, ImageStat
    a = a.resize((96, 60)).convert("L")
    b = b.resize((96, 60)).convert("L")
    return round(sum(ImageStat.Stat(ImageChops.difference(a, b)).mean), 2)


UNLOCK = r"""
() => {
  // cookie walls: decline first (privacy), only then dismiss; then experience gates
  const order = [/^(reject|decline|deny|refuse|necessary only|only necessary|reject all|avvisa|neka)/i,
                 /^(close|dismiss|×|x|no,? thanks?|no thank you|not now|maybe later|later|stäng)$/i,
                 /^(enter|enter site|enter experience|start|start experience|explore|begin|discover|continue|skip|skip intro|launch|initiate|initiate system|enter system|let'?s go|without sound|no sound|sound off|enter without sound|play)\b/i];
  const vis = e => { const r = e.getBoundingClientRect(); const s = getComputedStyle(e);
    return r.width > 4 && r.height > 4 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > 0.05 && r.bottom > 0 && r.top < innerHeight; };
  order.splice(2, 0, /^(enter )?(without sound|no sound|sound off|mute|muted)\b/i);  // sound-off before any other enter
  const cands = new Set(document.querySelectorAll('button, a, [role=button], [data-enter], .enter, #enter'));
  for (const e of document.querySelectorAll('body div, body span, body p')) {  // gates built from divs with cursor:pointer
    if (cands.size > 400) break;
    if (getComputedStyle(e).cursor === 'pointer' && (e.innerText || '').trim().length < 40) cands.add(e);
  }
  const els = [...cands].filter(vis);
  const hits = [];
  for (const rx of order) for (const e of els) {
    const t = (e.innerText || e.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ');
    if (t && t.length < 40 && rx.test(t) && !(e.tagName === 'A' && e.href && !e.href.includes('#') && new URL(e.href, location.href).pathname !== location.pathname)) {
      e.click(); hits.push(t); break;
    }
  }
  // "click anywhere" gates: click the body itself (never a link), only when the page asks for it
  if (!hits.length && /click anywhere|click to (enter|start|begin)|tap anywhere|klicka var som helst/i.test(document.body.innerText || '')) {
    const c = document.querySelector('canvas') || document.body;
    for (const ev of ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'])
      c.dispatchEvent(new MouseEvent(ev, { bubbles: true, clientX: innerWidth / 2, clientY: innerHeight / 2 }));
    hits.push('click-anywhere');
  }
  return hits;
}
"""


def capture(pg, url, outdir: Path):
    t0 = time.time()
    errors = []
    pg.on("pageerror", lambda e: errors.append(str(e)[:160]))
    try:
        pg.goto(url, wait_until="domcontentloaded", timeout=45000)
    except Exception as e:
        return {"url": url, "ok": False, "error": "goto: " + str(e)[:200]}
    intro = []
    for wait in (300, 900, 1300):  # intro at ~300 / 1200 / 2500 ms after DOMContentLoaded
        pg.wait_for_timeout(wait)
        im = shot(pg)
        if im:
            intro.append(im)
    try:
        pg.wait_for_load_state("networkidle", timeout=4000)
    except Exception:
        pass
    pg.wait_for_timeout(1000)
    try:
        unlocked = pg.evaluate(UNLOCK)
    except Exception:
        unlocked = []
    if unlocked:  # the gate's exit transition is the reference, so keep it in the intro strip
        for wait in (500, 1500):
            pg.wait_for_timeout(wait)
            im = shot(pg)
            if im:
                intro.append(im)
    fold = shot(pg)
    idle = shot(pg) if fold else None  # ambient motion with no input
    probe = pg.evaluate(DETECT)
    pg.mouse.move(W // 2, H // 2)
    frames, ys, lag = [], [], []
    last_y, same = -1, 0
    # whole page in <= MAX_FRAMES frames, but never coarser than half a viewport
    step_px = max(int(H * 0.5), int(probe.get('docHeight', 0) / MAX_FRAMES))
    while len(frames) < MAX_FRAMES and time.time() - t0 < SITE_BUDGET_S:
        y0 = pg.evaluate("scrollY")
        for _ in range(max(1, step_px // 120)):
            pg.mouse.wheel(0, 120)
            pg.wait_for_timeout(35)
        y_mid = pg.evaluate("scrollY")
        pg.wait_for_timeout(350)
        y = pg.evaluate("scrollY")
        lag.append(y - y_mid)  # distance still travelled after input stopped = smoothing
        im = shot(pg)
        if im:
            frames.append(im)
            ys.append(y)
        # virtual-scroll sites (WebGL, transform scrollers) never move scrollY: only stop when the picture stops too
        still = len(frames) < 2 or diff(frames[-2], frames[-1]) < 1.0
        if y == last_y and still:
            same += 1
            if same >= 2 and y == 0 and not probe.get("retried"):
                # stuck at the top: a long preloader or a gate the first pass missed - wait, unlock, retry once
                probe["retried"] = True
                pg.wait_for_timeout(3500)
                try:
                    unlocked = unlocked + pg.evaluate(UNLOCK)
                except Exception:
                    pass
                pg.wait_for_timeout(1500)  # ponytail: no blind click - it can follow a link; canvas-only gates stay uncaptured
                same = 0
                continue
            if same >= 2:
                break
        else:
            same = 0
        last_y = y
    probe2 = pg.evaluate(DETECT)
    for k in ("pinSpacers", "scrollTriggers", "webglCanvases", "videos", "splitTextSuspect", "docHeight"):
        probe[k + "AfterScroll"] = probe2.get(k)
    probe.update({
        "unlocked": unlocked,
        "url": url, "ok": bool(frames), "seconds": round(time.time() - t0, 1),
        "frames": len(frames), "scrollYs": ys, "smoothingLagPx": lag,
        "smoothed": (sum(1 for v in lag if v > 30) >= max(2, len(lag) // 3)),
        "idleMotion": diff(fold, idle) if fold and idle else None,
        "frameChange": [diff(a, b) for a, b in zip(frames, frames[1:])],
        "introChange": [diff(a, b) for a, b in zip(intro, intro[1:])],
        "errors": errors[:5],
    })
    if not frames:
        return probe
    (outdir / "motion").mkdir(parents=True, exist_ok=True)
    webp(sheet(intro, frames), outdir / "motion" / "sheet.webp", q=70)
    if not (outdir / "fold.webp").exists() and fold:
        webp(fold, outdir / "fold.webp", q=78)
    if not (outdir / "slices").exists():
        for i, im in enumerate(frames[:12]):
            webp(im, outdir / "slices" / f"{i:02d}.webp", width=960, q=68)
    if not (outdir / "shot.webp").exists():
        tw = 480
        th = round(H * tw / W)
        stack = Image.new("RGB", (tw, th * len(frames)))
        for i, im in enumerate(frames):
            stack.paste(im.resize((tw, th)), (0, i * th))
        if stack.height > 2200:
            stack = stack.resize((round(tw * 2200 / stack.height), 2200), Image.LANCZOS)
        webp(stack, outdir / "shot.webp", q=72)
    (outdir / "motion" / "probe.json").write_text(json.dumps(probe, ensure_ascii=False, indent=1), encoding="utf-8")
    return probe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", help="sites.json from the showcase scrape (url, host, src, ...)")
    ap.add_argument("--url")
    ap.add_argument("--slug")
    ap.add_argument("--only", default="")
    ap.add_argument("--redo", action="store_true")
    ap.add_argument("--log", default=str(ROOT / "design-catalogue" / "motion-capture.log.jsonl"))
    a = ap.parse_args()
    if a.url:
        jobs = [{"url": a.url, "slug": a.slug or slugify(re.sub(r"^https?://", "", a.url).split("/")[0])}]
    else:
        jobs = json.loads(Path(a.list).read_text(encoding="utf-8"))
        for j in jobs:
            j.setdefault("slug", slugify(j["host"]))
    only = {s for s in a.only.split(",") if s}
    if only:
        jobs = [j for j in jobs if j.get("host") in only or j["slug"] in only]
    single_flight()
    log = open(a.log, "a", encoding="utf-8")
    with sync_playwright() as p:
        browser = None
        for n, j in enumerate(jobs):
            out = ENTRIES / j["slug"]
            if (out / "motion" / "probe.json").exists() and not a.redo:
                continue
            # fresh browser every 10 sites: verify_motion.py died at 12+ pages in one browser
            if browser is None or n % 10 == 0:
                if browser:
                    browser.close()
                browser = p.chromium.launch(headless=True, channel="chromium",
                                            args=["--enable-gpu", "--ignore-gpu-blocklist", "--use-angle=d3d11",
                                                  "--autoplay-policy=no-user-gesture-required"])
            ctx = browser.new_context(viewport={"width": W, "height": H}, device_scale_factor=1,
                                      user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36")
            pg = ctx.new_page()
            try:
                r = capture(pg, j["url"], out)
            except Exception as e:
                r = {"url": j["url"], "ok": False, "error": str(e)[:300]}
            finally:
                ctx.close()
            r.update({"slug": j["slug"], "src": j.get("src")})
            log.write(json.dumps(r, ensure_ascii=False) + "\n")
            log.flush()
            print(f"[{n + 1}/{len(jobs)}] {j['slug']}: ok={r.get('ok')} frames={r.get('frames')} "
                  f"gsap={r.get('gsapVersions')} pins={r.get('pinSpacersAfterScroll')} lenis={r.get('lenis')} "
                  f"smoothed={r.get('smoothed')} {r.get('error', '')[:80]}", flush=True)
        if browser:
            browser.close()


if __name__ == "__main__":
    main()
