---
title: "Antoine Wodniack - Creative Developer"
url: https://wodniack.dev/
source_url: https://wodniack.dev/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: red-grid-tunnel-dev
dna: "Creative developer x a red grid tunnel and a wall of WORK letters with projects inside"
register: other
grammar: chaptered editorial
lane: "A developer folio in red and black: a tiny barcode loader, a red room drawn as a perspective grid with a bio card, awards as a wall of stamps (Awwwards, FWA, GSAP SOTM, CSSDA), a pill 'WORK', then a black field of red condensed 'W O R K' letters in rows where project screenshots (Durance, Black Hole, Envision, a 404 page) pass between them, a 'CODING MY WAY SINCE 1987' poster on a tilted plane and a closing grid."
mode: experience
traits: ["red perspective grid room", "stamp wall of awards", "rows of WORK letters as a field", "project shots passing through the letters", "tilted poster type", "red and black only"]
palette: ["#F40C3F", "#180201", "#74071A", "#E0677B"]
type: ["Bigger Display", "Editorial New", "Fraktion Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Turning the section word into a repeating field that projects pass through makes the work list a texture, and the grid room is a strong world.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Antoine Wodniack).

## What to borrow (principle)

- Repeat the section word as a field and pass the projects through it

## What to leave

- Small bio text

## Signature move

Rows of red W O R K letters with project screenshots sliding between them.

## Motion

Intro: red with a small barcode (~2 s), a black bar sweeps. Wheel (Lenis): the room's grid moves in perspective; stamps pop on the wall; the WORK pill rotates; the letter field scrolls in rows at different speeds while projects slide through; the poster tilts on a plane; '1987' rises.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; 34 video; smoothed scroll (median 154 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a developer folio in red and black: a tiny barcode loader, a red room drawn as a perspective grid with a bio card, awards as a wall of stamps (Awwwards, FWA, GSAP SOTM, CSSDA), a pill 'WORK', then a black field of red condensed 'W O R K' letters in rows where project screenshots (Durance, Black Hole, Envision, a 404 page) pass between them, a 'CODING MY WAY SINCE 1987' poster on a tilted plane and a closing grid. Type: Bigger Display, Editorial New, Fraktion Mono.
Ground and ink from the measured palette (#F40C3F, #180201, #74071A). Motion carries the page through
rows of red W O R K letters with project screenshots sliding between them. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project screenshots

## Reference lock

Primary reference/direction: Antoine Wodniack - Creative Developer — A developer folio in red and black: a tiny barcode loader, a red room drawn as a perspective grid with a bio card, awards as a wall of stamps (Awwwards, FWA, GSAP SOTM, CSSDA), a pill 'WORK', then a black field of red condensed 'W O R K' letters in rows where project screenshots (Durance, Black Hole, Envision, a 404 page) pass between them, a 'CODING MY WAY SINCE 1987' poster on a tilted plane and a closing grid.
Preserve (3-5 traits): red perspective grid room; stamp wall of awards; rows of WORK letters as a field; project shots passing through the letters; tilted poster type.
Borrow only (1-2): Repeat the section word as a field and pass the projects through it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project screenshots
Reject: Small bio text
Token commitments: palette #F40C3F, #180201, #74071A, #E0677B; type Bigger Display, Editorial New, Fraktion Mono; engine GSAP + Lenis linked (never vendored).
