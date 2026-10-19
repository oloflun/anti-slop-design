---
title: "Lumen Artspace - Heritage in Art"
url: https://www.lumenartspace.com/
source_url: https://www.lumenartspace.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "luxury-craft"
family: lacquer-art-gallery-3d
dna: "Vietnamese lacquer art gallery x serif italic titles and artworks in a 3D gallery"
register: cinematic dark
grammar: continuous world
lane: "A lacquer-art gallery on black: line-drawn clouds behind 'Heritage in Art' with a Visit Gallery button, a giant serif 'Heritage In Art' with an italic word, 'A (Journey) Through Time' with artworks drifting, 'Impressions Of Heritage' over a curved wall of lacquer paintings, 'Timeless Masterpieces' over a temple, a single painting presented in a dark 3D room, '2011' outline, a floor of paintings laid out in perspective for the mission, and 'Reflection Of Art' with a closing grid."
mode: read
traits: ["serif titles with italic accents", "line-drawn clouds", "curved wall of paintings", "single painting in a dark 3D room", "paintings laid out on a floor in perspective", "black ground"]
palette: ["#000000", "#212121", "#777777"]
type: ["LA Neue Montreal", "LA Playground", "La Ivyprestodisplay"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each chapter presents the same artworks in a different spatial arrangement (drifting, wall, room, floor), so the scroll is a walk through a gallery.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Rearrange the same artworks into a new spatial form per chapter

## What to leave

- Very small body text

## Signature move

Lacquer paintings laid out in perspective on a dark floor.

## Motion

Intro: black with line clouds and the title (~2 s), Visit Gallery clicked. Wheel (Lenis, 1 pin, WebGL): a painting rises and the giant title fills; artworks drift past; they assemble into a curved wall; the camera enters a dark room with one painting; the outline year passes; paintings lie down on a floor and the camera tilts over them.

Measured (`motion/probe.json`): GSAP 3.12.5; 12 ScrollTriggers; 1 pinned sections; Lenis; Barba page transitions; WebGL canvas x1; smoothed scroll (median 113 px still travelling after input stops); entry gate: Visit Gallery. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a lacquer-art gallery on black: line-drawn clouds behind 'Heritage in Art' with a Visit Gallery button, a giant serif 'Heritage In Art' with an italic word, 'A (Journey) Through Time' with artworks drifting, 'Impressions Of Heritage' over a curved wall of lacquer paintings, 'Timeless Masterpieces' over a temple, a single painting presented in a dark 3D room, '2011' outline, a floor of paintings laid out in perspective for the mission, and 'Reflection Of Art' with a closing grid. Type: LA Neue Montreal, LA Playground, La Ivyprestodisplay.
Ground and ink from the measured palette (#000000, #212121, #777777). Motion carries the page through
lacquer paintings laid out in perspective on a dark floor. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lacquer paintings, temple photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lacquer paintings, temple photography

## Reference lock

Primary reference/direction: Lumen Artspace - Heritage in Art — A lacquer-art gallery on black: line-drawn clouds behind 'Heritage in Art' with a Visit Gallery button, a giant serif 'Heritage In Art' with an italic word, 'A (Journey) Through Time' with artworks drifting, 'Impressions Of Heritage' over a curved wall of lacquer paintings, 'Timeless Masterpieces' over a temple, a single painting presented in a dark 3D room, '2011' outline, a floor of paintings laid out in perspective for the mission, and 'Reflection Of Art' with a closing grid.
Preserve (3-5 traits): serif titles with italic accents; line-drawn clouds; curved wall of paintings; single painting in a dark 3D room; paintings laid out on a floor in perspective.
Borrow only (1-2): Rearrange the same artworks into a new spatial form per chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lacquer paintings, temple photography
Reject: Very small body text
Token commitments: palette #000000, #212121, #777777; type LA Neue Montreal, LA Playground, La Ivyprestodisplay; engine GSAP + Lenis linked (never vendored).
