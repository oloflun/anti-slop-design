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


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()
    if L.tool_name(event) != "Read":
        return
    path = L.target_file(event)
    if not path:
        return

    skill = _skill_read(path)
    if skill:
        # cwd-based root, NOT project_root(event) — a SKILL.md always lives
        # in the shared skills directory (often under an OneDrive/vault
        # tree with its own .git), never inside the project being built.
        # Resolving root from the file path here would file the skill-read
        # into that vault's ledger instead of the session's actual project,
        # so design-stop.py would never see it and the gap would never close.
        root = L.project_root({"cwd": event.get("cwd")})
        L.log(root, event="skill-read", skill=skill, file=path)
        return

    if not path.lower().endswith(IMAGE_EXTS):
        return

    cwd_root = L.project_root({"cwd": event.get("cwd")})
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
