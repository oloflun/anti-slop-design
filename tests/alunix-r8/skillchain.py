#!/usr/bin/env python
"""Skill-kedjan per agent, Alunix r9. Stdlib only.

    python tests/alunix-r8/skillchain.py --round 4 [--lead <session-id>] [--cell V3c]
        -> tests/alunix-r8/runs/<cell>/SKILLCHAIN-r<N>.md

Two sources, two kinds of agent (plan § Skill-kedjan bevakad per agent):

  * headless builders: logs/round-N/*.meta.json carries the builder's own session id;
    its Skill calls come from the stream-json log, its ledger rows from
    .impeccable/design-session.jsonl grouped on that session.
  * Agent-tool subagents (architect, reviewers, copy agent): they share the lead's
    CLAUDE_CODE_SESSION_ID (F-014), so the ledger cannot tell them apart. Their Skill
    calls come from ~/.claude/projects/<slug>/<lead>/subagents/agent-*.jsonl; their
    ledger rows are the lead session's rows inside the agent's time window. Windows
    overlap when agents run in parallel, and the table says so per row.

Gap = strong craft routes (strength "code", cls "craft") whose skill was never loaded
in the same agent's window, the same definition design-stop.py § 2 uses.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

R8 = Path(__file__).resolve().parent
REPO = R8.parents[1]
sys.path.insert(0, str(REPO / "tests" / "alunix-ab-r6"))
from monitor import read_jsonl, TRANSCRIPTS  # noqa: E402  the r6 transcript reader

LEDGER = REPO / ".impeccable" / "design-session.jsonl"
CATS = ("taste", "feedback", "catalogue", "references", "scroll")


def ts(s: str) -> datetime:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(timezone.utc)


def skill_calls(objs: list[dict]) -> tuple[list[str], datetime | None, datetime | None]:
    """Skill tool_use names in order, and the first/last timestamp of the transcript."""
    names, first, last = [], None, None
    for o in objs:
        t = o.get("timestamp")
        if t:
            d = ts(t)
            first = first or d
            last = d
        if o.get("type") != "assistant":
            continue
        for b in (o.get("message") or {}).get("content") or []:
            if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Skill":
                names.append(str((b.get("input") or {}).get("skill") or "?"))
    return names, first, last


def summarise(rows: list[dict], skills: list[str]) -> dict:
    loaded = set(skills) | {str(r.get("skill", "")).split()[0] for r in rows if r.get("event") == "skill"}
    cats = Counter(str(r.get("cat") or "") for r in rows if r.get("event") == "ref-read")
    reads = Counter(str(r.get("skill") or "") for r in rows if r.get("event") == "skill-read")
    routes = [r for r in rows if r.get("event") == "route"]
    strong = {str(r.get("skill", "")) for r in routes
              if r.get("strength") == "code" and r.get("cls", "craft") == "craft"
              and r.get("skill") != "copy-gate"}
    gap = sorted(s for s in strong if s.split()[0] not in loaded)
    return {
        "skills": skills,
        "cats": " · ".join(f"{c} {cats.get(c, 0)}" for c in CATS),
        "skill_reads": ", ".join(f"{k} {v}" for k, v in reads.most_common()) or "0",
        "routes": f"{len(routes)} emitterade, {len(strong)} starka, gap {len(gap)}" + (f": {', '.join(gap)}" if gap else ""),
        "deny": sum(1 for r in rows if r.get("event") == "gate-deny"),
        "vision": sum(1 for r in rows if r.get("event") == "vision"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--round", type=int, required=True)
    ap.add_argument("--cell", default="V3c")
    ap.add_argument("--lead", default=None, help="lead session id (default: newest meta.json's parent transcript is NOT known; pass it)")
    a = ap.parse_args()

    ledger = []
    for lp in (LEDGER.with_suffix(".prev.jsonl"), LEDGER):   # design-stop rotates the ledger
        if lp.is_file():
            ledger += read_jsonl(lp)[0]
    for r in ledger:
        r["_t"] = ts(r["ts"]) if r.get("ts") else None
    L = [f"# Skill-kedjan per agent, {a.cell} runda {a.round}", "",
         f"Källa: `{LEDGER.relative_to(REPO)}`, `logs/round-{a.round}/*.meta.json`, "
         f"`~/.claude/projects/<slug>/<lead>/subagents/`. Genererad {datetime.now(timezone.utc).isoformat(timespec='seconds')}.", "",
         "| Agent | Form | Skill-anrop i ordning | ref-read per kategori | skill-read | route: emitterade / starka / gap | gate-deny | vision | fönster |",
         "|---|---|---|---|---|---|---|---|---|"]

    def row(name: str, form: str, s: dict, window: str) -> None:
        L.append(f"| {name} | {form} | {' → '.join(s['skills']) or '(inga)'} | {s['cats']} | {s['skill_reads']} | "
                 f"{s['routes']} | {s['deny']} | {s['vision']} | {window} |")

    # headless builders
    for meta in sorted((R8 / "logs" / f"round-{a.round}").glob("*.meta.json")):
        if not meta.name.startswith("B-" + a.cell):
            continue
        m = json.loads(meta.read_text(encoding="utf-8"))
        sid = m.get("session_id")
        stem = meta.name[:-len(".meta.json")]
        objs = []   # an interrupted round is resumed into a fresh log; the first half is kept as *.part1.jsonl
        for lg in sorted(meta.parent.glob(f"{stem}.part*.jsonl")) + [meta.parent / f"{stem}.jsonl"]:
            if lg.is_file():
                objs += read_jsonl(lg)[0]
        skills, first, last = skill_calls(objs)
        rows = [r for r in ledger if r.get("session") == sid]
        row(f"byggare ({m.get('model')})", f"headless, session `{sid[:8]}`", summarise(rows, skills),
            f"{first.isoformat(timespec='minutes') if first else '?'} – {last.isoformat(timespec='minutes') if last else '?'}")

    # subagents of the lead
    if a.lead:
        sub = TRANSCRIPTS / a.lead / "subagents"
        agents = []
        for mp in sorted(sub.glob("agent-*.meta.json")):
            aid = mp.name[:-len(".meta.json")]
            m = json.loads(mp.read_text(encoding="utf-8"))
            objs, _ = read_jsonl(sub / f"{aid}.jsonl")
            skills, first, last = skill_calls(objs)
            agents.append((aid, m, skills, first, last))
        for aid, m, skills, first, last in agents:
            if not first:
                continue
            rows = [r for r in ledger if r.get("session") == a.lead and r["_t"] and first <= r["_t"] <= last]
            overlap = sum(1 for o in agents if o[0] != aid and o[3] and o[4] and o[3] <= last and o[4] >= first)
            win = f"{first.isoformat(timespec='minutes')} – {last.isoformat(timespec='minutes')}"
            if overlap:
                win += f" (överlappar {overlap} agenter: ledgerraderna delas)"
            row(f"{m.get('description', aid)}", f"Agent `{m.get('agentType')}` / {m.get('model')} `{aid[-6:]}`",
                summarise(rows, skills), win)
    else:
        L.append("| (subagenter) | ge `--lead <session-id>` för att läsa dem | | | | | | | |")

    L += ["", "Gap-definitionen är design-stop.py § 2: en route som matchade på kod till en hantverksskill som "
          "aldrig laddades i samma agents fönster. Subagenter delar leadens ledger (F-014); rader i överlappande "
          "fönster räknas på varje agent som var igång, så talen där är tak, inte exakta."]
    out = R8 / "runs" / a.cell / f"SKILLCHAIN-r{a.round}.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
