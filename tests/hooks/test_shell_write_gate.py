#!/usr/bin/env python
"""The shell-write gate must fire AND stay quiet (gates.md, "Both directions").

r8 probe, 2026-09-09: a headless Opus builder wrote its UI file with
`cat > B.html <<'EOF'` and every Write/Edit-keyed check in the chain saw
nothing. This proves the Bash|PowerShell branch of design-gate.py denies
shell AUTHORING of a UI file in an armed session, warns only when unarmed,
and never touches copies or non-UI writes.

    python tests/hooks/test_shell_write_gate.py
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "hooks"))
from design_hook_lib import shell_ui_write_targets  # noqa: E402


def gate(command: str, armed: bool, tool: str = "Bash") -> str:
    td = tempfile.mkdtemp(prefix="shellgate-")
    env = dict(os.environ, PYTHONIOENCODING="utf-8",
               CLAUDE_CODE_SESSION_ID="shellgate1",
               DESIGN_HOOKS_FORCE_ARM="1" if armed else "")
    ev = {"cwd": td, "hook_event_name": "PreToolUse", "session_id": "shellgate1",
          "tool_name": tool, "tool_input": {"command": command}}
    r = subprocess.run([sys.executable, str(REPO / "hooks" / "design-gate.py")],
                       input=json.dumps(ev), capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    return r.stdout or ""


HEREDOC = "cat > runs/K3/index.html <<'EOF'\n<h1>x</h1>\nEOF"

DETECT = [
    ("heredoc into index.html", HEREDOC, ["runs/K3/index.html"]),
    ("echo >> styles.css", "echo 'a{}' >> runs/K3/styles.css", ["runs/K3/styles.css"]),
    ("tee page.html", "printf x | tee runs/K3/page.html", ["runs/K3/page.html"]),
    ("sed -i on index.html", "sed -i 's/a/b/' runs/K3/index.html", ["runs/K3/index.html"]),
    ("Set-Content on index.html", "Set-Content -Path runs/K3/index.html -Value $x", ["runs/K3/index.html"]),
    ("python open(...,'w')", "python -c \"open('runs/K3/index.html','w').write('x')\"", ["runs/K3/index.html"]),
    ("cp of the engine css is a copy, not authoring", "cp scripts/scroll/scrollcraft.css runs/K3/scroll/", []),
    ("Copy-Item is a copy", "Copy-Item scroll\\scrollcraft.js runs\\K3\\scroll\\", []),
    ("redirect into a .txt is not UI", "echo hi > NOTES.txt", []),
    ("stderr redirect is not a file", "python shoot.py 2>&1 | tail -3", []),
    ("probe output dirs are not UI", "python motion_probe.py --url x --out runs/K3/shots/r2", []),
]


def main() -> int:
    failed = 0
    for name, cmd, want in DETECT:
        got = shell_ui_write_targets(cmd)
        ok = got == want
        failed += not ok
        print(f"  [{'PASS' if ok else 'FAIL'}] detect: {name} -> {got}")

    out = gate(HEREDOC, armed=True)
    ok = '"deny"' in out and "skalskrivning" in out
    failed += not ok
    print(f"  [{'PASS' if ok else 'FAIL'}] armed session: heredoc into UI file is DENIED")

    out = gate(HEREDOC, armed=False)
    ok = '"deny"' not in out and "skalskrivning" in out
    failed += not ok
    print(f"  [{'PASS' if ok else 'FAIL'}] unarmed session: same command only WARNS")

    out = gate("cp scripts/scroll/scrollcraft.css runs/K3/scroll/", armed=True)
    ok = out.strip() == ""
    failed += not ok
    print(f"  [{'PASS' if ok else 'FAIL'}] armed session: copying the engine is silent")

    out = gate("Set-Content -Path runs/K3/index.html -Value $x", armed=True, tool="PowerShell")
    ok = '"deny"' in out
    failed += not ok
    print(f"  [{'PASS' if ok else 'FAIL'}] armed session: PowerShell Set-Content is DENIED")

    print()
    print("shell write gate: all cases behaved as specified." if not failed
          else f"shell write gate: {failed} case(s) wrong.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    raise SystemExit(main())
