---
title: "Farm Minerals"
url: https://www.farmminerals.com/
source_url: https://www.farmminerals.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: green-plinth-agritech
dna: "Low-carbon fertiliser x product on plinths in green light"
register: warm photographic
grammar: chaptered editorial
lane: "An agritech page that sets a carved fertiliser tablet on plinths in green dappled light under 'Fertilizer, Reinvented.', then product packs on green cards, a dotted world map of field trials, community updates over farmland, and farmer portraits in a green close."
mode: persuade
traits: ["product as a carved object on plinths", "green dappled light", "letters that resolve in the headline", "product pack cards", "dotted world map of trials", "farmer portraits"]
palette: ["#F5EDE7", "#5A6932", "#7B7B4C", "#263211", "#AAB28A"]
type: ["Aeonik"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Fertiliser is shown as a sculpture: one tablet with the leaf logo carved in, lit on plinths like a museum piece. That single image raises the product's status; the rest of the page (map, cards, people) is practical.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: ADELT).

## What to borrow (principle)

- Present a commodity product as a sculpture on plinths
- A dotted world map for distributed trials or locations

## What to leave

- Headline letters arriving out of order looks glitchy
- Long green close repeats

## Signature move

A carved fertiliser tablet on plinths in green dappled light.

## Motion

Intro: 'Fertilizer, Reinvented.' letters resolve out of order over the plinth scene (~1 s). Scroll (Lenis, ~140 px glide, 40 ScrollTriggers, SplitText): corn close-up transition to cream; product cards; field trials map with markers; NutriPeak early-access card; 'Latest from the community' over farmland; farmer cards; green 'See the Difference for Yourself' close.

Measured (`motion/probe.json`): GSAP 3.15.0; 40 ScrollTriggers; Lenis; 3 video; split text; smoothed scroll (median 122 px still travelling after input stops); entry gate: EXPLORE PRODUCTS. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: an agritech page that sets a carved fertiliser tablet on plinths in green dappled light under 'Fertilizer, Reinvented.', then product packs on green cards, a dotted world map of field trials, community updates over farmland, and farmer portraits in a green close. Type: Aeonik.
Ground and ink from the measured palette (#F5EDE7, #5A6932, #7B7B4C). Motion carries the page through
a carved fertiliser tablet on plinths in green dappled light. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product renders on plinths in green light, crops, farmers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product renders on plinths in green light, crops, farmers

## Reference lock

Primary reference/direction: Farm Minerals — An agritech page that sets a carved fertiliser tablet on plinths in green dappled light under 'Fertilizer, Reinvented.', then product packs on green cards, a dotted world map of field trials, community updates over farmland, and farmer portraits in a green close.
Preserve (3-5 traits): product as a carved object on plinths; green dappled light; letters that resolve in the headline; product pack cards; dotted world map of trials.
Borrow only (1-2): Present a commodity product as a sculpture on plinths; A dotted world map for distributed trials or locations
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product renders on plinths in green light, crops, farmers
Reject: Headline letters arriving out of order looks glitchy; Long green close repeats
Token commitments: palette #F5EDE7, #5A6932, #7B7B4C, #263211, #AAB28A; type Aeonik; engine GSAP + Lenis linked (never vendored).
