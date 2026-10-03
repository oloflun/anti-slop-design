#!/usr/bin/env python3
"""showcase_stats.py - the measured stack of the read showcase sites, as markdown for
skills/design/references/scroll/showcase-floor.md section 6.

Reads design-catalogue/showcase-readings.jsonl (what the lead read) and each site's
entries/<slug>/motion/probe.json (what the capture measured). reducedMotionQuery is left out
on purpose: it reports the capturing browser's preference, not the site's support.

    python scripts/catalogue/showcase_stats.py
"""
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "design-catalogue"


def load():
    rows = [json.loads(l) for l in (ROOT / "showcase-readings.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    out = []
    for r in rows:
        p = ROOT / "entries" / r["slug"] / "motion" / "probe.json"
        if p.exists():
            out.append((r, json.loads(p.read_text(encoding="utf-8"))))
    return out


def pct(n, d):
    return f"{n} ({round(100 * n / d)} %)" if d else "0"


def main():
    data = load()
    n = len(data)
    pr = [p for _, p in data]
    gsap = [p for p in pr if p.get("gsapVersions")]
    minor = Counter(".".join(v.split(".")[:2]) for p in gsap for v in set(p["gsapVersions"]))
    lag = [max(p.get("smoothingLagPx") or [0]) for p in pr if p.get("smoothed")]
    reads = [r for r, _ in data]
    lines = [
        f"Measured over **{n} read sites** from `motion/probe.json` (`scripts/catalogue/showcase_stats.py`).", "",
        "| Measure | Sites |", "|---|---|",
        f"| GSAP loaded | {pct(len(gsap), n)} |",
        f"| GSAP minor versions | {', '.join(f'{k}: {v}' for k, v in minor.most_common(6))} |",
        f"| Lenis | {pct(sum(bool(p.get('lenis')) for p in pr), n)} |",
        f"| ScrollSmoother | {pct(sum(bool(p.get('scrollSmoother')) for p in pr), n)} |",
        f"| Locomotive | {pct(sum(bool(p.get('locomotive')) for p in pr), n)} |",
        f"| Pinned sections | {pct(sum((p.get('pinSpacers') or 0) + (p.get('pinSpacersAfterScroll') or 0) > 0 for p in pr), n)} |",
        f"| WebGL canvas | {pct(sum((p.get('webglCanvases') or 0) + (p.get('webglCanvasesAfterScroll') or 0) > 0 for p in pr), n)} |",
        f"| Page transitions (Barba / Swup / Taxi) | {sum(bool(p.get('barba')) for p in pr)} / {sum(bool(p.get('swup')) for p in pr)} / {sum(bool(p.get('taxi')) for p in pr)} |",
        f"| Smoothed scroll | {pct(len(lag), n)}; px still travelling after the wheel stops: median {round(statistics.median(lag)) if lag else 0}, "
        f"p25 {round(statistics.quantiles(lag, n=4)[0]) if len(lag) > 3 else '-'}, p75 {round(statistics.quantiles(lag, n=4)[2]) if len(lag) > 3 else '-'} |",
        f"| Floor 2 / 1 / 0 (lead's reading) | {' / '.join(str(sum(r.get('floor') == f for r in reads)) for f in (2, 1, 0))} |",
        f"| Grammar | {', '.join(f'{k}: {v}' for k, v in Counter(r.get('gram') for r in reads).most_common())} |",
        f"| Register | {', '.join(f'{k}: {v}' for k, v in Counter(r.get('reg') for r in reads).most_common())} |",
        f"| Mode | {', '.join(f'{k}: {v}' for k, v in Counter(r.get('mode') for r in reads).most_common())} |",
    ]
    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
