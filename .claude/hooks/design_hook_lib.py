"""Shared helpers for the design hook chain.

Used by design-route.py, design-gate.py, design-telemetry.py,
design-verify-gate.py and design-stop.py.

Design rules for everything in here:
  * Never raise into the harness. A broken hook must never block the user's
    work, so every public function swallows its own errors and degrades to a
    no-op. Callers still wrap in try/except as a second net.
  * Never do slow work on the hot path. The routing table is parsed once and
    cached; DESIGN.md is read at most once per invocation.
  * The routing table is NOT duplicated here. It is parsed out of
    skills/design/references/component-routing.md so that file stays the
    single source of truth.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HOME = Path(os.path.expanduser("~"))
ROUTING_DOC = HOME / ".agents" / "skills" / "design" / "references" / "component-routing.md"
IMPECCABLE = HOME / ".agents" / "skills" / "impeccable"

KILL_SWITCH = "DESIGN_HOOKS_DISABLED"
STATE_DIR_NAME = ".impeccable"
LEDGER_NAME = "design-session.jsonl"

# Markers that make a project root. Closest match wins, so DESIGN.md is listed
# first on purpose: a design system nested inside a larger monorepo defines its
# own boundary, and resolving past it would read the wrong contract.
ROOT_MARKERS = ("DESIGN.md", "design.md", ".impeccable", ".git",
                "package.json", "pyproject.toml")


def disabled() -> bool:
    return os.environ.get(KILL_SWITCH, "").strip() not in ("", "0", "false")


def read_event() -> dict:
    """Parse the hook event from stdin. Returns {} on anything unexpected."""
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def emit(event_name: str, context: str) -> None:
    """Push text into the agent's context and exit cleanly."""
    if not context:
        return
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": context,
        }
    }))


def deny(reason: str) -> None:
    """Block a PreToolUse call. The agent sees `reason` and can self-correct."""
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))


# --------------------------------------------------------------------------
# Event shape
# --------------------------------------------------------------------------

def tool_name(event: dict) -> str:
    return event.get("tool_name") or event.get("toolName") or ""


def tool_input(event: dict) -> dict:
    ti = event.get("tool_input") or event.get("toolInput") or {}
    return ti if isinstance(ti, dict) else {}


def target_file(event: dict) -> str:
    """The path a Write/Edit/MultiEdit is aimed at, or ''."""
    ti = tool_input(event)
    for key in ("file_path", "filePath", "path", "notebook_path"):
        v = ti.get(key)
        if isinstance(v, str) and v:
            return v
    return ""


def written_content(event: dict) -> str:
    """Best-effort text a Write/Edit is about to introduce.

    Only the *incoming* side matters: we are checking what the agent is adding,
    not re-flagging what the file already contained.
    """
    ti = tool_input(event)
    parts = []
    for key in ("content", "new_string", "newString"):
        v = ti.get(key)
        if isinstance(v, str):
            parts.append(v)
    edits = ti.get("edits")
    if isinstance(edits, list):
        for e in edits:
            if isinstance(e, dict):
                v = e.get("new_string") or e.get("newString")
                if isinstance(v, str):
                    parts.append(v)
    return "\n".join(parts)


# --------------------------------------------------------------------------
# Project state
# --------------------------------------------------------------------------

def project_root(event: dict) -> Path:
    start = event.get("cwd") or os.getcwd()
    tf = target_file(event)
    if tf:
        try:
            start = str(Path(tf).parent)
        except Exception:
            pass
    try:
        cur = Path(start).resolve()
    except Exception:
        return Path(os.getcwd())
    for candidate in [cur, *cur.parents]:
        for marker in ROOT_MARKERS:
            if (candidate / marker).exists():
                return candidate
    return cur


def state_dir(root: Path) -> Path:
    d = root / STATE_DIR_NAME
    try:
        d.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass
    return d


def design_md(root: Path) -> Path | None:
    for name in ("DESIGN.md", "design.md", "Design.md"):
        p = root / name
        if p.exists():
            return p
    return None


def tier(root: Path) -> str:
    """Coarse tier signal for the ledger and the injected reminder.

    Only tier 0 is decidable mechanically — DESIGN.md exists or it does not.
    Distinguishing 1 from 2 from 3 is a judgment the model makes at the gate,
    so anything without DESIGN.md reports as 'ungated' rather than guessing.
    """
    return "0-locked" if design_md(root) else "ungated"


def design_tokens(root: Path) -> dict:
    """Parse the DESIGN.md frontmatter maps we care about.

    Deliberately small: enough to name the right token in a denial message.
    The authoritative check is impeccable's detector, which parses the full
    schema plus the .impeccable/design.json sidecar.
    """
    out = {"colors": {}, "fonts": [], "radii": []}
    p = design_md(root)
    if not p:
        return out
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return out
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return out
    fm = m.group(1)

    section = None
    for line in fm.splitlines():
        if re.match(r"^\w+:", line):
            section = line.split(":", 1)[0].strip()
            continue
        if section == "colors":
            km = re.match(r"^\s+([\w-]+):\s*[\"']?(#[0-9a-fA-F]{3,8}|oklch\([^)]*\))", line)
            if km:
                out["colors"][km.group(1)] = km.group(2).lower()
        elif section == "typography":
            fmatch = re.search(r"fontFamily:\s*[\"']([^\"']+)", line)
            if fmatch:
                out["fonts"].append(fmatch.group(1).strip())
        elif section == "rounded":
            rm = re.match(r"^\s+([\w-]+):\s*[\"']?([\d.]+(?:px|rem|em))", line)
            if rm:
                out["radii"].append(rm.group(2))
    return out


