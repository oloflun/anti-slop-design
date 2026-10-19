---
title: "Thomas Thorstensson - Portfolio"
url: https://www.thomasthorstensson.com/
source_url: https://www.thomasthorstensson.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: moon-white-dev-folio
dna: "Creative developer x a 3D moon over a white editorial folio"
register: modern clean
grammar: chaptered editorial
lane: "A creative developer's folio: 'Creative Developer' on white, a black band with a 3D moon rising under 'About', then staggered project thumbnails on white, an awards logo row, a 'Knowledge' section with black panels (data visualisation particles, UI/UX with a NEXT button) and a folio stack."
mode: read
traits: ["3D moon in a black band", "plain grotesk on white", "staggered project thumbnails", "awards logo row", "particle data-vis panel", "quiet minimal type"]
palette: ["#FAFAFA", "#1B1B1B", "#3E4155", "#A6ACA9"]
type: ["TWK Everett", "Switzer", "Cascadia Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The single black band with the moon is the event of the page; everything else stays white and quiet, which makes it feel deliberate.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One dark band with a 3D object in an otherwise white folio
- Stagger thumbnails left and right with lots of air

## What to leave

- Small captions
- Knowledge panels feel like demos

## Signature move

A 3D moon rising in a black band on a white folio.

## Motion

Intro: white with a thin loading line (~2 s), the title reveals. Wheel (Lenis ~140 px glide, 1 pin): the black band slides up and the moon rises and rotates; thumbnails enter alternating sides with a slight scale; award logos scroll; knowledge panels pin while particles form shapes.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; WebGL canvas x3 (three.js); split text; smoothed scroll (median 144 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a creative developer's folio: 'Creative Developer' on white, a black band with a 3D moon rising under 'About', then staggered project thumbnails on white, an awards logo row, a 'Knowledge' section with black panels (data visualisation particles, UI/UX with a NEXT button) and a folio stack. Type: TWK Everett, Switzer, Cascadia Mono.
Ground and ink from the measured palette (#FAFAFA, #1B1B1B, #3E4155). Motion carries the page through
a 3D moon rising in a black band on a white folio. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL moon, project thumbnails

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL moon, project thumbnails

## Reference lock

Primary reference/direction: Thomas Thorstensson - Portfolio — A creative developer's folio: 'Creative Developer' on white, a black band with a 3D moon rising under 'About', then staggered project thumbnails on white, an awards logo row, a 'Knowledge' section with black panels (data visualisation particles, UI/UX with a NEXT button) and a folio stack.
Preserve (3-5 traits): 3D moon in a black band; plain grotesk on white; staggered project thumbnails; awards logo row; particle data-vis panel.
Borrow only (1-2): One dark band with a 3D object in an otherwise white folio; Stagger thumbnails left and right with lots of air
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL moon, project thumbnails
Reject: Small captions; Knowledge panels feel like demos
Token commitments: palette #FAFAFA, #1B1B1B, #3E4155, #A6ACA9; type TWK Everett, Switzer, Cascadia Mono; engine GSAP + Lenis linked (never vendored).
