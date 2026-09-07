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
            return {"cat": "catalogue", "slug": rel.parts[1], "file": posix}
    return None


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    if L.tool_name(event) != "Read":
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
