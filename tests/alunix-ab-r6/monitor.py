#!/usr/bin/env python
"""Alunix A/B r6 monitor. Stdlib only.

Reads a cell's stream-json log (written by run.py) and the Claude Code
transcript for its session (main .jsonl + subagents/), and writes a per-cell
report plus a one-row-per-cell summary.

    python tests/alunix-ab-r6/monitor.py <arm> [K...]     -> monitor/<arm>-<K>.md (+ summary.md)
    python tests/alunix-ab-r6/monitor.py summary          -> monitor/summary.md over every cell found
    python tests/alunix-ab-r6/monitor.py --probe <arm>    -> monitor/probe-<arm>.md

Stream-json shapes (verified against the 2.1.241 binary):
    {"type":"system","subtype":"init", model, tools[], slash_commands[], permissionMode, mcp_servers[], plugins[]?, skills[]?, agents[]?}
    {"type":"system","subtype":"hook_started",  hook_id, hook_name, hook_event}
    {"type":"system","subtype":"hook_progress", hook_id, hook_name, hook_event, stdout, stderr, output}
    {"type":"system","subtype":"hook_response", hook_id, hook_name, hook_event, output, stdout, stderr, exit_code?, outcome}
    {"type":"assistant", message:{model, content:[{type:"tool_use", name, input}]}}
    {"type":"result", subtype, is_error, num_turns, duration_ms, total_cost_usd, modelUsage, permission_denials}
"""
from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
R6 = REPO / "tests" / "alunix-ab-r6"
RUNS, LOGS, PROBES, MONITOR = R6 / "runs", R6 / "logs", R6 / "probes", R6 / "monitor"
KEYS = ("K1", "K2", "K3")
ARMS = ("A", "B")
PROJECT_SLUG = re.sub(r"[^A-Za-z0-9]", "-", str(REPO))
TRANSCRIPTS = Path.home() / ".claude" / "projects" / PROJECT_SLUG
LEDGER_REL = Path(".impeccable") / "design-session.jsonl"
IMAGE_EXT = (".png", ".webp", ".jpg", ".jpeg")
CHAIN_MARKERS = (".agents/skills", ".agents\\skills", ".claude/skills", ".claude\\skills", "design-catalogue")
UNSPLASH_MARKERS = ("api.unsplash.com", "unsplash_sheet.py")
WRITE_TOOLS = ("Write", "Edit", "MultiEdit", "NotebookEdit")
HOOK_SUBTYPES = ("hook_started", "hook_progress", "hook_response")


def die(msg: str, code: int = 2) -> None:
    print(f"monitor.py: {msg}", file=sys.stderr)
    sys.exit(code)


def read_jsonl(path: Path) -> tuple[list[dict], int]:
    """(objects, bad_line_count). Tolerates partial/garbage lines."""
    objs, bad = [], 0
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except ValueError:
                bad += 1
                continue
            if isinstance(obj, dict):
                objs.append(obj)
            else:
                bad += 1
    return objs, bad


def norm(p: str) -> str:
    return p.replace("\\", "/")


def script_of(hook_name: str) -> str:
    """Basename of the hook script inside a hook command/name string."""
    m = re.search(r"([\w.\-]+\.(?:py|sh|js|mjs|cjs|ps1|cmd|bat))\b", hook_name or "")
    return m.group(1) if m else (hook_name or "?")[:60]


def hook_source(strings: list[str]) -> str:
    """repo / cache / plugin-root(unresolved) / other / none, from hook command strings."""
    if not strings:
        return "none"
    kinds: Counter = Counter()
    for s in strings:
        n = norm(s).lower()
        if "plugins/cache" in n:
            kinds["cache"] += 1
        elif "anti-slop-design" in n:
            kinds["repo"] += 1
        elif "${claude_plugin_root}" in n or "$claude_plugin_root" in n:
            kinds["plugin-root(unresolved)"] += 1
        else:
            kinds["other"] += 1
    return "+".join(f"{k}:{v}" for k, v in kinds.most_common())


def is_inside(path: str, root: Path | None) -> bool:
    if root is None:
        return True
    try:
        p = Path(path)
        if not p.is_absolute():
            p = REPO / p
        p = p.resolve()
        return root.resolve() in p.parents or p == root.resolve()
    except (OSError, ValueError):
        return False


# ----------------------------------------------------------------------------- collectors

