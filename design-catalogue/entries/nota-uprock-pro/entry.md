---
title: "NŌTA - smart pen"
url: https://nota.uprock.pro/
source_url: https://nota.uprock.pro/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: pen-macro-product-page
dna: "Smart pen x a macro of a fountain pen and colour backdrops per finish"
register: modern clean
grammar: chaptered editorial
lane: "A product page: a percent counter on grey, 'Smart pen for real thinking' in thin serif beside a chrome pen nib, 'Nota pen Specifications' with the pen standing upright, a black stepped wipe, a statement paragraph on black, the pen at macro, a notebook ('Looks like paper. Works like a system'), handwriting syncing to a phone, 'Inside the box', a pen nib through an oval mask, and the pen standing in different finishes on colour gradients ('Graphite Black. Clarity in silence.', 'Bright Orange. Steady focus.')."
mode: persuade
traits: ["thin serif titles", "pen macro shots", "stepped black wipe", "oval mask", "finish per gradient backdrop", "phrase split around the pen"]
palette: ["#FFFFFF", "#010101", "#8C9298", "#494C52", "#6C6F76", "#353638"]
type: ["Instrument Serif", "Inter", "YS Text"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Splitting each phrase around the upright pen ('Impossible to | overthink') makes the product the hinge of the sentence.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Uprock).

## What to borrow (principle)

- Split the line around the standing product
- One gradient backdrop per finish

## What to leave

- Small spec text

## Signature move

'Bright Orange. | Steady focus.' split around an upright orange pen.

## Motion

Intro: grey percent counter (~2 s), the pen slides in. Wheel (Lenis): the pen rotates upright; a stepped black wipe; text fades; macro shots scale; the notebook opens; the phone syncs; the oval mask reveals the nib; finishes swap with the backdrop.

Measured (`motion/probe.json`): GSAP 3.14.2/3.14.2/3.14.2; Lenis; 4 video; smoothed scroll (median 139 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a product page: a percent counter on grey, 'Smart pen for real thinking' in thin serif beside a chrome pen nib, 'Nota pen Specifications' with the pen standing upright, a black stepped wipe, a statement paragraph on black, the pen at macro, a notebook ('Looks like paper. Works like a system'), handwriting syncing to a phone, 'Inside the box', a pen nib through an oval mask, and the pen standing in different finishes on colour gradients ('Graphite Black. Clarity in silence.', 'Bright Orange. Steady focus.'). Type: Instrument Serif, Inter, YS Text.
Ground and ink from the measured palette (#FFFFFF, #010101, #8C9298). Motion carries the page through
'Bright Orange. | Steady focus.' split around an upright orange pen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product renders

## Reference lock

Primary reference/direction: NŌTA - smart pen — A product page: a percent counter on grey, 'Smart pen for real thinking' in thin serif beside a chrome pen nib, 'Nota pen Specifications' with the pen standing upright, a black stepped wipe, a statement paragraph on black, the pen at macro, a notebook ('Looks like paper. Works like a system'), handwriting syncing to a phone, 'Inside the box', a pen nib through an oval mask, and the pen standing in different finishes on colour gradients ('Graphite Black. Clarity in silence.', 'Bright Orange. Steady focus.').
Preserve (3-5 traits): thin serif titles; pen macro shots; stepped black wipe; oval mask; finish per gradient backdrop.
Borrow only (1-2): Split the line around the standing product; One gradient backdrop per finish
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product renders
Reject: Small spec text
Token commitments: palette #FFFFFF, #010101, #8C9298, #494C52, #6C6F76, #353638; type Instrument Serif, Inter, YS Text; engine GSAP + Lenis linked (never vendored).
