#!/usr/bin/env python
"""
inspo_import.py — convert anti-slop-design/design-catalogue entries into
Inspo MCP seed rows (packages/db/src/house-screens.json in the local
`inspo` fork).

Stdlib only. Reads:
  design-catalogue/index.json
  design-catalogue/entries/<slug>/entry.md        (YAML-ish frontmatter + H2 body)
  design-catalogue/entries/<slug>/extract/*-variables.css   (if present)

Writes:
  <INSPO_REPO>/packages/db/src/house-screens.json

Usage:
  python scripts/inspo_import.py                 # write house-screens.json
  python scripts/inspo_import.py --check          # write + validate, exit 1 on failure
  python scripts/inspo_import.py --selftest       # run mapping self-tests, no I/O

Env:
  HOUSE_IMG_BASE   base URL images are served from, must end in "/"
                   default: http://127.0.0.1:4610/design-catalogue/entries/
  INSPO_REPO       path to the local inspo clone
                   default: C:\\Users\\Anton L\\inspo
"""
import argparse
import colorsys
import glob
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOGUE_DIR = os.path.join(REPO_ROOT, "design-catalogue")

sys.path.insert(0, os.path.join(REPO_ROOT, "scripts", "catalogue"))
from build_page import body_sections  # noqa: E402  the catalogue's own section splitter
DEFAULT_INSPO_REPO = r"C:\Users\Anton L\inspo"
DEFAULT_IMG_BASE = "http://127.0.0.1:4610/design-catalogue/entries/"

# ─────────────────────── Inspo taxonomy (packages/taxonomy/src/index.ts) ───
STYLES = {
    "minimalism", "editorial", "brutalism", "glassmorphism", "swiss",
    "maximalism", "playful", "dark-mode", "monochrome", "vintage", "futurist",
}
INDUSTRIES = {
    "agency", "ai", "architecture", "automotive", "consumer-tech", "creator",
    "crypto", "culture", "developer-tools", "ecommerce", "education",
    "fashion", "fintech", "food-beverage", "furniture", "gaming", "health",
    "media", "music", "non-profit", "portfolio", "saas", "travel",
    "type-foundry",
}
COMPONENTS = {
    "sticky-nav", "hero-with-cta", "hero-fullbleed", "logo-cloud",
    "bento-grid", "feature-trio", "feature-alternating", "testimonial-wall",
    "testimonial-quote", "pricing-3-col", "faq-accordion", "footer-compact",
    "case-study-card", "stat-strip", "marquee-logos", "newsletter-signup",
    "blog-grid",
}
VIBES = {
    "calm", "loud", "playful", "serious", "luxe", "raw", "soft", "technical",
    "warm", "cold",
}
COLOR_WORDS = {
    "warm", "cool", "monochrome", "neon", "earthy", "pastel", "saturated",
    "muted", "high-contrast",
}
MODES = {"light", "dark"}
MACROSTRUCTURES = {
    "bento-grid", "long-document", "marquee-hero", "stat-led",
    "conversational-faq", "manifesto", "photographic", "specimen",
    "catalogue", "letter", "index-first", "narrative-workflow",
    "split-studio", "feature-stack", "type-specimen", "portfolio-grid",
    "map-diagram", "ecosystem-index", "component-playground",
}
PAGE_TYPES = {
    "landing", "pricing", "features", "auth", "about", "blog", "changelog",
    "docs", "other",
}

# ─────────────────────── explicit mapping tables ───────────────────────────
# Values that don't appear here are DROPPED, never invented. Every drop is
# counted and reported by main().

REGISTER_TO_STYLE = {
    "editorial print": "editorial",
    "modern clean": "minimalism",
    "cinematic dark": "dark-mode",
    "illustrated dark": "dark-mode",
    "historical art": "vintage",
    # "warm photographic" has no confident STYLES match -> dropped.
}
REGISTER_TO_VIBE = {
    "editorial print": "calm",
    "modern clean": "calm",
    "warm photographic": "warm",
    "cinematic dark": "serious",
    "illustrated dark": "playful",
    "historical art": "serious",
}
# mode (light/dark, Inspo's ScreenSummary.mode) is not tagged in our
# frontmatter at all (our "mode" field means persuade/operate/read/
# experience, a different axis) — derive the light/dark *theme* from
# register instead of guessing off an unordered palette list.
REGISTER_TO_THEME = {
    "cinematic dark": "dark",
    "illustrated dark": "dark",
}  # default "light"

GRAMMAR_TO_MACRO = {
    "gallery/catalog": "catalogue",
    "chaptered editorial": "long-document",
    "split stage": "split-studio",
    "typographic poster": "type-specimen",
    # "live surface", "rhythmic cutlist", "filmic one-shot",
    # "continuous world", "none" -> dropped, no confident match.
}

