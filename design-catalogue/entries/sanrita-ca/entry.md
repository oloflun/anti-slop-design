---
title: "San Rita"
url: https://sanrita.ca/
source_url: https://sanrita.ca/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: trail-map-studio
dna: "Creative studio x topographic trail map"
register: warm photographic
grammar: continuous world
lane: "A studio site that is a trail map: dots and a blob coalesce on pale grey with a manifesto, then a 3D aerial terrain with dashed trails, a glowing grid zone and pins, 'A creative studio where brands and stories move off-trails', and a featured case card in the corner."
mode: experience
traits: ["3D aerial terrain map", "dashed trail lines and pins", "glowing grid zone", "lime brush-script logo", "condensed lime caps", "case card docked bottom-right"]
palette: ["#DCE2E5", "#80756E", "#50544C", "#ADAC9A"]
type: ["mono", "F37stout", "centramono-bold-webfont", "centramono-book-webfont"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The positioning ('off-trails') is turned into navigation: the home is a terrain with trails, and projects are pins along them. The loader's scattered dots gather into the same blob shape that later marks the active zone on the map.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Turn the brand metaphor into the navigation surface (a trail map with pins)
- Let the loader's particles gather into the shape that marks the map's active zone

## What to leave

- Map holds still under the wheel in captures
- Small grey manifesto text in the intro

## Signature move

A 3D trail map where projects sit as pins along dashed paths.

## Motion

Intro: lime logo on grey, dots drift and gather into a dark blob with manifesto columns either side (~3 s). Then: the aerial terrain fades in through clouds, trails draw, a glowing grid zone appears around a pin, headline and case card settle. Wheel/drag explores the map (WebGL).

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the continuous world grammar: a studio site that is a trail map: dots and a blob coalesce on pale grey with a manifesto, then a 3D aerial terrain with dashed trails, a glowing grid zone and pins, 'A creative studio where brands and stories move off-trails', and a featured case card in the corner. Type: mono, F37stout, centramono-bold-webfont, centramono-book-webfont.
Ground and ink from the measured palette (#DCE2E5, #80756E, #50544C). Motion carries the page through
a 3D trail map where projects sit as pins along dashed paths. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — satellite-style terrain render with map graphics

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: satellite-style terrain render with map graphics

## Reference lock

Primary reference/direction: San Rita — A studio site that is a trail map: dots and a blob coalesce on pale grey with a manifesto, then a 3D aerial terrain with dashed trails, a glowing grid zone and pins, 'A creative studio where brands and stories move off-trails', and a featured case card in the corner.
Preserve (3-5 traits): 3D aerial terrain map; dashed trail lines and pins; glowing grid zone; lime brush-script logo; condensed lime caps.
Borrow only (1-2): Turn the brand metaphor into the navigation surface (a trail map with pins); Let the loader's particles gather into the shape that marks the map's active zone
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: satellite-style terrain render with map graphics
Reject: Map holds still under the wheel in captures; Small grey manifesto text in the intro
Token commitments: palette #DCE2E5, #80756E, #50544C, #ADAC9A; type mono, F37stout, centramono-bold-webfont, centramono-book-webfont; engine GSAP + Lenis linked (never vendored).
