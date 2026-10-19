---
title: "Tomoya Okada - portfolio v6"
url: https://v6.usestate.org/
source_url: https://v6.usestate.org/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: version-badge-monochrome-folio
dna: "Frontend engineer x a 'VER.6' ID badge and monochrome mockup photography"
register: modern clean
grammar: chaptered editorial
lane: "A developer folio: '(VER.6)' types in, an ID badge on a lanyard, a photo of a black notebook stamped 'VER.6' on a chair that grows to full screen with the bio, a dark technology section with small 3D objects, and selected works as laptop mockups in soft-light rooms."
mode: read
traits: ["version number as identity", "ID badge object", "notebook photo growing to full bleed", "monochrome", "3D tech objects", "laptop mockups in rooms"]
palette: ["#EFEFEF", "#7A7C7A", "#D4D4D4", "#2A2D2C", "#919392", "#4F514F"]
type: ["Figtree", "Lato"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Treating the site as version 6 of a product, with badge and notebook stamped VER.6, gives a personal folio a clear concept.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stamp the version number on physical objects as the identity

## What to leave

- Small text

## Signature move

A black notebook stamped 'VER.6' on a chair.

## Motion

Intro: white, '(VER.6)' types and scales (~2 s), the badge drops in. Wheel: the notebook photo grows to fill the screen; the bio fades in; the dark section rises; objects rotate; mockup photos slide in pairs.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; Barba page transitions; 1 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a developer folio: '(VER.6)' types in, an ID badge on a lanyard, a photo of a black notebook stamped 'VER.6' on a chair that grows to full screen with the bio, a dark technology section with small 3D objects, and selected works as laptop mockups in soft-light rooms. Type: Figtree, Lato.
Ground and ink from the measured palette (#EFEFEF, #7A7C7A, #D4D4D4). Motion carries the page through
a black notebook stamped 'VER.6' on a chair. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product photography, 3D objects

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product photography, 3D objects

## Reference lock

Primary reference/direction: Tomoya Okada - portfolio v6 — A developer folio: '(VER.6)' types in, an ID badge on a lanyard, a photo of a black notebook stamped 'VER.6' on a chair that grows to full screen with the bio, a dark technology section with small 3D objects, and selected works as laptop mockups in soft-light rooms.
Preserve (3-5 traits): version number as identity; ID badge object; notebook photo growing to full bleed; monochrome; 3D tech objects.
Borrow only (1-2): Stamp the version number on physical objects as the identity
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product photography, 3D objects
Reject: Small text
Token commitments: palette #EFEFEF, #7A7C7A, #D4D4D4, #2A2D2C, #919392, #4F514F; type Figtree, Lato; engine GSAP + Lenis linked (never vendored).
