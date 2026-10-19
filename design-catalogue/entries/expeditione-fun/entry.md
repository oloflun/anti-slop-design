---
title: "Expeditione"
url: https://expeditione.fun/
source_url: https://expeditione.fun/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: diorama-3d-encyclopedia
dna: "Interactive 3D encyclopedia x isometric dioramas"
register: cinematic dark
grammar: chaptered editorial
lane: "A dark, warm educational site with 'The Interactive 3D Encyclopedia' in serif italic beside a rotating isometric island diorama, then expedition cards (Soil, Ancient Egypt, Cell Biology), a destination vote, a philosophy statement, a vertical timeline of milestones and a long FAQ."
mode: read
traits: ["isometric 3D diorama hero", "serif italic accents", "colour-coded expedition cards", "vertical timeline with alternating entries", "warm dark brown ground", "community vote grid"]
palette: ["#141211", "#A59778", "#96D4DE", "#5B4E45", "#D0C8B6", "#302D2A"]
type: ["Fraunces", "Space Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A small rotating diorama (a whole island in a cube) promises worlds you can explore, and each expedition is a coloured card like a book cover. The rest reads as a calm founder's letter with a clear vertical timeline.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A rotating isometric diorama as a compact hero promise
- A vertical timeline with entries alternating sides for milestones

## What to leave

- Long text-heavy FAQ at the end
- Small timeline text

## Signature move

A rotating isometric island diorama beside a serif italic title.

## Motion

Intro: title on dark, the diorama fades in and rotates (~1 s). Scroll (window, WebGL): expedition cards rise; vote grid; philosophy statement fades; timeline line draws downward with entries alternating; FAQ; footer.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Start Expedition. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a dark, warm educational site with 'The Interactive 3D Encyclopedia' in serif italic beside a rotating isometric island diorama, then expedition cards (Soil, Ancient Egypt, Cell Biology), a destination vote, a philosophy statement, a vertical timeline of milestones and a long FAQ. Type: Fraunces, Space Grotesk.
Ground and ink from the measured palette (#141211, #A59778, #96D4DE). Motion carries the page through
a rotating isometric island diorama beside a serif italic title. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — isometric 3D dioramas, archival illustrations

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: isometric 3D dioramas, archival illustrations

## Reference lock

Primary reference/direction: Expeditione — A dark, warm educational site with 'The Interactive 3D Encyclopedia' in serif italic beside a rotating isometric island diorama, then expedition cards (Soil, Ancient Egypt, Cell Biology), a destination vote, a philosophy statement, a vertical timeline of milestones and a long FAQ.
Preserve (3-5 traits): isometric 3D diorama hero; serif italic accents; colour-coded expedition cards; vertical timeline with alternating entries; warm dark brown ground.
Borrow only (1-2): A rotating isometric diorama as a compact hero promise; A vertical timeline with entries alternating sides for milestones
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: isometric 3D dioramas, archival illustrations
Reject: Long text-heavy FAQ at the end; Small timeline text
Token commitments: palette #141211, #A59778, #96D4DE, #5B4E45, #D0C8B6, #302D2A; type Fraunces, Space Grotesk; engine GSAP + Lenis linked (never vendored).
