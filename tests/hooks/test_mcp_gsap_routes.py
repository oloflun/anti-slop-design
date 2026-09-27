# -*- coding: utf-8 -*-
"""mcp ledger event (inspo/ui-skills) + GSAP/Lenis craft routes + the Stop report's MCP line.

Three independent surfaces, one file because they share the same harness:
  A  design-vision-track.py logs event="mcp" for mcp__inspo__* / mcp__ui-skills__* calls,
     and leaves a plain Read behaving as before (no mcp row).
  B  design-route.py routes GSAP/ScrollTrigger/Lenis/SplitText code to the three craft
     skills (lenis, gsap-scrolltrigger, gsap-core), strength "code" — and does NOT route
     a GSAP-free file to them.
  C  design-stop.py's report carries one "MCP: ..." line, or "MCP: none".
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def _run(script: str, event: dict, cwd: Path, force_arm: bool = False) -> str:
    # Explicit override, not inherited: this harness's own shell may carry
    # DESIGN_HOOKS_DISABLED=1 (set for exactly this reason — outer hooks must
    # not fire on the agent's own work) which would make every hook a no-op.
    env = dict(os.environ, CLAUDE_CODE_SESSION_ID=event.get("session_id", ""),
               DESIGN_HOOKS_DISABLED="0", CLAUDE_HOOKS_DISABLED="0")
    if force_arm:
        env["DESIGN_HOOKS_FORCE_ARM"] = "1"
    r = subprocess.run(
        [sys.executable, str(REPO / "hooks" / script)],
        input=json.dumps(event), capture_output=True, text=True,
        encoding="utf-8", errors="replace", env=env, cwd=str(cwd),
    )
    return r.stdout or ""


def _ledger(root: Path) -> list[dict]:
    p = root / ".impeccable" / "design-session.jsonl"
    if not p.exists():
        return []
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _write_ledger(root: Path, rows: list[dict]) -> None:
    (root / ".impeccable").mkdir(parents=True, exist_ok=True)
    (root / ".impeccable" / "design-session.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")


# --------------------------------------------------------------------------
# A — mcp ledger event
# --------------------------------------------------------------------------

def _track(tool_name: str, tool_input: dict, cwd: Path, sid: str) -> list[dict]:
    (cwd / ".impeccable").mkdir(parents=True, exist_ok=True)
    ev = {"session_id": sid, "hook_event_name": "PostToolUse", "cwd": str(cwd),
          "tool_name": tool_name, "tool_input": tool_input}
    _run("design-vision-track.py", ev, cwd)
    return _ledger(cwd)


def test_mcp_inspo_get_screen_logs_row(tmp_path):
    rows = _track("mcp__inspo__get_screen", {"slug": "aspen-search"}, tmp_path, "mcpA1")
    mcp = [r for r in rows if r.get("event") == "mcp"]
    assert len(mcp) == 1, rows
    assert mcp[0]["server"] == "inspo"
    assert mcp[0]["tool"] == "get_screen"
    assert mcp[0]["arg"] == "aspen-search"


def test_mcp_ui_skills_get_skill_logs_row(tmp_path):
    rows = _track("mcp__ui-skills__get_skill",
                   {"name": "ibelick/fixing-motion-performance"}, tmp_path, "mcpA2")
    mcp = [r for r in rows if r.get("event") == "mcp"]
    assert len(mcp) == 1, rows
    assert mcp[0]["server"] == "ui-skills"
    assert mcp[0]["tool"] == "get_skill"
    assert mcp[0]["arg"] == "ibelick/fixing-motion-performance"


def test_read_still_behaves_as_before(tmp_path):
    f = tmp_path / "note.txt"
    f.write_text("hi", encoding="utf-8")
    rows = _track("Read", {"file_path": str(f)}, tmp_path, "mcpA3")
    assert not any(r.get("event") == "mcp" for r in rows)


# --------------------------------------------------------------------------
# B — GSAP/Lenis craft routes
# --------------------------------------------------------------------------

CRAFT_SKILLS = {"lenis", "gsap-scrolltrigger", "gsap-core"}


def _route(path: Path, content: str, cwd: Path, sid: str) -> list[dict]:
    (cwd / ".impeccable").mkdir(parents=True, exist_ok=True)
    ev = {"session_id": sid, "hook_event_name": "PostToolUse", "cwd": str(cwd),
          "tool_name": "Write", "tool_input": {"file_path": str(path), "content": content}}
    _run("design-route.py", ev, cwd)
    return _ledger(cwd)


def test_gsap_code_routes_to_all_three_craft_skills(tmp_path):
    f = tmp_path / "anim.js"
    content = "gsap.to('.box', {x: 100, scrollTrigger: {trigger: '.box'}});\nconst l = new Lenis();"
    rows = _route(f, content, tmp_path, "mcpB1")
    routes = [r for r in rows if r.get("event") == "route"]
    hit = {r.get("skill") for r in routes
           if r.get("strength") == "code" and r.get("cls") == "craft"}
    assert CRAFT_SKILLS <= hit, routes


def test_no_gsap_no_craft_route(tmp_path):
    f = tmp_path / "plain.js"
    content = "export function Foo() { return 1; }"
    rows = _route(f, content, tmp_path, "mcpB2")
    routes = [r for r in rows if r.get("event") == "route"]
    hit = {r.get("skill") for r in routes}
    assert not (CRAFT_SKILLS & hit), routes


# --------------------------------------------------------------------------
# C — Stop report's MCP line
# --------------------------------------------------------------------------

def _stop(cwd: Path, sid: str) -> str:
    ev = {"session_id": sid, "hook_event_name": "Stop", "cwd": str(cwd)}
    return _run("design-stop.py", ev, cwd, force_arm=True)


def _latest_report(root: Path) -> str:
    reports = sorted((root / ".impeccable").glob("design-report-*.md"))
    assert reports, "no report written"
    return reports[-1].read_text(encoding="utf-8")


def test_stop_report_has_mcp_line(tmp_path):
    sid = "mcpC1"
    rows = [
        {"ts": "2026-09-25T10:00:00+00:00", "session": sid, "event": "edit",
         "file": str(tmp_path / "index.html"), "component": "index", "tier": "ungated"},
        {"ts": "2026-09-25T10:00:01+00:00", "session": sid, "event": "vision", "file": "shot.png"},
        {"ts": "2026-09-25T10:00:02+00:00", "session": sid, "event": "mcp", "server": "inspo",
         "tool": "recommend", "arg": "editorial hero"},
        {"ts": "2026-09-25T10:00:03+00:00", "session": sid, "event": "mcp", "server": "inspo",
         "tool": "search_screens", "arg": "dark saas"},
        {"ts": "2026-09-25T10:00:04+00:00", "session": sid, "event": "mcp", "server": "inspo",
         "tool": "search_screens", "arg": "dark saas 2"},
        {"ts": "2026-09-25T10:00:05+00:00", "session": sid, "event": "mcp", "server": "inspo",
         "tool": "get_screen", "arg": "aspen-search"},
        {"ts": "2026-09-25T10:00:06+00:00", "session": sid, "event": "mcp", "server": "inspo",
         "tool": "get_screen", "arg": "vercel-pricing"},
        {"ts": "2026-09-25T10:00:07+00:00", "session": sid, "event": "mcp", "server": "ui-skills",
         "tool": "get_skill", "arg": "ibelick/fixing-motion-performance"},
        {"ts": "2026-09-25T10:00:08+00:00", "session": sid, "event": "mcp", "server": "ui-skills",
         "tool": "get_skill", "arg": "zeke/swiss-design"},
    ]
    _write_ledger(tmp_path, rows)
    _stop(tmp_path, sid)
    report = _latest_report(tmp_path)
    assert ("MCP: inspo 5 (recommend, search_screens×2, get_screen×2) · "
            "ui-skills 2 (get_skill: ibelick/fixing-motion-performance, zeke/swiss-design)") in report


def test_both_hooks_json_parse():
    for rel in ("hooks/hooks.json", ".claude/hooks/hooks.json"):
        json.loads((REPO / rel).read_text(encoding="utf-8"))


def test_stop_report_mcp_none(tmp_path):
    sid = "mcpC2"
    rows = [
        {"ts": "2026-09-25T10:00:00+00:00", "session": sid, "event": "edit",
         "file": str(tmp_path / "index.html"), "component": "index", "tier": "ungated"},
        {"ts": "2026-09-25T10:00:01+00:00", "session": sid, "event": "vision", "file": "shot.png"},
    ]
    _write_ledger(tmp_path, rows)
    _stop(tmp_path, sid)
    report = _latest_report(tmp_path)
    assert "MCP: none" in report
