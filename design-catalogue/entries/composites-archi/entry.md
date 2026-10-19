---
title: "Composites.archi - Composite materials"
url: https://www.composites.archi/
source_url: https://www.composites.archi/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: material-industry-orange-lines
dna: "Composite materials body x orange line drawings and condensed statements"
register: modern clean
grammar: chaptered editorial
lane: "A materials association: 'The power of composites' on grey, orange line drawings (a spiral polygon for construction, a ripple for renovation) as cards, construction/renovation categories with building photos, 'Why choose composites' on black, an orange topographic line field, 'It is through this paradox, which unites opposing materials...' in condensed caps, standards, 'An architectural revolution embraced by pioneers since 1950s', and a timeline of buildings floating in depth."
mode: read
traits: ["orange line drawings", "grey and black chapters", "condensed caps statements", "topographic line field", "timeline of buildings in depth", "small grey labels"]
palette: ["#CEC9C9", "#191919", "#786C61"]
type: ["tasa-orbiter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The orange line drawings give a technical industry a clean visual identity, and the timeline in depth turns history into a walk.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Sparkk).

## What to borrow (principle)

- Float a timeline of photos in depth

## What to leave

- Small labels

## Signature move

Orange line drawings of a spiral and a ripple for construction and renovation.

## Motion

Intro: grey with a thin loading line (~3 s). Wheel: drawings draw in; cards move to black; photos slide in rows; the line field ripples; statements reveal; timeline photos fly toward the camera.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 99 px still travelling after input stops); entry gate: SKIP. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a materials association: 'The power of composites' on grey, orange line drawings (a spiral polygon for construction, a ripple for renovation) as cards, construction/renovation categories with building photos, 'Why choose composites' on black, an orange topographic line field, 'It is through this paradox, which unites opposing materials...' in condensed caps, standards, 'An architectural revolution embraced by pioneers since 1950s', and a timeline of buildings floating in depth. Type: tasa-orbiter.
Ground and ink from the measured palette (#CEC9C9, #191919, #786C61). Motion carries the page through
orange line drawings of a spiral and a ripple for construction and renovation. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architecture photography, line drawings

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architecture photography, line drawings

## Reference lock

Primary reference/direction: Composites.archi - Composite materials — A materials association: 'The power of composites' on grey, orange line drawings (a spiral polygon for construction, a ripple for renovation) as cards, construction/renovation categories with building photos, 'Why choose composites' on black, an orange topographic line field, 'It is through this paradox, which unites opposing materials...' in condensed caps, standards, 'An architectural revolution embraced by pioneers since 1950s', and a timeline of buildings floating in depth.
Preserve (3-5 traits): orange line drawings; grey and black chapters; condensed caps statements; topographic line field; timeline of buildings in depth.
Borrow only (1-2): Float a timeline of photos in depth
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architecture photography, line drawings
Reject: Small labels
Token commitments: palette #CEC9C9, #191919, #786C61; type tasa-orbiter; engine GSAP + Lenis linked (never vendored).
