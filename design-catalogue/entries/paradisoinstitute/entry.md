---
title: "Paradiso Institute"
url: https://paradisoinstitute.org/
source_url: https://paradisoinstitute.org/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: pixel-manifesto-leaf-object
dna: "Art institute x a slowly turning 3D cut-paper leaf over a manifesto in pale pixel type"
register: editorial print
grammar: typographic poster
lane: "A manifesto page behind a 'Play!' gate: 'Institute' spaced wide over a pale brush wordmark, a webcam-like thumbnail in the corner, then a single 3D cut-paper leaf form turning and unfolding in the centre while a long manifesto in pale grey pixel capitals scrolls past behind it (before reason, before certainty, there is something that is not gentle; like leaves becoming dirt and mycelium), green status chips at the edges."
mode: experience
traits: ["play gate", "3D cut-paper leaf turning", "pale pixel-font manifesto", "tiny green status chips", "near-white everything"]
palette: ["#FFFFFF", "#9FA9A2"]
type: ["Paradiso", "ThermaL", "ThermaM", "Helv"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One object turning steadily in front of slow text sets the reading pace of the manifesto; the page is a meditation, not a brochure.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: SILENCIO).

## What to borrow (principle)

- Hold one slow object in the centre to pace a long text

## What to leave

- Manifesto contrast too low to read

## Signature move

A cut-paper leaf form turning in front of pale pixel capitals.

## Motion

Intro: gate, wordmark (~2 s). Wheel: the leaf rotates and folds continuously in WebGL while the manifesto translates up; chips blink.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: PLAY!, PLAY!. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the typographic poster grammar: a manifesto page behind a 'Play!' gate: 'Institute' spaced wide over a pale brush wordmark, a webcam-like thumbnail in the corner, then a single 3D cut-paper leaf form turning and unfolding in the centre while a long manifesto in pale grey pixel capitals scrolls past behind it (before reason, before certainty, there is something that is not gentle; like leaves becoming dirt and mycelium), green status chips at the edges. Type: Paradiso, ThermaL, ThermaM, Helv.
Ground and ink from the measured palette (#FFFFFF, #9FA9A2). Motion carries the page through
a cut-paper leaf form turning in front of pale pixel capitals. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL paper object

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL paper object

## Reference lock

Primary reference/direction: Paradiso Institute — A manifesto page behind a 'Play!' gate: 'Institute' spaced wide over a pale brush wordmark, a webcam-like thumbnail in the corner, then a single 3D cut-paper leaf form turning and unfolding in the centre while a long manifesto in pale grey pixel capitals scrolls past behind it (before reason, before certainty, there is something that is not gentle; like leaves becoming dirt and mycelium), green status chips at the edges.
Preserve (3-5 traits): play gate; 3D cut-paper leaf turning; pale pixel-font manifesto; tiny green status chips; near-white everything.
Borrow only (1-2): Hold one slow object in the centre to pace a long text
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL paper object
Reject: Manifesto contrast too low to read
Token commitments: palette #FFFFFF, #9FA9A2; type Paradiso, ThermaL, ThermaM, Helv; engine GSAP + Lenis linked (never vendored).
