---
title: "TrueKind - clean skincare"
url: https://truekindskincare.com/
source_url: https://truekindskincare.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: skincare-counter-oval-crops
dna: "Clean skincare x a big counter loader and oval-cropped beauty portraits"
register: warm photographic
grammar: chaptered editorial
lane: "A skincare brand: a giant serif counter 00 to 99 on charcoal, a full-bleed skin close-up, 'Clean, conscious, performance skincare' with an oval-cropped smiling portrait and a drawn line, 'Explore pure potency', product blends beside skin close-ups, 'Radical transparency. Hide nothing.' with product swatches, offers, a journal on black and Instagram."
mode: persuade
traits: ["giant serif counter loader", "oval-cropped portraits", "italic script accent words", "skin close-ups", "product swatch smears", "drawn connecting line"]
palette: ["#FFFFFF", "#512E22", "#E2C3B6", "#C8A28A", "#864F3C", "#9E7563"]
type: ["Editorial New", "PP Mori"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The oval crops and swatch smears tie product and skin together; the counter loader sets an editorial tone.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Oval-crop portraits to soften a beauty layout

## What to leave

- Generic offers and journal

## Signature move

An oval-cropped smiling portrait under 'Clean, conscious, performance skincare'.

## Motion

Intro: charcoal with a big counter (~2 s), the wordmark, then a skin close-up. Wheel (Lenis): the close-up shrinks; the oval portrait slides; the line draws; products slide beside skin; swatches scale; sections stack.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; 2 video; smoothed scroll (median 104 px still travelling after input stops); entry gate: close. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a skincare brand: a giant serif counter 00 to 99 on charcoal, a full-bleed skin close-up, 'Clean, conscious, performance skincare' with an oval-cropped smiling portrait and a drawn line, 'Explore pure potency', product blends beside skin close-ups, 'Radical transparency. Hide nothing.' with product swatches, offers, a journal on black and Instagram. Type: Editorial New, PP Mori.
Ground and ink from the measured palette (#FFFFFF, #512E22, #E2C3B6). Motion carries the page through
an oval-cropped smiling portrait under 'Clean, conscious, performance skincare'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — beauty and product photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: beauty and product photography

## Reference lock

Primary reference/direction: TrueKind - clean skincare — A skincare brand: a giant serif counter 00 to 99 on charcoal, a full-bleed skin close-up, 'Clean, conscious, performance skincare' with an oval-cropped smiling portrait and a drawn line, 'Explore pure potency', product blends beside skin close-ups, 'Radical transparency. Hide nothing.' with product swatches, offers, a journal on black and Instagram.
Preserve (3-5 traits): giant serif counter loader; oval-cropped portraits; italic script accent words; skin close-ups; product swatch smears.
Borrow only (1-2): Oval-crop portraits to soften a beauty layout
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: beauty and product photography
Reject: Generic offers and journal
Token commitments: palette #FFFFFF, #512E22, #E2C3B6, #C8A28A, #864F3C, #9E7563; type Editorial New, PP Mori; engine GSAP + Lenis linked (never vendored).
