---
title: "Codapress Publishing"
url: https://codapress.co.uk/
source_url: https://codapress.co.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: ""
family: mono-smoke-tech-publisher
dna: "Technical book publisher x mono type and grey smoke"
register: cinematic dark
grammar: chaptered editorial
lane: "A technical publisher in JetBrains Mono on black: a grey smoke field under 'ACCELERATING TECHNICAL KNOWLEDGE' set in three offset lines, a draggable shelf of colourful book covers, and articles with drawn line illustrations."
mode: read
traits: ["monospace throughout", "grey smoke/halftone hero", "three offset headline lines", "draggable book-cover shelf", "line-drawn article thumbnails", "scrambled placeholder text reveals"]
palette: ["#000000", "#393A39", "#1C1C1C", "#504F4E", "#C0D5DE", "#767773"]
type: ["JetBrains Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Only the books have colour: everything else is mono type, black and a grey smoke texture, so the covers on the draggable shelf read as the product immediately. Text reveals scramble through random characters before settling, which suits a technical audience.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Keep the page monochrome so the product (covers) is the only colour
- Scramble text into place for a technical brand
- A draggable shelf for a short product list

## What to leave

- Scrambled placeholder frames read as broken text
- Empty 'Latest release' panel while loading

## Signature move

Book covers on a draggable shelf as the only colour on a mono page.

## Motion

Intro: white with a logo, cut to the black smoke hero; the three headline lines settle with offset (~2 s). Scroll (Lenis, ~140 px glide, DrawSVG, Draggable/Inertia, ScrambleText): body text scrambles in; the book shelf slides in and can be dragged with inertia; articles grid with line illustrations drawing.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x2; split text; smoothed scroll (median 139 px still travelling after input stops); entry gate: Decline cookies. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a technical publisher in JetBrains Mono on black: a grey smoke field under 'ACCELERATING TECHNICAL KNOWLEDGE' set in three offset lines, a draggable shelf of colourful book covers, and articles with drawn line illustrations. Type: JetBrains Mono.
Ground and ink from the measured palette (#000000, #393A39, #1C1C1C). Motion carries the page through
book covers on a draggable shelf as the only colour on a mono page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — bright book covers on black; line drawings

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: bright book covers on black; line drawings

## Reference lock

Primary reference/direction: Codapress Publishing — A technical publisher in JetBrains Mono on black: a grey smoke field under 'ACCELERATING TECHNICAL KNOWLEDGE' set in three offset lines, a draggable shelf of colourful book covers, and articles with drawn line illustrations.
Preserve (3-5 traits): monospace throughout; grey smoke/halftone hero; three offset headline lines; draggable book-cover shelf; line-drawn article thumbnails.
Borrow only (1-2): Keep the page monochrome so the product (covers) is the only colour; Scramble text into place for a technical brand
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: bright book covers on black; line drawings
Reject: Scrambled placeholder frames read as broken text; Empty 'Latest release' panel while loading
Token commitments: palette #000000, #393A39, #1C1C1C, #504F4E, #C0D5DE, #767773; type JetBrains Mono; engine GSAP + Lenis linked (never vendored).
