#!/usr/bin/env python3
"""motion_summary.py [slug ...] [--next N] - one line per captured site, read next to its sheet.

--next N lists the next N captured slugs (showcase order) that have no reading yet.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CAT = ROOT / "design-catalogue"
sites = json.loads((CAT / "showcase-sites.json").read_text(encoding="utf-8"))
read = set()
rp = CAT / "showcase-readings.jsonl"
if rp.exists():
    read = {json.loads(l)["slug"] for l in rp.read_text(encoding="utf-8").splitlines() if l.strip()}


def line(s):
    p = json.loads((CAT / "entries" / s["slug"] / "motion" / "probe.json").read_text(encoding="utf-8"))
    pins = max(p.get("pinSpacers") or 0, p.get("pinSpacersAfterScroll") or 0)
    return (f"{s['slug']} | {p.get('title', '')[:50]} | {s['url']} | gsap={p.get('gsapVersions')} st={p.get('scrollTriggersAfterScroll')} "
            f"pins={pins} lenis={p.get('lenis')} smoother={p.get('scrollSmoother')} webgl={p.get('webglCanvases')} "
            f"three={p.get('three')} vid={p.get('videos')} split={p.get('splitTextSuspect')} "
            f"trans={'barba' if p.get('barba') else 'swup' if p.get('swup') else 'taxi' if p.get('taxi') else '-'} "
            f"smooth={p.get('smoothed')} lag={p.get('smoothingLagPx', [])[:4]} y={p.get('scrollYs', [])[-1:]} "
            f"doc={p.get('docHeight')} idle={p.get('idleMotion')} intro={p.get('introChange')} gate={p.get('unlocked')} "
            f"fonts={(p.get('fonts') or [])[:4]} plugins={s.get('plugins')} credits={s.get('credits', [])[:3]}")


args = [a for a in sys.argv[1:] if not a.startswith("--")]
if "--next" in sys.argv:
    n = int(sys.argv[sys.argv.index("--next") + 1])
    args = [s["slug"] for s in sites if s["slug"] not in read
            and (CAT / "entries" / s["slug"] / "motion" / "probe.json").exists()][:n]
by = {s["slug"]: s for s in sites}
for a in args:
    print(line(by[a]))
