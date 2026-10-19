---
title: "Decor24 - Residential Interiors"
url: https://decor24.in/
source_url: https://decor24.in/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "hospitality"
family: cream-interiors-studio-serif
dna: "Indian interiors studio x cream ground, serif headings and a peony"
register: warm photographic
grammar: chaptered editorial
lane: "An interiors firm on cream: serif 'Crafting Bespoke Interiors for Residential Apartments', a hero image that grows to full width, a room list beside a dining photo, advantages and stats, a project grid, a process timeline with a peony that follows the steps, testimonials, FAQ and a large wordmark footer."
mode: persuade
traits: ["cream and butter yellow ground", "light serif headings with bracket tags", "hero image that grows", "room index beside photo", "peony as recurring object", "vertical process timeline"]
palette: ["#FFFDED", "#836D55", "#C7BCA7", "#E8E6D2"]
type: ["Space Grotesk", "Spectral"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The peony gives a conventional services page one recurring object, and the image that grows from card to full width is the one strong scroll moment.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Grow the hero image from a card to full bleed
- One recurring natural object along a timeline

## What to leave

- Low contrast pale text
- Generic stats and FAQ

## Signature move

A peony that follows the process timeline down a cream page.

## Motion

Intro: cream with the headline fading in (~1.5 s). Wheel (ScrollSmoother ~170 px glide, 3 pins): the hero image grows to full width and pins; the room list highlights as rooms pass; stat numbers count up; project tiles slide in pairs; the peony drifts beside the timeline as steps reveal; FAQ rows stagger in.

Measured (`motion/probe.json`): GSAP 3.15.0; 12 ScrollTriggers; 3 pinned sections; Lenis; 2 video; smoothed scroll (median 163 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: an interiors firm on cream: serif 'Crafting Bespoke Interiors for Residential Apartments', a hero image that grows to full width, a room list beside a dining photo, advantages and stats, a project grid, a process timeline with a peony that follows the steps, testimonials, FAQ and a large wordmark footer. Type: Space Grotesk, Spectral.
Ground and ink from the measured palette (#FFFDED, #836D55, #C7BCA7). Motion carries the page through
a peony that follows the process timeline down a cream page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — interior photography, peony cut-out

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: interior photography, peony cut-out

## Reference lock

Primary reference/direction: Decor24 - Residential Interiors — An interiors firm on cream: serif 'Crafting Bespoke Interiors for Residential Apartments', a hero image that grows to full width, a room list beside a dining photo, advantages and stats, a project grid, a process timeline with a peony that follows the steps, testimonials, FAQ and a large wordmark footer.
Preserve (3-5 traits): cream and butter yellow ground; light serif headings with bracket tags; hero image that grows; room index beside photo; peony as recurring object.
Borrow only (1-2): Grow the hero image from a card to full bleed; One recurring natural object along a timeline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: interior photography, peony cut-out
Reject: Low contrast pale text; Generic stats and FAQ
Token commitments: palette #FFFDED, #836D55, #C7BCA7, #E8E6D2; type Space Grotesk, Spectral; engine GSAP + Lenis linked (never vendored).
