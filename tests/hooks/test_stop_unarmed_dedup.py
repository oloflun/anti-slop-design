# -*- coding: utf-8 -*-
"""Unarmed-session Stop advisory: once per edit count, and scratchpad writes never count.

2026-10-19, ai-job-search: one HTML artifact written to the Claude scratchpad made
design-stop.py re-emit "[design] 1 UI-filer ändrade utan armad designsession" on
every Stop, re-invoking an idle agent ~8 times in a row.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]


def _run(script: str, event: dict, cwd: Path, **env_extra: str) -> str:
    env = dict(os.environ, CLAUDE_CODE_SESSION_ID=event["session_id"],
               DESIGN_HOOKS_DISABLED="0", CLAUDE_HOOKS_DISABLED="0", **env_extra)
    env.pop("DESIGN_HOOKS_FORCE_ARM", None)  # the unarmed branch is the subject
    r = subprocess.run(
        [sys.executable, str(REPO / "hooks" / script)],
        input=json.dumps(event), capture_output=True, text=True,
        encoding="utf-8", errors="replace", env=env, cwd=str(cwd),
    )
    return r.stdout or ""


def _edit_row(root: Path, sid: str, name: str) -> str:
    return json.dumps({"ts": "2026-10-19T10:00:00+00:00", "session": sid,
                       "event": "edit", "file": str(root / name)}) + "\n"


def test_second_stop_with_same_edit_count_is_silent(tmp_path):
    sid = "unarmed-dedup-1"
    led = tmp_path / ".impeccable" / "design-session.jsonl"  # .impeccable = root marker
    led.parent.mkdir()
    led.write_text(_edit_row(tmp_path, sid, "a.html"), encoding="utf-8")
    stop = {"session_id": sid, "hook_event_name": "Stop", "cwd": str(tmp_path)}

    assert "1 UI-filer" in _run("design-stop.py", stop, tmp_path)
    assert _run("design-stop.py", stop, tmp_path) == ""  # same count: nothing

    with led.open("a", encoding="utf-8") as fh:
        fh.write(_edit_row(tmp_path, sid, "b.html"))
    assert "2 UI-filer" in _run("design-stop.py", stop, tmp_path)  # grew: once more
    assert _run("design-stop.py", stop, tmp_path) == ""


def test_scratchpad_write_logs_no_edit_row(tmp_path):
    (tmp_path / ".impeccable").mkdir()
    temp = tmp_path / "temp"
    scratch = temp / "claude" / "proj" / "sess" / "scratchpad" / "page.html"
    scratch.parent.mkdir(parents=True)
    html = "<!doctype html><html><body><main><h1>Hej</h1></main></body></html>"

    def write(path: Path) -> None:
        path.write_text(html, encoding="utf-8")
        ev = {"session_id": "scratch-1", "hook_event_name": "PostToolUse",
              "cwd": str(tmp_path), "tool_name": "Write",
              "tool_input": {"file_path": str(path), "content": html}}
        _run("design-route.py", ev, tmp_path, TEMP=str(temp), TMP=str(temp), TMPDIR=str(temp))

    def edit_files() -> list[str]:
        p = tmp_path / ".impeccable" / "design-session.jsonl"
        rows = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()
                if l.strip()] if p.exists() else []
        return [Path(r["file"]).name for r in rows if r.get("event") == "edit"]

    write(scratch)
    assert edit_files() == []
    write(tmp_path / "control.html")  # control: an in-project write still logs
    assert edit_files() == ["control.html"]
