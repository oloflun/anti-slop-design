---
title: "Unseen Studio - Year in Review 2025"
url: https://2025.unseen.co/
source_url: https://2025.unseen.co/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: year-review-month-timeline
dna: "Studio year review x 'Twenty Twenty Five' on a pixel eye, then a white timeline of months in mixed serif with a flying mascot along a drawn line"
register: editorial print
grammar: chaptered editorial
lane: "A studio's year in review: a winged mascot loader, a pixel-dot eye with 'Twenty Twenty' in yellow condensed type, 'Year in Review / Twenty Twenty Five', then a white page where each month ('January', 'February') is set in a mixed swash serif and a little winged mascot flies along a drawn line past project frames (Netflix concept, motion explorations, a sneaker render, L'Oréal 'Salon of the Future', a rose)."
mode: read
traits: ["months in swash serif", "mascot flying along a drawn line", "pixel eye intro", "project frames per month"]
palette: ["#E2E2E2", "#0C0C0C", "#BEAD71", "#371A14"]
type: ["DM Mono", "Bootzy Condensed TM", "Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

A mascot flying a line through the months turns an archive into a journey through the year.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Unseen Studio®).

## What to borrow (principle)

- Let a small character travel the timeline line

## What to leave

- Captions very small

## Signature move

A winged mascot flying along a line past the month titles.

## Motion

Intro: pixel eye with yellow title (~3 s). Wheel (Lenis): horizontal-feeling timeline; the line draws and the mascot follows; frames scale in.

Measured (`motion/probe.json`): GSAP 3.14.2; Taxi page transitions; WebGL canvas x1 (three.js); 32 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a studio's year in review: a winged mascot loader, a pixel-dot eye with 'Twenty Twenty' in yellow condensed type, 'Year in Review / Twenty Twenty Five', then a white page where each month ('January', 'February') is set in a mixed swash serif and a little winged mascot flies along a drawn line past project frames (Netflix concept, motion explorations, a sneaker render, L'Oréal 'Salon of the Future', a rose). Type: DM Mono, Bootzy Condensed TM, Neue Montreal.
Ground and ink from the measured palette (#E2E2E2, #0C0C0C, #BEAD71). Motion carries the page through
a winged mascot flying along a line past the month titles. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project imagery, 3D renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project imagery, 3D renders

## Reference lock

Primary reference/direction: Unseen Studio - Year in Review 2025 — A studio's year in review: a winged mascot loader, a pixel-dot eye with 'Twenty Twenty' in yellow condensed type, 'Year in Review / Twenty Twenty Five', then a white page where each month ('January', 'February') is set in a mixed swash serif and a little winged mascot flies along a drawn line past project frames (Netflix concept, motion explorations, a sneaker render, L'Oréal 'Salon of the Future', a rose).
Preserve (3-5 traits): months in swash serif; mascot flying along a drawn line; pixel eye intro; project frames per month.
Borrow only (1-2): Let a small character travel the timeline line
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project imagery, 3D renders
Reject: Captions very small
Token commitments: palette #E2E2E2, #0C0C0C, #BEAD71, #371A14; type DM Mono, Bootzy Condensed TM, Neue Montreal; engine GSAP + Lenis linked (never vendored).
