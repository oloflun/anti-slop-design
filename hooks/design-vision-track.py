#!/usr/bin/env python
"""PostToolUse on Read — record that pixels actually entered context.

The chain had no way to know whether a render was ever LOOKED at, so the Stop
report could not flag its absence and nothing could enforce the exit bar.
This hook logs a `vision` event whenever an image file is Read. design-stop.py
compares the last vision timestamp against the last UI edit: an edit nobody
looked at afterwards blocks the stop.

Logs to the session cwd's ledger and, when the image lives in another project
tree (a shots dir inside the site being built), to that root's ledger too, so
cross-project sessions stay visible from both sides.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import design_hook_lib as L
except Exception:
    sys.exit(0)

IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp")

# inspo (visual reference archive) and ui-skills (a skill library, not a design
# one) both arrive as MCP calls, not Read/generation — the route/reference-floor
# hooks never see them. Logged here, not in design-route.py, because vision-
# track already owns "advisory instrumentation for a tool that isn't a file
# write" (see is_generation_tool above).
_MCP_TRACKED = {"mcp__inspo__": "inspo", "mcp__ui-skills__": "ui-skills"}


def _mcp_server(tool: str) -> str:
    """'inspo' | 'ui-skills' | '' for a tracked MCP call."""
    for prefix, server in _MCP_TRACKED.items():
        if tool.startswith(prefix):
            return server
    return ""


def _mcp_fields(tool: str, event: dict) -> dict:
    """Tool suffix + a short arg naming what was asked for."""
    suffix = tool.split("__", 2)[-1]
    ti = L.tool_input(event)
    if suffix == "get_skill":
        arg = ti.get("name", "")
    elif suffix.startswith("search") or suffix == "recommend":
        arg = ti.get("query") or ti.get("brief") or ""
    elif suffix in ("get_screen", "get_design_system"):
        arg = ti.get("slug", "")
    else:
        arg = ""
    return {"tool": suffix, "arg": str(arg)[:80]}

# A Read of a skill's own reference material closes the Stop report's route
# gap the same way invoking the Skill tool does (design-telemetry.py's
# "skill" event) — an agent that opened emil-design-eng/SKILL.md and applied
# its guidance inline, without a formal Skill() call, still did the work the
# router asked for.
_SKILLS_ROOTS = (L.HOME / ".agents" / "skills", L.HOME / ".claude" / "skills")


def _skill_read(path: str) -> str:
    """Skill dir name if `path` is a .md file under a skills root, else ""."""
    try:
        p = Path(path).resolve()
    except Exception:
        return ""
    if p.suffix.lower() != ".md":
        return ""
    for base in _SKILLS_ROOTS:
        try:
            rel = p.relative_to(base.resolve())
        except Exception:
            continue
        if rel.parts:
            return rel.parts[0]
    return ""


# design-gate.py's reference floor needs to know WHICH reference got read,
# not just that a skill-scoped .md was opened — TASTE.md and a scroll device
# note both live under a "design" skill read but satisfy different floor
# requirements. This classifies a Read against the same two root families
# the floor checks against: the design skill's own references/scripts, and
# the project's design-catalogue (taste, feedback, per-entry examples).
def _classify_ref(path: str, root) -> dict | None:
    try:
        p = Path(path).resolve()
    except Exception:
        return None
    posix = p.as_posix()

    for base in L.design_skill_roots():
        try:
            rel = p.relative_to(base)
        except Exception:
            continue
        if not rel.parts:
            continue
        top = rel.parts[0]
        if top == "references":
            out = {"cat": "references", "file": posix}
            if len(rel.parts) > 1 and rel.parts[1] == "scroll":
                out["sub"] = "scroll"
            return out
        if top == "scripts":
            return {"cat": "scripts", "file": posix}

    for cat_root in L.catalogue_roots(root):
        try:
            rel = p.relative_to(cat_root)
        except Exception:
            continue
        if not rel.parts:
            continue
        if rel.parts == ("TASTE.md",):
            return {"cat": "taste", "file": posix}
        if rel.parts == ("FEEDBACK.md",):
            return {"cat": "feedback", "file": posix}
        if rel.parts[0] == "entries" and len(rel.parts) > 1:
            # `kind` (T3, 2026-09-08). Before this, ANY file under
            # entries/<slug>/ logged as cat=catalogue, so a single fold.webp
            # satisfied a floor whose prose asks for 2-4 entries read as
            # pixels AND text. The gate could not tell a thumbnail from the
            # entry contract. Kinds are named after what the floor needs to
            # distinguish, not after the file system.
            name = rel.parts[-1].lower()
            if name == "entry.md":
                kind = "entry-md"
            elif name.endswith("-design-language.md") or (
                    len(rel.parts) > 2 and rel.parts[2] == "extract" and name.endswith(".md")):
                kind = "design-md"
            elif name.startswith("fold."):
                kind = "fold"
            elif len(rel.parts) > 2 and rel.parts[2] == "slices":
                kind = "slice"
            elif name.startswith("shot."):
                kind = "shot"
            else:
                kind = "other"
            return {"cat": "catalogue", "slug": rel.parts[1], "kind": kind, "file": posix}
        # The fingerprint registry lives in the vault, not the catalogue, but
        # the floor treats it as catalogue evidence: a concept that repeats an
        # earlier build's grammar is the failure it exists to stop.
        if rel.parts[-1] == "design-fingerprints.md":
            return {"cat": "registry", "file": posix}
    # Vault path for the registry, reached directly rather than via a
    # catalogue root.
    if p.name == "design-fingerprints.md":
        return {"cat": "registry", "file": posix}
    return None


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    tool = L.tool_name(event)

    # Generated material is a skill call like any other and gets measured like
    # one. Before this, a Higgsfield call left no trace at all: the ledger
    # could tell you which reference the builder read and not that it had spent
    # 17.5 credits on a clip (T12, 2026-09-08).
    if L.is_generation_tool(tool):
        root = L.project_root({"cwd": event.get("cwd")})
        L.log(root, event="generation", **L.generation_fields(event))
        return

    mcp_server = _mcp_server(tool)
    if mcp_server:
        root = L.project_root({"cwd": event.get("cwd")})
        L.log(root, event="mcp", server=mcp_server, **_mcp_fields(tool, event))
        return

    if tool != "Read":
        return
    path = L.target_file(event)
    if not path:
        return

    # cwd-based root, NOT project_root(event) — a SKILL.md or catalogue file
    # always lives in the shared skills directory or the catalogue (often
    # under an OneDrive/vault tree, or this repo, with its own .git), never
    # necessarily inside the project being built. Resolving root from the
    # file path here would file the read into the wrong ledger, so
    # design-stop.py / design-gate.py would never see it.
    root = L.project_root({"cwd": event.get("cwd")})

    skill = _skill_read(path)
    if skill:
        L.log(root, event="skill-read", skill=skill, file=path)

    ref = _classify_ref(path, root)
    if ref:
        L.log(root, event="ref-read", **ref)

    if not path.lower().endswith(IMAGE_EXTS):
        return

    # Images inside a catalogue entry (entries/<slug>/*.png) match `ref`
    # above AND still count toward the exit bar's vision requirement — the
    # reference floor and the "were the pixels ever looked at" check are
    # independent concerns, so both log unconditionally.
    cwd_root = root
    file_root = L.project_root(event)
    L.log(cwd_root, event="vision", file=path)
    if file_root != cwd_root:
        L.log(file_root, event="vision", file=path)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
