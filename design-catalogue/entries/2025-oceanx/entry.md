---
title: "OceanX 2025 Year in Review"
url: http://2025.oceanx.org/
source_url: http://2025.oceanx.org/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: globe-to-ocean-year-review
dna: "Ocean exploration nonprofit x globe zoom to expedition ship"
register: cinematic dark
grammar: continuous world
lane: "A year-in-review that starts on a rotating 3D Earth, dives to a satellite view of an island and the expedition ship on dark water, and then keeps the ship centred while chapter cards (UNOC3, Africa's Ocean Leaders, Technology Stewardship) slide past."
mode: read
traits: ["3D globe intro", "dive to top-down ocean view", "ship as fixed anchor", "chapter cards sliding past", "deep navy palette", "audio toggle"]
palette: ["#020E1D", "#11263F", "#434E5B", "#7C8289"]
type: ["Zeist", "DM"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ship is the anchor: once the camera dives from the globe to the ocean, the vessel stays in the centre while the year's chapters slide past like waypoints on a voyage. The scale change from planet to ship sets the mission in one move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Zoom from a globe to one object and keep it centred as the chapters pass
- Treat chapters of a report as waypoints on a journey

## What to leave

- Many near-identical frames of the ship
- Small card text

## Signature move

A dive from a rotating Earth to the expedition ship on dark water.

## Motion

Intro: navy with the OceanX mark and a dot loader (~2.5 s), the globe rotates. Wheel (virtual, WebGL): the camera dives to an island coast; the ship appears top-down; chapter cards slide in and out beside it; the island drifts away; water texture keeps moving.

Measured (`motion/probe.json`): GSAP 3.13.0/3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: ENTER EXPERIENCE ENTER EXPERIENCE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a year-in-review that starts on a rotating 3D Earth, dives to a satellite view of an island and the expedition ship on dark water, and then keeps the ship centred while chapter cards (UNOC3, Africa's Ocean Leaders, Technology Stewardship) slide past. Type: Zeist, DM.
Ground and ink from the measured palette (#020E1D, #11263F, #434E5B). Motion carries the page through
a dive from a rotating Earth to the expedition ship on dark water. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — satellite and 3D ocean imagery, research vessel, deep navy

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: satellite and 3D ocean imagery, research vessel, deep navy

## Reference lock

Primary reference/direction: OceanX 2025 Year in Review — A year-in-review that starts on a rotating 3D Earth, dives to a satellite view of an island and the expedition ship on dark water, and then keeps the ship centred while chapter cards (UNOC3, Africa's Ocean Leaders, Technology Stewardship) slide past.
Preserve (3-5 traits): 3D globe intro; dive to top-down ocean view; ship as fixed anchor; chapter cards sliding past; deep navy palette.
Borrow only (1-2): Zoom from a globe to one object and keep it centred as the chapters pass; Treat chapters of a report as waypoints on a journey
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: satellite and 3D ocean imagery, research vessel, deep navy
Reject: Many near-identical frames of the ship; Small card text
Token commitments: palette #020E1D, #11263F, #434E5B, #7C8289; type Zeist, DM; engine GSAP + Lenis linked (never vendored).
