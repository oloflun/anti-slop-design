---
title: "TRIONN"
url: https://trionn.com/
source_url: https://trionn.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: shard-dark-to-light-agency
dna: "Indian design studio x floating glass shards and Swiss sans"
register: modern clean
grammar: chaptered editorial
lane: "A studio page that assembles its logo from dots on grey, falls into a dark field of drifting glass shards under 'Designed to mean something', runs a horizontal 'IMPACT · INSPIRE · INNOVATE' band, then wipes to white through horizontal bars for key facts and work cards."
mode: persuade
traits: ["dots that assemble the logo", "floating 3D shards in the dark", "Neue Haas Grotesk at large light sizes", "horizontal word band", "horizontal bar wipe from dark to light", "lion-mascot key-facts cards"]
palette: ["#0C0C0C", "#6E6E6E"]
type: ["neueHaas", "martianMono", "familjen"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The transition from the dark brand chapter to the white business chapter is made with horizontal bars that slide across like blinds, so the change of ground has a cause. The shards in the dark section give depth without imagery.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: TRIONN, Trionn).

## What to borrow (principle)

- Switch dark to light through horizontal bars sliding across
- Drifting abstract 3D fragments as the dark hero's texture
- A horizontal values band as a bridge between chapters

## What to leave

- Generic large light sans statements
- Small text in the work cards

## Signature move

Horizontal bars wiping the dark shard field into the white key-facts page.

## Motion

Intro: scattered dots on grey join into the logo mark (~1 s). Scroll (Lenis, ~125 px glide, 4 pins, three.js): dark hero with shards drifting; statement lines reveal over the shards; 'IMPACT + INSPIRE + INNOVATE' runs horizontally; horizontal bars sweep across to white; 'Key facts' with cards tilting in; logos; 'Selected work & explorations' with cards sliding from the right.

Measured (`motion/probe.json`): GSAP 3.15.0; 4 pinned sections; Lenis; WebGL canvas x1 (three.js); 6 video; smoothed scroll (median 142 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a studio page that assembles its logo from dots on grey, falls into a dark field of drifting glass shards under 'Designed to mean something', runs a horizontal 'IMPACT · INSPIRE · INNOVATE' band, then wipes to white through horizontal bars for key facts and work cards. Type: neueHaas, martianMono, familjen.
Ground and ink from the measured palette (#0C0C0C, #6E6E6E). Motion carries the page through
horizontal bars wiping the dark shard field into the white key-facts page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — abstract glass 3D fragments; campaign visuals for work cards

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: abstract glass 3D fragments; campaign visuals for work cards

## Reference lock

Primary reference/direction: TRIONN — A studio page that assembles its logo from dots on grey, falls into a dark field of drifting glass shards under 'Designed to mean something', runs a horizontal 'IMPACT · INSPIRE · INNOVATE' band, then wipes to white through horizontal bars for key facts and work cards.
Preserve (3-5 traits): dots that assemble the logo; floating 3D shards in the dark; Neue Haas Grotesk at large light sizes; horizontal word band; horizontal bar wipe from dark to light.
Borrow only (1-2): Switch dark to light through horizontal bars sliding across; Drifting abstract 3D fragments as the dark hero's texture
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: abstract glass 3D fragments; campaign visuals for work cards
Reject: Generic large light sans statements; Small text in the work cards
Token commitments: palette #0C0C0C, #6E6E6E; type neueHaas, martianMono, familjen; engine GSAP + Lenis linked (never vendored).
