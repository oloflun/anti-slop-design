#!/usr/bin/env python
"""T10 control: the reviewer contract check must fire AND stay quiet.

House rule (gates.md, "Both directions"): a check that can only fire is as
useless as one that never does. So a well-formed report must pass, and each way
of breaking the contract must be caught on its own.

    python tests/hooks/test_reviewer_contract.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
from check_reviewer_report import check  # noqa: E402

GOOD = """fix

## persistence
Read this run: BRIEF.md, concepts.md K3, shots/r3/ (7 images), garden-eight fold.webp.
perf_probe and motion_probe both ran against 127.0.0.1:3302 at 02:11.

## fidelity
s1 matches the target image. s3 drifts: the plate sits 40px low against the rail. Defect.

## ceiling
- garden-eight: står sig bredvid. Its silence between the two moments is longer than ours.
- mattis-studio: slår. Their console card is flat; ours is a card that turns.

## material_fixes
- Plate offset 40 -> 0 px against --rail-x at s3.
- LCP 2.4 -> 1.8 s: preload the display weight only.

## keep
The single accent on the measurement numbers. Nothing else carries colour.
"""

CASES = [
    ("well-formed report", GOOD, 0),
    ("no disposition word", GOOD.replace("fix\n", "Here is my review.\n", 1), 1),
    ("disposition not alone on line 1", GOOD.replace("fix\n", "fix - looks close\n", 1), 1),
    ("missing a section", GOOD.replace("## ceiling", "## celing"), 1),
    ("sixth section", GOOD + "\n## recommendations\nUse a warmer paper.\n", 1),
    ("sections out of order",
     GOOD.replace("## fidelity", "## TMP").replace("## ceiling", "## fidelity").replace("## TMP", "## ceiling"), 1),
    ("nine material fixes",
     GOOD.replace("- LCP 2.4 -> 1.8 s: preload the display weight only.",
                  "\n".join(f"- Fix number {i} with target {i * 4} px." for i in range(1, 9))), 1),
    ("raises reduced motion as a finding",
     GOOD.replace("## keep", "## keep\nAdd a prefers-reduced-motion fallback for the flip.\n"), 1),
    ("empty report", "   \n", 1),
]


def main() -> int:
    failed = 0
    for name, text, want in CASES:
        bad = check(text)
        got = 1 if bad else 0
        ok = got == want
        failed += not ok
        verdict = "PASS" if ok else "FAIL"
        detail = f" -> {bad[0][:78]}" if bad else " -> contract held"
        print(f"  [{verdict}] {name}{detail}")
    print()
    print("reviewer contract: all cases behaved as specified." if not failed
          else f"reviewer contract: {failed} case(s) wrong.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