class Report:
    def __init__(self, label: str, arm: str, key: str, cell_dir: Path | None):
        self.label, self.arm, self.key, self.cell_dir = label, arm, key, cell_dir
        self.session_id: str | None = None
        self.model: Counter = Counter()
        self.effort: Counter = Counter()
        self.turns = self.duration_ms = self.cost = None
        self.result_subtype = None
        self.is_error = None
        self.init: dict = {}
        self.tools_main: Counter = Counter()
        self.tools_sub: Counter = Counter()
        self.skills: list[tuple[str, int, str]] = []         # (skill, turn, agent)
        self.hooks: list[dict] = []                           # from stream log
        self.hook_scripts: Counter = Counter()
        self.hook_outcomes: Counter = Counter()
        self.hook_strings: list[str] = []
        self.transcript_hooks: Counter = Counter()            # from transcript system lines
        self.chain_reads: OrderedDict = OrderedDict()
        self.image_reads: OrderedDict = OrderedDict()
        self.unsplash_calls = 0
        self.writes: list[tuple[str, str, str, bool]] = []    # (tool, path, agent, outside)
        self.agents: list[dict] = []
        self.subagents: list[dict] = []
        self.ledger: Counter = Counter()
        self.ledger_paths: list[str] = []
        self.ref_read_cats: Counter = Counter()
        self.ref_read_rows: list[dict] = []
        self.scroll_routes = 0
        self.permission_denials = 0
        self.bad_lines: dict[str, int] = {}
        self.notes: list[str] = []
        self.meta: dict = {}
        self.final_text = ""

    def note_tool_use(self, block: dict, agent: str, turn: int) -> None:
        name = block.get("name") or "?"
        inp = block.get("input") or {}
        if not isinstance(inp, dict):
            inp = {}
        (self.tools_main if agent == "main" else self.tools_sub)[name] += 1
        if name == "Skill":
            self.skills.append((str(inp.get("skill") or inp.get("name") or "?"), turn, agent))
        elif name == "Read":
            fp = str(inp.get("file_path") or "")
            if any(m in fp for m in CHAIN_MARKERS):
                self.chain_reads[norm(fp)] = True
            if fp.lower().endswith(IMAGE_EXT):
                self.image_reads[norm(fp)] = True
        elif name == "Bash":
            cmd = str(inp.get("command") or "")
            if any(m in cmd for m in UNSPLASH_MARKERS):
                self.unsplash_calls += 1
        elif name in WRITE_TOOLS:
            fp = str(inp.get("file_path") or inp.get("notebook_path") or "")
            self.writes.append((name, norm(fp), agent, not is_inside(fp, self.cell_dir)))
        elif name == "Agent":
            self.agents.append({"subagent_type": inp.get("subagent_type"), "model": inp.get("model"),
                                "description": inp.get("description"), "agent": agent})


