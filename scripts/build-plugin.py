#!/usr/bin/env python3
"""Build the slim plugin the marketplace installs: dist/plugin/.

The marketplace used to point at the repo root ("source": "."), and
`claude plugin install/update` copied the WHOLE repo into
~/.claude/plugins/cache/ - 3.4 GB per version (catalogue images, test runs).
The plugin only needs its manifest, skills, hooks and agents (~11 MB).

    python scripts/build-plugin.py          # rebuild dist/plugin/
    python scripts/build-plugin.py --check  # exit 1 if dist/plugin/ is stale

Run after scripts/sync-from-live.py (which calls this at its end), then bump
.claude-plugin/plugin.json "version" and `claude plugin update
anti-slop-design@anti-slop-design` - update only acts on a new version.
"""
import filecmp, shutil, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "dist" / "plugin"
PARTS = [".claude-plugin/plugin.json", "skills", "hooks", "agents"]
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store", ".impeccable")


def stale() -> list[str]:
    bad = []
    for part in PARTS:
        src, dst = REPO / part, OUT / part
        if src.is_file():
            if not dst.is_file() or not filecmp.cmp(src, dst, shallow=False):
                bad.append(part)
            continue
        cmp = filecmp.dircmp(src, dst, ignore=["__pycache__", ".DS_Store", ".impeccable"]) if dst.is_dir() else None
        stack = [cmp] if cmp else []
        if not cmp:
            bad.append(part)
        while stack:
            c = stack.pop()
            if c.left_only or c.right_only or c.diff_files:
                bad.append(f"{part}: {c.left_only + c.right_only + c.diff_files}"[:200])
            stack.extend(c.subdirs.values())
    return bad


def build() -> None:
    # Incremental, never rmtree: Windows denies removing a directory some
    # process holds open, and a half-deleted build is worse than a stale one.
    want = set()
    for part in PARTS:
        src = REPO / part
        files = [src] if src.is_file() else [f for f in src.rglob("*") if f.is_file()
                                             and not ({"__pycache__", ".impeccable"} & set(f.parts))
                                             and f.suffix != ".pyc" and f.name != ".DS_Store"]
        for f in files:
            rel = f.relative_to(REPO); dst = OUT / rel; want.add(dst)
            if not dst.is_file() or not filecmp.cmp(f, dst, shallow=False):
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dst)
    for f in [f for f in OUT.rglob("*") if f.is_file()]:
        if f not in want:
            f.unlink()
    size = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
    print(f"built {OUT.relative_to(REPO)} ({size / 1e6:.1f} MB)")


if __name__ == "__main__":
    if "--check" in sys.argv:
        bad = stale()
        print("dist/plugin in sync" if not bad else "dist/plugin STALE: " + "; ".join(bad))
        sys.exit(1 if bad else 0)
    build()
