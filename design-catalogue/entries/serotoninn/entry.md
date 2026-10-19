---
title: "Serotoninn"
url: https://serotoninn.com/
source_url: https://serotoninn.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: ""
family: glam-grunge-fashion-shop
dna: "Fashion label x glam-grunge spray-paint editorial"
register: editorial print
grammar: chaptered editorial
lane: "A fashion shop that loads by colouring a black-and-white model with a red sunglasses flash, sprays the hero with a black aerosol gesture, then runs categories as vertical rotated labels between cut-out models, spray-painted words over photos and a lip-shaped video mask."
mode: persuade
traits: ["percentage loader colouring a model photo", "spray-paint gesture and graffiti words", "rotated vertical category labels", "cut-out models on off-white", "lip-shaped video mask", "condensed caps (Thunder) + mono"]
palette: ["#FEFEFE", "#040505", "#1C1C27", "#E4E1E1", "#74716B"]
type: ["Inter", "Thunder", "PP Fraktion Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

'Where glam meets grunge' is executed literally: clean cut-out fashion shots get spray-painted words and a black aerosol cloud over them. Categories sit as rotated labels between models, and the closing film plays inside a lip shape, a mask from the brand's own iconography.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Artycoders, BL/S®, Black Lead Studio).

## What to borrow (principle)

- Mask a video with a brand shape (lips) instead of a rectangle
- Rotated vertical labels between cut-out products as category navigation
- A loader that colours the hero image as it counts

## What to leave

- Cookie notice over all frames
- Many type treatments at once

## Signature move

A black aerosol spray sweeping across the hero model.

## Motion

Intro: model in black and white, the sunglasses flash red, 'LOADING… 18% → 66%' (~2 s). Scroll (Lenis, 2 pins, Draggable/Inertia, Observer, SplitText): the spray gesture sweeps the hero; product cards slide up; dark section with a model walking past green tiles; 'NEW DRESSES'; category strip with rotated labels; dresses and corsets with sliding labels; 'BOLD FASHION' graffiti over a crouching model; 'A VISION IN MOTION' with the film inside a lip mask that grows to full screen; wordmark close.

Measured (`motion/probe.json`): GSAP 3.14.2; 2 pinned sections; Lenis; 31 video; split text; smoothed scroll (median 126 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a fashion shop that loads by colouring a black-and-white model with a red sunglasses flash, sprays the hero with a black aerosol gesture, then runs categories as vertical rotated labels between cut-out models, spray-painted words over photos and a lip-shaped video mask. Type: Inter, Thunder, PP Fraktion Mono.
Ground and ink from the measured palette (#FEFEFE, #040505, #1C1C27). Motion carries the page through
a black aerosol spray sweeping across the hero model. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — cut-out fashion shots on off-white plus moody editorial film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: cut-out fashion shots on off-white plus moody editorial film

## Reference lock

Primary reference/direction: Serotoninn — A fashion shop that loads by colouring a black-and-white model with a red sunglasses flash, sprays the hero with a black aerosol gesture, then runs categories as vertical rotated labels between cut-out models, spray-painted words over photos and a lip-shaped video mask.
Preserve (3-5 traits): percentage loader colouring a model photo; spray-paint gesture and graffiti words; rotated vertical category labels; cut-out models on off-white; lip-shaped video mask.
Borrow only (1-2): Mask a video with a brand shape (lips) instead of a rectangle; Rotated vertical labels between cut-out products as category navigation
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: cut-out fashion shots on off-white plus moody editorial film
Reject: Cookie notice over all frames; Many type treatments at once
Token commitments: palette #FEFEFE, #040505, #1C1C27, #E4E1E1, #74716B; type Inter, Thunder, PP Fraktion Mono; engine GSAP + Lenis linked (never vendored).
