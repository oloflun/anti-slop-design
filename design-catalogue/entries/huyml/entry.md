---
title: "Huy Phan"
url: https://huyml.co/
source_url: https://huyml.co/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: tilted-plane-project-wheel
dna: "Designer folio x tilted 3D project carousel"
register: modern clean
grammar: gallery/catalog
lane: "A folio that opens with a cartoon character pushing a black panel off screen, then shows projects as images on a tilted 3D plane that rolls under the wheel while huge blurred index numbers pass along the bottom."
mode: experience
traits: ["character-led intro wipe", "red condensed serif name", "projects on a tilted 3D plane", "huge blurred index numbers along the bottom edge", "small project metadata blocks", "vertical rotated wordmark"]
palette: ["#EEEEEE", "#734D4D", "#C6B7B4"]
type: ["BT Grotesk Medium", "BT Grotesk Regular", "F37 Bolton Trial Regular", "BT Glyphius Regular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The intro has a personality: an illustrated figure physically shoves the black loading panel aside to reveal the page. After that the folio is a machine: project images ride a tilted plane like a conveyor, and the index number of the current project passes huge and motion-blurred at the bottom, which gives a sense of speed and position at once.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Huy Phan).

## What to borrow (principle)

- Have a character or object physically push the loader away so the transition has a cause
- Use a huge, motion-blurred index number as the progress indicator for a project wheel
- Put a project list on a tilted plane in perspective so a plain list reads as a space

## What to leave

- Virtual infinite scroll with tiny metadata text
- The plane crops images at the top edge

## Signature move

An illustrated kid shoving the black loader off the screen.

## Motion

Intro: black, then a cartoon figure walks in and pushes the black panel off to the right, revealing white and 'HUY PHAN' in red (~2.5 s). Wheel (virtual, ScrollSmoother, WebGL): project images travel up a tilted plane in perspective; the current index number (01–19) slides past at the bottom with heavy motion blur; metadata on the right swaps per project.

Measured (`motion/probe.json`): GSAP 3.13.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a folio that opens with a cartoon character pushing a black panel off screen, then shows projects as images on a tilted 3D plane that rolls under the wheel while huge blurred index numbers pass along the bottom. Type: BT Grotesk Medium, BT Grotesk Regular, F37 Bolton Trial Regular, BT Glyphius Regular.
Ground and ink from the measured palette (#EEEEEE, #734D4D, #C6B7B4). Motion carries the page through
an illustrated kid shoving the black loader off the screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — varied project stills and portraits, mixed colour, cropped as cards

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: varied project stills and portraits, mixed colour, cropped as cards

## Reference lock

Primary reference/direction: Huy Phan — A folio that opens with a cartoon character pushing a black panel off screen, then shows projects as images on a tilted 3D plane that rolls under the wheel while huge blurred index numbers pass along the bottom.
Preserve (3-5 traits): character-led intro wipe; red condensed serif name; projects on a tilted 3D plane; huge blurred index numbers along the bottom edge; small project metadata blocks.
Borrow only (1-2): Have a character or object physically push the loader away so the transition has a cause; Use a huge, motion-blurred index number as the progress indicator for a project wheel
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: varied project stills and portraits, mixed colour, cropped as cards
Reject: Virtual infinite scroll with tiny metadata text; The plane crops images at the top edge
Token commitments: palette #EEEEEE, #734D4D, #C6B7B4; type BT Grotesk Medium, BT Grotesk Regular, F37 Bolton Trial Regular, BT Glyphius Regular; engine GSAP + Lenis linked (never vendored).
