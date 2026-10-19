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

import hashlib
import json
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


def mcp_summary_line(rows: list[dict]) -> str:
    """'MCP: inspo 5 (recommend, search_screens×2, get_screen×2) · ui-skills 2 (...)' or 'MCP: none'.

    get_skill's arg IS the point of the call (which skill loaded) so it lists
    the names; every other tool just gets a ×count — the query/slug text is
    already 80-char-truncated in the ledger row and would clutter this line.
    """
    mcps = [r for r in rows if r.get("event") == "mcp"]
    if not mcps:
        return "MCP: none"
    by_server: "OrderedDict[str, list[dict]]" = OrderedDict()
    for r in mcps:
        by_server.setdefault(r.get("server", "?"), []).append(r)
    parts = []
    for server, items in by_server.items():
        by_tool: "OrderedDict[str, list[str]]" = OrderedDict()
        for r in items:
            by_tool.setdefault(r.get("tool", "?"), []).append(r.get("arg", ""))
        bits = []
        for tool, args in by_tool.items():
            if tool == "get_skill":
                named = ", ".join(a for a in args if a)
                bits.append(f"{tool}: {named}" if named else tool)
            elif len(args) > 1:
                bits.append(f"{tool}×{len(args)}")
            else:
                bits.append(tool)
        parts.append(f"{server} {len(items)} ({', '.join(bits)})")
    return "MCP: " + " · ".join(parts)


