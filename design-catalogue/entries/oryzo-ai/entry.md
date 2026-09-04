---
title: "ORYZO AI"
url: https://oryzo.ai
source_url: https://oryzo.ai
captured: 2026-09-04
origin: refero
extract: ok
category: luxury-craft
category2: "product-focused"
family: darkroom-cork-artifact
dna: "Museum-artifact product reveal x deadpan AI-launch typographic voice"
register: cinematic dark
grammar: continuous world
lane: "A warm-dark canvas holds an ordinary cork coaster like a museum artifact: full-viewport void-mode sections stack a centred 3D render between flanking uppercase headline and body-copy columns, with a single orange used only for credit lines, never for a button"
mode: experience
traits: ["uppercase weight-500 everything except one body voice", "warm walnut void, never pure black", "100vh per section, one statement each", "orange accent for credits only, never CTAs", "dashed hairline dividers, no solid rules", "0.9 line-height stacking display type"]
palette: ["#ffedd7", "#100904", "#445231", "#382416", "#dc5000", "#000000"]
type: ["halyard-display-variable"]
measured: designlang
kind: reference-style
source: anton
status: ready
refero: processed/ORYZO AI.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Warm walnut `#100904` and warm cream `#ffedd7` stand in for black and
white everywhere — the source is explicit that "purity reads as wrong here."
Depth comes from exactly one luminance step (canvas to Bark Brown), never from
shadow, which keeps every void-mode section reading as a continuous dark stage
rather than a stack of elevated cards.

A single typeface carries the entire system in exactly two modes: uppercase
weight 500 for everything functional — nav, headings, labels, buttons — and one
narrow exception, 29px weight-400 mixed-case body copy, reserved solely for
product description. The shift from all-caps declarative label to lowercase
sentence is itself the signal that tells a reader "you are now reading
description, not a UI label." Display sizes are stacked at an unusually tight
0.9 line-height, which the source describes as making uppercase letterforms
overlap their line bounds into a sculptural block rather than sitting in
readable lines.

The single accent colour, ember orange, is fenced to an unusually narrow role —
credit lines and one studio link — and explicitly banned from CTAs or any
interactive surface. Combined with sections that are each locked to a full
100vh (never compressed into a band) and dashed hairline dividers as the only
structural break, the page reads as a sequence of gallery installations rather
than a scrolling marketing page — appropriate for a project whose entire premise
is presenting an ordinary object with mock-serious "AI product launch" gravity.
The designlang extract also surfaces a moss-green `#445231` (417 uses, second
only to the cream ink colour) not present in the original capture — a second
void-mode section tone alongside walnut, corrected into the palette above.

## What to borrow (principle)

- **Warm both ends of the black/white scale.** Neither pure black nor pure
  white appears anywhere; a warm near-black and warm near-white can carry an
  entire dark system without feeling clinical.
- **Use case and weight, not colour, to separate label from description.**
  Switching from uppercase/500 to mixed-case/400 for exactly one text role is a
  legible, colour-free way to mark "this is prose."
- **Fence an accent colour to editorial credit only.** Explicitly banning the
  accent from buttons and CTAs keeps it reading as rare and earned rather than
  decorative.
- **Give every section a full viewport and one statement.** Locking sections to
  100vh with no compression forces genuine editorial pacing rather than dense
  stacking.
- **Compress display leading until letterforms overlap.** A 0.9 line-height at
  large uppercase sizes turns type into a stacked sculptural block rather than
  conventional readable lines.

## What to leave

- Locking every section to 100vh is a strong commitment that works for a
  single-product showcase but would feel padded and slow on a page with more
  than a handful of genuine content sections.
- A single typeface with only two permitted voices (uppercase label, one
  mixed-case body size) leaves no room for a third register — a testimonial or
  a pull-quote would need to borrow one of the two existing voices rather than
  getting its own treatment.
- The premise-dependent tone (treating an ordinary object with mock-serious
  product-launch gravity) is a specific creative conceit; applied to a genuinely
  premium product without the self-aware wink, the same typographic solemnity
  could read as simply humourless.

## Signature move

The vertical sidebar serial-number label: rotated 90° text ("ORYZO 1-MODEL")
running flush down the right viewport margin — a physical-product artifact
detail (like a stamped serial number) translated directly into a persistent UI
element.

