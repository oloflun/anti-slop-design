---
title: "Cash App Tags - Wand"
url: https://cash.app/tags/wand
source_url: https://cash.app/tags/wand
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: single-object-webgl-toy
dna: "Fintech promo x one white 3D object on black that morphs from card to leaf to wand to star"
register: cinematic dark
grammar: filmic one-shot
lane: "A single promo for a tag: black screen, one small white WebGL object centred over 'Meet Cash App Wand', a white flash, then the object turns through shapes (a card, a leaf, a wand, a star-topped wand) as you scroll, with a legal line at the foot. Nothing else on the page."
mode: experience
traits: ["one object only", "black ground, white object", "shape morphs on scroll", "white flash cut", "tiny centred caption"]
palette: ["#000000", "#AAAAAA", "#FFFFFF", "#1D1D1D", "#393939", "#777777"]
type: ["Cash Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Reducing the page to one object that changes shape makes the product (a tag that becomes whatever you want) the whole story without a single paragraph.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Christophe Massolin, Index, Quentin Hocde).

## What to borrow (principle)

- Let one object change form as the only scroll event when the product is a single idea

## What to leave

- Caption too small to carry the message
- Long scroll for few states

## Signature move

A small white object on black turning from card to leaf to star-tipped wand.

## Motion

Intro: black, then the object fades in (~1 s); a white flash. Wheel (Lenis): the WebGL object morphs between shapes and rotates; the caption stays fixed.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Start over, Start over. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the filmic one-shot grammar: a single promo for a tag: black screen, one small white WebGL object centred over 'Meet Cash App Wand', a white flash, then the object turns through shapes (a card, a leaf, a wand, a star-topped wand) as you scroll, with a legal line at the foot. Nothing else on the page. Type: Cash Sans.
Ground and ink from the measured palette (#000000, #AAAAAA, #FFFFFF). Motion carries the page through
a small white object on black turning from card to leaf to star-tipped wand. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL object

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL object

## Reference lock

Primary reference/direction: Cash App Tags - Wand — A single promo for a tag: black screen, one small white WebGL object centred over 'Meet Cash App Wand', a white flash, then the object turns through shapes (a card, a leaf, a wand, a star-topped wand) as you scroll, with a legal line at the foot. Nothing else on the page.
Preserve (3-5 traits): one object only; black ground, white object; shape morphs on scroll; white flash cut; tiny centred caption.
Borrow only (1-2): Let one object change form as the only scroll event when the product is a single idea
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL object
Reject: Caption too small to carry the message; Long scroll for few states
Token commitments: palette #000000, #AAAAAA, #FFFFFF, #1D1D1D, #393939, #777777; type Cash Sans; engine GSAP + Lenis linked (never vendored).
