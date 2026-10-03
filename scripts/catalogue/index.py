#!/usr/bin/env python3
"""index.py

Regenerates design-catalogue/index.json and design-catalogue/categories.json
(+ families.json) from all design-catalogue/entries/*/entry.md files. Uses a small hand-rolled YAML-subset parser
(scalars, `[a, b]` lists, and `- a` block lists) -- no PyYAML dependency.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CATALOG_ROOT = ROOT / "design-catalogue"
CATALOG_DIR = CATALOG_ROOT / "entries"

FAMILY_DESCRIPTIONS = {}


def strip_quotes(s: str) -> str:
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def parse_inline_list(s: str):
    s = s.strip()
    if not (s.startswith("[") and s.endswith("]")):
        return None
    inner = s[1:-1].strip()
    if not inner:
        return []
    items = []
    for part in inner.split(","):
        items.append(strip_quotes(part.strip()))
    return items


def parse_frontmatter(text: str) -> dict:
    """Parses a minimal YAML subset: top-level scalars, `key: [a, b]`
    inline lists, and `key:` followed by `- item` block lists."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, ""
    fm_text, body = m.group(1), m.group(2)
    lines = fm_text.split("\n")
    data = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        km = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not km:
            i += 1
            continue
        key, rest = km.group(1), km.group(2)
        rest = rest.strip()
        if rest == "" :
            # possible block list follows
            items = []
            j = i + 1
            while j < len(lines) and re.match(r"^\s*-\s+", lines[j]):
                item = re.sub(r"^\s*-\s+", "", lines[j]).strip()
                items.append(strip_quotes(item))
                j += 1
            data[key] = items
            i = j
            continue
        lst = parse_inline_list(rest)
        if lst is not None:
            data[key] = lst
        else:
            data[key] = strip_quotes(rest)
        i += 1
    return data, body


def ranking() -> dict:
    """design-catalogue/ranking.txt: one slug per line, best first (Anton's order).
    Returns slug -> 1-based rank. Everything not listed ranks after, by motion_floor."""
    p = CATALOG_ROOT / "ranking.txt"
    if not p.exists():
        return {}
    slugs = [l.split("#")[0].strip() for l in p.read_text(encoding="utf-8").splitlines()]
    return {s: i + 1 for i, s in enumerate(s for s in slugs if s)}


def main():
    entries = []
    ranks = ranking()
    if CATALOG_DIR.exists():
        for entry_dir in sorted(CATALOG_DIR.iterdir()):
            if not entry_dir.is_dir():
                continue
            entry_path = entry_dir / "entry.md"
            if not entry_path.exists():
                continue
            text = entry_path.read_text(encoding="utf-8")
            fm, _body = parse_frontmatter(text)
            slug = entry_dir.name
            record = {
                "slug": slug,
                "title": fm.get("title", slug),
                "url": fm.get("url", ""),
                "captured": fm.get("captured", ""),
                "family": fm.get("family", "unknown"),
                "dna": fm.get("dna", ""),
                "register": fm.get("register", "other"),
                "grammar": fm.get("grammar", "none"),
                "lane": fm.get("lane", ""),
                "mode": fm.get("mode", "read"),
                "traits": fm.get("traits", []) or [],
                "palette": fm.get("palette", []) or [],
                "type": fm.get("type", []) or [],
                "kind": fm.get("kind", "example"),
                "source": fm.get("source", "claude"),
                "status": fm.get("status", "pending"),
                "category": fm.get("category", "uncategorised"),
                "category2": fm.get("category2", ""),
                "origin": fm.get("origin", ""),
                "extract": fm.get("extract", "none"),
                "source_url": fm.get("source_url", fm.get("url", "")),
                "has_image": (entry_dir / "fold.webp").exists() or (entry_dir / "shot.webp").exists(),
                "showcase": fm.get("showcase", ""),
                "motion_floor": int(fm.get("motion_floor", 0) or 0),
                "rank": ranks.get(slug, 0),
                "has_sheet": (entry_dir / "motion" / "sheet.webp").exists(),
            }
            entries.append(record)
    # ranked first in Anton's order, then by motion floor, then name
    entries.sort(key=lambda e: (e["rank"] == 0, e["rank"], -e["motion_floor"], e["title"].lower()))
    unknown = [s for s in ranks if s not in {e["slug"] for e in entries}]

    index_path = CATALOG_ROOT / "index.json"
    index_path.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    family_counts = {}
    for e in entries:
        fam = e["family"] or "unknown"
        family_counts[fam] = family_counts.get(fam, 0) + 1

    families = [
        {"family": fam, "count": count, "description": FAMILY_DESCRIPTIONS.get(fam, "")}
        for fam, count in sorted(family_counts.items(), key=lambda x: (-x[1], x[0]))
    ]
    families_path = CATALOG_ROOT / "families.json"
    families_path.write_text(json.dumps(families, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    cat_counts = {}
    for e in entries:
        c = e["category"] or "uncategorised"
        cat_counts[c] = cat_counts.get(c, 0) + 1
    cat_desc = {}
    desc_path = CATALOG_ROOT / "categories.md"
    if desc_path.exists():
        for line in desc_path.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^-\s*\*\*([^*]+)\*\*\s*[:—-]\s*(.+)$", line.strip())
            if m:
                cat_desc[m.group(1).strip()] = m.group(2).strip()
    categories = [
        {"category": c, "count": n, "description": cat_desc.get(c, "")}
        for c, n in sorted(cat_counts.items(), key=lambda x: (-x[1], x[0]))
    ]
    (CATALOG_ROOT / "categories.json").write_text(json.dumps(categories, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    missing_img = [e["slug"] for e in entries if not e["has_image"]]
    uncat = [e["slug"] for e in entries if e["category"] == "uncategorised"]
    dirs_without_entry = [d.name for d in sorted(CATALOG_DIR.iterdir()) if d.is_dir() and not (d / "entry.md").exists()]
    print(f"index.py: wrote {len(entries)} entries to {index_path} ({len(ranks)} ranked)")
    if unknown: print(f"index.py: RANKED BUT NO ENTRY: {', '.join(unknown)}")
    print(f"index.py: wrote {len(categories)} categories")
    if missing_img: print(f"index.py: NO IMAGE: {', '.join(missing_img)}")
    if uncat: print(f"index.py: UNCATEGORISED: {', '.join(uncat)}")
    if dirs_without_entry: print(f"index.py: DIRS WITHOUT entry.md: {', '.join(dirs_without_entry)}")
    print(f"index.py: wrote {len(families)} families to {families_path}")


if __name__ == "__main__":
    main()
