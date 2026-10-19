---
title: "Millemann Wines"
url: https://millemannwines.fr/
source_url: https://millemannwines.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: ""
family: black-terroir-webgl
dna: "Winemaker manifesto x scanned-rock WebGL"
register: cinematic dark
grammar: continuous world
lane: "A black void where a scanned slab of limestone drifts diagonally through frame under a thin serif 'Imaginer & Composer', and the wheel dissolves the rock into scattered points of light."
mode: experience
traits: ["pure black ground", "photogrammetry rock as the only image", "thin high-contrast serif with ampersand flourish", "vertical side rail nav", "particle dissolve on scroll"]
palette: ["#000000", "#151515", "#313131", "#5D5D5D", "#8B8B8B"]
type: ["Sackers Gothic Std", "SangBleu Sunrise"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Everything is subtracted except the terroir: one scanned stone lit from above, a serif headline set small and centred, a hairline vertical rail. The wheel never moves the window; it moves the camera, so scrolling feels like travelling through the material rather than down a page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Index Studio, Quentin Hocdé).

## What to borrow (principle)

- Let the brand's raw material be the only image and give it real 3D form
- Scroll drives a camera/time value, not a document offset, when the page is a world rather than a list
- Fade headline letters in out of blur at different speeds so the line assembles

## What to leave

- The dissolve leaves several viewports of near-empty black with a few dots: orientation is lost
- Virtual scroll with no visible progress

## Signature move

A scanned limestone slab that scroll turns into a starfield.

## Motion

Intro: black, then the serif headline assembles letter by letter out of blur while the rock fades up behind it (~2.5 s). Scroll (virtual, window stays at 0): the rock slides diagonally up and out, the headline fades, the rock breaks into sparse points that drift like stars. Side rail stays fixed throughout.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x7; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a black void where a scanned slab of limestone drifts diagonally through frame under a thin serif 'Imaginer & Composer', and the wheel dissolves the rock into scattered points of light. Type: Sackers Gothic Std, SangBleu Sunrise.
Ground and ink from the measured palette (#000000, #151515, #313131). Motion carries the page through
a scanned limestone slab that scroll turns into a starfield. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — photogrammetry or macro of the actual soil/stone, top light, pure black surround

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: photogrammetry or macro of the actual soil/stone, top light, pure black surround

## Reference lock

Primary reference/direction: Millemann Wines — A black void where a scanned slab of limestone drifts diagonally through frame under a thin serif 'Imaginer & Composer', and the wheel dissolves the rock into scattered points of light.
Preserve (3-5 traits): pure black ground; photogrammetry rock as the only image; thin high-contrast serif with ampersand flourish; vertical side rail nav; particle dissolve on scroll.
Borrow only (1-2): Let the brand's raw material be the only image and give it real 3D form; Scroll drives a camera/time value, not a document offset, when the page is a world rather than a list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: photogrammetry or macro of the actual soil/stone, top light, pure black surround
Reject: The dissolve leaves several viewports of near-empty black with a few dots: orientation is lost; Virtual scroll with no visible progress
Token commitments: palette #000000, #151515, #313131, #5D5D5D, #8B8B8B; type Sackers Gothic Std, SangBleu Sunrise; engine GSAP + Lenis linked (never vendored).
