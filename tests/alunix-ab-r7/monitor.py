#!/usr/bin/env python
"""Alunix A/B r7 monitor. Thin wrapper over r6's monitor.py: same report
format and Report/scan machinery, r7's own runs/logs/probes/monitor paths, a
2-key KEYS map (K1/K2 only), and round-scoped logs (--round N), since r7
builds arrive across resumed rounds rather than one shot.

    python tests/alunix-ab-r7/monitor.py <arm> [K...] [--round N]
                                    -> monitor/<arm>-<K>[-r<N>].md (+ summary.md)
    python tests/alunix-ab-r7/monitor.py summary [--round N]
                                    -> one round's cells, or (no --round) every
                                       round dir found under logs/, combined
    python tests/alunix-ab-r7/monitor.py --probe <arm>  -> monitor/probe-<arm>.md
"""
from __future__ import annotations

import sys
from pathlib import Path

R7 = Path(__file__).resolve().parent
sys.path.insert(0, str(R7.parent / "alunix-ab-r6"))
import monitor as r6mon  # noqa: E402

R6 = R7
RUNS = R7 / "runs"
LOGS = R7 / "logs"
PROBES = R7 / "probes"
MONITOR = R7 / "monitor"
KEYS = ("K1", "K2")

r6mon.R6 = R6
r6mon.RUNS = RUNS
r6mon.LOGS = LOGS
r6mon.PROBES = PROBES
r6mon.MONITOR = MONITOR
r6mon.KEYS = KEYS


def label_for(arm: str, key: str, round_n: int | None) -> str:
    if key == "probe":
        return f"probe-{arm}"
    return f"{arm}-{key}-r{round_n}" if round_n is not None else f"{arm}-{key}"


def build_and_write(arm: str, key: str, logs_dir: Path, round_n: int | None) -> "r6mon.Report":
    if key == "probe":
        log, meta, cell_dir = PROBES / f"{arm}.jsonl", PROBES / f"{arm}.meta.json", PROBES
    else:
        log, meta, cell_dir = (logs_dir / f"{arm}-{key}.jsonl", logs_dir / f"{arm}-{key}.meta.json",
                               RUNS / arm / key)
    label = label_for(arm, key, round_n)
    rep = r6mon.build_report(label, arm, key, log, meta, cell_dir)
    MONITOR.mkdir(parents=True, exist_ok=True)
    out = MONITOR / f"{label}.md"
    out.write_text(r6mon.render_cell(rep), encoding="utf-8")
    print(f"wrote {out}")
    return rep


def build_cells_in(logs_dir: Path) -> list[tuple[str, str]]:
    return [(a, k) for a in r6mon.ARMS for k in KEYS if (logs_dir / f"{a}-{k}.jsonl").is_file()]


def round_dirs() -> list[Path]:
    if not LOGS.is_dir():
        return []
    dirs = [p for p in LOGS.iterdir() if p.is_dir() and p.name.startswith("round-")
            and p.name[len("round-"):].isdigit()]
    return sorted(dirs, key=lambda p: int(p.name[len("round-"):]))


def all_reports() -> list["r6mon.Report"]:
    """Every cell found: every round-N dir under logs/, the plain logs/ dir
    (if used directly, without --round), and each arm's probe (round-less)."""
    reports = []
    for rd in round_dirs():
        rn = int(rd.name[len("round-"):])
        reports += [build_and_write(a, k, rd, rn) for a, k in build_cells_in(rd)]
    reports += [build_and_write(a, k, LOGS, None) for a, k in build_cells_in(LOGS)]
    reports += [build_and_write(a, "probe", LOGS, None) for a in r6mon.ARMS
                if (PROBES / f"{a}.jsonl").is_file()]
    return reports


def print_summary(reports: list) -> None:
    reports.sort(key=lambda r: (r.key == "probe", r.arm, r.label))
    path = r6mon.write_summary(reports)
    print(f"wrote {path}")
    print(r6mon.SUMMARY_HEAD)
    for r in reports:
        print(r6mon.summary_row(r))


def main(argv: list[str]) -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    round_n = None
    if "--round" in argv:
        i = argv.index("--round")
        round_n = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]

    if argv[0] == "--probe":
        if len(argv) < 2 or argv[1] not in r6mon.ARMS:
            r6mon.die("usage: monitor.py --probe A|B")
        rep = build_and_write(argv[1], "probe", LOGS, None)
        print(r6mon.SUMMARY_HEAD)
        print(r6mon.summary_row(rep))
        return

    if argv[0] == "summary":
        if round_n is not None:
            logs_dir = LOGS / f"round-{round_n}"
            targets = build_cells_in(logs_dir)
            if not targets:
                r6mon.die(f"no cell logs found under {logs_dir}")
            reports = [build_and_write(a, k, logs_dir, round_n) for a, k in targets]
        else:
            reports = all_reports()
            if not reports:
                r6mon.die(f"no cell logs found under {LOGS} (incl. round-* subdirs) or {PROBES}")
        print_summary(reports)
        return

    arm = argv[0]
    if arm not in r6mon.ARMS:
        r6mon.die(f"unknown arm {arm!r}; usage: monitor.py A|B [K1 K2] [--round N] | summary [--round N] | --probe A|B")
    keys = argv[1:] or list(KEYS)
    bad = [k for k in keys if k not in KEYS]
    if bad:
        r6mon.die(f"unknown key(s) {bad}")
    logs_dir = LOGS / f"round-{round_n}" if round_n is not None else LOGS
    reports = [build_and_write(arm, k, logs_dir, round_n) for k in keys]
    print_summary(reports)


if __name__ == "__main__":
    main(sys.argv[1:])
