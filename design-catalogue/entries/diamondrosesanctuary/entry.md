---
title: "Diamond Rose Sanctuary"
url: https://diamondrosesanctuary.com/
source_url: https://diamondrosesanctuary.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: ""
family: forest-green-retreat
dna: "Nature retreat x thin serif caps and a golden lotus temple"
register: warm photographic
grammar: chaptered editorial
lane: "A retreat page that opens on an aerial of islands in dark water with 'DIAMOND ROSE' and a vertical 'SANCTUARY', moves through stone-coloured pages with small photo clusters, then pins on a golden lotus temple render while chapter lines change beneath it."
mode: persuade
traits: ["aerial water hero", "vertical word along the right edge", "stone ground with forest-green panels", "small photo clusters", "pinned golden temple render", "thin serif caps"]
palette: ["#DFD8CA", "#24492F", "#68665B", "#14100A", "#8C918C", "#BFC3C0"]
type: ["Aime", "NM"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Calm through scarcity: small photos on a stone ground, thin serif caps, one forest green. The single exception is a golden render of the planned temple that pins and stays while the copy changes under it, the page's one immersive moment.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Pin one immersive render and change only the copy beneath it
- A vertical word along the frame edge for a quiet hero
- Small photo clusters instead of full-bleed images on a reading page

## What to leave

- Heavy smoothing (~160 px glide)
- Very light, small text

## Signature move

A golden lotus-temple render that pins while chapter lines change beneath it.

## Motion

Intro: aerial film with 'DIAMOND ROSE' and vertical 'SANCTUARY' (~1.5 s). Scroll (Lenis, ~165 px glide, 1 pin, 4 ScrollTriggers): story paragraph; 'PRESERVED LAND. OPEN WATER.' with a photo rising; three photos gather; green panel with retreat list beside a hot-tub photo; retreats; pinned temple render with lines 'FORMING IN THE LIGHT', 'A NEW CHAPTER BEGINS', 'SPACE FOR HEALING'; 'REMEMBER HOW IT FEELS TO BREATHE'; rentals and retreats cards; green footer.

Measured (`motion/probe.json`): GSAP 3.12.2; 4 ScrollTriggers; 1 pinned sections; Lenis; 1 video; smoothed scroll (median 151 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a retreat page that opens on an aerial of islands in dark water with 'DIAMOND ROSE' and a vertical 'SANCTUARY', moves through stone-coloured pages with small photo clusters, then pins on a golden lotus temple render while chapter lines change beneath it. Type: Aime, NM.
Ground and ink from the measured palette (#DFD8CA, #24492F, #68665B). Motion carries the page through
a golden lotus-temple render that pins while chapter lines change beneath it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — aerial nature, interiors with soft daylight, one golden 3D render

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: aerial nature, interiors with soft daylight, one golden 3D render

## Reference lock

Primary reference/direction: Diamond Rose Sanctuary — A retreat page that opens on an aerial of islands in dark water with 'DIAMOND ROSE' and a vertical 'SANCTUARY', moves through stone-coloured pages with small photo clusters, then pins on a golden lotus temple render while chapter lines change beneath it.
Preserve (3-5 traits): aerial water hero; vertical word along the right edge; stone ground with forest-green panels; small photo clusters; pinned golden temple render.
Borrow only (1-2): Pin one immersive render and change only the copy beneath it; A vertical word along the frame edge for a quiet hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: aerial nature, interiors with soft daylight, one golden 3D render
Reject: Heavy smoothing (~160 px glide); Very light, small text
Token commitments: palette #DFD8CA, #24492F, #68665B, #14100A, #8C918C, #BFC3C0; type Aime, NM; engine GSAP + Lenis linked (never vendored).
