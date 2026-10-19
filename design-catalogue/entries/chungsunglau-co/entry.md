---
title: "Chung-Sung Lau (Jawns)"
url: https://chungsunglau.co.uk/
source_url: https://chungsunglau.co.uk/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: zoomable-canvas-folio
dna: "Product designer folio x zoomable infinite canvas"
register: cinematic dark
grammar: live surface
lane: "A dark canvas folio: a small profile card sits at the centre and project cards (sneakers, posters, screens) float around it on an infinite board you pan and zoom, with bracketed controls '[ reset cam ] [ zoom in ] [ zoom out ]'."
mode: operate
traits: ["infinite pan/zoom canvas", "project cards scattered around a profile card", "bracketed mono controls", "pixel/grid display font", "marquee of skills along the bottom"]
palette: ["#17161B", "#3E4154", "#9CA0B2"]
type: ["Spacegrotesk", "BitcountGridSingle"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The folio is a moodboard you navigate rather than a page you scroll: everything is on one board, and the camera controls are the navigation. It suits a designer whose work is many small objects.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Chung-Sung Lau).

## What to borrow (principle)

- A pan-and-zoom board for a body of small, varied work
- Explicit camera controls in brackets so the interaction is discoverable

## What to leave

- The wheel zooms rather than scrolls, which surprises
- Cards are small at the default zoom

## Signature move

A profile card at the centre of an infinite board of floating project cards with bracketed camera controls.

## Motion

Intro: tiny loader text, then cards fly in to scattered positions around the profile card (~1.5 s). Interaction (Observer): drag pans the board, wheel zooms; cards drift slightly at idle; the skills marquee runs along the bottom.

Measured (`motion/probe.json`): GSAP 3.15.0; 6 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a dark canvas folio: a small profile card sits at the centre and project cards (sneakers, posters, screens) float around it on an infinite board you pan and zoom, with bracketed controls '[ reset cam ] [ zoom in ] [ zoom out ]'. Type: Spacegrotesk, BitcountGridSingle.
Ground and ink from the measured palette (#17161B, #3E4154, #9CA0B2). Motion carries the page through
a profile card at the centre of an infinite board of floating project cards with bracketed camera controls. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product shots and posters as small cards on near-black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product shots and posters as small cards on near-black

## Reference lock

Primary reference/direction: Chung-Sung Lau (Jawns) — A dark canvas folio: a small profile card sits at the centre and project cards (sneakers, posters, screens) float around it on an infinite board you pan and zoom, with bracketed controls '[ reset cam ] [ zoom in ] [ zoom out ]'.
Preserve (3-5 traits): infinite pan/zoom canvas; project cards scattered around a profile card; bracketed mono controls; pixel/grid display font; marquee of skills along the bottom.
Borrow only (1-2): A pan-and-zoom board for a body of small, varied work; Explicit camera controls in brackets so the interaction is discoverable
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product shots and posters as small cards on near-black
Reject: The wheel zooms rather than scrolls, which surprises; Cards are small at the default zoom
Token commitments: palette #17161B, #3E4154, #9CA0B2; type Spacegrotesk, BitcountGridSingle; engine GSAP + Lenis linked (never vendored).
