---
title: "Pahari"
url: https://pahari.vercel.app/
source_url: https://pahari.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: ""
family: floating-miniature-gallery
dna: "Indian Pahari miniature collection x floating 3D gallery"
register: historical art
grammar: gallery/catalog
lane: "A digital gallery of Pahari miniature paintings floating in 3D over a parchment ground; the wheel moves the camera so paintings drift past and occasionally one comes close and large, with a toggle between sphere and cylinder views."
mode: experience
traits: ["parchment ground", "miniature paintings floating in 3D", "sphere/cylinder view toggle", "small serif title at centre", "camera drift on wheel"]
palette: ["#E8D8BD", "#4F453A", "#B8A486"]
type: ["Kalnia", "Elms Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Miniatures are small and dense; floating them at different depths lets one come close enough to read while the rest stay as a field. The parchment ground and tiny serif keep the gallery quiet so the paintings' colour carries everything.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Float a collection at depth so individual pieces come close in turn
- Offer a view toggle (sphere/cylinder) for one collection
- Parchment ground for historical art

## What to leave

- No reading path or captions in the field
- Virtual scroll without progress

## Signature move

Pahari miniatures drifting in 3D over parchment, one at a time coming close.

## Motion

Intro: 'Pahari' on parchment, then paintings gather at the centre and scatter outward (~2 s). Wheel (virtual, Lenis, WebGL): the camera moves through the field; paintings pass at different depths, some coming large into the foreground; view toggle switches arrangement.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the gallery/catalog grammar: a digital gallery of Pahari miniature paintings floating in 3D over a parchment ground; the wheel moves the camera so paintings drift past and occasionally one comes close and large, with a toggle between sphere and cylinder views. Type: Kalnia, Elms Sans.
Ground and ink from the measured palette (#E8D8BD, #4F453A, #B8A486). Motion carries the page through
pahari miniatures drifting in 3D over parchment, one at a time coming close. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — historical miniature paintings, rich pigments, on parchment

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: historical miniature paintings, rich pigments, on parchment

## Reference lock

Primary reference/direction: Pahari — A digital gallery of Pahari miniature paintings floating in 3D over a parchment ground; the wheel moves the camera so paintings drift past and occasionally one comes close and large, with a toggle between sphere and cylinder views.
Preserve (3-5 traits): parchment ground; miniature paintings floating in 3D; sphere/cylinder view toggle; small serif title at centre; camera drift on wheel.
Borrow only (1-2): Float a collection at depth so individual pieces come close in turn; Offer a view toggle (sphere/cylinder) for one collection
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: historical miniature paintings, rich pigments, on parchment
Reject: No reading path or captions in the field; Virtual scroll without progress
Token commitments: palette #E8D8BD, #4F453A, #B8A486; type Kalnia, Elms Sans; engine GSAP + Lenis linked (never vendored).