def build_report(rows: list[dict], findings: list[dict], root: Path) -> tuple[str, str]:
    """Returns (context_summary, full_markdown)."""
    edits = [r for r in rows if r.get("event") == "edit"]
    routes = [r for r in rows if r.get("event") == "route"]
    skills = [r for r in rows if r.get("event") == "skill"]
    skill_reads = [r for r in rows if r.get("event") == "skill-read"]
    denies = [r for r in rows if r.get("event") == "gate-deny"]
    traps = [r for r in rows if r.get("event") == "trap"]

    invoked = {r.get("skill", "") for r in skills}
    read = {r.get("skill", "") for r in skill_reads}
    loaded = invoked | read

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

    # 2. unloaded strong routes — the number that must be zero.
    #
    # Redefined (idea-2ao follow-up) from "any route the router named" to
    # "a route that matched on real CODE, to a CRAFT skill, that nothing
    # ever invoked or read". The old, broader definition counted
    # react-components / next-best-practices constantly — they route on
    # generic framework structure ("export function", "app/") that fires on
    # almost every file in a React/Next project, and nothing "invokes" a
    # framework-conventions skill the way it invokes emil-design-eng for a
    # drawer. That produced a permanent false "must be zero" alarm. A
    # path-only match (skill named because the FOLDER was "components/",
    # not because of anything written) is weak for the same reason a
    # path-only is_ui_file() extension check is weak — see match_routes().
    strong_craft = [r for r in routes
                    if r.get("strength") == "code"
                    and r.get("cls", "craft") == "craft"]
    wanted = defaultdict(set)
    for r in strong_craft:
        skill = r.get("skill", "")
        if skill and skill != "copy-gate":
            wanted[skill].add(r.get("component", "?"))
    unloaded = {s: c for s, c in wanted.items()
                if s.split()[0] not in loaded and s not in loaded}
    # Split the unloaded routes by whether the agent could have closed them.
    # Counting a user-invocable-only skill or a route to a skill that does not
    # exist as an "invocation gap" made the number impossible to act on
    # (2026-09-08).
    gaps, user_only, broken = {}, {}, {}
    for sk, comps in unloaded.items():
        st = L.skill_status(sk)
        if st == "user-only":
            user_only[sk] = comps
        elif st == "missing":
            broken[sk] = comps
        else:
            gaps[sk] = comps

    # 3. coverage
    routed_files = {r.get("file", "") for r in routes}
    uncovered = sorted(rel(f, root) for f in ({r.get("file", "") for r in edits} - routed_files - {""}))

    md = [f"# Design session report — {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}", ""]
    md.append(f"{len(edits)} UI edits · {len(routes)} routes emitted · "
              f"{len(skills)} skill invocations · {len(denies)} denials · {len(traps)} trap firings")
    md.append(mcp_summary_line(rows))
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

    md.append("## 2. Unloaded strong routes")
    md.append("")
    md.append("_A route that matched real CODE (not just a path fragment) to a craft "
              "skill (not a framework-conventions one), that nothing ever invoked or "
              "read. This must be zero._")
    md.append("")
    if gaps:
        md.append("| Skill named | For | Loaded |")
        md.append("|---|---|---|")
        for s, comps in sorted(gaps.items()):
            md.append(f"| `{s}` | {', '.join(sorted(comps))} | **NO** |")
        md.append("")
        md.append(f"**UNLOADED STRONG ROUTES = {len(gaps)}.** The routing fired on real "
                  f"code but the skill never loaded or was read.")
    else:
        md.append("**UNLOADED STRONG ROUTES = 0.** Every strong craft route was "
                  "invoked or read.")
    md.append("")

    if user_only:
        md.append("### Routed, but only the user can run them")
        md.append("")
        md.append("_These set `disable-model-invocation`, so no agent can close them. "
                  "They are listed so the work is visible, not as a gap._")
        md.append("")
        for sk, comps in sorted(user_only.items()):
            md.append(f"- `/{sk}` for {', '.join(sorted(comps))}")
        md.append("")
    if broken:
        md.append("### Broken routes")
        md.append("")
        md.append("_The route names something that is not an installed skill. This is a "
                  "defect in `component-routing.md`, not a skipped step._")
        md.append("")
        for sk, comps in sorted(broken.items()):
            md.append(f"- `{sk}` (no such skill) for {', '.join(sorted(comps))}")
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

    # 6. Deep detector pass — ALWAYS present, even empty. A section that only
    # appears when it has findings is indistinguishable from a section that
    # never ran; the report must say which happened.
    edit_files = sorted({r.get("file", "") for r in edits if r.get("file")})
    md.append("## 6. Deep detector pass")
    md.append("")
    if not edit_files:
        md.append("Not run (no touched UI files).")
    elif not findings:
        md.append(f"0 findings across {len(edit_files)} files.")
    else:
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

    # 8. Referensgolv — always rendered, same reasoning as section 6: a
    # section that only appears when there is something to report is
    # indistinguishable from one that never ran.
    ref_reads = [r for r in rows if r.get("event") == "ref-read"]
    taste_n = sum(1 for r in ref_reads if r.get("cat") == "taste")
    feedback_n = sum(1 for r in ref_reads if r.get("cat") == "feedback")
    catalogue_reads = [r for r in ref_reads if r.get("cat") == "catalogue"]
    catalogue_slugs = sorted({r.get("slug") for r in catalogue_reads if r.get("slug")})
    references_reads = [r for r in ref_reads
                         if r.get("cat") == "references" and r.get("sub") != "scroll"]
    scroll_reads = [r for r in ref_reads
                    if r.get("cat") == "references" and r.get("sub") == "scroll"]
    scripts_n = sum(1 for r in ref_reads if r.get("cat") == "scripts")

    gens = [r for r in rows if r.get("event") == "generation" and not r.get("preflight")]
    pres = [r for r in rows if r.get("event") == "generation" and r.get("preflight")]
    if gens or pres:
        md.append("## 7b. Genererat material")
        md.append("")
        spent = sum(float(r.get("credits") or 0) for r in gens)
        models = sorted({r.get("model", "?") for r in gens})
        md.append(f"{len(gens)} jobb · {len(pres)} get_cost-preflights · "
                  f"{spent:.1f} credits lasta · modeller: {', '.join(models) or 'okand'}")
        md.append("")
        md.append("| Modell | Jobb | Credits |")
        md.append("|---|---|---|")
        for r in gens[:20]:
            md.append(f"| `{r.get('model','?')}` | `{str(r.get('job',''))[:8]}` | "
                      f"{r.get('credits','?')} |")
        if len(gens) > len(pres):
            md.append("")
            md.append(f"**{len(gens) - len(pres)} jobb utan foregaende get_cost.** "
                      "Kostnaden ar lasbar utan att koa nagot; att inte lasa den ar ett val.")
        md.append("")
        md.append("Stam av mot `credits.json` och mot `balance` fore och efter "
                  "(references/generation.md § Kreditgrinden).")
        md.append("")

    md.append("## 8. Referensgolv")
    md.append("")
    md.append(f"- **taste** — {taste_n} read(s)")
    md.append(f"- **feedback** — {feedback_n} read(s)")
    md.append(f"- **catalogue** — {len(catalogue_reads)} read(s)"
              + (f" ({', '.join(catalogue_slugs)})" if catalogue_slugs else ""))
    ref_paths = sorted({rel(r.get("file", ""), root) for r in references_reads if r.get("file")})
    md.append(f"- **references** — {len(references_reads)} read(s)"
              + (": " + ", ".join(f"`{p}`" for p in ref_paths[:12]) if ref_paths else ""))
    scroll_names = sorted({Path(r.get("file", "")).name for r in scroll_reads if r.get("file")})
    md.append(f"- **scroll** — {len(scroll_reads)} read(s)"
              + (": " + ", ".join(f"`{n}`" for n in scroll_names) if scroll_names else ""))
    md.append(f"- **scripts** — {scripts_n} read(s)")
    if _scroll_condition(rows) and not scroll_reads:
        md.append("")
        md.append("**scroll gap** — scrollkoreografi signalerades (intent eller route) "
                  "men inga scroll-referenser (devices.md / feel-and-fingerprint.md) "
                  "har lästs.")
    md.append("")

    # Terse context summary — the report file carries the detail.
    summary = [
        f"[design session] {len(edits)} UI edits · {len(routes)} routes · {len(skills)} skill loads",
    ]
    if gaps:
        summary.append(
            f"UNLOADED STRONG ROUTES = {len(gaps)} — route gap (strong, craft only): " +
            ", ".join(sorted(gaps)) + " matched real code but never loaded."
        )
    else:
        summary.append("Route gap (strong, craft only) = 0.")
    if traps:
        summary.append(f"GATE 60 fired {len(traps)}x — demoted-skill palette reached the build.")
    if findings:
        summary.append(f"Deep detector: {len(findings)} findings across "
                       f"{len({f.get('antipattern') for f in findings})} rules.")
    if uncovered:
        summary.append(f"{len(uncovered)} UI files got no route.")

    return "\n".join(summary), "\n".join(md)


