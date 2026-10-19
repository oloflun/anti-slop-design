---
title: "More Nutrition - Matcha meets Protein"
url: https://more-nutrition.webflow.io/
source_url: https://more-nutrition.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: product-tub-path-ecommerce
dna: "Matcha protein drink x a product tub that travels along a drawn path"
register: modern clean
grammar: chaptered editorial
lane: "A product page in sage greens: the logo draws itself, a curved 'It's a match(a)' text band sweeps across, polaroid photos of people, then the product tub moves along a white curved path down the page, stopping next to each benefit card (More taste, More caffeine, More weight loss, No added sugar), a flavour lineup with fruit flying, a comparison table, reviews and a chunky flavour add-on."
mode: persuade
traits: ["product tub travelling along a path", "curved text band", "benefit cards beside the product", "polaroid photos with handwriting", "fruit flying around flavours", "comparison table"]
palette: ["#E8F0E6", "#AFC69C", "#7F886A"]
type: ["Founders Grotesk Condensed"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The tub is the signature object and the path is its route: every benefit is a stop on the way, so a list of claims becomes a journey with the product in hand.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: FUTURE THREE).

## What to borrow (principle)

- Move the product along a drawn path, stopping at each benefit

## What to leave

- Generic review and payment sections
- Small handwriting

## Signature move

A matcha tub travelling down a white path and stopping beside each benefit.

## Motion

Intro: sage, the logo writes itself (~2 s). Wheel (Lenis ~80 px glide, 21 triggers): the curved band rotates; polaroids drop in; the tub rides the path, turning to show its sides, with benefit cards sliding in beside it; the tub lands in the lineup; fruit flies in; the table rows tick.

Measured (`motion/probe.json`): GSAP 3.15.0; 21 ScrollTriggers; Lenis; 3 video; smoothed scroll (median 51 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a product page in sage greens: the logo draws itself, a curved 'It's a match(a)' text band sweeps across, polaroid photos of people, then the product tub moves along a white curved path down the page, stopping next to each benefit card (More taste, More caffeine, More weight loss, No added sugar), a flavour lineup with fruit flying, a comparison table, reviews and a chunky flavour add-on. Type: Founders Grotesk Condensed.
Ground and ink from the measured palette (#E8F0E6, #AFC69C, #7F886A). Motion carries the page through
a matcha tub travelling down a white path and stopping beside each benefit. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product renders, lifestyle polaroids

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product renders, lifestyle polaroids

## Reference lock

Primary reference/direction: More Nutrition - Matcha meets Protein — A product page in sage greens: the logo draws itself, a curved 'It's a match(a)' text band sweeps across, polaroid photos of people, then the product tub moves along a white curved path down the page, stopping next to each benefit card (More taste, More caffeine, More weight loss, No added sugar), a flavour lineup with fruit flying, a comparison table, reviews and a chunky flavour add-on.
Preserve (3-5 traits): product tub travelling along a path; curved text band; benefit cards beside the product; polaroid photos with handwriting; fruit flying around flavours.
Borrow only (1-2): Move the product along a drawn path, stopping at each benefit
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product renders, lifestyle polaroids
Reject: Generic review and payment sections; Small handwriting
Token commitments: palette #E8F0E6, #AFC69C, #7F886A; type Founders Grotesk Condensed; engine GSAP + Lenis linked (never vendored).