# --------------------------------------------------------------------------
# Routing table — parsed from the reference, never duplicated
# --------------------------------------------------------------------------

_ROUTING_CACHE: dict | None = None


def routing_table() -> dict:
    global _ROUTING_CACHE
    if _ROUTING_CACHE is not None:
        return _ROUTING_CACHE
    table = {"rules": [], "ui_extensions": [], "trap_hexes": {}}
    try:
        text = ROUTING_DOC.read_text(encoding="utf-8", errors="replace")
        for block in re.findall(r"```json\s*\n(.*?)\n```", text, re.S):
            try:
                parsed = json.loads(block)
            except Exception:
                continue
            if isinstance(parsed, dict) and "rules" in parsed:
                table = parsed
                break
    except Exception:
        pass
    _ROUTING_CACHE = table
    return table


def is_ui_file(path: str) -> bool:
    if not path:
        return False
    exts = routing_table().get("ui_extensions") or []
    low = path.lower()
    return any(low.endswith(e) for e in exts)


def match_routes(path: str, content: str) -> list[dict]:
    """Which routing rules fire for this write. Most specific first."""
    table = routing_table()
    low_path = (path or "").replace("\\", "/").lower()
    hits, fallback = [], None

    for rule in table.get("rules", []):
        if rule.get("fallback"):
            fallback = rule
            continue
        matched = False
        for frag in rule.get("path", []):
            if frag.lower() in low_path:
                matched = True
                break
        if not matched:
            use_regex = bool(rule.get("regex"))
            for frag in rule.get("code", []):
                try:
                    if use_regex:
                        if re.search(frag, content):
                            matched = True
                            break
                    elif frag in content:
                        matched = True
                        break
                except re.error:
                    continue
        if matched:
            hits.append(rule)

    if not [h for h in hits if h.get("id") != "copy"] and fallback:
        hits.append(fallback)
    return hits


def trap_hits(content: str) -> list[tuple[str, str]]:
    """(skill, hex) for every demoted-skill palette value in the content.

    This is gate 60, the flag under test.
    """
    out = []
    if not content:
        return out
    low = content.lower()
    for skill, hexes in (routing_table().get("trap_hexes") or {}).items():
        for hx in hexes:
            if hx.lower() in low:
                out.append((skill, hx))
    return out


# --------------------------------------------------------------------------
# Ledger
# --------------------------------------------------------------------------

def log(root: Path, **fields) -> None:
    """Append one event to the session ledger. Silent on failure."""
    try:
        rec = {"ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        rec.update({k: v for k, v in fields.items() if v not in (None, "")})
        path = state_dir(root) / LEDGER_NAME
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass


def read_ledger(root: Path) -> list[dict]:
    try:
        path = state_dir(root) / LEDGER_NAME
        if not path.exists():
            return []
        rows = []
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
        return rows
    except Exception:
        return []


def component_of(path: str) -> str:
    """Human label for the thing being edited — the file stem is enough."""
    try:
        return Path(path).stem or Path(path).name
    except Exception:
        return path or "?"


def once_per_session(root: Path, key: str) -> bool:
    """True the first time this key is seen, False after. Used to keep
    session-level reminders from repeating on every single tool call."""
    try:
        flag = state_dir(root) / f".once-{re.sub(r'[^a-z0-9]+', '-', key.lower())}"
        if flag.exists():
            return False
        flag.write_text("1", encoding="utf-8")
        return True
    except Exception:
        return False


def _cache_path(root: Path) -> Path:
    return state_dir(root) / ".detect-cache.json"


def cache_detect(root: Path, content: str, findings: list[dict]) -> None:
    """Stash detector findings keyed by content hash.

    design-gate.py (PreToolUse) and design-route.py (PostToolUse) both want the
    detector's verdict on the same bytes. Without this the detector runs twice
    per UI write, which is the single largest cost in the chain.
    """
    try:
        import hashlib
        key = hashlib.sha1(content.encode("utf-8", "replace")).hexdigest()
        p = _cache_path(root)
        data = {}
        if p.exists():
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
            except Exception:
                data = {}
        data[key] = findings
        # keep it small — this is a hot-path read
        if len(data) > 20:
            data = dict(list(data.items())[-20:])
        p.write_text(json.dumps(data), encoding="utf-8")
    except Exception:
        pass


def cached_detect(root: Path, content: str):
    """Findings for these exact bytes, or None if not cached."""
    try:
        import hashlib
        key = hashlib.sha1(content.encode("utf-8", "replace")).hexdigest()
        p = _cache_path(root)
        if not p.exists():
            return None
        return json.loads(p.read_text(encoding="utf-8")).get(key)
    except Exception:
        return None


def detect(files: list[str], root: Path, timeout: int = 25) -> list[dict]:
    """Run impeccable's deterministic detector. [] if unavailable.

    NOTE: the detector exits 0 even when it has findings, so the JSON is the
    only signal. Never branch on returncode here.
    """
    script = IMPECCABLE / "scripts" / "detect.mjs"
    if not script.exists() or not files:
        return []
    try:
        import subprocess
        proc = subprocess.run(
            ["node", str(script), "--json", *files],
            capture_output=True, text=True, timeout=timeout, cwd=str(root),
        )
        out = (proc.stdout or "").strip()
        if not out:
            return []
        start = out.find("[")
        if start < 0:
            return []
        data = json.loads(out[start:])
        return data if isinstance(data, list) else []
    except Exception:
        return []