def _is_reduced_shot(file: str) -> bool:
    """A vision row's file looks like a reduced-motion capture.

    Unused since the 2026-09-07 motion-always override (FEEDBACK.md F-011):
    builds no longer branch on prefers-reduced-motion, so there is no separate
    reduced-motion render left to verify. Kept only so old ledger rows/tests
    referencing "rm-" filenames don't need rewriting.

    Filename convention only ("reduced" anywhere, or "rm-" as a prefix) — the
    ledger has no way to know what prefers-reduced-motion state a screenshot
    was actually taken under, so the naming convention IS the signal.
    """
    try:
        name = Path(file).name.lower()
    except Exception:
        return False
    return "reduced" in name or name.startswith("rm-")


def _scroll_condition(rows: list[dict]) -> bool:
    """True when this session's brief or a route named scroll choreography."""
    intent_rows = [r for r in rows if r.get("event") == "intent"]
    latest_scroll = bool(intent_rows) and intent_rows[-1].get("scroll") == 1
    route_scroll = any(
        r.get("event") == "route" and r.get("skill") == "design"
        and r.get("signal") == "scroll" for r in rows
    )
    return latest_scroll or route_scroll


def exit_bar_block(rows: list[dict], root: Path) -> str | None:
    """The mechanical /goal. A design session may not end sight unseen.

    Blocks the stop when UI edits happened and no rendered image was Read
    after the last edit. This is the enforcement the Snajp session proved out:
    six shipped-quality defects were found in rounds run AFTER the page
    already looked done, and every one was found in a screenshot, not in code.

    Scroll choreography no longer has a second, stricter bar: since the
    2026-09-07 motion-always override (FEEDBACK.md F-011), builds never branch
    on prefers-reduced-motion, so a reduced-motion capture would just be the
    same render again, not a different one worth verifying separately.

    Capped at 2 blocks per session so a
    genuinely broken capture path degrades to the old advisory behaviour
    instead of a livelock.
    """
    edits = [r.get("ts", "") for r in rows if r.get("event") == "edit"]
    if not edits:
        return None
    visions = [r for r in rows if r.get("event") == "vision"]
    vision_tss = [r.get("ts", "") for r in visions]

    if not (vision_tss and max(vision_tss) > max(edits)):
        looked = "no rendered image was ever Read" if not vision_tss else \
            "the last rendered image you Read is older than your last edit"
        message = (
            f"[design-stop] {len(edits)} UI edits this session and {looked}. "
            "The exit bar (CARL DESIGN rules 5-7): render the page, capture PNGs "
            "(shoot.py / shoot_slices.py or the browser pane), Read every PNG so "
            "the pixels actually enter context, fix what you see, and repeat "
            "until a full pass finds nothing. Then state plainly whether the "
            "result honestly beats the references named before the build. "
            "Judging from code does not count. If capture is genuinely "
            "impossible, say so to the user explicitly instead of stopping "
            "silently."
        )
    else:
        return None

    counter = L.session_file(root, ".stop-blocks")
    try:
        n = int(counter.read_text(encoding="utf-8").strip() or "0")
    except Exception:
        n = 0
    if n >= 2:
        return None
    try:
        counter.write_text(str(n + 1), encoding="utf-8")
    except Exception:
        pass
    return message


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    root = L.project_root(event)

    rows = L.scope_to_session(L.all_rows(root))

    # Arm/disarm (idea-2ao follow-up): an unarmed session gets a one-line
    # advisory, never the full report and never the exit-bar block. Blocking
    # the Stop hook on a session that never showed real design intent — a
    # stray .ts edit in a repo that happens to have a DESIGN.md — was exactly
    # the kind of over-trigger this whole chain was rebuilt to stop doing.
    if not L.armed(root):
        edits = [r for r in rows if r.get("event") == "edit"]
        if not edits:
            return
        # Once per edit count, not once per Stop: Stop fires after every reply,
        # and re-emitting the same line re-invoked an idle agent ~8 times in a
        # row (ai-job-search, 2026-10-19). Same idea as .stop-signature below.
        stamp = L.session_file(root, ".unarmed-notice")
        try:
            if stamp.exists() and int(stamp.read_text(encoding="utf-8") or 0) >= len(edits):
                return
            stamp.write_text(str(len(edits)), encoding="utf-8")
        except Exception:
            pass
        L.emit("Stop", f"[design] {len(edits)} UI-filer ändrade utan armad "
               "designsession (ingen rapport). Var det designarbete: ladda "
               "Skill(design) nästa gång.")
        return

    # Stay silent unless real design work happened. Bookkeeping rows alone
    # (a verify-discipline injection, an intent detection) are not a session
    # worth reporting on, and a report for zero edits reads as noise.
    if not any(r.get("event") in ("edit", "gate-deny", "trap") for r in rows):
        return

    # The exit bar comes before the report: an unseen build is not reportable,
    # it is unfinished.
    reason = exit_bar_block(rows, root)
    if reason:
        print(json.dumps({"decision": "block", "reason": reason}))
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

    # Dedup. This fires on every turn end, so a conversational stretch after the
    # design work is done re-emitted a byte-identical block once per turn and
    # re-wrote the report under a fresh timestamp. Same signature means nothing
    # changed: skip both. The title line carries a per-minute timestamp and must
    # NOT enter the hash — hashing it made "identical" mean "same wall-clock
    # minute" and produced 48 spam reports.
    sig_src = md.split("\n", 1)[1] if "\n" in md else md
    sig = hashlib.sha256(sig_src.encode("utf-8")).hexdigest()
    try:
        stamp = L.state_dir(root) / ".stop-signature"
        if stamp.exists() and stamp.read_text(encoding="utf-8").strip() == sig:
            return
        stamp.write_text(sig, encoding="utf-8")
    except Exception:
        pass

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