def scan_stream(rep: Report, log: Path) -> set[str]:
    """Collect from the stream-json log. Returns tool_use ids seen (to dedupe vs transcript)."""
    objs, bad = read_jsonl(log)
    rep.bad_lines[log.name] = bad
    seen_ids: set[str] = set()
    hooks_by_id: dict[str, dict] = {}
    turn = 0
    for o in objs:
        t, st = o.get("type"), o.get("subtype")
        if t == "system" and st == "init":
            rep.session_id = rep.session_id or o.get("session_id")
            rep.init = {k: o.get(k) for k in ("model", "tools", "slash_commands", "skills", "agents",
                                              "plugins", "plugin_errors", "permissionMode",
                                              "claude_code_version", "mcp_servers") if k in o}
        elif t == "system" and st in HOOK_SUBTYPES:
            hid = str(o.get("hook_id") or f"anon-{len(hooks_by_id)}")
            h = hooks_by_id.setdefault(hid, {"hook_id": hid, "hook_name": o.get("hook_name"),
                                             "hook_event": o.get("hook_event"), "started": False,
                                             "outcome": None, "exit_code": None, "output": "",
                                             "decision": None, "tool_name": None})
            if st == "hook_started":
                h["started"] = True
                rep.hook_scripts[script_of(str(o.get("hook_name") or ""))] += 1
                rep.hook_strings.append(str(o.get("hook_name") or ""))
            elif st == "hook_response":
                h["outcome"] = o.get("outcome")
                h["exit_code"] = o.get("exit_code")
                out = str(o.get("output") or o.get("stdout") or "")
                h["output"] = out[:300]
                rep.hook_outcomes[str(o.get("outcome"))] += 1
                try:
                    j = json.loads(out)
                    if isinstance(j, dict):
                        hso = j.get("hookSpecificOutput") or {}
                        h["decision"] = (j.get("decision") or hso.get("permissionDecision")
                                         or ("additionalContext" if hso.get("additionalContext") else None))
                        h["tool_name"] = j.get("tool_name") or hso.get("tool_name")
                except ValueError:
                    pass
            for k in ("hook_name", "hook_event"):
                if not h.get(k) and o.get(k):
                    h[k] = o.get(k)
            # hook_name is often "PreToolUse:Write" style or the command; keep a tool hint
            if not h.get("tool_name"):
                m = re.match(r"^(?:\w+):([\w|]+)$", str(o.get("hook_name") or ""))
                if m:
                    h["tool_name"] = m.group(1)
        elif t == "assistant":
            msg = o.get("message") or {}
            if msg.get("model"):
                rep.model[str(msg["model"])] += 1
            turn += 1
            for b in msg.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    seen_ids.add(str(b.get("id")))
                    rep.note_tool_use(b, "main", turn)
        elif t == "result":
            rep.turns = o.get("num_turns")
            rep.duration_ms = o.get("duration_ms")
            rep.cost = o.get("total_cost_usd")
            rep.result_subtype = st
            rep.is_error = o.get("is_error")
            rep.final_text = str(o.get("result") or "")[:800]
            pd = o.get("permission_denials")
            if isinstance(pd, list):
                rep.permission_denials = len(pd)
            rep.session_id = rep.session_id or o.get("session_id")
    rep.hooks = list(hooks_by_id.values())
    return seen_ids


def scan_transcript(rep: Report, seen_ids: set[str]) -> None:
    if not rep.session_id:
        rep.notes.append("no session id (no init/result line and no meta) — transcript not read")
        return
    main = TRANSCRIPTS / f"{rep.session_id}.jsonl"
    if not main.is_file():
        rep.notes.append(f"transcript missing: {main}")
        return
    objs, bad = read_jsonl(main)
    rep.bad_lines[main.name] = bad
    turn = 0
    for o in objs:
        t = o.get("type")
        if t == "assistant":
            turn += 1
            if o.get("effort"):
                rep.effort[str(o["effort"])] += 1
            msg = o.get("message") or {}
            if msg.get("model"):
                rep.model[str(msg["model"])] += 0  # presence only; stream already counted
            for b in msg.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use" and str(b.get("id")) not in seen_ids:
                    seen_ids.add(str(b.get("id")))
                    rep.note_tool_use(b, "main", turn)
        elif t == "system":
            for info in o.get("hookInfos") or []:
                cmd = str((info or {}).get("command") or "")
                if cmd and cmd != "callback":
                    rep.transcript_hooks[script_of(cmd)] += 1
                    rep.hook_strings.append(cmd)
            if o.get("subtype") == "hook_summary" or "hookErrors" in o:
                for err in o.get("hookErrors") or []:
                    rep.notes.append(f"hook error: {str(err)[:200]}")
        elif t == "user" and o.get("toolDenialKind"):
            rep.permission_denials += 1

    sub_dir = TRANSCRIPTS / rep.session_id / "subagents"
    if sub_dir.is_dir():
        for meta in sorted(sub_dir.glob("agent-*.meta.json")):
            aid = meta.name[:-len(".meta.json")]
            try:
                m = json.loads(meta.read_text(encoding="utf-8"))
            except ValueError:
                m = {}
            entry = {"id": aid, "agentType": m.get("agentType"), "model": m.get("model"),
                     "description": m.get("description"), "tool_uses": 0, "skills": []}
            jl = sub_dir / f"{aid}.jsonl"
            if jl.is_file():
                sobjs, sbad = read_jsonl(jl)
                rep.bad_lines[jl.name] = sbad
                sturn = 0
                for o in sobjs:
                    if o.get("type") != "assistant":
                        continue
                    sturn += 1
                    if o.get("effort"):
                        rep.effort[str(o["effort"])] += 1
                    for b in (o.get("message") or {}).get("content") or []:
                        if isinstance(b, dict) and b.get("type") == "tool_use":
                            entry["tool_uses"] += 1
                            rep.note_tool_use(b, aid, sturn)
                            if b.get("name") == "Skill":
                                entry["skills"].append(str((b.get("input") or {}).get("skill")))
            rep.subagents.append(entry)


