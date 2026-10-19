---
title: "Pelata Pieces - Finnish design games"
url: https://www.pelatapieces.com/
source_url: https://www.pelatapieces.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "editorial"
family: wood-toy-catalogue-grid
dna: "Design toys x orange cover, then a cream ruled grid where each wooden piece floats in 3D beside its name in coloured slab caps"
register: editorial print
grammar: gallery/catalog
lane: "A collection of wooden games: an orange cover with the pelata wordmark and a typewriter note, then a cream page ruled into a grid where each piece (a xylophone, a labyrinth, a backgammon board, mushroom skittles, a ring toss) rotates in 3D above its name and designer set in a different colour of slab caps, typewriter descriptions in two columns and a spec row of material and size."
mode: persuade
traits: ["cream ruled grid", "3D wooden objects rotating", "slab caps per product in its own colour", "typewriter body copy", "spec row"]
palette: ["#FEFCFB", "#E8E9E4", "#BFA372"]
type: ["ABCDailySlabMono", "BasteB", "GT Zirkon"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A strict grid with one turning object per product lets playful pieces feel collectible, like a catalogue page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- One turning object per catalogue entry inside a strict grid

## What to leave

- Long typewriter paragraphs

## Signature move

A wooden labyrinth turning above 'Sokkelo' in slab caps on a ruled cream grid.

## Motion

Intro: orange cover splits (~1 s). Wheel (Lenis, smoothed, WebGL): each object rotates as its row passes; names rise; grid lines draw.

Measured (`motion/probe.json`): Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 137 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the gallery/catalog grammar: a collection of wooden games: an orange cover with the pelata wordmark and a typewriter note, then a cream page ruled into a grid where each piece (a xylophone, a labyrinth, a backgammon board, mushroom skittles, a ring toss) rotates in 3D above its name and designer set in a different colour of slab caps, typewriter descriptions in two columns and a spec row of material and size. Type: ABCDailySlabMono, BasteB, GT Zirkon.
Ground and ink from the measured palette (#FEFCFB, #E8E9E4, #BFA372). Motion carries the page through
a wooden labyrinth turning above 'Sokkelo' in slab caps on a ruled cream grid. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL product models

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL product models

## Reference lock

Primary reference/direction: Pelata Pieces - Finnish design games — A collection of wooden games: an orange cover with the pelata wordmark and a typewriter note, then a cream page ruled into a grid where each piece (a xylophone, a labyrinth, a backgammon board, mushroom skittles, a ring toss) rotates in 3D above its name and designer set in a different colour of slab caps, typewriter descriptions in two columns and a spec row of material and size.
Preserve (3-5 traits): cream ruled grid; 3D wooden objects rotating; slab caps per product in its own colour; typewriter body copy; spec row.
Borrow only (1-2): One turning object per catalogue entry inside a strict grid
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL product models
Reject: Long typewriter paragraphs
Token commitments: palette #FEFCFB, #E8E9E4, #BFA372; type ABCDailySlabMono, BasteB, GT Zirkon; engine GSAP + Lenis linked (never vendored).
