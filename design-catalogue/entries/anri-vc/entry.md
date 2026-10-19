---
title: "Changer Capital ANRI"
url: https://anri.vc/
source_url: https://anri.vc/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: 3d-letter-sculpture-vc
dna: "Japanese VC x a sculptural 3D wordmark among floating shapes that recolour per section"
register: modern clean
grammar: live surface
lane: "A venture capital firm: a dotted circle loader with a percent, then a grey studio space where 'ANRI' is a chrome 3D sculpture of tubes surrounded by floating shapes, and each section (Home, We Are, Team, Projects) recolours the shapes (grey, red/purple, navy, green) while a pill nav and Prev/Next buttons switch them."
mode: experience
traits: ["chrome 3D wordmark", "floating shapes recoloured per section", "grey studio ground", "Prev/Next buttons", "pill nav with 'story of'", "dotted circle loader"]
palette: ["#000000", "#B2B2B2", "#D8D8D8", "#2C1513", "#7A777A"]
type: ["polySansWide"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The wordmark is the signature object, and recolouring the shapes around it per section gives a VC site a playful, gallery-like identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: FunTech, NEWPEACE).

## What to borrow (principle)

- Recolour the same 3D scene for each section

## What to leave

- Navigation hidden in small labels
- Little content per section

## Signature move

A chrome 'ANRI' sculpture among floating shapes that change colour per section.

## Motion

Intro: white, then black with a dotted circle loader and percent (~2 s). Virtual scroll: each step rotates the shapes and swaps their colour set while the section word slides; the wordmark turns and catches light.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the live surface grammar: a venture capital firm: a dotted circle loader with a percent, then a grey studio space where 'ANRI' is a chrome 3D sculpture of tubes surrounded by floating shapes, and each section (Home, We Are, Team, Projects) recolours the shapes (grey, red/purple, navy, green) while a pill nav and Prev/Next buttons switch them. Type: polySansWide.
Ground and ink from the measured palette (#000000, #B2B2B2, #D8D8D8). Motion carries the page through
a chrome 'ANRI' sculpture among floating shapes that change colour per section. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL 3D sculpture

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL 3D sculpture

## Reference lock

Primary reference/direction: Changer Capital ANRI — A venture capital firm: a dotted circle loader with a percent, then a grey studio space where 'ANRI' is a chrome 3D sculpture of tubes surrounded by floating shapes, and each section (Home, We Are, Team, Projects) recolours the shapes (grey, red/purple, navy, green) while a pill nav and Prev/Next buttons switch them.
Preserve (3-5 traits): chrome 3D wordmark; floating shapes recoloured per section; grey studio ground; Prev/Next buttons; pill nav with 'story of'.
Borrow only (1-2): Recolour the same 3D scene for each section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL 3D sculpture
Reject: Navigation hidden in small labels; Little content per section
Token commitments: palette #000000, #B2B2B2, #D8D8D8, #2C1513, #7A777A; type polySansWide; engine GSAP + Lenis linked (never vendored).