CATEGORY_TO_INDUSTRY = {
    "portfolio": "portfolio",
    "hospitality": "travel",  # INDUSTRY_LABELS["travel"] = "Travel & Hospitality"
    "editorial": "media",
    # "luxury-craft", "consumer-brand", "institutional", "product-focused",
    # "playful" -> dropped, no confident INDUSTRIES match.
}

# Ordered (substring, component) pairs scanned against each lowercased
# trait string. First match wins per trait.
TRAIT_TO_COMPONENT = [
    ("sticky nav", "sticky-nav"),
    ("sticky-nav", "sticky-nav"),
    ("marquee logo", "marquee-logos"),
    ("marquee-logos", "marquee-logos"),
    ("logo cloud", "logo-cloud"),
    ("logo wall", "logo-cloud"),
    ("logo grid", "logo-cloud"),
    ("bento", "bento-grid"),
    ("testimonial wall", "testimonial-wall"),
    ("testimonial quote", "testimonial-quote"),
    ("testimonial", "testimonial-quote"),
    ("pricing", "pricing-3-col"),
    ("faq", "faq-accordion"),
    ("footer", "footer-compact"),
    ("case study", "case-study-card"),
    ("case-study", "case-study-card"),
    ("stat strip", "stat-strip"),
    ("counter", "stat-strip"),
    ("newsletter", "newsletter-signup"),
    ("blog grid", "blog-grid"),
    ("full-bleed", "hero-fullbleed"),
    ("full bleed", "hero-fullbleed"),
    ("fullbleed", "hero-fullbleed"),
    ("cta button", "hero-with-cta"),
    ("call to action", "hero-with-cta"),
    ("call-to-action", "hero-with-cta"),
]

FRONTMATTER_ARRAY_FIELDS = {"traits", "palette", "type"}

# ─────────────────────── frontmatter / body parsing ─────────────────────────


def parse_frontmatter(text):
    """Minimal parser for this repo's flat, single-line YAML frontmatter.

    Every field in SCHEMA.md is either a bare scalar, a quoted string, or an
    inline JSON-style array — all 97 entries were verified to follow this
    (no YAML block lists). Returns (frontmatter_dict, body_str).
    """
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("no frontmatter block")
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.split("\n"):
        lm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not lm:
            continue
        key, raw = lm.group(1), lm.group(2).strip()
        if raw.startswith("["):
            try:
                fm[key] = json.loads(raw)
            except json.JSONDecodeError:
                fm[key] = []
        elif raw.startswith('"') and raw.endswith('"') and len(raw) >= 2:
            fm[key] = raw[1:-1]
        else:
            fm[key] = raw
    for f in FRONTMATTER_ARRAY_FIELDS:
        fm.setdefault(f, [])
    return fm, body


def strip_markdown(text):
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*([^*]*)\*\*", r"\1", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def first_paragraph(section_text):
    if not section_text:
        return ""
    para = section_text.split("\n\n", 1)[0]
    return strip_markdown(re.sub(r"\s+", " ", para))


def first_sentence(section_text):
    para = first_paragraph(section_text)
    if not para:
        return ""
    m = re.search(r"^(.*?[.!?])(\s|$)", para)
    return (m.group(1) if m else para).strip()


def plain_section(section_text):
    return strip_markdown(section_text)


# ─────────────────────── mapping functions ─────────────────────────────────


def map_register(register, dropped):
    style = REGISTER_TO_STYLE.get(register)
    vibe = REGISTER_TO_VIBE.get(register)
    if style is None and vibe is None:
        dropped["register"][register] = dropped["register"].get(register, 0) + 1
    styles = [style] if style else []
    vibes = [vibe] if vibe else []
    return styles, vibes


def map_theme(register):
    return REGISTER_TO_THEME.get(register, "light")


def map_grammar(grammar, dropped):
    macro = GRAMMAR_TO_MACRO.get(grammar)
    if macro is None:
        dropped["grammar"][grammar] = dropped["grammar"].get(grammar, 0) + 1
    return macro


def map_categories(category, category2, dropped):
    out = []
    for c in (category, category2):
        if not c:
            continue
        ind = CATEGORY_TO_INDUSTRY.get(c)
        if ind is None:
            dropped["category"][c] = dropped["category"].get(c, 0) + 1
        elif ind not in out:
            out.append(ind)
    return out


