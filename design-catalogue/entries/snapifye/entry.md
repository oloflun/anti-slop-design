---
title: "Snapifye"
url: https://snapifye.webflow.io/
source_url: https://snapifye.webflow.io/
captured: 2026-09-04
origin: raw-url
raw: raw/256539ed814eeb99-try-webflow-com.webp
extract: ok
category: portfolio
category2: playful
family: vintage-polaroid-portfolio
dna: "Vintage photo-booth polaroids x condensed poster headline"
register: warm photographic
grammar: gallery/catalog
lane: "A dark maroon hero scatters tilted vintage-toned polaroids beside a huge condensed headline with one script-italic word, then the page shifts to a salmon-pink featured-work gallery of tilted photo cards before closing on a purple neon portrait and a dark footer"
mode: experience
traits: ["dark maroon hero ground", "salmon-pink gallery section", "tilted polaroid-style photo frames", "condensed bold display sans", "single script-italic accent word", "horizontal marquee text band", "warm vintage colour grading", "purple neon closing photo"]
palette: ["#701E1F", "#EC7672", "#F8DCC6", "#3D1219", "#914D56", "#882048"]
type: ["GT Walsheim", "Libre Caslon Text"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The page runs on a colour-field structure rather than a grid: a dark maroon hero, a
salmon-pink featured-work section, a purple neon closing photo, and a near-black footer,
each a full-bleed flat colour rather than a bordered card. Photography supplies almost all
the remaining colour and texture — every field is populated with tilted, slightly
rotated photo frames that read as physical prints scattered on a table rather than
uniformly cropped grid tiles.

Type carries a small but deliberate second voice: the condensed bold display sans sets
every headline ("VINTAGE THROUGH LENS", "OUR FEATURED"), but exactly one word per
headline breaks into a script italic ("**experiences**", "**work**") — the same device as
EXAMPLE and Picnic in this set, where the accent typeface marks the word the sentence
turns on rather than adding random flourish. Because it's always one word, never a full
line, the condensed voice stays dominant.

A horizontal marquee band of oversized type ("...ENCY CREATIV...") runs between the
gallery and the closing photo, functioning as a rhythm break between two very different
colour fields — the same technique this set has already seen used to bridge intensity
shifts rather than to hold a message. The vintage colour grading (warm reds, faded film
tones) unifies photography shot in very different settings — studio portraits, street
candids, a neon-lit club scene — into one continuous mood.

## What to borrow (principle)

- **Use full-bleed flat colour fields as the only section divider you need**, and let
  photography carry the texture within each field.
- **Tilt photos slightly and let them overlap their container** to read as physical,
  handled prints rather than a uniform grid — works especially well for portfolio/gallery
  content.
- **Break exactly one word per headline into a second, softer typeface.** Never a whole
  line — the accent stays an accent.
- **Grade all photography toward one consistent vintage/warm tone**, even when subject
  matter and lighting vary wildly between shots, so the gallery reads as one body of work.

## What to leave

- The floating template-marketplace widget (Figma/Buy button, bottom-right of the hero) is
  a Webflow showcase artifact, not part of the design — exclude entirely from any build.
- Photo tilt applied inconsistently in density (heavily scattered in the hero, more
  regular in the featured-work grid) reads as two different systems; picking one tilt
  range and applying it everywhere would tighten the identity.
- The marquee band's cropped-at-both-edges text ("ENCY CREATIV") gives no readable message
  in a static capture — fine if genuinely scrolling live, but a static fallback state
  should show a complete word.

## Signature move

The scattered tilted-polaroid hero: several small, rotated, warm-toned photographs
arranged loosely around the headline rather than in a single hero image slot, so the page
reads as a photographer's contact sheet spilled across the screen rather than a single
curated hero shot.

## Motion

Overall feel reads as mixed on a scroll-linked page. Three duration steps cover
interaction states: `xs` 100ms, `sm` 250ms and `md` 300ms. Several transitions animate
`text-decoration-color` specifically (0.25s and, combined with `color`, folded into the
0.3s/0.35s group) rather than plain `color` alone — a tell for an underline-sweep hover
state, where the underline's colour fades in on its own timing separate from the text.
Other pairs (`background-color`/`color` at 0.1s, `color`+`background-color` at 0.35s)
suggest fast link/button state swaps. No easing function is declared on any transition, so
all fall through to the browser default rather than a spring/overshoot curve. The one
keyframe present is a plain 360° `spin` (loader icon), not the marquee itself — the extract
gives no evidence for a staggered scroll-reveal on the scattered polaroids, so that remains
unconfirmed. (from designlang extract)

| Token | Value | Curve |
|---|---|---|
| `xs` | 100ms | default ease (bg/color swap) |
| `sm` | 250ms | default ease (`text-decoration-color`) |
| `md` | 300ms | default ease (color + background-color) |
| `spin` keyframe | rotate 0deg → 360deg | unspecified (loader) |

## Brief

Build a photography-studio portfolio page structured as stacked full-bleed colour fields
rather than a bordered grid: a dark warm-red hero, a salmon-pink featured-work section, a
saturated neon closing photo, and a near-black footer. Populate every field with tilted,
overlapping photographs graded toward one consistent warm/vintage tone, regardless of the
original shoot's lighting. Set headlines in a condensed bold display sans, breaking
exactly one word per headline into a script italic accent — never a full line. Use a
horizontal marquee band of oversized type as the transition between two colour fields
rather than a rule or gap. Close on a quote block with a small avatar and a dark footer
restating the studio's tagline.

## Image recipe

Vintage-toned portrait or candid photograph of [SUBJECT] — a photo-booth style portrait, a
street candid, a neon-lit night scene — shot with warm film-like colour grading (reds and
ambers pushed, shadows warm rather than cool), slight grain, cropped to a small
polaroid-like frame that can be rotated a few degrees without losing legibility.

## Photo search

Unsplash first, Pexels second.
- "vintage film portrait warm tone"
- "photo booth style portrait candid"
- "neon lit portrait night club"
- "street candid film grain warm"

## Reference lock

Primary reference/direction: Snapifye — full-bleed colour-field portfolio with scattered
tilted vintage polaroids and a script-italic accent word per headline.
Preserve (3-5 traits): stacked full-bleed flat colour fields as the only section
structure; tilted, overlapping photo frames rather than a uniform grid; exactly one
script-italic accent word per condensed headline; consistent warm/vintage colour grading
across all photography regardless of original shoot conditions; a horizontal marquee band
as the transition device between colour fields.
Borrow only (1-2): the quote block with small circular avatar; the "SEE MORE" arrow-link
styling.
Role rules: script italic never sets more than one word per headline; every photograph
gets the same vintage colour grade, no exceptions; colour fields are always flat and
full-bleed, never gradient or textured.
Media strategy: photo:unsplash — warm, film-toned portrait and candid photography, single
consistent grade applied across the whole set, no cool/neutral outliers.
Reject: a uniform, untilted photo grid; more than one accent word per headline; template-
marketplace UI chrome (buy buttons, tool badges) left in the design; cool or desaturated
photography breaking the warm grade.
Token commitments: hero-bg `#701E1F`, gallery-bg `#EC7672`, tint `#F8DCC6`, footer-bg
`#3D1219`, closing-accent `#882048`, warm-mid `#914D56`; display `GT Walsheim` (condensed
bold), accent script/italic serif for single headline words; photo frames rotated a few
degrees, never axis-aligned in hero/gallery sections.
