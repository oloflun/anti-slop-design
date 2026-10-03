#!/usr/bin/env python3
"""section_probe.py - did a change somewhere make ANOTHER section worse?

The gap this closes (2026-09-25, Alunix V3g)
--------------------------------------------
A round that only touched the showcase made the thesis headline further up
the page visibly choppier. Nothing measured the untouched sections, so the
regression shipped. Root cause: iframes inside a pinned element reloaded on
every ScrollTrigger.refresh (the pin-spacer re-parents them), each reload's
`load` asked for another refresh, and the loop ran ~1/s for the whole visit.

One headless (GPU) browser, one real wheel pass top -> bottom, and per
`section[id]`:
  p95_ms / over33   frame time while that section is on screen
and for the page:
  iframe_loads      per iframe id - more than one per iframe = reload loop
  st_refreshes      ScrollTrigger refreshes after the reader started scrolling
  px_per_notch      how far ONE wheel notch moves the page once smoothing
                    settles (house pace: see references/scroll/devices.md)

  python section_probe.py URL [--out result.json] [--baseline old.json]

With --baseline, exits 1 if any section's p95 is worse than 1.5x the
baseline's AND over 33 ms, if any iframe loads more than once, or if a
refresh fires during the pass. Run it twice; one pass is noise.
Headless only, one browser at a time (lock file) - never a window on the
desktop.
"""
import argparse, json, os, sys, time
from playwright.sync_api import sync_playwright

LOCK = os.path.join(os.environ.get("TEMP", "/tmp"), "alunix-browser.lock")


def owner_alive():
    """Stale only when the lock's owner PID is dead: an mtime timeout let a 2nd run in beside a long one (2026-10-03)."""
    try:
        pid = int(open(LOCK).read().strip() or 0)
    except (OSError, ValueError):
        return False
    if pid <= 0:
        return False
    if os.name != "nt":
        try:
            os.kill(pid, 0); return True
        except OSError:
            return False
    import ctypes  # os.kill(pid, 0) terminates the process on Windows
    k = ctypes.windll.kernel32
    h = k.OpenProcess(0x1000, False, pid)
    if not h:
        return False
    code = ctypes.c_ulong(); k.GetExitCodeProcess(h, ctypes.byref(code)); k.CloseHandle(h)
    return code.value == 259
INIT = """
window.__sp = {f:[], y:[], ev:[]};
let last = performance.now();
(function loop(now){ window.__sp.f.push(now-last); window.__sp.y.push(scrollY); last=now; requestAnimationFrame(loop); })(performance.now());
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('iframe').forEach(f => f.addEventListener('load', () => window.__sp.ev.push(['load', f.id || f.src, performance.now()])));
  const hook = () => window.ScrollTrigger
    ? ScrollTrigger.addEventListener('refresh', () => window.__sp.ev.push(['refresh', '', performance.now()]))
    : setTimeout(hook, 20);
  hook();
});
"""


def lock():
    if os.environ.get("ALUNIX_BROWSER_LOCK_HELD"):
        return  # held by browser_lock.py around us
    deadline = time.time() + 1800
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, str(os.getpid()).encode()); os.close(fd)
            import atexit
            atexit.register(lambda: os.path.exists(LOCK) and os.remove(LOCK))
            return
        except FileExistsError:
            if not owner_alive():
                os.remove(LOCK); continue
            if time.time() > deadline:
                sys.exit("section_probe: browser lock held too long: " + LOCK)
            time.sleep(2)


def p95(xs):
    xs = sorted(xs)
    return round(xs[min(len(xs) - 1, int(0.95 * len(xs)))], 1) if xs else 0


def run(url):
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True, channel="chromium",
                              args=["--enable-gpu", "--ignore-gpu-blocklist", "--use-angle=d3d11"])
        try:
            pg = b.new_page(viewport={"width": 1440, "height": 900})
            pg.add_init_script(INIT)
            pg.goto(url, wait_until="load")
            pg.wait_for_timeout(2500)                      # let load-time refreshes settle
            pg.mouse.move(700, 450)
            # pace: one notch, wait for smoothing to settle
            y0 = pg.evaluate("scrollY"); pg.mouse.wheel(0, 100); pg.wait_for_timeout(1500)
            notch = round(pg.evaluate("scrollY") - y0)
            sections = pg.evaluate("""[...document.querySelectorAll('section[id]')].map(s => {
                const r = s.getBoundingClientRect(); return [s.id, r.top + scrollY, r.bottom + scrollY]; })""")
            start = pg.evaluate("performance.now()"); i0 = pg.evaluate("window.__sp.f.length")
            maxy = pg.evaluate("document.documentElement.scrollHeight - innerHeight")
            while pg.evaluate("scrollY") < maxy - 2 and pg.evaluate("performance.now()") - start < 90000:
                pg.mouse.wheel(0, 100); pg.wait_for_timeout(16)
            pg.wait_for_timeout(1200)
            t = pg.evaluate("window.__sp")
        finally:
            b.close()
    f, y = t["f"][i0:], t["y"][i0:]
    out = {"url": url, "px_per_notch": notch, "sections": {}}
    for sid, top, bot in sections:
        idx = [k for k, v in enumerate(y) if top - 900 < v < bot]   # section anywhere in view
        fr = [f[k] for k in idx]
        out["sections"][sid] = {"frames": len(fr), "p95_ms": p95(fr), "over33": sum(1 for x in fr if x > 33.4)}
    loads = {}
    for kind, name, _ in t["ev"]:
        if kind == "load": loads[name] = loads.get(name, 0) + 1
    out["iframe_loads"] = loads
    out["st_refreshes_during_pass"] = sum(1 for kind, _, ts in t["ev"] if kind == "refresh" and ts >= start)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url"); ap.add_argument("--out"); ap.add_argument("--baseline")
    a = ap.parse_args()
    lock()
    r = run(a.url)
    fails = [f"iframe {k} loaded {n}x" for k, n in r["iframe_loads"].items() if n > 1]
    if r["st_refreshes_during_pass"]:
        fails.append(f"{r['st_refreshes_during_pass']} ScrollTrigger refresh(es) during the scroll pass")
    if a.baseline:
        base = json.load(open(a.baseline, encoding="utf-8"))["sections"]
        for sid, s in r["sections"].items():
            b = base.get(sid)
            if b and s["p95_ms"] > 33.4 and s["p95_ms"] > 1.5 * max(b["p95_ms"], 16.7):
                fails.append(f"#{sid} p95 {s['p95_ms']} ms vs baseline {b['p95_ms']} ms")
    r["fails"] = fails
    if a.out:
        json.dump(r, open(a.out, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(json.dumps(r, indent=2, ensure_ascii=False))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