def map_traits(traits, dropped):
    out = []
    for t in traits:
        low = t.lower()
        hit = None
        for needle, component in TRAIT_TO_COMPONENT:
            if needle in low:
                hit = component
                break
        if hit is None:
            dropped["trait"][t] = dropped["trait"].get(t, 0) + 1
        elif hit not in out:
            out.append(hit)
    return out


# ─────────────────────── design tokens (from *-variables.css) ──────────────

CSS_VAR_RE = re.compile(r"^\s*(--[\w-]+):\s*([^;]+);\s*$", re.M)


def _px_scale(css_vars, prefix):
    """Sorted, de-duped px values (rounded to int) for vars starting with
    `prefix`. Values are already stripped by parse_css_vars."""
    return sorted(
        {
            int(round(float(v[:-2])))
            for n, v in css_vars.items()
            if n.startswith(prefix) and v.endswith("px")
        }
    )


def parse_css_vars(css_text):
    css_vars = {}
    for name, value in CSS_VAR_RE.findall(css_text):
        css_vars[name] = value.strip()
    spacing = _px_scale(css_vars, "--spacing-")
    radius = _px_scale(css_vars, "--radius-")
    return css_vars, spacing, radius


def find_variables_css(entry_dir):
    hits = glob.glob(os.path.join(entry_dir, "extract", "*-variables.css"))
    return hits[0] if hits else None


# ─────────────────────── colour heuristics ──────────────────────────────────


def hex_to_hsl(hexcolor):
    """Returns (hue in degrees 0-360, sat 0-1, lum 0-1), same units the
    original hand-rolled HSL math used — thin wrapper because colorsys
    returns (h, l, s) with h as a 0-1 fraction, not (h, s, l) in degrees."""
    h = hexcolor.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        r, g, b = (int(h[i : i + 2], 16) / 255.0 for i in (0, 2, 4))
    except ValueError:
        return None
    hue, lum, sat = colorsys.rgb_to_hls(r, g, b)
    return hue * 360, sat, lum


def compute_color_words(palette):
    """Small deterministic heuristic over the palette's HSL values. Never
    invents a word the numbers don't support; returns [] on an empty/odd
    palette rather than guessing."""
    hsls = [hex_to_hsl(h) for h in palette]
    hsls = [x for x in hsls if x is not None]
    if not hsls:
        return []
    words = []
    hues = [h for h, s, l in hsls]
    sats = [s for h, s, l in hsls]
    lums = [l for h, s, l in hsls]
    avg_sat = sum(sats) / len(sats)
    avg_lum = sum(lums) / len(lums)
    lum_range = max(lums) - min(lums)
    chromatic_hues = [h for h, s, l in hsls if s > 0.15]

    if avg_sat < 0.12:
        words.append("monochrome")
    if avg_sat > 0.55:
        words.append("saturated")
    if avg_sat < 0.25:
        words.append("muted")
    if avg_sat > 0.75 and 0.4 <= avg_lum <= 0.7:
        words.append("neon")
    if 0.25 <= avg_sat <= 0.6 and avg_lum > 0.7:
        words.append("pastel")
    if lum_range > 0.6:
        words.append("high-contrast")
    if chromatic_hues:
        warm = sum(1 for h in chromatic_hues if h <= 60 or h >= 300)
        cool = sum(1 for h in chromatic_hues if 150 <= h <= 270)
        if warm > cool and warm > len(chromatic_hues) / 2:
            words.append("warm")
        elif cool > warm and cool > len(chromatic_hues) / 2:
            words.append("cool")
    return [w for w in words if w in COLOR_WORDS]


# ─────────────────────── row builder ─────────────────────────────────────


