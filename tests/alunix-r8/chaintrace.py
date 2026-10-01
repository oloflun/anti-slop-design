#!/usr/bin/env python
"""Skill-kedjan per subagent: varje inspo-, ui-skills- och Skill-anrop i ordning.

    python tests/alunix-r8/chaintrace.py <lead-session-id> [--since ISO]

Läser ~/.claude/projects/<slug>/<lead>/subagents/agent-*.jsonl. Stdlib only.
"""
import json, sys
from pathlib import Path

WATCH = ("mcp__inspo__", "mcp__ui-skills__")
lead = sys.argv[1]
since = sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv else ""
root = Path.home() / ".claude" / "projects" / "C--Users-Anton-L-anti-slop-design" / lead / "subagents"

for f in sorted(root.glob("agent-*.jsonl"), key=lambda p: p.stat().st_mtime):
    rows, first, other = [], None, 0
    for line in f.open(encoding="utf-8"):
        try:
            o = json.loads(line)
        except ValueError:
            continue
        t = o.get("timestamp", "")
        first = first or t
        if o.get("type") != "assistant":
            continue
        for b in (o.get("message") or {}).get("content") or []:
            if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                continue
            n, inp = b.get("name", ""), b.get("input") or {}
            if n.startswith(WATCH) or n == "Skill":
                arg = inp.get("name") or inp.get("skill") or inp.get("slug") or inp.get("query") or inp.get("brief") or inp.get("id") or ""
                rows.append(f"  {t[11:19]}  {n.replace('mcp__', '')}  {str(arg)[:70]}")
            else:
                other += 1
    if first < since:
        continue
    print(f"{f.stem}  start {first[:19]}  kedjeanrop {len(rows)}  övriga verktyg {other}")
    print("\n".join(rows) or "  (inga inspo/ui-skills/Skill-anrop)")
