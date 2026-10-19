---
title: "NUSET - Dermatologist skincare"
url: https://nuset.jp/
source_url: https://nuset.jp/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "luxury-craft"
family: japanese-skincare-soft-beige
dna: "Japanese skincare x soft beige photography and vertical poems"
register: warm photographic
grammar: chaptered editorial
lane: "A skincare brand: a model with the product and the wordmark, the photo veiling to beige as a vertical poem appears, a white section with product shots and Japanese copy, 'Line up' ReCell series with circle diagrams, products in vertical columns on taupe, a blue science section, user voices and a styled product group."
mode: read
traits: ["soft beige veil", "vertical Japanese poem", "taupe product columns", "thin serif English labels", "circle diagrams", "product still life"]
palette: ["#F8F4EC", "#A99180", "#D7CEC6", "#B9A799", "#7F6B5E"]
type: ["Lato", "Noto Sans JP", "Zen Old Mincho"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Veiling the hero photo into beige as the poem appears sets a calm tone suited to skincare.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Veil the hero image into a flat tone before the copy appears

## What to leave

- Small text

## Signature move

A model holding a skincare bottle as the photo veils to beige.

## Motion

Intro: the hero photo. Wheel (Lenis): a beige veil fades over the photo as poem lines appear; panels slide; product columns reveal; circle diagrams draw.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; WebGL canvas x1; 8 video; split text; smoothed scroll (median 201 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a skincare brand: a model with the product and the wordmark, the photo veiling to beige as a vertical poem appears, a white section with product shots and Japanese copy, 'Line up' ReCell series with circle diagrams, products in vertical columns on taupe, a blue science section, user voices and a styled product group. Type: Lato, Noto Sans JP, Zen Old Mincho.
Ground and ink from the measured palette (#F8F4EC, #A99180, #D7CEC6). Motion carries the page through
a model holding a skincare bottle as the photo veils to beige. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — skincare product and model photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: skincare product and model photography

## Reference lock

Primary reference/direction: NUSET - Dermatologist skincare — A skincare brand: a model with the product and the wordmark, the photo veiling to beige as a vertical poem appears, a white section with product shots and Japanese copy, 'Line up' ReCell series with circle diagrams, products in vertical columns on taupe, a blue science section, user voices and a styled product group.
Preserve (3-5 traits): soft beige veil; vertical Japanese poem; taupe product columns; thin serif English labels; circle diagrams.
Borrow only (1-2): Veil the hero image into a flat tone before the copy appears
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: skincare product and model photography
Reject: Small text
Token commitments: palette #F8F4EC, #A99180, #D7CEC6, #B9A799, #7F6B5E; type Lato, Noto Sans JP, Zen Old Mincho; engine GSAP + Lenis linked (never vendored).
