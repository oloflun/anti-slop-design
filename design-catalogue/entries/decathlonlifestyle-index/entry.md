---
title: "Decathlon Lifestyle - Landing page"
url: https://decathlonlifestyle.index.studio/
source_url: https://decathlonlifestyle.index.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: ""
family: sportswear-colour-block-lookbook
dna: "Sportswear lifestyle line x colour blocks that open into photos"
register: warm photographic
grammar: chaptered editorial
lane: "A lookbook landing page: 'SPORTSWEAR' with photo tiles sliding through the letters over a stair photo, colour swatch blocks that open into campaign photos, 'Nouvelle collection lifestyle pour tous les jours', category rows (T-shirts, Baskets, Sweats, Shorts, Headwear) each with a colour block opening into a photo, RR2K and RR70 shoe blocks, 'Step in your comfort', 'Your style, your colors' and a category index."
mode: persuade
traits: ["colour swatch blocks opening into photos", "giant word with photos sliding through", "category rows", "shoe name blocks in team colours", "warm campaign photography", "letters with gaps that fill"]
palette: ["#FFFFFF", "#B8A39A", "#0F443D", "#3B314F", "#03151C", "#585554"]
type: ["Decathlon Text", "Decathlon Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The colour blocks are the transition material: every category enters as a swatch of its palette that opens into the photo, tying product colour to the layout.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Index Studio).

## What to borrow (principle)

- Let a flat colour swatch open into the photo it represents

## What to leave

- Long product rows
- Small prices

## Signature move

Colour swatches opening into campaign photos for each category.

## Motion

Intro: the word assembles with photos sliding through its letters (~2 s). Wheel (Lenis): swatch blocks slide and split open into photos; headings fill letter by letter; shoe blocks rise; products scroll sideways; the closing index highlights categories.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; 7 video; split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a lookbook landing page: 'SPORTSWEAR' with photo tiles sliding through the letters over a stair photo, colour swatch blocks that open into campaign photos, 'Nouvelle collection lifestyle pour tous les jours', category rows (T-shirts, Baskets, Sweats, Shorts, Headwear) each with a colour block opening into a photo, RR2K and RR70 shoe blocks, 'Step in your comfort', 'Your style, your colors' and a category index. Type: Decathlon Text, Decathlon Display.
Ground and ink from the measured palette (#FFFFFF, #B8A39A, #0F443D). Motion carries the page through
colour swatches opening into campaign photos for each category. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — sportswear campaign photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: sportswear campaign photography

## Reference lock

Primary reference/direction: Decathlon Lifestyle - Landing page — A lookbook landing page: 'SPORTSWEAR' with photo tiles sliding through the letters over a stair photo, colour swatch blocks that open into campaign photos, 'Nouvelle collection lifestyle pour tous les jours', category rows (T-shirts, Baskets, Sweats, Shorts, Headwear) each with a colour block opening into a photo, RR2K and RR70 shoe blocks, 'Step in your comfort', 'Your style, your colors' and a category index.
Preserve (3-5 traits): colour swatch blocks opening into photos; giant word with photos sliding through; category rows; shoe name blocks in team colours; warm campaign photography.
Borrow only (1-2): Let a flat colour swatch open into the photo it represents
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: sportswear campaign photography
Reject: Long product rows; Small prices
Token commitments: palette #FFFFFF, #B8A39A, #0F443D, #3B314F, #03151C, #585554; type Decathlon Text, Decathlon Display; engine GSAP + Lenis linked (never vendored).
