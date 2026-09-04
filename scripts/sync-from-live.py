#!/usr/bin/env python
"""Mirror the live design system into this repo. Live copies are canonical:
    SKILLS_LIVE = ~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills
    HOOKS_LIVE  = this repo's own hooks/ (the plugin checkout)

The design hooks moved out of super-intelligence and into this repo
(2026-09-04, see CHANGELOG). hooks/ here is no longer a mirror of an
external source for hook *content* — it IS the plugin, loaded into a
session via ${CLAUDE_PLUGIN_ROOT}. What still gets synced is .claude/hooks/,
a full local-dev copy of those same files kept for testing this repo's own
Claude Code session; its source is now hooks/ itself, not super-intelligence.
The one-time copy into super-intelligence/skills/design (the old plugin
location) is gone too — that directory no longer exists there and should not
be recreated by this script.

Usage:
    python scripts/sync-from-live.py          copy live -> repo
    python scripts/sync-from-live.py --check  report drift, write nothing
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

HOME = Path.home()
SKILLS_LIVE = HOME / "OneDrive" / "Dokument" / "Obsidian" / "Knowledge Base" / ".agents" / "skills"
REPO_ROOT = Path(__file__).resolve().parent.parent
HOOKS_LIVE = REPO_ROOT / "hooks"

SKILL_NAMES = ("design", "design-verify", "brand-system", "a11y-audit", "design-catalog")
# hooks.json is deliberately NOT synced here: hooks/hooks.json (HOOKS_LIVE) is
# the plugin's own isolated 8-entry manifest, while .claude/hooks/hooks.json
# is a full local-dev copy of every hook this repo's own Claude Code session
# wires (carl-hook.py, marketing/business hooks, chorus, the design hooks,
# etc. — 28 entries). Only the design-*.py / design_*.py script files are
# shared between the two; the manifests themselves are different documents.
HOOK_NAMES: tuple[str, ...] = ()  # scripts only, matched by hook_files()'s startswith check
SKIP_NAMES = {"__pycache__", ".DS_Store", ".impeccable"}


def skip(name: str) -> bool:
    return name in SKIP_NAMES or name.endswith(".pyc")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def walk_files(root: Path) -> dict[str, Path]:
    """relative posix path -> absolute path, for every file under root."""
    if not root.exists():
        return {}
    return {
        p.relative_to(root).as_posix(): p
        for p in root.rglob("*")
        if p.is_file() and not any(skip(part) for part in p.relative_to(root).parts)
    }


def hook_files(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    return {
        p.name: p for p in root.iterdir()
        if p.is_file() and not skip(p.name)
        and (p.name in HOOK_NAMES or p.name.startswith(("design-", "design_")))
    }


def diff_pair(src_files: dict, dst_files: dict, prefix: str) -> list[str]:
    lines = []
    for rel, src in sorted(src_files.items()):
        dst = dst_files.get(rel)
        if dst is None:
            lines.append(f"missing-in-repo:{prefix}{rel}")
        elif sha256(src) != sha256(dst):
            lines.append(f"differ:{prefix}{rel}")
    for rel in sorted(set(dst_files) - set(src_files)):
        lines.append(f"extra-in-repo:{prefix}{rel}")
    return lines


def apply_pair(src_files: dict, dst_files: dict, dst_root: Path) -> tuple[int, int, int]:
    copied = deleted = unchanged = 0
    for rel, src in src_files.items():
        dst = dst_root / rel
        if dst.exists() and sha256(src) == sha256(dst):
            unchanged += 1
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
        copied += 1
    for rel in set(dst_files) - set(src_files):
        dst_files[rel].unlink()
        deleted += 1
    return copied, deleted, unchanged


def main() -> int:
    check = "--check" in sys.argv[1:]

    # (prefix, src_files, dst_files, dst_root)
    pairs = [
        (f"skills/{n}/", walk_files(SKILLS_LIVE / n), walk_files(REPO_ROOT / "skills" / n),
         REPO_ROOT / "skills" / n)
        for n in SKILL_NAMES
    ]
    hooks_dst = REPO_ROOT / ".claude" / "hooks"
    pairs.append((".claude/hooks/", hook_files(HOOKS_LIVE), hook_files(hooks_dst), hooks_dst))

    if check:
        diffs = [line for prefix, s, d, _ in pairs for line in diff_pair(s, d, prefix)]
        print("\n".join(diffs) if diffs else "in sync")
        return 1 if diffs else 0

    copied = deleted = unchanged = 0
    for _prefix, s, d, dst_root in pairs:
        c, de, u = apply_pair(s, d, dst_root)
        copied += c
        deleted += de
        unchanged += u
    print(f"copied {copied}, deleted {deleted}, unchanged {unchanged}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
