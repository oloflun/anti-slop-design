---
title: "Blackbird - SR-71 story"
url: https://www.sr-seventy.one/
source_url: https://www.sr-seventy.one/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: ""
family: aircraft-history-wireframe
dna: "SR-71 history x wireframe aircraft resolving into a lit model"
register: cinematic dark
grammar: continuous world
lane: "A history piece: a percent counter over faint typewriter text, 'BLACKBIRD' and the story intro 'Fall of 1957. The CIA wanted something new...', archival black-and-white photos of a wind-tunnel model, 'Two years and 11 ideas later' surrounded by small aircraft silhouettes with specs, then a wireframe aircraft that rotates in a spotlight and resolves into a solid model labelled 'KINGFISH'."
mode: read
traits: ["archival photography", "small aircraft silhouettes with specs", "wireframe to solid model", "spotlight on black", "red accent dates", "typewriter background text"]
palette: ["#030303", "#92908F"]
type: ["Right Grotesk", "Acid Grotesk", "Sohne Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The design sketches around the headline and the wireframe that becomes solid tell the engineering story visually.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Resolve a wireframe into a solid model as the design is 'chosen'

## What to leave

- Very small spec text

## Signature move

A wireframe aircraft rotating in a spotlight and becoming solid.

## Motion

Intro: black with faint text and a counter to 100% (~3 s). Wheel: the title fades; the story statement slides up; archival photos scale in; silhouettes appear around the centre text; the wireframe descends and rotates under a light; it fills in as solid while the label appears.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: a history piece: a percent counter over faint typewriter text, 'BLACKBIRD' and the story intro 'Fall of 1957. The CIA wanted something new...', archival black-and-white photos of a wind-tunnel model, 'Two years and 11 ideas later' surrounded by small aircraft silhouettes with specs, then a wireframe aircraft that rotates in a spotlight and resolves into a solid model labelled 'KINGFISH'. Type: Right Grotesk, Acid Grotesk, Sohne Mono.
Ground and ink from the measured palette (#030303, #92908F). Motion carries the page through
a wireframe aircraft rotating in a spotlight and becoming solid. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — archival photos, 3D wireframe and model

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: archival photos, 3D wireframe and model

## Reference lock

Primary reference/direction: Blackbird - SR-71 story — A history piece: a percent counter over faint typewriter text, 'BLACKBIRD' and the story intro 'Fall of 1957. The CIA wanted something new...', archival black-and-white photos of a wind-tunnel model, 'Two years and 11 ideas later' surrounded by small aircraft silhouettes with specs, then a wireframe aircraft that rotates in a spotlight and resolves into a solid model labelled 'KINGFISH'.
Preserve (3-5 traits): archival photography; small aircraft silhouettes with specs; wireframe to solid model; spotlight on black; red accent dates.
Borrow only (1-2): Resolve a wireframe into a solid model as the design is 'chosen'
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: archival photos, 3D wireframe and model
Reject: Very small spec text
Token commitments: palette #030303, #92908F; type Right Grotesk, Acid Grotesk, Sohne Mono; engine GSAP + Lenis linked (never vendored).
