---
title: "T-Rex Leather - lab-grown leather bag"
url: https://lab-grown-leather.com/t-rex-leather
source_url: https://lab-grown-leather.com/t-rex-leather
captured: 2026-10-03
origin: raw-url
extract: none
category: luxury-craft
category2: "product-focused"
family: lab-specimen-product-film
dna: "Lab-grown leather x a 3D bag turning on a ruled white specimen sheet, inverted to X-ray and scattered into swatches"
register: modern clean
grammar: filmic one-shot
lane: "A product film for one bag: a black loader at 100 %, a white specimen sheet with ruler ticks down both edges and an inkblot creature over 'The world's first T-Rex leather', the green bag swings in from the corner and turns, '65 million years in the making', the page flips to black and the bag goes X-ray white with labelled hotspots (/re-engineered, /lab-grown), back to white with a video case, 'The world's first T-Rex leather bag' as a collage of photos that scatters outward, then dozens of leather swatches floating on white, gathering, and a final zoom into the grain."
mode: experience
traits: ["ruler ticks framing the page", "inkblot creature mark", "3D bag turning", "negative X-ray flip with hotspots", "photo collage that scatters", "floating leather swatches", "macro zoom into material"]
palette: ["#FFFFFF", "#000000", "#BABFC0", "#455252", "#151E1E"]
type: ["Helvetica"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Going from the whole bag to its scan to loose swatches to the grain itself tells a material story by zooming, so the claim 'lab-grown' is felt rather than read.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Gaspard Hedde).

## What to borrow (principle)

- Zoom the story from object to inside to material
- Flip to a negative for the technical chapter

## What to leave

- Tiny monospaced data labels

## Signature move

The green bag turning to X-ray white on black with labelled hotspots.

## Motion

Intro: loader count to 100 % (~3 s), the inkblot morphs. Wheel (Lenis, pin 1): the bag enters and rotates; ground inverts with a hard cut; hotspots fade in; the collage spreads out with depth; swatches drift and converge; a closing scale into the texture.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 pinned sections; Lenis; 2 video; smoothed scroll (median 155 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the filmic one-shot grammar: a product film for one bag: a black loader at 100 %, a white specimen sheet with ruler ticks down both edges and an inkblot creature over 'The world's first T-Rex leather', the green bag swings in from the corner and turns, '65 million years in the making', the page flips to black and the bag goes X-ray white with labelled hotspots (/re-engineered, /lab-grown), back to white with a video case, 'The world's first T-Rex leather bag' as a collage of photos that scatters outward, then dozens of leather swatches floating on white, gathering, and a final zoom into the grain. Type: Helvetica.
Ground and ink from the measured palette (#FFFFFF, #000000, #BABFC0). Motion carries the page through
the green bag turning to X-ray white on black with labelled hotspots. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D product render, material photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D product render, material photography

## Reference lock

Primary reference/direction: T-Rex Leather - lab-grown leather bag — A product film for one bag: a black loader at 100 %, a white specimen sheet with ruler ticks down both edges and an inkblot creature over 'The world's first T-Rex leather', the green bag swings in from the corner and turns, '65 million years in the making', the page flips to black and the bag goes X-ray white with labelled hotspots (/re-engineered, /lab-grown), back to white with a video case, 'The world's first T-Rex leather bag' as a collage of photos that scatters outward, then dozens of leather swatches floating on white, gathering, and a final zoom into the grain.
Preserve (3-5 traits): ruler ticks framing the page; inkblot creature mark; 3D bag turning; negative X-ray flip with hotspots; photo collage that scatters.
Borrow only (1-2): Zoom the story from object to inside to material; Flip to a negative for the technical chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D product render, material photography
Reject: Tiny monospaced data labels
Token commitments: palette #FFFFFF, #000000, #BABFC0, #455252, #151E1E; type Helvetica; engine GSAP + Lenis linked (never vendored).
