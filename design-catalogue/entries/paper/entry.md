---
title: "Paper"
url: https://paper.design/
source_url: https://paper.design/
captured: 2026-09-04
origin: refero
extract: ok
category: product-focused
category2: editorial
family: warm-notebook-studio-blue
dna: "Two-tone editorial headline x cream notebook canvas with one restrained blue mark"
register: modern clean
grammar: split stage
lane: "A warm cream canvas holds a left-aligned two-tone headline — dark first line, mid-gray continuation — above a single elevated product-screenshot card, with a faint isometric grid the only decorative flourish and a lone blue accent confined to the logo mark and code syntax"
mode: persuade
traits: ["two-tone headline, one weight, two fill colours", "cream canvas, white reserved for elevated cards", "single filled dark button, no chromatic CTA", "4px buttons, 8px cards, 12-24px product frames", "three-layer shadow reserved for product chrome only", "blue confined to logo mark and code accents"]
palette: ["#efefe4", "#fcfcf9", "#181818", "#83837e", "#5d8cd7", "#d7d7d6"]
type: ["Matter", "Inter", "Paper Mono"]
measured: designlang
kind: reference-style
source: anton
status: ready
refero: processed/Paper.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Bone canvas `#efefe4` replaces white as the page background, with
paper white and bright card white reserved strictly for elevated surfaces — the
source's Do's list states this distinction outright: "reserve #ffffff for
elevated cards and product chrome only." That three-step neutral stack (canvas
→ paper white → bright white) gives the page a printed, notebook-page feel
before a single UI element loads.

The two-tone headline is the system's most legible device: identical Matter
metrics (same size, same weight 400, same tracking) split across two fill
colours — ink `#181818` for the declarative first line, slate `#83837e` for the
continuation — so the effect comes entirely from colour, never from a size or
weight change. The source is explicit that mixing sizes or fonts for the two
lines would break the device; the whole trick depends on identical typography
with only colour differing.

Colour discipline elsewhere is equally strict: the one chromatic accent, studio
blue `#5d8cd7`, is confined to the brand mark and code syntax highlighting —
never a button, never a link, never large text. Combined with a filled CTA
that is always neutral ink, never chromatic, and a shadow system reserved
exclusively for the product screenshot and floating tool panels (marketing
cards stay flat with hairline borders instead), the page keeps all its visual
richness inside the product itself, exactly as a design tool's marketing site
should. Note: the designlang extract's raw colour counts are dominated by
near-black IDE tones and syntax-style blue/green accents (`#3d7cff`, `#0fa821`)
rather than the cream/ink marketing palette above — consistent with an embedded
dark code-editor product demo (matching the Paper Mono font's heavy element
count) outweighing the surrounding marketing chrome in raw element count, not
with the page itself running dark. The cream canvas and slate-headline reading
stand as originally documented.

## What to borrow (principle)

- **Split one headline across two fill colours, not two sizes.** Identical
  type metrics with only colour differing is a subtler, more controllable
  device than a bold/light size contrast.
- **Distinguish canvas from elevated surface with two near-white values.**
  "Cream for the page, pure white only for cards" gives elevation meaning
  without needing a shadow on every surface.
- **Confine the single accent colour to identity and code, never UI action.**
  Keeping the brand blue out of buttons and links makes "neutral dark" read as
  a deliberate action language, not an oversight.
- **Reserve complex shadow for the product itself.** A three-layer shadow used
  only on the screenshot card (never on headings, logos or marketing cards)
  keeps that one element reading as the page's real focal point.
- **Let a faint geometric pattern add depth without colour.** A low-opacity
  isometric line grid, clipped to a corner wedge, provides spatial interest
  that a gradient or illustration would otherwise need to supply.

## What to leave

- The two-tone headline device only reads correctly with genuinely calm,
  short copy; a headline needing emphasis mid-sentence has nowhere to put it
  since bold and italic are both explicitly forbidden.
- Confining shadow entirely to product chrome is a strict rule that a growing
  marketing team will be tempted to break for a "featured" testimonial or
  pricing card — the system offers no secondary elevation pattern to fall
  back on.
- A single studio-blue accent restricted to logo and code means any new
  semantic need (a warning state, a highlighted diff) has to invent its own
  convention within an otherwise near-achromatic palette.

## Signature move

The two-tone headline: two lines of identical Matter type, one in ink, one in
slate, at the same size and weight — treating the hero statement as a
composition of colour rather than a single block of emphasis.

## Motion

