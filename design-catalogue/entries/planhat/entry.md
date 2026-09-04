---
title: "Planhat"
url: https://www.planhat.com
source_url: https://www.planhat.com
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: "institutional"
family: darkroom-annual-report
dna: "Cinematic forest-hero photography x architectural monochrome editorial grid"
register: cinematic dark
grammar: split stage
lane: "A single dark, golden-lit forest photograph carries the entire hero, then the page snaps to pure white for a compact, architecturally precise editorial grid where hairline borders and negative space do all the separating a shadow would otherwise do"
mode: persuade
traits: ["one photograph total, everywhere else flat white", "-0.06em tracking at 113px display", "strictly monochrome + one taupe, no marketing chroma", "4px radius interactive, 8px cards, hard rule", "hairline 1px borders replace all shadow", "10px uppercase eyebrow above every section"]
palette: ["#000000", "#ffffff", "#121211", "#575551", "#958d7e", "#e8552b"]
type: ["Geigy LL Duplex Var", "Inter"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
refero: processed/Planhat.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Photography is rationed to exactly one instance: a single full-bleed
dark forest hero with warm golden light, under a 60%+ black gradient wash for
legibility. The source states this explicitly — "below the fold, there is no
photography at all." That scarcity is what makes the hero feel cinematic rather
than decorative; everything after it is pure white space, hairline borders, and
type, so the one photograph a reader sees carries maximum weight.

A custom neo-grotesque variable face with five active stylistic alternates
carries every headline at increasingly aggressive negative tracking as size
grows — from -0.02em at 24px to -0.06em at 113px — producing a compressed,
architectural quality the source calls the brand's defining trait. Inter
handles every functional role beneath it, itself lightly negative-tracked
(-0.01em to -0.02em) to keep density tight without crowding — never looser than
that, and the source explicitly forbids anything looser than -0.01em on body
text.

The marketing surface stays strictly monochrome plus one warm taupe accent; a
second colour (Ember Tag orange) exists only inside embedded product-UI
mockups, never on the marketing chrome itself — a boundary the source enforces
by name ("never on CTAs, headings, or background fills"). Combined with 1px
hairline borders replacing shadow for every card, table, and logo grid, the
page reads as a precise, architectural annual report rather than a typical
SaaS marketing site.

## What to borrow (principle)

- **Ration photography to a single, deliberate instance.** One cinematic hero
  photograph, with nothing else photographic below the fold, gives that image
  outsized emotional weight.
- **Escalate negative tracking with size, not just leading.** A precise
  tracking curve (-0.02em to -0.06em) across the type scale is what makes an
  87px+ headline read as compressed and architectural rather than merely big.
- **Fence a functional accent colour to the product, never the marketing
  chrome.** Keeping Ember Tag inside product-UI mockups only means the
  marketing surface can stay genuinely monochrome without losing a working
  accent for the product itself.
- **Use hairline borders as a complete substitute for shadow.** A 1px black
  rule doing every job a shadow normally does — card edges, table dividers,
  logo-grid separation — reads as more precise, less "app-like."
- **Anchor every section with an identical eyebrow pattern.** A 10px uppercase
  label at fixed tracking, positioned a fixed distance above every heading,
  turns section openers into a predictable rhythm a reader can scan.

## What to leave

- A single hero photograph and nothing else photographic is a strict
  discipline; a content or growth team will be tempted to add photography
  elsewhere (testimonials, team pages) and needs a firm no to preserve the
  rarity.
- The custom variable typeface's five stylistic alternates (cv03, cv04, cv09,
  cv11, blwf) are explicitly non-negotiable per the source — a generic
  substitute grotesque will visibly lose the letterform distinction that
  defines the brand.
- Confining a functional accent colour strictly to product mockups is a subtle
  rule that erodes easily; a "new feature" badge on the marketing site would be
  a natural but rule-breaking place to reach for Ember Tag.

## Signature move

The single-photograph hero-to-white cut: one full-bleed cinematic forest
photograph under a black wash carries the entire above-the-fold statement, then
the page cuts hard to pure white with zero photography for the remainder of the
scroll — a stark tonal and material shift used exactly once.

## Motion

