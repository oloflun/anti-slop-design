# design-catalogue — entry contract

One folder per reference: `entries/<slug>/`. The slug is kebab-case from the site name
(`happyrobot`, `insign`, `raus`). Never edit `raw/` or `processed/` — they are Anton's originals.

```
entries/<slug>/
  entry.md          frontmatter + body (below)
  fold.webp         first viewport 1440x900       (capture.py, or copied from processed/)
  shot.webp         full page, longest edge <= 2200 (capture.py; for refero: the jpg re-encoded)
  shot.png          lossless fold for vision       (capture.py)
  slices/NN.webp    viewport slices, max 12        (capture.py)
  extract/          designlang output when a live URL exists (--wait 2000 --ignore-widgets -q)
```

## Frontmatter (all keys required; empty string or [] when unknown)

```yaml
---
title: "Raus"
url: https://raus.life                # the live URL, or file:// for local; "" if unknown
source_url: https://raus.life         # same as url, kept separate for raw-image entries that later get a URL
captured: 2026-09-04
origin: refero | raw-url | raw-image | example-site
extract: ok | none | failed: <one line reason>
category: <one of categories.md>
category2: ""                         # optional second category
family: <short kebab-case style family, e.g. paper-atelier, mono-cinema, warm-cabin>
dna: "A x B"                          # two-part lineage, e.g. "Editorial journal x cabin postcard"
register: editorial print | cinematic dark | illustrated dark | modern clean | warm photographic | historical art | other
grammar: filmic one-shot | chaptered editorial | live surface | continuous world | typographic poster | gallery/catalog | split stage | rhythmic cutlist | none
lane: "one sentence: what the page IS as you scroll it"
mode: persuade | operate | read | experience
traits: ["4-8 short chips"]
palette: ["#hex", ...]                # from extract tokens or read off the image
type: ["Font A", "Font B"]
kind: example | reference-style
source: anton | claude
status: ready | pending
---
```

## Body — H2s in this order

1. `## Why it works` — 2-4 paragraphs. Describe the **relations**: how type weight,
   spacing, image treatment, surface and motion depend on each other. Not a token list.
2. `## What to borrow (principle)` — bullets, each a transferable principle, never a value.
3. `## What to leave` — bullets, honest.
4. `## Signature move` — the one bespoke device.
5. `## Motion` — from `extract/*-design-language.md` (motion tokens, choreography) and what
   the page does on scroll/hover. If no extract: what the screenshot implies, marked
   "(inferred from image)". Include durations/easings when extracted.
6. `## Brief` — a paragraph a builder could work from (register, grammar, type, ground, accent,
   fold, below-fold structure, close).
7. `## Image recipe` — art direction with `[SUBJECT]` placeholder.
8. `## Photo search` — source + 2-4 phrases.
9. `## Reference lock` — Primary / Preserve (3-5) / Borrow only (1-2) / Role rules /
   Media strategy / Reject / Token commitments. Same shape as `entries/calyx/entry.md`.

## Sources of truth per origin

- **refero** — `processed/<Name>.md` (tokens, components, do/don't, similar brands) + the
  jpg/png. Copy the image to `shot.webp` and `fold.webp` (top 900px crop). URL: search the
  brand name; if found, run designlang and set `origin: refero`, `extract: ok`.
- **raw-url** — domain in the filename (`www-happyrobot-ai` → `https://www.happyrobot.ai`;
  `*-webflow-io` / `*-framer-website` are template hosts, try `https://<name>.webflow.io`).
  Run `capture.py` + designlang. The raw webp stays where it is; reference it in `entry.md`
  as `raw: raw/<filename>`.
- **raw-image** — no domain. Identify the site from the image (logo, wordmark, product
  names) and web search. Found → treat as raw-url. Not found with confidence → `url: ""`,
  `extract: none`, everything read from the image, `Motion` marked inferred.

## Invariants

- Never invent a URL. Uncertain = raw-image.
- Never invent tokens: palette/type come from the extract or are visibly read off the image
  (say which in `Why it works`).
- Describe, don't grade. "Good/bad" is the taste profile's job, not the entry's.
- One entry per source. If two raw files are the same site, one entry, both raw filenames noted.
- Write only under `entries/<your slugs>/`. Run nothing that modifies `raw/` or `processed/`.

## Commands

```bash
# from repo root
python scripts/catalogue/capture.py <url> <slug>
designlang <url> --wait 2000 --ignore-widgets -q -o design-catalogue/entries/<slug>/extract
python scripts/catalogue/index.py          # rebuilds index.json + categories.json, reports gaps
python scripts/catalogue/query.py --category playful
```
