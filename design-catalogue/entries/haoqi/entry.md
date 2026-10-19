---
title: "HAOQI - design and engineering"
url: https://haoqi.design/
source_url: https://haoqi.design/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: balloon-hello-grid-folio
dna: "Designer-engineer x an inflated 'hello' in a sky and a project grid that ends in warp speed"
register: modern clean
grammar: chaptered editorial
lane: "A folio: a light grid with 'I BRING CRAFT & TASTE TO DIGITAL WORK' scrambling in beside an inflated blue 'hello' in clouds, a portrait and bio with underlined links, project tiles (Inspire Mono, icons, a phone, posters) in a loose grid with mono labels, a blue panel 'INNOVATE WITH PURPOSE' that opens into a starfield at warp speed, ending 'INNOVATE WITH A HUMAN TOUCH'."
mode: read
traits: ["inflated balloon word in a sky", "scrambled headline", "mono coordinates labels", "loose project grid", "warp-speed starfield finale", "blue accent"]
palette: ["#F8F9F4", "#BEDCEE", "#63210D", "#9D9698"]
type: ["tiktok", "mono", "tronica-mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The warp finale turns a quiet grid into a moment, and the balloon 'hello' sets a playful tone first.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: HAOQI).

## What to borrow (principle)

- End a calm folio with one high-energy full-screen scene

## What to leave

- Mono labels very small

## Signature move

'INNOVATE WITH PURPOSE' inside a starfield at warp speed.

## Motion

Intro: grey (~1 s), the headline scrambles into place, the balloon word drifts. Wheel: bio slides; tiles rise in a loose grid; a blue panel grows and breaks into streaks; the starfield streams; the line swaps.

Measured (`motion/probe.json`): Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a folio: a light grid with 'I BRING CRAFT & TASTE TO DIGITAL WORK' scrambling in beside an inflated blue 'hello' in clouds, a portrait and bio with underlined links, project tiles (Inspire Mono, icons, a phone, posters) in a loose grid with mono labels, a blue panel 'INNOVATE WITH PURPOSE' that opens into a starfield at warp speed, ending 'INNOVATE WITH A HUMAN TOUCH'. Type: tiktok, mono, tronica-mono.
Ground and ink from the measured palette (#F8F9F4, #BEDCEE, #63210D). Motion carries the page through
'INNOVATE WITH PURPOSE' inside a starfield at warp speed. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D type, project tiles

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D type, project tiles

## Reference lock

Primary reference/direction: HAOQI - design and engineering — A folio: a light grid with 'I BRING CRAFT & TASTE TO DIGITAL WORK' scrambling in beside an inflated blue 'hello' in clouds, a portrait and bio with underlined links, project tiles (Inspire Mono, icons, a phone, posters) in a loose grid with mono labels, a blue panel 'INNOVATE WITH PURPOSE' that opens into a starfield at warp speed, ending 'INNOVATE WITH A HUMAN TOUCH'.
Preserve (3-5 traits): inflated balloon word in a sky; scrambled headline; mono coordinates labels; loose project grid; warp-speed starfield finale.
Borrow only (1-2): End a calm folio with one high-energy full-screen scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D type, project tiles
Reject: Mono labels very small
Token commitments: palette #F8F9F4, #BEDCEE, #63210D, #9D9698; type tiktok, mono, tronica-mono; engine GSAP + Lenis linked (never vendored).