(from designlang extract) Feel reads as springy, and the page is scroll-linked —
correcting the earlier "no motion tokens" read substantially. A fast-settling
ease-out curve (`cubic-bezier(0.16, 1, 0.3, 1)`, 32 uses) carries most
transitions across four durations (100-800ms), and a genuine spring/overshoot
curve, `cubic-bezier(0.34, 1.3, 0.64, 1)`, is confirmed in use (5 times). The
keyframe behind it, `terminal-chunk-in` (slide-y, combining opacity, filter and
transform, 3 uses), is the overlapping terminal/MCP panel: output chunks slide
up and sharpen into focus as they appear, rather than sitting in a static
composition. (observed in capture) given the flat, hairline-bordered marketing
surface and the shadow reserved only for product chrome, a plain card hover
most plausibly still shifts from a bordered ghost treatment to the elevated
three-layer shadow rather than introducing colour, even though the terminal
panel itself is genuinely animated.

| Token | Value | Easing |
|---|---|---|
| xs | 100ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| md | 300ms | `cubic-bezier(0.16, 1, 0.3, 1)` |
| lg | 500ms | spring |
| xl | 800ms | spring |
| spring/overshoot | — | `cubic-bezier(0.34, 1.3, 0.64, 1)` |
| terminal-chunk-in | slide-y, opacity, filter | 3 uses |

## Brief

Build a design-tool marketing homepage. Canvas is bone cream `#efefe4`
throughout; reserve paper white `#fcfcf9` and pure white `#ffffff` strictly for
elevated cards and product chrome. Set the hero as a left-aligned two-tone
headline in Matter at 64px: first line in ink `#181818`, continuation line(s)
in slate `#83837e`, identical weight and tracking (-1.28px at 64px), lines
nearly touching at 1.0-1.14 leading. Below, a Matter 18px lead paragraph in
iron gray, max-width ~56ch. Pair one filled dark button (`#181818` fill, 4px
radius) with a ghost arrow-link — never a chromatic CTA. Centre a product-
screenshot card below the hero, 8px radius, elevated with a genuine three-layer
shadow; this is the only card in the system permitted that shadow. Use studio
blue `#5d8cd7` only for the brand mark and code-syntax accents. Add a faint,
low-opacity isometric line grid clipped to the hero's upper-right corner. Keep
marketing cards flat with 1px hairline borders instead of shadow, 96px section
gaps, and a consistent eyebrow → two-tone heading → lead → visual rhythm
throughout.

## Image recipe

Not primarily photographic — the sole hero visual is a product screenshot
(the design tool's own UI, rendered flat with traffic-light window dots, a
file-tree sidebar, and a properties panel) rather than photography. Where a
supplementary image is needed: a plain, evenly lit [SUBJECT] product-UI
mockup on a neutral background, no lifestyle staging, styled to match the
existing product chrome rather than introducing new imagery language.

## Photo search

Unsplash first, Pexels second.
- "software interface mockup minimal desk"
- "laptop screen design tool workspace"
- "minimal desk setup natural light"
- "abstract isometric line grid pattern"

## Reference lock

Primary reference/direction: Paper — warm cream design-tool marketing page,
two-tone headline, colour confined to logo and code.
Preserve (3-5 traits): bone cream `#efefe4` canvas with paper/bright white
reserved for elevated cards only; two-tone headline (identical Matter size and
weight, ink first line, slate continuation), never varied by size or font;
single filled ink `#181818` CTA, no chromatic button ever; three-layer shadow
reserved exclusively for the product screenshot and floating panels, hairline
borders elsewhere; studio blue `#5d8cd7` confined to the brand mark and code
syntax only.
Borrow only (1-2): the low-opacity isometric line-grid corner overlay; the
overlapping terminal/MCP panel composed against the product screenshot card.
Role rules: blue never appears on a button, link, or large text area; the
two-tone headline never mixes fonts or sizes between its lines; card shadow
never applies to headings, logos, or plain marketing cards.
Media strategy: none beyond the product's own UI screenshots — no lifestyle
photography, no illustration, no stock imagery.
Reject: a chromatic CTA fill; shadow on non-product cards; bold or italic
inline emphasis in body copy; pure white as the page background; a gradient
anywhere.
Token commitments: bg `#efefe4`, card `#fcfcf9`/`#ffffff`, hairline `#d7d7d6`,
ink `#181818`, secondary `#83837e`, accent `#5d8cd7`; display Matter 400 at
48-64px/leading 1.0-1.14/-0.96 to -1.28px tracking; body Inter 400-600 at
12-18px; radius 4px buttons, 8px cards, 12-24px product frames; page max-width
1200px, section gap 96px.