(from designlang extract) Feel reads as mixed, and the page is scroll-linked.
Transitions run at 300ms and 500ms on a plain `ease` or a custom
`cubic-bezier(0.44, 0, 0.56, 1)` curve. One keyframe is confirmed firing —
`ch2-bar-bottom-in-2`, a slide-y combining opacity and transform — its name
("ch2-bar," i.e. chart 2, bar) points to an animated bar-chart element rising
into place, most likely inside one of the numbered editorial sections rather
than the hero itself. (observed in capture) given the "no drop shadows...
separation is achieved through hairline borders and surface color shifts only"
elevation philosophy, a button hover most plausibly still shifts between filled
and outlined treatments (as documented for LOG IN / REQUEST A DEMO) alongside
that one confirmed chart animation.

| Token | Value | Easing |
|---|---|---|
| md | 300ms | `ease` |
| lg | 500ms | `cubic-bezier(0.44, 0, 0.56, 1)` |
| ch2-bar-bottom-in-2 | slide-y (opacity + transform) | chart bar reveal |

## Brief

Build a B2B SaaS marketing page with an editorial, architectural register. Use
exactly one photograph: a full-bleed dark forest/nature hero with warm golden
light, under a 60%+ black gradient wash, left-aligned white text at roughly 45%
viewport width. Below the fold, the canvas is pure white `#ffffff` with no
further photography — only hairline 1px black borders, generous negative
space, and type. Set every heading 32px and above in a custom neo-grotesque
variable face at weight 400, negative tracking escalating from -0.02em at 24px
to -0.06em at 113px; use Inter for all UI, body and button text at 14-16px with
light negative tracking (-0.01em to -0.02em), and 10px uppercase eyebrow labels
at +0.1em tracking above every section heading. Cap radius at 4px for buttons/
inputs/images, 8px for cards — never softer. Build the customer-logo section as
a strict hairline-bordered grid table, not cards. Confine the one functional
accent colour (a warm ember orange) to illustrations of the product UI itself,
never to marketing CTAs, headings or fills. Keep sections to 64-80px vertical
gaps on a 1280px max-width grid.

## Image recipe

Cinematic environmental photograph of [SUBJECT] — a misty forest or natural
landscape with warm golden-hour light filtering through, atmospheric and
moody, shot wide with genuine depth, intended to sit beneath a 60%+ black
gradient wash for text legibility — used once, as the singular photographic
moment on the entire page.

## Photo search

Unsplash first, Pexels second.
- "misty forest golden hour light"
- "sunlight through trees atmospheric"
- "moody forest landscape warm tone"
- "golden light woodland cinematic"

## Reference lock

Primary reference/direction: Planhat — cinematic single-photograph hero
cutting to a monochrome architectural editorial grid.
Preserve (3-5 traits): exactly one photograph on the entire page, a dark
golden-lit forest hero under a 60%+ black wash, nothing photographic below the
fold; custom variable display face with negative tracking escalating from
-0.02em to -0.06em across the type scale; strictly monochrome-plus-one-taupe
marketing surface, with the one functional accent (Ember Tag) confined to
product-UI mockups only; 1px hairline borders as the complete substitute for
shadow; radius capped at 4px interactive, 8px cards.
Borrow only (1-2): the 6×2 hairline-bordered logo-grid table pattern; the
10px uppercase eyebrow label fixed above every section heading.
Role rules: Ember Tag never appears on marketing CTAs, headings or fills; the
display face never substitutes for a system grotesque; body text never loosens
past -0.01em tracking.
Media strategy: photo:unsplash for the single cinematic hero photograph only;
everything else is flat illustration/mockup or pure typography — no further
photography anywhere on the page.
Reject: a second photograph anywhere below the fold; drop shadows on any card
or panel; radius above 8px on content containers; centred body paragraphs;
Ember Tag on marketing chrome.
Token commitments: bg `#ffffff`, card `#f5f5f3`, mockup-surface `#f0eeea`,
ink `#000000`, ink-soft `#121211`, muted `#575551`, warm `#958d7e`, product-
accent `#e8552b`; display -0.02em to -0.06em tracking at 24-113px/leading
1.0-1.4; body Inter 400-500 at 10-16px; radius 4px buttons/inputs/images, 8px
cards; page max-width 1280px, section gap 64-80px.
