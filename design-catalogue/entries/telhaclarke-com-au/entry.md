---
title: "Telha Clarke - Melbourne Architecture and Interiors"
url: https://telhaclarke.com.au/
source_url: https://telhaclarke.com.au/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: architect-bracket-titles-scatter
dna: "Melbourne architecture studio x bracketed project titles and a 3D photo scatter"
register: modern clean
grammar: chaptered editorial
lane: "An architecture studio: a full-bleed video of timber screens and trees, then a centred statement on white, a list of selected works where each project name sits between square brackets and its photo slides up between the names, and an 'All Work (31)' title surrounded by photos flying past in depth before the page closes on a full-bleed image."
mode: read
traits: ["project names framed in square brackets", "photo slides between consecutive titles", "photos flying past in z-space around a count", "neutral white with warm photography", "small grotesk metadata", "Taxi page transitions"]
palette: ["#FFFFFF", "#0D0E0C", "#807D72", "#ABA9A7", "#28221A", "#E7E6E6"]
type: ["Europa-Grotesk"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The brackets turn each project name into a frame that the photo passes through, and the flying scatter makes '31 projects' a felt quantity rather than a number.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Grégory Lallé, StudioPaack, Thomas Monavon).

## What to borrow (principle)

- Frame titles with brackets and pass the image between them
- Fly the archive past the camera around its count

## What to leave

- Empty white loading frames
- Tiny metadata

## Signature move

Project names held in square brackets with their photos sliding up between them.

## Motion

Intro: white for ~1.5 s, then the hero video fades in. Wheel (virtual scroll, frame diff): the video lifts to reveal the statement which slides up line by line; each bracketed title holds while its photo rises from below and pushes the next title up; at 'All Work' photos fly from the centre outward in depth; the last photo scales to full bleed.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Taxi page transitions; 1 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an architecture studio: a full-bleed video of timber screens and trees, then a centred statement on white, a list of selected works where each project name sits between square brackets and its photo slides up between the names, and an 'All Work (31)' title surrounded by photos flying past in depth before the page closes on a full-bleed image. Type: Europa-Grotesk.
Ground and ink from the measured palette (#FFFFFF, #0D0E0C, #807D72). Motion carries the page through
project names held in square brackets with their photos sliding up between them. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural photography and video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural photography and video

## Reference lock

Primary reference/direction: Telha Clarke - Melbourne Architecture and Interiors — An architecture studio: a full-bleed video of timber screens and trees, then a centred statement on white, a list of selected works where each project name sits between square brackets and its photo slides up between the names, and an 'All Work (31)' title surrounded by photos flying past in depth before the page closes on a full-bleed image.
Preserve (3-5 traits): project names framed in square brackets; photo slides between consecutive titles; photos flying past in z-space around a count; neutral white with warm photography; small grotesk metadata.
Borrow only (1-2): Frame titles with brackets and pass the image between them; Fly the archive past the camera around its count
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural photography and video
Reject: Empty white loading frames; Tiny metadata
Token commitments: palette #FFFFFF, #0D0E0C, #807D72, #ABA9A7, #28221A, #E7E6E6; type Europa-Grotesk; engine GSAP + Lenis linked (never vendored).
