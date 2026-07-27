#!/usr/bin/env python
"""Stop — the deep pass and the skill-call ledger report.

Two jobs at the end of a session:

  1. Run the full detector ruleset over every UI file touched, deduped against
     what the per-edit pass already reported.
  2. Render the report that makes the router *evaluable* instead of assumed.

The report always prints when design work happened, even when everything is
clean. A build that looks right but ships an empty or gap-heavy ledger has not
passed — it got lucky, and there is no way to tell which.
"""

import sys
from collections import OrderedDict, defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import design_hook_lib as L
except Exception:
    sys.exit(0)


def rel(path: str, root: Path) -> str:
    """Project-relative path — absolute paths make the report unreadable."""
    if not path:
        return ""
    try:
        return str(Path(path).resolve().relative_to(root.resolve())).replace("\\", "/")
    except Exception:
        return Path(path).name


def build_report(rows: list[dict], findings: list[dict], root: Path) -> tuple[str, str]:
    """Returns (context_summary, full_markdown)."""
    edits = [r for r in rows if r.get("event") == "edit"]
    routes = [r for r in rows if r.get("event") == "route"]
    skills = [r for r in rows if r.get("event") == "skill"]
    denies = [r for r in rows if r.get("event") == "gate-deny"]
    traps = [r for r in rows if r.get("event") == "trap"]

    invoked = {r.get("skill", "") for r in skills}

    # 1. component -> skills, in order
    per_component: "OrderedDict[str, list[str]]" = OrderedDict()
    for r in rows:
        comp = r.get("component") or ""
        if not comp:
            continue
        per_component.setdefault(comp, [])
        if r.get("event") == "skill":
            s = r.get("skill", "")
            if s and s not in per_component[comp]:
                per_component[comp].append(s)

    # 2. route-vs-invocation gap — the number that must be zero
    wanted = defaultdict(set)
    for r in routes:
        skill = r.get("skill", "")
        if skill and skill != "copy-gate":
            wanted[skill].add(r.get("component", "?"))
    gaps = {s: c for s, c in wanted.items() if s.split()[0] not in invoked and s not in invoked}

    # 3. coverage
    routed_files = {r.get("file", "") for r in routes}
    uncovered = sorted(rel(f, root) for f in ({r.get("file", "") for r in edits} - routed_files - {""}))

    md = [f"# Design session report — {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}", ""]
    md.append(f"{len(edits)} UI edits · {len(routes)} routes emitted · "
              f"{len(skills)} skill invocations · {len(denies)} denials · {len(traps)} trap firings")
    md.append("")

    md.append("## 1. Component → skills, in order")
    md.append("")
    if per_component:
        md.append("| Component | Skills applied |")
        md.append("|---|---|")
        for comp, sk in per_component.items():
            md.append(f"| `{comp}` | {' → '.join(sk) if sk else '**none**'} |")
    else:
        md.append("_No components touched._")
    md.append("")

    md.append("## 2. Route-vs-invocation gap")
    md.append("")
    md.append("_The router named a skill and nothing loaded it. This must be zero._")
    md.append("")
    if gaps:
        md.append("| Skill named | For | Loaded |")
        md.append("|---|---|---|")
        for s, comps in sorted(gaps.items()):
            md.append(f"| `{s}` | {', '.join(sorted(comps))} | **NO** |")
        md.append("")
        md.append(f"**GAP = {len(gaps)}.** The routing fired but the skill never loaded.")
    else:
        md.append("**GAP = 0.** Every named skill was invoked.")
    md.append("")

    md.append("## 3. Coverage")
    md.append("")
    if uncovered:
        md.append("UI files edited with no route emitted:")
        md.extend(f"- `{f}`" for f in uncovered)
    else:
        md.append("Every edited UI file produced a route.")
    md.append("")

    md.append("## 4. Gate activity")
    md.append("")
    if denies:
        md.append("| Rule | File | Detail |")
        md.append("|---|---|---|")
        for d in denies:
            md.append(f"| `{d.get('signal','?')}` | `{rel(d.get('file',''), root)}` | {d.get('detail','')} |")
    else:
        md.append("No denials.")
    md.append("")

    md.append("## 5. Trap firings (gate 60)")
    md.append("")
    if traps:
        md.append("| Skill palette | Value | File | Caught |")
        md.append("|---|---|---|---|")
        for t in traps:
            caught = "pre-write (denied)" if t.get("signal") == "pre" else "post-write (advisory)"
            md.append(f"| {t.get('skill','?')} | `{t.get('detail','')}` | `{rel(t.get('file',''), root)}` | {caught} |")
        md.append("")
        md.append("_A demoted skill's hardcoded palette reached a locked build._")
    else:
        md.append("None. No demoted-skill palette values appeared.")
    md.append("")

    if findings:
        md.append("## 6. Deep detector pass")
        md.append("")
        by_rule = defaultdict(list)
        for f in findings:
            by_rule[f.get("antipattern") or "?"].append(f)
        md.append("| Rule | Count | Example |")
        md.append("|---|---|---|")
        for rule, items in sorted(by_rule.items(), key=lambda kv: -len(kv[1])):
            ex = items[0]
            md.append(f"| `{rule}` | {len(items)} | {ex.get('snippet','')[:70]} |")
        md.append("")

    md.append("## 7. Timeline")
    md.append("")
    md.append("| # | Event | Component | Detail |")
    md.append("|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        detail = r.get("skill") or r.get("signal") or r.get("detail") or ""
        md.append(f"| {i} | {r.get('event','')} | `{r.get('component','')}` | {detail} |")
    md.append("")

    # Terse context summary — the report file carries the detail.
    summary = [
        f"[design session] {len(edits)} UI edits · {len(routes)} routes · {len(skills)} skill loads",
    ]
    if gaps:
        summary.append(
            f"ROUTE GAP = {len(gaps)}: " + ", ".join(sorted(gaps)) +
            " were named by the router but never loaded."
        )
    else:
        summary.append("Route gap = 0.")
    if traps:
        summary.append(f"GATE 60 fired {len(traps)}x — demoted-skill palette reached the build.")
    if findings:
        summary.append(f"Deep detector: {len(findings)} findings across "
                       f"{len({f.get('antipattern') for f in findings})} rules.")
    if uncovered:
        summary.append(f"{len(uncovered)} UI files got no route.")

    return "\n".join(summary), "\n".join(md)


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    root = L.project_root(event)

    rows = L.read_ledger(root)
    # Stay silent unless real design work happened. Bookkeeping rows alone
    # (a verify-discipline injection, an intent detection) are not a session
    # worth reporting on, and a report for zero edits reads as noise.
    if not any(r.get("event") in ("edit", "gate-deny", "trap") for r in rows):
        return

    touched = []
    for r in rows:
        f = r.get("file")
        if r.get("event") == "edit" and f and f not in touched:
            try:
                if Path(f).exists():
                    touched.append(f)
            except Exception:
                pass

    findings = L.detect(touched[:40], root, timeout=90) if touched else []

    summary, md = build_report(rows, findings, root)

    try:
        out = L.state_dir(root) / f"design-report-{datetime.now(timezone.utc):%Y%m%d-%H%M}.md"
        out.write_text(md, encoding="utf-8")
        summary += f"\nReport: {rel(str(out), root)}"
    except Exception:
        pass

    L.emit("Stop", summary)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
