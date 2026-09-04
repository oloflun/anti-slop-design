---
title: "Graft (furniture studio template)"
url: https://graft.framer.website/
source_url: https://graft.framer.website/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/8c8376110793a116-screenshot-upload.webp
category: luxury-craft
category2: ""
family: inline-thumbnail-catalog
dna: "Warm interior photography x inline circular product thumbnails"
register: warm photographic
grammar: gallery/catalog
lane: "A warm interior photograph carries a giant lowercase wordmark and a small provenance address, then a cream category list where circular product thumbnails interrupt mid-sentence"
mode: persuade
traits: ["warm interior hero photo", "giant lowercase wordmark overlaid on photo", "small provenance address line", "floating product thumbnail card", "numbered footer nav", "cream category section", "inline circular thumbnails mid-word", "large stacked type list"]
palette: ["#B08554", "#F4EEE3", "#2B2620", "#FBF9F5", "#8C7A5E"]
type: ["Inter"]
measured: designlang
kind: reference-style
source: anton
status: ready
---

## Why it works

The hero is a single warm, styled interior photograph — rattan lamp, wood
panelling, a low sofa — with the studio's giant lowercase wordmark ("Graft")
set directly onto it at the bottom-left, large enough to read as part of the
room rather than a logo pasted over it. A small provenance line ("Strada di
Montegiano 42, 60030 Marche, Italia") sits in the header, doing the "this is a
real atelier, not a marketplace" work in eight words.

The mission line — "We don't make mass furniture. We make tables where kids will
grow up." — is placed top-right, small, plain-set, deliberately underplayed
against the giant wordmark. It's the kind of claim that would usually anchor a
whole hero; here it's treated as a caption, which paradoxically makes it read
as more sincere.

Below the fold, the category list is the real signature: "Sofas / Sidetables /
Chairs / Tables / Dressing Room / Beds" set in huge stacked type, with a small
circular product photo dropped inline mid-word for several of the entries. It
turns a plain text navigation list into a browsable catalogue without a grid,
letting typography and thumbnail share one line.

## What to borrow (principle)

- **Set the wordmark directly into the hero photograph at scale**, large enough
  to feel like part of the room rather than a logo overlay.
- **Underplay your mission statement** — small, plain, captioned rather than
  hero-sized — so it reads as sincerity rather than marketing copy.
- **Drop a small circular product photo inline within a large type list**,
  turning a plain category index into a browsable, photographic one without
  building a grid.
- **State a provenance address in the header** as a quiet craft/authenticity
  signal for a maker brand.

## What to leave

- Interrupting large display type with an inline circular thumbnail can hurt
  legibility at smaller viewport widths — it needs a clear fallback (thumbnail
  drops below the word) rather than breaking the line awkwardly.
- The footer nav row ("01 / Our works / Inspiration / Use for free") mixes a
  page-index numeral with a template-marketplace CTA ("Use for free") — a
  giveaway that this is demo content, worth stripping before shipping.

## Signature move

The inline circular thumbnail interrupting large stacked type: a category word
like "Sidetables" or "Tables" gets a small round product photo dropped directly
into the letterforms, so the huge type list doubles as a photographic index
without ever becoming a conventional grid.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed,
but the captured CSS carries almost nothing concrete — no duration tokens, no
easing families, and no content keyframes beyond a generic loading spinner;
only a bare `transition: all` and a `background, box-shadow` hover rule are
present. As with the giant-wordmark hero and inline thumbnails, the page's
real reveals are almost certainly driven by Framer's inline whileInView
animation rather than static CSS, so the hover-swap read on the inline
thumbnails stays inferred, not confirmed by the extract.

## Brief

Build a warm-photography furniture-atelier page. Open on one full-bleed styled
interior photograph with the studio wordmark set directly into it at giant
lowercase scale, a small provenance address in the header, and a plainly-set
one-line mission statement placed as a caption rather than a headline. Below the
fold, on a cream ground, list product categories in very large stacked type,
dropping a small circular product photo inline within two or three of the
words. Keep the whole page to warm wood, cream and near-black ink, no additional
accent colour.

## Image recipe

A warm, styled interior of [SUBJECT] — natural wood tones, soft directional
window light, one or two considered objects (a lamp, a vase, a woven basket),
shot at a slight angle into the room rather than head-on, colour graded warm
and slightly desaturated.

## Photo search

Unsplash first, Pexels second.
- "warm wood interior living room natural light"
- "rattan lamp wood cabinetry styled interior"
- "handmade furniture workshop warm tones"

## Reference lock

Primary reference/direction: Graft — giant wordmark set into a warm interior photograph, category list interrupted by inline circular product thumbnails.
Preserve (3-5 traits): wordmark set at giant scale directly into the hero photograph rather than overlaid as a logo; mission statement underplayed as a small caption, not a headline; provenance address stated plainly in the header; large stacked category type with inline circular product thumbnails replacing a conventional grid.
Borrow only (1-2): the numbered footer nav row; the floating "featured work" thumbnail card.
Role rules: wordmark appears at giant scale exactly once per page (the hero); inline thumbnails limited to 2-3 words per category list, never every line; no accent colour beyond warm wood and cream tones.
Media strategy: photo:unsplash — warm, styled, natural-light interior photography only; product thumbnails may be studio-lit but must match the hero's warm colour grade.
Reject: a conventional product grid replacing the inline-thumbnail type list; a bold hero mission statement competing with the wordmark; cool-toned or white-background product photography breaking the warm palette.
Token commitments: wood `#B08554`, cream `#F4EEE3`, ink `#2B2620`, paper `#FBF9F5`, taupe `#8C7A5E`; rounded sans for wordmark and body, wordmark set lowercase at giant scale.
