---
title: "Pacôme Pertant"
url: http://pacomepertant.com/
source_url: http://pacomepertant.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: spiral-card-cloud-folio
dna: "Designer folio x spiral of bent cards"
register: illustrated dark
grammar: gallery/catalog
lane: "A dark folio that says 'hey' with a blue dot, morphs into a little logo, then spins all projects as bent colourful cards in a spiral that turns with the wheel, the active title appearing in a small label."
mode: experience
traits: ["blob/dot loader that morphs", "projects as bent cards in a spiral", "saturated illustrated work", "small floating title label", "rotating 'showreel' badge in the corner"]
palette: ["#0A0A0A", "#9CA697", "#2A2D3C"]
type: []
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The work is colourful illustration and motion; arranged as a spiral of bent cards, it reads as a single colourful object turning, with each card catching the light as it passes the front.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Arrange a varied illustrated body of work as a rotating spiral of bent cards
- A friendly morphing blob loader ('hey', 'I'm …')

## What to leave

- Wheel-only; no list
- Labels very small

## Signature move

A spiral of bent, colourful project cards turning in the dark.

## Motion

Intro: a blue dot says 'hey', morphs into 'I'm Pacôme', then a green planet dot (~2 s). Wheel (virtual, Lenis, WebGL): the spiral of cards turns; the front card's title label updates; cards bend as they pass.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: close, enter with sound. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the gallery/catalog grammar: a dark folio that says 'hey' with a blue dot, morphs into a little logo, then spins all projects as bent colourful cards in a spiral that turns with the wheel, the active title appearing in a small label. Type: read from the captures.
Ground and ink from the measured palette (#0A0A0A, #9CA697, #2A2D3C). Motion carries the page through
a spiral of bent, colourful project cards turning in the dark. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — colourful illustration and 3D motion stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: colourful illustration and 3D motion stills

## Reference lock

Primary reference/direction: Pacôme Pertant — A dark folio that says 'hey' with a blue dot, morphs into a little logo, then spins all projects as bent colourful cards in a spiral that turns with the wheel, the active title appearing in a small label.
Preserve (3-5 traits): blob/dot loader that morphs; projects as bent cards in a spiral; saturated illustrated work; small floating title label; rotating 'showreel' badge in the corner.
Borrow only (1-2): Arrange a varied illustrated body of work as a rotating spiral of bent cards; A friendly morphing blob loader ('hey', 'I'm …')
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: colourful illustration and 3D motion stills
Reject: Wheel-only; no list; Labels very small
Token commitments: palette #0A0A0A, #9CA697, #2A2D3C; type -; engine GSAP + Lenis linked (never vendored).
