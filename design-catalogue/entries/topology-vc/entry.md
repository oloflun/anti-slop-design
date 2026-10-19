---
title: "Topology - venture firm"
url: https://topology.vc/
source_url: https://topology.vc/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "portfolio"
family: iridescent-contour-vc
dna: "Venture firm x a white contour field with iridescent edges you fall into, then dark chapters of principles, team and investments"
register: cinematic dark
grammar: continuous world
lane: "An early-stage fund: 'Meet us at the edge' over a white rippled surface, the camera diving into a contour hole with rainbow fringes ('You jump...'), black chapters ('Topology: where our name comes from', 'What we do', 'How we do it', 'Principles' with the active principle bright), 3D bust portraits of the team, a grid of investments, 'Public goods' as a list, and the contour field returning and flowing at the end."
mode: persuade
traits: ["white contour surface", "iridescent fringes", "dive into the surface", "active principle highlighted", "3D bust portraits"]
palette: ["#151515", "#313231", "#656663"]
type: ["LazareGrotesk", "Magnetik", "Space Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The contour field is literally the firm's name (topology) and bookends the page, so the brand is a surface you fall into.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Unseen Studio®).

## What to borrow (principle)

- Make the name into the surface the page starts and ends on

## What to leave

- Small mono paragraphs

## Signature move

A white contour surface with rainbow edges the camera falls into.

## Motion

Intro: black (~1 s). Wheel (Lenis): the surface is scrubbed in WebGL toward a dive; chapters fade; principles light in turn; the surface flows again at the end.

Measured (`motion/probe.json`): GSAP 3.14.2; 1 pinned sections; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: EXPLORE. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: an early-stage fund: 'Meet us at the edge' over a white rippled surface, the camera diving into a contour hole with rainbow fringes ('You jump...'), black chapters ('Topology: where our name comes from', 'What we do', 'How we do it', 'Principles' with the active principle bright), 3D bust portraits of the team, a grid of investments, 'Public goods' as a list, and the contour field returning and flowing at the end. Type: LazareGrotesk, Magnetik, Space Mono.
Ground and ink from the measured palette (#151515, #313231, #656663). Motion carries the page through
a white contour surface with rainbow edges the camera falls into. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL surface, 3D portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL surface, 3D portraits

## Reference lock

Primary reference/direction: Topology - venture firm — An early-stage fund: 'Meet us at the edge' over a white rippled surface, the camera diving into a contour hole with rainbow fringes ('You jump...'), black chapters ('Topology: where our name comes from', 'What we do', 'How we do it', 'Principles' with the active principle bright), 3D bust portraits of the team, a grid of investments, 'Public goods' as a list, and the contour field returning and flowing at the end.
Preserve (3-5 traits): white contour surface; iridescent fringes; dive into the surface; active principle highlighted; 3D bust portraits.
Borrow only (1-2): Make the name into the surface the page starts and ends on
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL surface, 3D portraits
Reject: Small mono paragraphs
Token commitments: palette #151515, #313231, #656663; type LazareGrotesk, Magnetik, Space Mono; engine GSAP + Lenis linked (never vendored).
