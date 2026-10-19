---
title: "Longbow"
url: https://db-longbow.webflow.io/
source_url: https://db-longbow.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: featherweight-ev-condensed
dna: "British featherweight sports car x condensed caps and grey studio"
register: cinematic dark
grammar: chaptered editorial
lane: "A sports-car page on studio grey where condensed caps headlines are split by the car, renders of the green and silver roadsters slide past in panels, an archer emblem anchors a black brand section, and road footage widens from a frame to full bleed."
mode: persuade
traits: ["ultra-condensed caps split across the frame", "studio-grey product renders", "panel slides between render crops", "black brand chapter with archer emblem", "road film widening to full bleed", "italic serif philosophy line in brackets"]
palette: ["#898D90", "#676669", "#AFAFB1", "#161418", "#E8E8E9", "#4D4A4E"]
type: ["Ebgaramond Variablefont Wght 0", "Geist Mono V4", "Bebas Neue", "EB Garamond"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The car is shown like a magazine spread: big condensed words broken apart so the car can sit in the gap, and renders sliding in as panels. The 'lightness' message gets a single emblem (an archer) on black and a bracketed italic line, a quiet beat between the loud headline sections.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Split a condensed headline so the product sits in the gap
- Let a road film widen from a framed panel to full bleed
- A bracketed italic line as the quiet 'philosophy' beat

## What to leave

- Very heavy smoothing (~210 px glide)
- Long grey stretches waiting for images

## Signature move

Condensed caps headlines split apart so the roadster sits between the words.

## Motion

Intro: grey-blue gradient with a small loader pill (~2 s). Scroll (Lenis, ~210 px glide, SplitText): 'HOW LONGBOW…' with the green roadster; render panels slide over each other; 'A NEW SPECIES' words separate; 'THE SPEED OF LIGHTNESS' black chapter with the archer emblem; press logos; road footage grows from a framed panel to full width; render pairs; 'A VISION BORN OF SPIRIT / FORGED BY REASON'; founders.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 19 video; split text; smoothed scroll (median 197 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a sports-car page on studio grey where condensed caps headlines are split by the car, renders of the green and silver roadsters slide past in panels, an archer emblem anchors a black brand section, and road footage widens from a frame to full bleed. Type: Ebgaramond Variablefont Wght 0, Geist Mono V4, Bebas Neue, EB Garamond.
Ground and ink from the measured palette (#898D90, #676669, #AFAFB1). Motion carries the page through
condensed caps headlines split apart so the roadster sits between the words. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — studio product renders on neutral grey plus road footage

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: studio product renders on neutral grey plus road footage

## Reference lock

Primary reference/direction: Longbow — A sports-car page on studio grey where condensed caps headlines are split by the car, renders of the green and silver roadsters slide past in panels, an archer emblem anchors a black brand section, and road footage widens from a frame to full bleed.
Preserve (3-5 traits): ultra-condensed caps split across the frame; studio-grey product renders; panel slides between render crops; black brand chapter with archer emblem; road film widening to full bleed.
Borrow only (1-2): Split a condensed headline so the product sits in the gap; Let a road film widen from a framed panel to full bleed
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: studio product renders on neutral grey plus road footage
Reject: Very heavy smoothing (~210 px glide); Long grey stretches waiting for images
Token commitments: palette #898D90, #676669, #AFAFB1, #161418, #E8E8E9, #4D4A4E; type Ebgaramond Variablefont Wght 0, Geist Mono V4, Bebas Neue, EB Garamond; engine GSAP + Lenis linked (never vendored).
