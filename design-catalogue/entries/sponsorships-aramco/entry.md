---
title: "Aramco - Shoot for the Future court project"
url: https://sponsorships.aramco.com/cba/shoot-for-the-future
source_url: https://sponsorships.aramco.com/cba/shoot-for-the-future
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "consumer-brand"
family: green-tile-sponsorship-story
dna: "Sponsorship report x pale grey 3D floor of white tiles where green court tiles rise, number and tumble"
register: modern clean
grammar: continuous world
lane: "A sponsorship case as one floor: a pale grey 3D plane of loose white tiles with a few green ones, 'Shoot for the future' in wide caps, the tiles drifting as the camera glides while chapters about community basketball sit in corners, photos of the renovated courts slid in at an angle, 'A strategic partnership' on white, a video of a player, 'Advanced materials for community sport', then the process told by three green tiles that rise and carry numerals 1, 2, 3 (recycling plastic waste, creating granules, producing flooring), and the whole floor flooding green for the closing statement."
mode: persuade
traits: ["3D field of loose tiles", "green tiles as the brand colour", "numbered tiles carry the process", "angled photo inserts", "floor floods green at the close", "wide caps"]
palette: ["#FFFFFF", "#E2E2E2", "#779083"]
type: ["Ghawar", "Beta Manifa Advertising V1.20.4 Bd Wide", "Beta Manifa Advertising V1.20.4 SmBd Wide", "ghawar"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The material story (waste into court flooring) is told with the court tile itself as the moving object, so the process steps are the product.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Immersive Garden).

## What to borrow (principle)

- Let the product's own unit carry the numbered process steps

## What to leave

- Cookie bar on the hero
- Small corner copy

## Signature move

Three green court tiles rising out of a white tile floor with numerals 1, 2, 3.

## Motion

Intro: tiles settle (~2 s). Wheel (Lenis, swup): the WebGL camera glides over the floor; tiles tilt and lift per chapter; photos slide in rotated; the numbered tiles rise and flip; the floor turns green with a fade.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Swup page transitions; WebGL canvas x1 (three.js); 2 video; smoothed scroll (median 79 px still travelling after input stops); entry gate: Reject All. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the continuous world grammar: a sponsorship case as one floor: a pale grey 3D plane of loose white tiles with a few green ones, 'Shoot for the future' in wide caps, the tiles drifting as the camera glides while chapters about community basketball sit in corners, photos of the renovated courts slid in at an angle, 'A strategic partnership' on white, a video of a player, 'Advanced materials for community sport', then the process told by three green tiles that rise and carry numerals 1, 2, 3 (recycling plastic waste, creating granules, producing flooring), and the whole floor flooding green for the closing statement. Type: Ghawar, Beta Manifa Advertising V1.20.4 Bd Wide, Beta Manifa Advertising V1.20.4 SmBd Wide, ghawar.
Ground and ink from the measured palette (#FFFFFF, #E2E2E2, #779083). Motion carries the page through
three green court tiles rising out of a white tile floor with numerals 1, 2, 3. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL tiles, documentary photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL tiles, documentary photography

## Reference lock

Primary reference/direction: Aramco - Shoot for the Future court project — A sponsorship case as one floor: a pale grey 3D plane of loose white tiles with a few green ones, 'Shoot for the future' in wide caps, the tiles drifting as the camera glides while chapters about community basketball sit in corners, photos of the renovated courts slid in at an angle, 'A strategic partnership' on white, a video of a player, 'Advanced materials for community sport', then the process told by three green tiles that rise and carry numerals 1, 2, 3 (recycling plastic waste, creating granules, producing flooring), and the whole floor flooding green for the closing statement.
Preserve (3-5 traits): 3D field of loose tiles; green tiles as the brand colour; numbered tiles carry the process; angled photo inserts; floor floods green at the close.
Borrow only (1-2): Let the product's own unit carry the numbered process steps
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL tiles, documentary photography
Reject: Cookie bar on the hero; Small corner copy
Token commitments: palette #FFFFFF, #E2E2E2, #779083; type Ghawar, Beta Manifa Advertising V1.20.4 Bd Wide, Beta Manifa Advertising V1.20.4 SmBd Wide, ghawar; engine GSAP + Lenis linked (never vendored).