def build_row(slug, entry_dir, img_base, dropped):
    entry_md = os.path.join(entry_dir, "entry.md")
    text = open(entry_md, encoding="utf-8").read()
    fm, _body = parse_frontmatter(text)
    sections = body_sections(text)

    why = sections.get("Why it works", "")
    signature = sections.get("Signature move", "")
    motion = sections.get("Motion", "")
    ref_lock = sections.get("Reference lock", "")

    url = fm.get("url") or fm.get("source_url") or f"https://house.invalid/{slug}"

    styles, vibes_from_register = map_register(fm.get("register", ""), dropped)
    is_playful = "playful" in (fm.get("category"), fm.get("category2"))
    if is_playful and "playful" not in vibes_from_register:
        vibes_from_register.append("playful")
    macro = map_grammar(fm.get("grammar", ""), dropped)
    industries = map_categories(fm.get("category", ""), fm.get("category2", ""), dropped)
    components = map_traits(fm.get("traits", []), dropped)

    css_path = find_variables_css(entry_dir)
    css_vars, spacing_scale, radius_scale = ({}, [], [])
    if css_path:
        css_vars, spacing_scale, radius_scale = parse_css_vars(
            open(css_path, encoding="utf-8").read()
        )

    palette = [p for p in fm.get("palette", []) if isinstance(p, str)]
    fonts = [f for f in fm.get("type", []) if isinstance(f, str)]

    autopsy_parts = [
        f"{label}: {plain_section(text)}"
        for label, text in (
            ("WHY IT WORKS", why),
            ("SIGNATURE MOVE", signature),
            ("MOTION", motion),
            ("REFERENCE LOCK", ref_lock),
        )
        if text
    ]
    autopsy = "\n\n".join(autopsy_parts)[:6000]

    row = {
        "id": f"house-{slug}",
        "slug": f"house-{slug}",
        "siteSlug": f"house-{slug}",
        "title": fm.get("title", slug),
        "sourceUrl": url,
        "capturedAt": fm.get("captured", ""),
        "imageUrl": img_base + slug + "/fold.webp",
        "fullPageUrl": img_base + slug + "/shot.webp",
        "thumbUrl": img_base + slug + "/fold.webp",
        "description": first_paragraph(why),
        "northstar": first_sentence(signature),
        "autopsy": autopsy,
        "palette": palette,
        "fonts": fonts,
        "tech": [],
        "mode": map_theme(fm.get("register", "")),
        "pageType": "landing",
        "tags": {
            "style": styles,
            "industry": industries,
            "components": components,
            "vibe": vibes_from_register,
            **({"macrostructure": macro} if macro else {}),
        },
        "designSystem": {
            "typeRamp": [],
            "spacingScale": spacing_scale,
            "radiusScale": radius_scale,
            "containerWidth": None,
            "cssVariables": css_vars,
            "colorWords": compute_color_words(palette),
        },
        "components": [],
        "source": "house",
    }
    return row


# ─────────────────────── validation ─────────────────────────────────────


def validate_row(row, errors):
    slug = row.get("slug", "?")
    req = [
        "id", "slug", "siteSlug", "title", "sourceUrl", "capturedAt",
        "imageUrl", "fullPageUrl", "thumbUrl", "description", "mode",
        "pageType",
    ]
    for f in req:
        if not row.get(f):
            errors.append(f"{slug}: missing/empty required field '{f}'")
    if row.get("mode") not in MODES:
        errors.append(f"{slug}: invalid mode {row.get('mode')!r}")
    if row.get("pageType") not in PAGE_TYPES:
        errors.append(f"{slug}: invalid pageType {row.get('pageType')!r}")
    for hexcolor in row.get("palette", []):
        if not re.match(r"^#[0-9a-fA-F]{6}$", hexcolor):
            errors.append(f"{slug}: bad palette hex {hexcolor!r}")
    tags = row.get("tags", {})
    for style in tags.get("style", []):
        if style not in STYLES:
            errors.append(f"{slug}: invalid style {style!r}")
    for ind in tags.get("industry", []):
        if ind not in INDUSTRIES:
            errors.append(f"{slug}: invalid industry {ind!r}")
    for comp in tags.get("components", []):
        if comp not in COMPONENTS:
            errors.append(f"{slug}: invalid component {comp!r}")
    for vibe in tags.get("vibe", []):
        if vibe not in VIBES:
            errors.append(f"{slug}: invalid vibe {vibe!r}")
    macro = tags.get("macrostructure")
    if macro is not None and macro not in MACROSTRUCTURES:
        errors.append(f"{slug}: invalid macrostructure {macro!r}")
    for cw in row.get("designSystem", {}).get("colorWords", []):
        if cw not in COLOR_WORDS:
            errors.append(f"{slug}: invalid colorWord {cw!r}")


# ─────────────────────── self-test ─────────────────────────────────────


