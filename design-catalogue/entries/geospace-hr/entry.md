---
title: "Geospace - Innovative Solutions in Geodesy"
url: https://geospace.hr/en/
source_url: https://geospace.hr/en/
captured: 2026-10-02
origin: raw-url
extract: none
category: institutional
category2: "product-focused"
family: terrain-tile-geodesy
dna: "Geodesy company x a satellite terrain tile that rotates in 3D"
register: cinematic dark
grammar: chaptered editorial
lane: "A surveying company on dark grey: wireframe mountain lines under 'Where gravity meets innovation', a 3D satellite terrain tile of a valley that rotates and shrinks beside stats counting up, a drone operator photo, industries list, service cards with photos, client logos and a contact footer with the line terrain."
mode: persuade
traits: ["3D satellite terrain tile", "wireframe mountain lines", "counting stats", "wide uppercase display", "dark grey and pale green", "drone photography"]
palette: ["#262626", "#3E4038", "#908F80"]
type: ["Syoog Regular", "Barlow Semibold", "Inter Regular", "Inter Bold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The terrain tile is literally the company's product (a measured landscape), and turning it in 3D makes geodesy tangible.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Mater Agency).

## What to borrow (principle)

- Show the product as an object (here a terrain tile) that turns in 3D

## What to leave

- Generic cards and logos
- Small text

## Signature move

A 3D satellite terrain tile rotating beside counting stats.

## Motion

Intro: cookie banner, then wireframe lines rise (~2 s). Wheel (native): the terrain tile tilts from flat to 3D and rotates as it shrinks; stats count up; the drone photo slides in; industries list fades; cards rise; the line terrain returns in the footer.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); 5 video; entry gate: Reject All. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a surveying company on dark grey: wireframe mountain lines under 'Where gravity meets innovation', a 3D satellite terrain tile of a valley that rotates and shrinks beside stats counting up, a drone operator photo, industries list, service cards with photos, client logos and a contact footer with the line terrain. Type: Syoog Regular, Barlow Semibold, Inter Regular, Inter Bold.
Ground and ink from the measured palette (#262626, #3E4038, #908F80). Motion carries the page through
a 3D satellite terrain tile rotating beside counting stats. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — satellite terrain, drone and fieldwork photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: satellite terrain, drone and fieldwork photography

## Reference lock

Primary reference/direction: Geospace - Innovative Solutions in Geodesy — A surveying company on dark grey: wireframe mountain lines under 'Where gravity meets innovation', a 3D satellite terrain tile of a valley that rotates and shrinks beside stats counting up, a drone operator photo, industries list, service cards with photos, client logos and a contact footer with the line terrain.
Preserve (3-5 traits): 3D satellite terrain tile; wireframe mountain lines; counting stats; wide uppercase display; dark grey and pale green.
Borrow only (1-2): Show the product as an object (here a terrain tile) that turns in 3D
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: satellite terrain, drone and fieldwork photography
Reject: Generic cards and logos; Small text
Token commitments: palette #262626, #3E4038, #908F80; type Syoog Regular, Barlow Semibold, Inter Regular, Inter Bold; engine GSAP + Lenis linked (never vendored).
