#!/usr/bin/env python
"""Gate a reviewer report against the quartet's output contract.

T10's own control was written as "design-stop.py rejects a reviewer report
without a disposition word". It cannot live there: design-stop.py sees only
ledger rows, a reviewer's returned text never enters the ledger, and there is
no SubagentStop hook to put it there. Building that producer would also bet on
teammate mechanics that are unproven. The report is a file the lead already
reads, so the check is a file check.

    python scripts/check_reviewer_report.py runs/K3/reviews/craft-r3.md
    python scripts/check_reviewer_report.py --json report.md
    cat report.md | python scripts/check_reviewer_report.py -

Exit 0 = contract held. Exit 1 = violated (reasons on stdout). Exit 2 = usage.

The contract is in agents/design-{critic,heuristics,a11y-reviewer,perf-reviewer}.md
under "## Output contract"; this script is the mechanical half of it.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DISPOSITIONS = ("recapture", "rebuild", "fix", "ship")
SECTIONS = ("persistence", "fidelity", "ceiling", "material_fixes", "keep")
MAX_FIXES = 8
# F-011: motion always plays. A reviewer raising reduced motion as a finding is
# reporting against a rule this project retired, so the report is not usable.
RM = re.compile(r"prefers-reduced-motion|reduced[- ]motion", re.I)
RM_OK = re.compile(r"F-011|superseded|never flag|aldrig flagga", re.I)
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+`?([A-Za-z_]+)`?\s*$")


def check(text: str) -> list[str]:
    """Every way the report breaks the contract, in reading order."""
    bad: list[str] = []
    lines = text.strip().split("\n")
    if not lines or not lines[0].strip():
        return ["report is empty"]

    first = lines[0].strip().strip("`*_ ").lower()
    if first not in DISPOSITIONS:
        bad.append(f"line 1 is not a disposition word alone: {lines[0].strip()[:60]!r} "
                   f"(expected one of {'/'.join(DISPOSITIONS)})")

    found = [m.group(1).lower() for ln in lines if (m := HEADING.match(ln))]
    known = [s for s in found if s in SECTIONS]
    extra = [s for s in found if s not in SECTIONS]

    missing = [s for s in SECTIONS if s not in known]
    if missing:
        bad.append("missing section(s): " + ", ".join(missing))
    if extra:
        bad.append("section(s) outside the contract: " + ", ".join(extra)
                   + " (a table may sit inside one of the five; a sixth may not)")
    dupes = sorted({s for s in known if known.count(s) > 1})
    if dupes:
        bad.append("section(s) appearing more than once: " + ", ".join(dupes))
    if not missing and not dupes and known != list(SECTIONS):
        bad.append("sections out of order: " + " -> ".join(known))

    # material_fixes caps at eight; the ninth was not material.
    body = _section_body(lines, "material_fixes")
    fixes = [ln for ln in body if re.match(r"^\s*(?:[-*+]|\d+[.)])\s+\S", ln)]
    if len(fixes) > MAX_FIXES:
        bad.append(f"material_fixes has {len(fixes)} items, contract caps at {MAX_FIXES}")

    for i, ln in enumerate(lines, 1):
        if RM.search(ln) and not RM_OK.search(ln):
            bad.append(f"line {i} raises reduced motion as a finding (F-011): {ln.strip()[:70]!r}")
            break
    return bad


def _section_body(lines: list[str], name: str) -> list[str]:
    out, inside = [], False
    for ln in lines:
        m = HEADING.match(ln)
        if m:
            inside = m.group(1).lower() == name
            continue
        if inside:
            out.append(ln)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("report", help="path to the report, or - for stdin")
    ap.add_argument("--json", action="store_true", help="machine-readable result")
    a = ap.parse_args()

    if a.report == "-":
        text = sys.stdin.read()
    else:
        p = Path(a.report)
        if not p.is_file():
            print(f"check_reviewer_report: no such file: {p}", file=sys.stderr)
            return 2
        text = p.read_text(encoding="utf-8", errors="replace")

    bad = check(text)
    if a.json:
        print(json.dumps({"ok": not bad, "violations": bad}, ensure_ascii=False, indent=1))
    elif bad:
        print(f"contract violated ({len(bad)}):")
        for b in bad:
            print("  -", b)
    else:
        print("contract held")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