def selftest():
    dropped = {"register": {}, "grammar": {}, "category": {}, "trait": {}}

    styles, vibes = map_register("editorial print", dropped)
    assert styles == ["editorial"], styles
    assert vibes == ["calm"], vibes

    styles, vibes = map_register("warm photographic", dropped)
    assert styles == [], styles
    assert vibes == ["warm"], vibes
    assert dropped["register"] == {}, "warm photographic has a vibe match, should not be dropped"

    styles, vibes = map_register("not-a-real-register", dropped)
    assert styles == [] and vibes == []
    assert dropped["register"].get("not-a-real-register") == 1

    assert map_theme("cinematic dark") == "dark"
    assert map_theme("editorial print") == "light"
    assert map_theme("unknown") == "light"

    assert map_grammar("gallery/catalog", dropped) == "catalogue"
    assert map_grammar("none", dropped) is None
    assert dropped["grammar"].get("none") == 1

    industries = map_categories("portfolio", "", dropped)
    assert industries == ["portfolio"], industries
    industries = map_categories("luxury-craft", "consumer-brand", dropped)
    assert industries == [], industries
    assert dropped["category"].get("luxury-craft") == 1
    assert dropped["category"].get("consumer-brand") == 1

    comps = map_traits(["outline pill CTA button", "sticky nav", "unmatched trait xyz"], dropped)
    assert "hero-with-cta" in comps
    assert "sticky-nav" in comps
    assert dropped["trait"].get("unmatched trait xyz") == 1

    assert strip_markdown("**bold** and *italic* and `code`") == "bold and italic and code"
    assert first_sentence("One. Two. Three.") == "One."
    assert first_paragraph("Para one line one.\nline two.\n\nPara two.") == \
        "Para one line one. line two."

    sample_entry = (
        '---\ntitle: "Test Site"\nurl: https://example.com\n'
        'palette: ["#FFFFFF", "#000000"]\ncategory2: ""\n---\n'
        "## Why it works\n\nIt just does.\n"
    )
    fm, _body = parse_frontmatter(sample_entry)
    assert fm["title"] == "Test Site"
    assert fm["url"] == "https://example.com"
    assert fm["palette"] == ["#FFFFFF", "#000000"]
    assert fm["category2"] == ""
    sections = body_sections(sample_entry)
    assert sections["Why it works"] == "It just does."

    css_vars, spacing, radius = parse_css_vars(
        ":root {\n  --spacing-4: 4px;\n  --spacing-96: 96px;\n"
        "  --radius-8: 8px;\n  --color-bg: #fff;\n  broken-line-no-match\n}\n"
    )
    assert css_vars["--color-bg"] == "#fff"
    assert spacing == [4, 96]
    assert radius == [8]

    hue, sat, lum = hex_to_hsl("#893F28")
    assert 0 <= hue <= 360 and 0 <= sat <= 1 and 0 <= lum <= 1

    words = compute_color_words(["#F7F3EB", "#ECE7DE", "#12120B"])
    assert isinstance(words, list)
    assert all(w in COLOR_WORDS for w in words)

    print("selftest: all assertions passed")


# ─────────────────────── main ─────────────────────────────────────


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate emitted rows, exit 1 on failure")
    ap.add_argument("--selftest", action="store_true", help="run mapping self-tests and exit")
    ap.add_argument("--inspo-repo", default=os.environ.get("INSPO_REPO", DEFAULT_INSPO_REPO))
    ap.add_argument("--img-base", default=os.environ.get("HOUSE_IMG_BASE", DEFAULT_IMG_BASE))
    args = ap.parse_args()

    if args.selftest:
        selftest()
        return

    img_base = args.img_base
    if not img_base.endswith("/"):
        img_base += "/"

    index_path = os.path.join(CATALOGUE_DIR, "index.json")
    index = json.load(open(index_path, encoding="utf-8"))

    dropped = {"register": {}, "grammar": {}, "category": {}, "trait": {}}
    rows = []
    seen_slugs = set()
    for entry in index:
        slug = entry["slug"]
        entry_dir = os.path.join(CATALOGUE_DIR, "entries", slug)
        if not os.path.isdir(entry_dir):
            print(f"WARN: no entry dir for {slug}, skipping", file=sys.stderr)
            continue
        row = build_row(slug, entry_dir, img_base, dropped)
        house_slug = row["slug"]
        if house_slug in seen_slugs:
            print(f"ERROR: duplicate slug {house_slug}", file=sys.stderr)
            sys.exit(1)
        seen_slugs.add(house_slug)
        rows.append(row)

    out_path = os.path.join(args.inspo_repo, "packages", "db", "src", "house-screens.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)

    print(f"wrote {len(rows)} rows -> {out_path}")
    print("dropped tag values (unmapped, never invented):")
    for field, counts in dropped.items():
        if not counts:
            continue
        total = sum(counts.values())
        print(f"  {field}: {total} occurrences across {len(counts)} distinct values")
        for value, n in sorted(counts.items(), key=lambda kv: -kv[1]):
            print(f"    {value!r}: {n}")

    if args.check:
        errors = []
        for row in rows:
            validate_row(row, errors)
        if errors:
            print(f"\nCHECK FAILED: {len(errors)} problems", file=sys.stderr)
            for e in errors[:200]:
                print(f"  {e}", file=sys.stderr)
            sys.exit(1)
        print(f"\nCHECK OK: {len(rows)} rows validated against taxonomy + required fields")


if __name__ == "__main__":
    main()