## Motion

(from designlang extract) Feel reads as springy, and the page is scroll-linked —
correcting the earlier "no durations specified" read. Four duration steps run
150-500ms, and a genuine spring/overshoot curve, `cubic-bezier(0.3, 0, 0.66,
-0.3)`, is confirmed in use alongside a plain `ease`. The one keyframe firing is
`grip-instruction-wheel-dash`, animating `stroke-dashoffset` on what reads as an
SVG dial or wheel graphic — most plausibly a "how to hold/rotate it" instruction
element paired with the product render, tracing a dash pattern around a circular
path rather than a static icon. (observed in capture) the live capture confirms
a real-time WebGL/Three.js render of the coaster with visible inertia and
weight as it moves — the spring easing found in the extract is consistent with
that same weighted, springy feel carrying into the interactive object itself.

| Token | Value | Easing |
|---|---|---|
| xs | 150ms | `ease` |
| sm | 180ms | `ease` |
| md | 300ms | spring |
| lg | 500ms | spring |
| spring/overshoot | — | `cubic-bezier(0.3, 0, 0.66, -0.3)` |

## Brief

Build a deadpan, museum-grade single-product showcase page. Canvas is warm
walnut `#100904` throughout — never pure black; text is warm cream `#ffedd7` —
never pure white. Depth comes from exactly one elevated surface, Bark Brown
`#382416`, used only for the system's one filled CTA; everything else is flat.
Set all UI text — nav, headings, labels, buttons — in a single geometric sans at
weight 500, uppercase, with display sizes compressed to 0.9 line-height; reserve
one exception, 29px weight-400 mixed-case, for product description copy only.
Ember orange `#dc5000` appears only on credit lines and a single studio link —
never on a button or CTA. Structure the page as a sequence of full 100vh
sections: a top-down photographic hero with tools-of-the-craft context, followed
by void-mode reveals where a centred 3D product render sits flanked by a
left-aligned uppercase heading and a right-aligned mixed-case body column. Use
dashed 1px hairlines as the only divider, 12px radius for cards, 36px for the
one pill CTA, 22.5px for ghost buttons, 0px for inputs. Add a rotated
serial-number label fixed to the right margin as a persistent artifact detail.

## Image recipe

Top-down documentary photograph of [SUBJECT] and its tools-of-the-craft — laid
on a green cutting mat or workbench surface, natural or warm practical light,
sharp focus throughout, genuine workshop clutter (pencil, blade, paperclip)
visible in frame but not staged, warm high-contrast colour grading, full-bleed
with no vignette.

## Photo search

Unsplash first, Pexels second.
- "craft tools top down workbench flat lay"
- "cutting mat pencil knife top down"
- "product design workshop overhead warm light"
- "cork material texture close up"

## Reference lock

Primary reference/direction: ORYZO AI — deadpan museum-artifact single-product
page, warm dark void with an uppercase-only type voice.
Preserve (3-5 traits): warm walnut `#100904` canvas and warm cream `#ffedd7`
text, never pure black or white; single typeface locked to uppercase weight 500
for everything except one 29px mixed-case body voice; ember `#dc5000` fenced to
credit lines only, never a CTA or interactive surface; every section locked to
100vh, one statement per screen; dashed 1px hairlines as the only divider, zero
shadow-based elevation.
Borrow only (1-2): the rotated 90° serial-number sidebar label; the semi-
transparent attribution info-card overlay on the hero photograph.
Role rules: ember never touches a button or interactive surface; body copy
(29px mixed-case) is the only non-uppercase text in the system; body text
never centres, even when flanking a centred object.
Media strategy: top-down documentary/workshop photography for hero context;
real-time 3D/WebGL render for the isolated product reveal; no lifestyle
photography, no stock people.
Reject: pure black or pure white anywhere; ember on any button; solid (non-
dashed) dividers; border-radius below 12px on containers; compressing a
section below 100vh.
Token commitments: bg `#100904`, elevated `#382416`, hairline `#40372e`,
mid-tone `#6c5f51`, ink `#ffedd7`, accent `#dc5000`; display 41-51px/leading
0.9; body 29px weight 400/leading 1.26; label 8-24px weight 500 uppercase;
radius 12px cards, 22.5px ghost buttons, 36px filled pill, 0px inputs.
