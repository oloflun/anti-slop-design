# -*- coding: utf-8 -*-
"""T3 fixture: build a fake session ledger, run design-gate.py, report allow/deny."""
import json, os, subprocess, sys, shutil
try:                       # Windows console is cp1252; the deny messages are Swedish
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
from pathlib import Path

REPO = Path(r"C:/Users/Anton L/anti-slop-design")
SP = Path(r"C:/Users/ANTONL~1/AppData/Local/Temp/claude/C--Users-Anton-L-anti-slop-design/284cb161-2d87-493a-9b93-7fafef935807/scratchpad")
ROOT = SP / "t3-root"
CAT = REPO / "design-catalogue"
SKILL = Path(r"C:/Users/Anton L/.claude/skills/design").resolve()
SID = "cccccccc-0000-4000-8000-00000000000c"

def entry_files(slug):
    d = CAT / "entries" / slug
    out = {"entry-md": d / "entry.md", "fold": d / "fold.webp"}
    ex = sorted((d / "extract").glob("*-design-language.md")) if (d/"extract").is_dir() else []
    if ex: out["design-md"] = ex[0]
    return out

def build(rows):
    if ROOT.exists(): shutil.rmtree(ROOT)
    (ROOT / ".impeccable").mkdir(parents=True)
    (ROOT / ".impeccable" / "design-session.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")

def run(label):
    ev = {"session_id": SID, "hook_event_name": "PreToolUse", "cwd": str(ROOT),
          "tool_name": "Write",
          "tool_input": {"file_path": str(ROOT / "index.html"),
                         "content": "<!doctype html><html><body><h1>x</h1></body></html>"}}
    env = dict(os.environ, DESIGN_HOOKS_FORCE_ARM="1")
    r = subprocess.run([sys.executable, str(REPO / "hooks" / "design-gate.py")],
                       input=json.dumps(ev), capture_output=True, text=True, env=env, cwd=str(ROOT))
    out = r.stdout.strip()
    if not out:
        print(f"{label}: ALLOW"); return "ALLOW", ""
    try:
        d = json.loads(out)
        dec = d.get("hookSpecificOutput", {}).get("permissionDecision", "?")
        reason = d.get("hookSpecificOutput", {}).get("permissionDecisionReason", "")
    except Exception:
        return "?", out
    print(f"{label}: {dec.upper()}")
    for line in reason.splitlines()[1:]:
        print("    -", line[:150])
    return dec, reason

def base_rows(extra=()):
    rows = [
        {"ts": "2026-09-08T10:00:00+00:00", "session": SID, "event": "skill", "skill": "design"},
        {"ts": "2026-09-08T10:00:01+00:00", "session": SID, "event": "ref-read", "cat": "taste",
         "file": (CAT / "TASTE.md").as_posix()},
        {"ts": "2026-09-08T10:00:02+00:00", "session": SID, "event": "ref-read", "cat": "feedback",
         "file": (CAT / "FEEDBACK.md").as_posix()},
        {"ts": "2026-09-08T10:00:03+00:00", "session": SID, "event": "ref-read", "cat": "references",
         "file": (SKILL / "references" / "reference-lock.md").as_posix()},
    ]
    rows.extend(extra)
    return rows

SLUGS = [s for s in ("garden-eight", "mattis-studio", "dovetail", "paper")
         if (CAT / "entries" / s / "entry.md").exists()][:2]
print("slugs used:", SLUGS)

# A: only a fold read, no select row  -> must DENY
build(base_rows([
    {"ts": "2026-09-08T10:00:04+00:00", "session": SID, "event": "ref-read", "cat": "catalogue",
     "slug": SLUGS[0], "kind": "fold", "file": str(entry_files(SLUGS[0])["fold"])},
]))
run("A  fold only, no select")

# B: select row with 2 slugs, everything read -> must ALLOW
extra = [{"ts": "2026-09-08T10:00:04+00:00", "session": SID, "event": "catalogue-select",
          "slugs": SLUGS, "brief": "BRIEF.md"}]
t = 5
for s in SLUGS:
    for kind, f in entry_files(s).items():
        extra.append({"ts": f"2026-09-08T10:00:{t:02d}+00:00", "session": SID, "event": "ref-read",
                      "cat": "catalogue", "slug": s, "kind": kind, "file": str(f)})
        t += 1
build(base_rows(extra))
run("B  select + full reads")

# C: select row but one slug only half-read -> must DENY
partial = [e for e in extra if not (e.get("slug") == SLUGS[1] and e.get("kind") == "entry-md")]
build(base_rows(partial))
run("C  one slug missing entry.md")

# D: scroll brief, everything read EXCEPT the scroll refs and the registry -> DENY
scroll_extra = list(extra) + [
    {"ts": "2026-09-08T10:00:30+00:00", "session": SID, "event": "intent",
     "tier": "gated", "signal": "scroll", "scroll": 1},
]
build(base_rows(scroll_extra))
dec, reason = run("D  scroll brief, no scroll refs / registry")
assert dec == "deny" and "design-fingerprints.md" in reason, "D must name the registry"

# E: same, with the scroll refs and the registry read -> ALLOW
scroll_ok = list(scroll_extra) + [
    {"ts": "2026-09-08T10:00:31+00:00", "session": SID, "event": "ref-read", "cat": "references",
     "sub": "scroll", "file": (SKILL / "references" / "scroll" / "devices.md").as_posix()},
    {"ts": "2026-09-08T10:00:32+00:00", "session": SID, "event": "ref-read", "cat": "references",
     "sub": "scroll", "file": (SKILL / "references" / "scroll" / "feel-and-fingerprint.md").as_posix()},
    {"ts": "2026-09-08T10:00:33+00:00", "session": SID, "event": "ref-read", "cat": "registry",
     "file": "C:/Users/Anton L/OneDrive/Dokument/Obsidian/Knowledge Base/wiki/projects/_index/design-fingerprints.md"},
]
build(base_rows(scroll_ok))
dec, _ = run("E  scroll brief, refs + registry read")
assert dec == "ALLOW", "E must allow"

# F: a stale select row (unread slugs) followed by the real one, fully read
# -> must ALLOW. r8 R1: the V3c builder ran select.py against the unfilled
# skeleton first; the latest row is the lock, older rows do not accumulate.
stale = [{"ts": "2026-09-08T09:59:00+00:00", "session": SID, "event": "catalogue-select",
          "slugs": ["aarke", "alet"], "brief": "BRIEF.md"}]
build(base_rows(stale + extra))
dec, _ = run("F  stale select row, then the real one fully read")
assert dec == "ALLOW", "F must allow: only the latest selection is the lock"

# G: the same two rows in the other order -> must DENY (latest is the stale one)
build(base_rows(extra + [dict(stale[0], ts="2026-09-08T10:59:00+00:00")]))
dec, reason = run("G  real row, then a stale one last")
assert dec == "deny" and "aarke" in reason, "G must deny on the latest (unread) selection"
print("T3 fixtures: all seven cases behaved as specified.")
