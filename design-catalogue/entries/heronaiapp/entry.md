---
title: "Heron AI - architecture compliance dashboard"
url: https://heronaiapp.com/
source_url: https://heronaiapp.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: blueprint-line-drawing-saas
dna: "Architecture AI x line drawings that draw themselves and red approval tiles"
register: editorial print
grammar: chaptered editorial
lane: "A SaaS page on drafting-paper cream: a building elevation drawing itself line by line, 'See every change, flag and approval in one place' with dashboard UI over a mountain photo, client logos, 'Full oversight, no digging around' with tabbed features where a building model, floor plans and a section drawing animate (a room filling red to approve or reject, change records stacking, approvers on a section), 'From activity to oversight, in 3 steps' and FAQ."
mode: persuade
traits: ["line drawings drawing themselves", "drafting cream ground", "red accent fills", "tabbed feature panel", "floor plans and sections", "caps grotesk"]
palette: ["#F6F5EC", "#D8D6CF", "#846A60"]
type: ["Geistmono", "BT Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Using the users' own medium (line drawings, plans) as the motion material makes the product feel native to architects.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Bearplus).

## What to borrow (principle)

- Draw the customer's own medium as the motion

## What to leave

- Cookie bar

## Signature move

A building elevation drawing itself line by line.

## Motion

Intro: cream with lines drawing an elevation (~3 s). Wheel: the hero UI slides; tabs advance with the scroll; the model rotates; a room fills red; plans draw; records stack; the section drawing shows approvers.

Measured (`motion/probe.json`): GSAP 3.12.5; 39 ScrollTriggers; Barba page transitions; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: DISCOVER MORE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a SaaS page on drafting-paper cream: a building elevation drawing itself line by line, 'See every change, flag and approval in one place' with dashboard UI over a mountain photo, client logos, 'Full oversight, no digging around' with tabbed features where a building model, floor plans and a section drawing animate (a room filling red to approve or reject, change records stacking, approvers on a section), 'From activity to oversight, in 3 steps' and FAQ. Type: Geistmono, BT Grotesk.
Ground and ink from the measured palette (#F6F5EC, #D8D6CF, #846A60). Motion carries the page through
a building elevation drawing itself line by line. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — line drawings, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: line drawings, UI

## Reference lock

Primary reference/direction: Heron AI - architecture compliance dashboard — A SaaS page on drafting-paper cream: a building elevation drawing itself line by line, 'See every change, flag and approval in one place' with dashboard UI over a mountain photo, client logos, 'Full oversight, no digging around' with tabbed features where a building model, floor plans and a section drawing animate (a room filling red to approve or reject, change records stacking, approvers on a section), 'From activity to oversight, in 3 steps' and FAQ.
Preserve (3-5 traits): line drawings drawing themselves; drafting cream ground; red accent fills; tabbed feature panel; floor plans and sections.
Borrow only (1-2): Draw the customer's own medium as the motion
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: line drawings, UI
Reject: Cookie bar
Token commitments: palette #F6F5EC, #D8D6CF, #846A60; type Geistmono, BT Grotesk; engine GSAP + Lenis linked (never vendored).
