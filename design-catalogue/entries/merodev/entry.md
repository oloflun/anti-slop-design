---
title: "Merouane Bali - developer"
url: https://merodev.net/
source_url: https://merodev.net/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: isometric-node-hub-folio
dna: "Developer x a glowing cube that unfolds into an isometric node map"
register: cinematic dark
grammar: live surface
lane: "A developer folio as a 3D hub: a loader, Enter, a glowing hexagon cube dropping onto a pad, a burst of cubes, then an isometric dark map where the pad connects by glowing lines to stations (Experience, Skills, About me, Projects) each with a small 3D object."
mode: experience
traits: ["glowing cube on a pad", "cube burst transition", "isometric node map", "glowing connector lines", "3D station objects", "dark grid floor"]
palette: ["#0C0E12", "#38474C"]
type: ["BigShouldersDisplay", "Iceland"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The CV becomes a circuit: the centre node literally connects to each section.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Draw the sitemap as a glowing node map

## What to leave

- Navigation hidden in small labels

## Signature move

A glowing cube on a pad wired to stations of a CV.

## Motion

Intro: loader, Enter (unlocked), a hexagon drops onto a pad (~3 s). Scroll: cubes burst outward; the camera pulls up to the isometric map; connector lines light up; station objects animate.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Enter. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the live surface grammar: a developer folio as a 3D hub: a loader, Enter, a glowing hexagon cube dropping onto a pad, a burst of cubes, then an isometric dark map where the pad connects by glowing lines to stations (Experience, Skills, About me, Projects) each with a small 3D object. Type: BigShouldersDisplay, Iceland.
Ground and ink from the measured palette (#0C0E12, #38474C). Motion carries the page through
a glowing cube on a pad wired to stations of a CV. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D scene

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D scene

## Reference lock

Primary reference/direction: Merouane Bali - developer — A developer folio as a 3D hub: a loader, Enter, a glowing hexagon cube dropping onto a pad, a burst of cubes, then an isometric dark map where the pad connects by glowing lines to stations (Experience, Skills, About me, Projects) each with a small 3D object.
Preserve (3-5 traits): glowing cube on a pad; cube burst transition; isometric node map; glowing connector lines; 3D station objects.
Borrow only (1-2): Draw the sitemap as a glowing node map
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D scene
Reject: Navigation hidden in small labels
Token commitments: palette #0C0E12, #38474C; type BigShouldersDisplay, Iceland; engine GSAP + Lenis linked (never vendored).
