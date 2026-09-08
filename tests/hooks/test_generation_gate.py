# -*- coding: utf-8 -*-
"""T12 fixtures — the generation layer is measured and gated like every other call.

Four cases:
  A  generate_* with no budget line and no preflight   -> DENY, naming both
  B  the same call with `get_cost: true`               -> ALLOW (a preflight is free)
  C  budget line + a logged preflight, then the real call -> ALLOW
  D  a completed call is logged as `event: generation` with model, job and credits
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

REPO = Path(r"C:/Users/Anton L/anti-slop-design")
SP = Path(r"C:/Users/ANTONL~1/AppData/Local/Temp/claude/"
          r"C--Users-Anton-L-anti-slop-design/284cb161-2d87-493a-9b93-7fafef935807/scratchpad")
ROOT = SP / "t12-root"
SID = "dddddddd-0000-4000-8000-00000000000d"
TOOL = "mcp__cef36fd1-bedf-4056-ae8d-c1fde27b3553__generate_video"


def build(rows=(), brief=None):
    if ROOT.exists():
        shutil.rmtree(ROOT)
    (ROOT / ".impeccable").mkdir(parents=True)
    (ROOT / ".impeccable" / "design-session.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    if brief:
        (ROOT / "runs" / "cell").mkdir(parents=True, exist_ok=True)
        (ROOT / "runs" / "cell" / "BRIEF.md").write_text(brief, encoding="utf-8")


def run_gate(label, params):
    ev = {"session_id": SID, "hook_event_name": "PreToolUse", "cwd": str(ROOT),
          "tool_name": TOOL, "tool_input": {"params": params}}
    r = subprocess.run([sys.executable, str(REPO / "hooks" / "design-gate.py")],
                       input=json.dumps(ev), capture_output=True, text=True,
                       encoding="utf-8", env=dict(os.environ), cwd=str(ROOT))
    out = (r.stdout or "").strip()
    if not out:
        print(label + ": ALLOW")
        return "ALLOW", ""
    d = json.loads(out)
    hso = d.get("hookSpecificOutput", {})
    reason = hso.get("permissionDecisionReason", "")
    print(label + ": " + hso.get("permissionDecision", "?").upper())
    for line in reason.splitlines()[1:]:
        print("    - " + line[:120])
    return hso.get("permissionDecision", "?"), reason


def run_track(params, response):
    ev = {"session_id": SID, "hook_event_name": "PostToolUse", "cwd": str(ROOT),
          "tool_name": TOOL, "tool_input": {"params": params}, "tool_response": response}
    subprocess.run([sys.executable, str(REPO / "hooks" / "design-vision-track.py")],
                   input=json.dumps(ev), capture_output=True, text=True,
                   encoding="utf-8", env=dict(os.environ), cwd=str(ROOT))
    rows = []
    p = ROOT / ".impeccable" / "design-session.jsonl"
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


BUDGET_BRIEF = "# BRIEF\n\ngeneration budget: 20 credits\n"

# A — nothing in place
build()
dec, reason = run_gate("A  no budget, no preflight", {"model": "kling3_0"})
assert dec == "deny" and "generation budget" in reason and "get_cost" in reason

# B — a preflight call itself is always allowed; that is the point of it
build()
dec, _ = run_gate("B  the get_cost preflight itself", {"model": "kling3_0", "get_cost": True})
assert dec == "ALLOW"

# C — budget written, preflight logged, real call goes through
rows = [{"ts": "2026-09-08T12:00:00+00:00", "session": SID, "event": "generation",
         "tool": TOOL, "model": "kling3_0", "preflight": 1}]
build(rows, brief=BUDGET_BRIEF)
dec, _ = run_gate("C  budget + logged preflight", {"model": "kling3_0"})
assert dec == "ALLOW"

# D — the completed call lands in the ledger with its facts
build(rows, brief=BUDGET_BRIEF)
after = run_track({"model": "kling3_0"},
                  "queued job 8e58cea5-0000-4000-8000-000000000001, cost 17.5 credits")
gen = [r for r in after if r.get("event") == "generation" and not r.get("preflight")]
assert gen, "no generation row logged"
g = gen[-1]
print("D  ledger row: model=%s job=%s credits=%s session=%s"
      % (g.get("model"), (g.get("job") or "")[:8], g.get("credits"), (g.get("session") or "")[:8]))
assert g.get("model") == "kling3_0"
assert g.get("credits") == 17.5
assert g.get("session") == SID

print("T12 fixtures: all four cases behaved as specified.")