def scan_ledger(rep: Report) -> None:
    if not rep.session_id:
        return
    candidates = [REPO / LEDGER_REL]
    if rep.cell_dir:
        candidates.append(rep.cell_dir / LEDGER_REL)
    for path in candidates:
        if not path.is_file():
            continue
        objs, _ = read_jsonl(path)
        hits = 0
        for o in objs:
            if o.get("session") == rep.session_id:
                event = str(o.get("event"))
                rep.ledger[event] += 1
                hits += 1
                if event == "ref-read":
                    rep.ref_read_cats[str(o.get("cat") or "")] += 1
                    rep.ref_read_rows.append(o)
                elif event == "route" and o.get("signal") == "scroll":
                    rep.scroll_routes += 1
        if hits:
            rep.ledger_paths.append(str(path))


def build_report(label: str, arm: str, key: str, log: Path, meta_path: Path,
                 cell_dir: Path | None) -> Report:
    if not log.is_file():
        die(f"no stream log at {log} — has `run.py {'probe' if key == 'probe' else 'build'} {arm}` been run?")
    rep = Report(label, arm, key, cell_dir)
    if meta_path.is_file():
        try:
            rep.meta = json.loads(meta_path.read_text(encoding="utf-8"))
            rep.session_id = rep.meta.get("session_id")
        except ValueError:
            rep.notes.append(f"meta unreadable: {meta_path}")
    else:
        rep.notes.append(f"meta missing: {meta_path}")
    seen = scan_stream(rep, log)
    scan_transcript(rep, seen)
    scan_ledger(rep)
    return rep


# ----------------------------------------------------------------------------- rendering

def fmt_cost(c) -> str:
    return f"${c:.2f}" if isinstance(c, (int, float)) else "-"


def fmt_dur(ms) -> str:
    return f"{ms / 1000:.0f}s" if isinstance(ms, (int, float)) else "-"


def md_list(items, empty="(none)") -> str:
    items = list(items)
    return "\n".join(f"- {i}" for i in items) if items else f"- {empty}"


def ref_read_line(row: dict) -> str:
    cat = str(row.get("cat") or "?")
    if row.get("sub"):
        cat += f"/{row['sub']}"
    slug = f" [{row['slug']}]" if row.get("slug") else ""
    return f"{cat}{slug} — {row.get('file', '')}"


