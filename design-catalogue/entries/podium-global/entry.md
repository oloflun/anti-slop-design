---
title: "Podium"
url: https://podium.global/
source_url: https://podium.global/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: liquid-blob-sports-film
dna: "Sports film studio x liquid blob mask and carved stone"
register: cinematic dark
grammar: chaptered editorial
lane: "A sports production studio that opens through a liquid black-and-white blob that reveals film stills, then floats stills over a carved stone object on black, lays out an index of projects, a dashed-grid 'behind the scenes' section on white, and closes with the stone turning above 'LET'S BUILD YOUR VISION'."
mode: persuade
traits: ["liquid metaball mask revealing images", "carved stone 3D object as recurring mark", "floating film stills index", "dashed construction grid on white", "topographic line texture", "condensed caps"]
palette: ["#000000", "#FFFFFF", "#4C4638", "#8B8776", "#141615"]
type: ["Futura", "Univers Condensed"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Two materials frame the work: a liquid mask that opens the page like ink dispersing, and a carved stone that keeps returning (behind the stills, at the close). Between them the work is a loose index of film stills, then a white chapter drawn on a dashed grid like a field map.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: San Rita).

## What to borrow (principle)

- Open the hero through a liquid metaball mask
- A single physical object (carved stone) as the recurring brand mark
- Dashed grid and topographic lines for a 'fieldwork' chapter

## What to leave

- Index cards small and crowded
- Long black stretches

## Signature move

A liquid black-and-white blob that opens to reveal film stills.

## Motion

Intro: white with a dot and percentage 1% → 79% (~2.5 s). Scroll (Lenis, ~125 px glide, WebGL, 27 videos): metaball blob expands, revealing stills; stills float over the stone on black; project index with titles; dark statement; white 'WE HELP SPORTS BRANDS…' with BTS photo strip; dashed grid with client lists; stone turning over 'LET'S BUILD YOUR VISION / WORK WITH US'.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); 27 video; smoothed scroll (median 123 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a sports production studio that opens through a liquid black-and-white blob that reveals film stills, then floats stills over a carved stone object on black, lays out an index of projects, a dashed-grid 'behind the scenes' section on white, and closes with the stone turning above 'LET'S BUILD YOUR VISION'. Type: Futura, Univers Condensed.
Ground and ink from the measured palette (#000000, #FFFFFF, #4C4638). Motion carries the page through
a liquid black-and-white blob that opens to reveal film stills. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — sports and outdoor film stills, raw textures, carved stone

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: sports and outdoor film stills, raw textures, carved stone

## Reference lock

Primary reference/direction: Podium — A sports production studio that opens through a liquid black-and-white blob that reveals film stills, then floats stills over a carved stone object on black, lays out an index of projects, a dashed-grid 'behind the scenes' section on white, and closes with the stone turning above 'LET'S BUILD YOUR VISION'.
Preserve (3-5 traits): liquid metaball mask revealing images; carved stone 3D object as recurring mark; floating film stills index; dashed construction grid on white; topographic line texture.
Borrow only (1-2): Open the hero through a liquid metaball mask; A single physical object (carved stone) as the recurring brand mark
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: sports and outdoor film stills, raw textures, carved stone
Reject: Index cards small and crowded; Long black stretches
Token commitments: palette #000000, #FFFFFF, #4C4638, #8B8776, #141615; type Futura, Univers Condensed; engine GSAP + Lenis linked (never vendored).
