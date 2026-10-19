---
title: "Modus - AI agent framework"
url: https://modus.fantik.studio/
source_url: https://modus.fantik.studio/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: ""
family: dot-matrix-ai-framework
dna: "AI framework x a dot-matrix wordmark in a starfield and a draggable 3D card stack"
register: cinematic dark
grammar: continuous world
lane: "A product site in greyscale: a dot-matrix counter on black, 'MODUS' built from glowing dot-matrix blocks in a drifting starfield, 'Start building', 'IMAGINE A COGNITIVE SYSTEM WITH COMPLETE AUTONOMY' inside a glowing ring of dots, 'UNLIMITED INTELLIGENCE', then 'PERKS OF SMART DAO'S' as a 3D stack of curved cards you drag ('Plug and play')."
mode: experience
traits: ["dot-matrix display type", "drifting starfield", "glowing ring of dots", "draggable curved 3D cards", "greyscale only", "mono labels and corner frames"]
palette: ["#0F0F0F", "#252525", "#484848", "#818181"]
type: ["My Pager", "Roobert-Regular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Everything is built from the same dots (logo, ring, starfield), so the page reads as one machine.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Build the logo, rings and background from one dot unit

## What to leave

- Long empty black frames
- Drag-only card stack

## Signature move

'MODUS' in glowing dot-matrix blocks in a starfield.

## Motion

Intro: black with a dot counter (~2 s), the wordmark assembles. Wheel: stars drift; the wordmark scrolls; a ring of dots forms around the statement; the cards rise in 3D and wait for drag.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x2 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Start Building. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a product site in greyscale: a dot-matrix counter on black, 'MODUS' built from glowing dot-matrix blocks in a drifting starfield, 'Start building', 'IMAGINE A COGNITIVE SYSTEM WITH COMPLETE AUTONOMY' inside a glowing ring of dots, 'UNLIMITED INTELLIGENCE', then 'PERKS OF SMART DAO'S' as a 3D stack of curved cards you drag ('Plug and play'). Type: My Pager, Roobert-Regular.
Ground and ink from the measured palette (#0F0F0F, #252525, #484848). Motion carries the page through
'MODUS' in glowing dot-matrix blocks in a starfield. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL dots, 3D cards

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL dots, 3D cards

## Reference lock

Primary reference/direction: Modus - AI agent framework — A product site in greyscale: a dot-matrix counter on black, 'MODUS' built from glowing dot-matrix blocks in a drifting starfield, 'Start building', 'IMAGINE A COGNITIVE SYSTEM WITH COMPLETE AUTONOMY' inside a glowing ring of dots, 'UNLIMITED INTELLIGENCE', then 'PERKS OF SMART DAO'S' as a 3D stack of curved cards you drag ('Plug and play').
Preserve (3-5 traits): dot-matrix display type; drifting starfield; glowing ring of dots; draggable curved 3D cards; greyscale only.
Borrow only (1-2): Build the logo, rings and background from one dot unit
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL dots, 3D cards
Reject: Long empty black frames; Drag-only card stack
Token commitments: palette #0F0F0F, #252525, #484848, #818181; type My Pager, Roobert-Regular; engine GSAP + Lenis linked (never vendored).