def render_cell(rep: Report) -> str:
    L: list[str] = []
    L.append(f"# {rep.label}")
    L.append("")
    L.append(f"- session: `{rep.session_id or '?'}`")
    L.append(f"- model: {dict(rep.model) or '?'}")
    L.append(f"- effort (transcript): {dict(rep.effort) or '?'}")
    L.append(f"- turns: {rep.turns if rep.turns is not None else '-'} · duration: {fmt_dur(rep.duration_ms)} · cost: {fmt_cost(rep.cost)}")
    L.append(f"- result: {rep.result_subtype or '(no result line)'} · is_error={rep.is_error} · permission denials={rep.permission_denials}")
    if rep.meta:
        L.append(f"- exit code: {rep.meta.get('exit_code')} · start {rep.meta.get('start')} → end {rep.meta.get('end')}")
        L.append(f"- env keys added: {rep.meta.get('env_keys_added')}")
    L.append("")
    L.append("## Init message")
    if rep.init:
        tools = rep.init.get("tools") or []
        L.append(f"- Skill tool present: {'Skill' in tools}")
        L.append(f"- tools ({len(tools)}): {', '.join(map(str, tools))}")
        sc = rep.init.get("slash_commands")
        L.append(f"- slash_commands ({len(sc) if isinstance(sc, list) else '-'}): "
                 f"{', '.join(map(str, sc)) if isinstance(sc, list) else sc!r}")
        for k in ("skills", "agents", "plugins", "plugin_errors", "permissionMode", "claude_code_version"):
            if k in rep.init:
                L.append(f"- {k}: {json.dumps(rep.init[k], ensure_ascii=False)[:1500]}")
    else:
        L.append("- (no init message in the stream log)")
    L.append("")
    L.append("## Tool use")
    L.append("main: " + (", ".join(f"{k}={v}" for k, v in rep.tools_main.most_common()) or "(none)"))
    L.append("")
    L.append("subagents: " + (", ".join(f"{k}={v}" for k, v in rep.tools_sub.most_common()) or "(none)"))
    L.append("")
    L.append("## Skill invocations (ordered)")
    L.append(md_list(f"`{s}` — turn {t}, agent {a}" for s, t, a in rep.skills))
    L.append("")
    L.append("## Hook events (stream log)")
    L.append(f"- started={sum(rep.hook_scripts.values())} · outcomes: {dict(rep.hook_outcomes) or '{}'} · source: {hook_source(rep.hook_strings)}")
    L.append("- per script: " + (", ".join(f"{k}={v}" for k, v in rep.hook_scripts.most_common()) or "(none)"))
    if rep.transcript_hooks:
        L.append("- per script (transcript hookInfos): " + ", ".join(f"{k}={v}" for k, v in rep.transcript_hooks.most_common()))
    if rep.hooks:
        L.append("")
        L.append("| event | hook | tool | outcome | exit | decision | output |")
        L.append("|---|---|---|---|---|---|---|")
        for h in rep.hooks:
            out = (h.get("output") or "").replace("|", "\\|").replace("\n", " ")[:120]
            L.append(f"| {h.get('hook_event') or ''} | {script_of(str(h.get('hook_name') or ''))} | {h.get('tool_name') or ''} "
                     f"| {h.get('outcome') or ''} | {h.get('exit_code') if h.get('exit_code') is not None else ''} "
                     f"| {h.get('decision') or ''} | {out} |")
    L.append("")
    L.append("## Chain references read (.agents/skills)")
    L.append(md_list(f"`{p}`" for p in rep.chain_reads))
    L.append("")
    L.append(f"## Image reads ({len(rep.image_reads)})")
    L.append(md_list(f"`{p}`" for p in rep.image_reads))
    L.append("")
    L.append(f"## Unsplash calls (Bash mentioning api.unsplash.com / unsplash_sheet.py): {rep.unsplash_calls}")
    L.append("")
    outside = [w for w in rep.writes if w[3]]
    L.append(f"## Write/Edit targets ({len(rep.writes)}, {len(outside)} outside cell dir)")
    L.append(md_list(f"{'**OUTSIDE** ' if o else ''}{tool} `{p}` ({a})" for tool, p, a, o in rep.writes))
    L.append("")
    L.append(f"## Agent spawns ({len(rep.agents)} tool calls, {len(rep.subagents)} subagent transcripts)")
    L.append(md_list(f"{a.get('subagent_type')} / {a.get('model')} — {a.get('description')} (from {a.get('agent')})" for a in rep.agents))
    if rep.subagents:
        L.append("")
        L.append(md_list(f"`{s['id']}` {s.get('agentType')} / {s.get('model')} — {s.get('description')} · tool_uses={s['tool_uses']} · skills={s['skills']}"
                         for s in rep.subagents))
    L.append("")
    L.append("## Ledger (.impeccable/design-session.jsonl, this session)")
    L.append(f"- by event: {dict(rep.ledger) or '{}'}")
    L.append(f"- files: {rep.ledger_paths or '(no lines for this session)'}")
    L.append(f"- ref-read by category: {dict(rep.ref_read_cats) or '{}'}")
    L.append(f"- scroll routes: {rep.scroll_routes}")
    L.append("")
    L.append(f"## ref-read rows ({len(rep.ref_read_rows)})")
    L.append(md_list(ref_read_line(r) for r in rep.ref_read_rows))
    L.append("")
    if rep.final_text:
        L.append("## Final assistant text (first 800 chars)")
        L.append("")
        L.append("```")
        L.append(rep.final_text)
        L.append("```")
        L.append("")
    L.append("## Notes")
    notes = list(rep.notes) + [f"bad/partial lines skipped: {rep.bad_lines}"]
    L.append(md_list(notes))
    L.append("")
    return "\n".join(L)


def ref_read_col(rep: Report) -> str:
    c = rep.ref_read_cats
    return (f"{c.get('taste', 0)}/{c.get('feedback', 0)}/{c.get('catalogue', 0)}/"
            f"{c.get('references', 0)}/{sum(1 for r in rep.ref_read_rows if r.get('sub') == 'scroll')}")


