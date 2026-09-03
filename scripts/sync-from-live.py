#!/usr/bin/env python
"""Mirror the live design system into this repo. Live copies are canonical:
    SKILLS_LIVE = ~/OneDrive/Dokument/Obsidian/Knowledge Base/.agents/skills
    HOOKS_LIVE  = ~/super-intelligence/hooks

Usage:
    python scripts/sync-from-live.py             copy live -> repo (+ plugin)
    python scripts/sync-from-live.py --check      report drift, write nothing
    python scripts/sync-from-live.py --no-plugin  skip the plugin copy sync
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

HOME = Path.home()
SKILLS_LIVE = HOME / "OneDrive" / "Dokument" / "Obsidian" / "Knowledge Base" / ".agents" / "skills"
HOOKS_LIVE = HOME / "super-intelligence" / "hooks"
REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGIN_DESIGN = HOME / "super-intelligence" / "skills" / "design"

SKILL_NAMES = ("design", "design-verify", "brand-system", "a11y-audit", "design-catalog")
HOOK_NAMES = ("hooks.json",)  # plus design*.py / design_*.py, see hook_files()
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
    plugin = "--no-plugin" not in sys.argv[1:]

    # (prefix, src_files, dst_files, dst_root)
    pairs = [
        (f"skills/{n}/", walk_files(SKILLS_LIVE / n), walk_files(REPO_ROOT / "skills" / n),
         REPO_ROOT / "skills" / n)
        for n in SKILL_NAMES
    ]
    hooks_dst = REPO_ROOT / ".claude" / "hooks"
    pairs.append((".claude/hooks/", hook_files(HOOKS_LIVE), hook_files(hooks_dst), hooks_dst))
    if plugin:
        pairs.append(("(plugin) super-intelligence/skills/design/",
                       walk_files(SKILLS_LIVE / "design"), walk_files(PLUGIN_DESIGN), PLUGIN_DESIGN))

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
