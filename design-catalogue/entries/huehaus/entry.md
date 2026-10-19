---
title: "Huehaus - small studio"
url: https://huehaus.design/
source_url: https://huehaus.design/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pixel-block-studio-blue
dna: "Small studio x cobalt blue and cream, pixel-block wordmark and pixel transitions, serif service titles"
register: modern clean
grammar: chaptered editorial
lane: "A small design studio: 'HUEHAUS' assembling in red, blue and yellow pixel letters, a sentence where letters are missing and fill in over a field of yellow and blue pixel blocks, 'HAUS' on blue with 'Grids. Hierarchy. Systems.', 'You bring the vision. We give it a face, a voice and a future the world can't ignore' with letters dropping in, a cream panel with a pixel edge, services (Website, Branding) in a large serif with three meta columns, 'Good (seriously) Works' over project photos, project cards, 'Look 10x bigger', 'Strategic storytelling', 'Transparent pricing', 'Design for conversion' each on a colour band with a pixel-cut top edge, and 'Ready to build something great?' dissolving in pixels."
mode: persuade
traits: ["pixel-block wordmark", "pixel-cut edges between bands", "letters filling into sentences", "serif service titles", "primary colour bands"]
palette: ["#F7F1EC", "#0444B4", "#0F110F", "#152742", "#607994"]
type: ["Geist Mono", "PP Neue Montreal Medium", "PP Mondwest Regular", "Inter Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The pixel cut edges are the studio's mark and its transition, so each colour band arrives as part of the identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Huehaus Studio).

## What to borrow (principle)

- Make the logo's unit the edge of every transition

## What to leave

- Very small meta columns

## Signature move

Colour bands meeting along pixel-cut edges.

## Motion

Intro: pixel letters build (~2 s). Wheel (Lenis): pixel blocks dissolve between grounds; letters fill in; bands slide up with stepped edges.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 3 video; split text; smoothed scroll (median 124 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a small design studio: 'HUEHAUS' assembling in red, blue and yellow pixel letters, a sentence where letters are missing and fill in over a field of yellow and blue pixel blocks, 'HAUS' on blue with 'Grids. Hierarchy. Systems.', 'You bring the vision. We give it a face, a voice and a future the world can't ignore' with letters dropping in, a cream panel with a pixel edge, services (Website, Branding) in a large serif with three meta columns, 'Good (seriously) Works' over project photos, project cards, 'Look 10x bigger', 'Strategic storytelling', 'Transparent pricing', 'Design for conversion' each on a colour band with a pixel-cut top edge, and 'Ready to build something great?' dissolving in pixels. Type: Geist Mono, PP Neue Montreal Medium, PP Mondwest Regular, Inter Display.
Ground and ink from the measured palette (#F7F1EC, #0444B4, #0F110F). Motion carries the page through
colour bands meeting along pixel-cut edges. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project photography

## Reference lock

Primary reference/direction: Huehaus - small studio — A small design studio: 'HUEHAUS' assembling in red, blue and yellow pixel letters, a sentence where letters are missing and fill in over a field of yellow and blue pixel blocks, 'HAUS' on blue with 'Grids. Hierarchy. Systems.', 'You bring the vision. We give it a face, a voice and a future the world can't ignore' with letters dropping in, a cream panel with a pixel edge, services (Website, Branding) in a large serif with three meta columns, 'Good (seriously) Works' over project photos, project cards, 'Look 10x bigger', 'Strategic storytelling', 'Transparent pricing', 'Design for conversion' each on a colour band with a pixel-cut top edge, and 'Ready to build something great?' dissolving in pixels.
Preserve (3-5 traits): pixel-block wordmark; pixel-cut edges between bands; letters filling into sentences; serif service titles; primary colour bands.
Borrow only (1-2): Make the logo's unit the edge of every transition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project photography
Reject: Very small meta columns
Token commitments: palette #F7F1EC, #0444B4, #0F110F, #152742, #607994; type Geist Mono, PP Neue Montreal Medium, PP Mondwest Regular, Inter Display; engine GSAP + Lenis linked (never vendored).