def summary_row(rep: Report) -> str:
    skills = ", ".join(s for s, _, _ in rep.skills) or "-"
    subs = f"{len(rep.subagents)}" + (f" ({', '.join(str(s.get('model')) for s in rep.subagents)})" if rep.subagents else "")
    outside = sum(1 for w in rep.writes if w[3])
    return (f"| {rep.label} | {rep.turns if rep.turns is not None else '-'} | {fmt_cost(rep.cost)} "
            f"| {len(rep.skills)}: {skills} | {sum(rep.hook_scripts.values())} | {hook_source(rep.hook_strings)} "
            f"| {len(rep.chain_reads)} | {len(rep.image_reads)} | {rep.unsplash_calls} | {outside} | {subs} "
            f"| {ref_read_col(rep)} |")


SUMMARY_HEAD = ("| cell | turns | cost | Skill calls | hook events | hook source | chain refs read "
                "| images read | unsplash | out-of-scope writes | subagents | ref-read t/f/c/r/scroll |\n"
                "|---|---|---|---|---|---|---|---|---|---|---|---|")


def write_summary(reports: list[Report]) -> Path:
    MONITOR.mkdir(parents=True, exist_ok=True)
    path = MONITOR / "summary.md"
    lines = ["# Alunix A/B r6 — summary", "", SUMMARY_HEAD]
    lines += [summary_row(r) for r in reports]
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def cell_paths(arm: str, key: str) -> tuple[Path, Path, Path | None]:
    if key == "probe":
        return PROBES / f"{arm}.jsonl", PROBES / f"{arm}.meta.json", PROBES
    return LOGS / f"{arm}-{key}.jsonl", LOGS / f"{arm}-{key}.meta.json", RUNS / arm / key


def all_cells() -> list[tuple[str, str]]:
    found = []
    for arm in ARMS:
        for key in KEYS:
            if (LOGS / f"{arm}-{key}.jsonl").is_file():
                found.append((arm, key))
    for arm in ARMS:
        if (PROBES / f"{arm}.jsonl").is_file():
            found.append((arm, "probe"))
    return found


def main(argv: list[str]) -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    reports: list[Report] = []

    if argv[0] == "--probe":
        if len(argv) < 2 or argv[1] not in ARMS:
            die("usage: monitor.py --probe A|B")
        arm = argv[1]
        log, meta, cell_dir = cell_paths(arm, "probe")
        rep = build_report(f"probe-{arm}", arm, "probe", log, meta, cell_dir)
        MONITOR.mkdir(parents=True, exist_ok=True)
        out = MONITOR / f"probe-{arm}.md"
        out.write_text(render_cell(rep), encoding="utf-8")
        print(f"wrote {out}")
        print(SUMMARY_HEAD)
        print(summary_row(rep))
        return

    if argv[0] == "summary":
        targets = all_cells()
        if not targets:
            die(f"no cell logs found under {LOGS} or {PROBES}")
    else:
        arm = argv[0]
        if arm not in ARMS:
            die(f"unknown arm {arm!r}; usage: monitor.py A|B [K1 K2 K3] | summary | --probe A|B")
        keys = argv[1:] or list(KEYS)
        bad = [k for k in keys if k not in KEYS]
        if bad:
            die(f"unknown key(s) {bad}")
        targets = [(arm, k) for k in keys]

    for arm, key in targets:
        log, meta, cell_dir = cell_paths(arm, key)
        label = f"probe-{arm}" if key == "probe" else f"{arm}-{key}"
        rep = build_report(label, arm, key, log, meta, cell_dir)
        MONITOR.mkdir(parents=True, exist_ok=True)
        out = MONITOR / f"{label}.md"
        out.write_text(render_cell(rep), encoding="utf-8")
        print(f"wrote {out}")
        reports.append(rep)

    if argv[0] != "summary":
        # keep summary.md covering every cell that exists, not just the ones re-run now
        done = {(r.arm, r.key) for r in reports}
        for arm, key in all_cells():
            if (arm, key) in done:
                continue
            log, meta, cell_dir = cell_paths(arm, key)
            label = f"probe-{arm}" if key == "probe" else f"{arm}-{key}"
            reports.append(build_report(label, arm, key, log, meta, cell_dir))
        reports.sort(key=lambda r: (r.key == "probe", r.arm, r.key))
    path = write_summary(reports)
    print(f"wrote {path}")
    print(SUMMARY_HEAD)
    for r in reports:
        print(summary_row(r))


if __name__ == "__main__":
    main(sys.argv[1:])
