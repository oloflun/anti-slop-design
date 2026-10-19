---
title: "Hubcycle - Upcycled ingredients"
url: https://www.hubcycled.com/
source_url: https://www.hubcycled.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: upcycled-ingredient-b2b
dna: "Upcycled food ingredients x wireframe globes and floating ingredient cards"
register: modern clean
grammar: chaptered editorial
lane: "A B2B ingredients marketplace: 'We turn what's left' in coral with a wireframe globe, floating ingredient cards (tomato, peanut, vanilla), top products on a dark teal band, a contact form, 'More profits. Positive impact.' and a giant 'UNUSED' footer word sliding."
mode: persuade
traits: ["coral display type", "wireframe globe drawings", "floating ingredient cards", "dark teal bands", "contact form mid-page", "giant footer word"]
palette: ["#F2F2F2", "#0E1F25", "#004250", "#A29992"]
type: ["Ppvalve", "Manrope"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Floating ingredient cards give a dry B2B catalogue a sense of physical goods.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Float product cards around a headline

## What to leave

- Form in the middle of the story
- Generic layout

## Signature move

Ingredient cards floating around a coral headline and a wireframe globe.

## Motion

Intro: the headline with cards (Discover gate clicked). Wheel (native, 30 triggers): cards drift up past the headline; the dark band rises; product tiles slide; the form scales in; the footer word slides sideways.

Measured (`motion/probe.json`): GSAP 3.15.0; 30 ScrollTriggers; entry gate: Discover our portfolio. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a B2B ingredients marketplace: 'We turn what's left' in coral with a wireframe globe, floating ingredient cards (tomato, peanut, vanilla), top products on a dark teal band, a contact form, 'More profits. Positive impact.' and a giant 'UNUSED' footer word sliding. Type: Ppvalve, Manrope.
Ground and ink from the measured palette (#F2F2F2, #0E1F25, #004250). Motion carries the page through
ingredient cards floating around a coral headline and a wireframe globe. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — ingredient cut-outs, line drawings

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: ingredient cut-outs, line drawings

## Reference lock

Primary reference/direction: Hubcycle - Upcycled ingredients — A B2B ingredients marketplace: 'We turn what's left' in coral with a wireframe globe, floating ingredient cards (tomato, peanut, vanilla), top products on a dark teal band, a contact form, 'More profits. Positive impact.' and a giant 'UNUSED' footer word sliding.
Preserve (3-5 traits): coral display type; wireframe globe drawings; floating ingredient cards; dark teal bands; contact form mid-page.
Borrow only (1-2): Float product cards around a headline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: ingredient cut-outs, line drawings
Reject: Form in the middle of the story; Generic layout
Token commitments: palette #F2F2F2, #0E1F25, #004250, #A29992; type Ppvalve, Manrope; engine GSAP + Lenis linked (never vendored).
