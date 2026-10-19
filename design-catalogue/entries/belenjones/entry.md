---
title: "Belen Jones"
url: https://belenjones.com/
source_url: https://belenjones.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: rotating-box-name-list
dna: "Creative director folio x 3D project box over a client list"
register: modern clean
grammar: gallery/catalog
lane: "A folio where a list of clients (ASAP Rocky, Bvlgari, Gant, Trident…) is set huge in outlined wide caps, and a single 3D box rotates over it, each face showing the active client's work while that name fills in solid."
mode: experience
traits: ["huge outlined wide caps list (Monument Extended)", "one rotating 3D box with project media on its faces", "active name filled solid, rest outlined", "ground colour changing per project", "loading label on black"]
palette: ["#BFC7DA", "#1C1C19", "#E8DBCF", "#8B8986", "#B6B5B4", "#706660"]
type: ["Monument Extended Regular", "Monument Extended Ultrabold", "Robotomono Regular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The client list is the page and the box is the viewer: as the wheel turns, the box rotates to a new face with that project's film, the matching name in the list turns solid, and the background takes the project's colour. One object, one list, nothing else.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use one rotating 3D object as the media viewer over a typographic index
- Fill the active item of an outlined list solid as the selection
- Change the page ground colour per project

## What to leave

- Wheel-only; the list is not clickable in the captures
- Box covers most of the names

## Signature move

A 3D box rotating over a giant outlined client list, each face a different project.

## Motion

Intro: black with a small 'loading' label (~2.5 s). Wheel (virtual, WebGL): the box rotates face by face; each face plays the project film; the corresponding name fills solid while the ground shifts colour (blush, beige, grey, yellow, lavender).

Measured (`motion/probe.json`): GSAP 3.12.4; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a folio where a list of clients (ASAP Rocky, Bvlgari, Gant, Trident…) is set huge in outlined wide caps, and a single 3D box rotates over it, each face showing the active client's work while that name fills in solid. Type: Monument Extended Regular, Monument Extended Ultrabold, Robotomono Regular.
Ground and ink from the measured palette (#BFC7DA, #1C1C19, #E8DBCF). Motion carries the page through
a 3D box rotating over a giant outlined client list, each face a different project. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign films and editorial stills mapped onto box faces

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign films and editorial stills mapped onto box faces

## Reference lock

Primary reference/direction: Belen Jones — A folio where a list of clients (ASAP Rocky, Bvlgari, Gant, Trident…) is set huge in outlined wide caps, and a single 3D box rotates over it, each face showing the active client's work while that name fills in solid.
Preserve (3-5 traits): huge outlined wide caps list (Monument Extended); one rotating 3D box with project media on its faces; active name filled solid, rest outlined; ground colour changing per project; loading label on black.
Borrow only (1-2): Use one rotating 3D object as the media viewer over a typographic index; Fill the active item of an outlined list solid as the selection
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign films and editorial stills mapped onto box faces
Reject: Wheel-only; the list is not clickable in the captures; Box covers most of the names
Token commitments: palette #BFC7DA, #1C1C19, #E8DBCF, #8B8986, #B6B5B4, #706660; type Monument Extended Regular, Monument Extended Ultrabold, Robotomono Regular; engine GSAP + Lenis linked (never vendored).
