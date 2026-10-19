---
title: "Immersive Garden - digital experiences studio"
url: https://immersive-g.com/
source_url: https://immersive-g.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: plaster-relief-luxury-studio
dna: "Luxury digital studio x a soft grey plaster relief of leaves and figures, a light serif statement and framed WebGL project windows"
register: editorial print
grammar: chaptered editorial
lane: "A luxury digital studio: a line of serif 'Innovative digital experiences studio', then a grey plaster wall with sculpted leaves and hands in relief, 'Transcend anything seen or felt before…' in a light serif, a project window (a dark conservatory with a screen) rising and growing, 'Our approach' centred, and case windows (a pink lake with a glass trunk, a quilted monogram) drifting over the relief beside short captions."
mode: persuade
traits: ["plaster relief ground", "light serif statements", "project windows over a sculpted wall", "muted grey palette", "cases as drifting framed windows"]
palette: ["#C0C0C0", "#384040", "#9FA19F"]
type: ["PSTimes", "HelveticaNeueRegular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A sculpted plaster wall gives a digital studio a tactile, gallery-like ground that the colourful project windows can glow against.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Use a tactile relief as the page's ground so screens read as objects in a room

## What to leave

- Very small captions

## Signature move

Grey plaster relief of leaves and hands behind a light serif statement.

## Motion

Intro: one line of serif fades in (~2 s). Wheel: the relief parallaxes; project windows rise and scale; text fades between.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); split text; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a luxury digital studio: a line of serif 'Innovative digital experiences studio', then a grey plaster wall with sculpted leaves and hands in relief, 'Transcend anything seen or felt before…' in a light serif, a project window (a dark conservatory with a screen) rising and growing, 'Our approach' centred, and case windows (a pink lake with a glass trunk, a quilted monogram) drifting over the relief beside short captions. Type: PSTimes, HelveticaNeueRegular.
Ground and ink from the measured palette (#C0C0C0, #384040, #9FA19F). Motion carries the page through
grey plaster relief of leaves and hands behind a light serif statement. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D plaster render, WebGL project scenes

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D plaster render, WebGL project scenes

## Reference lock

Primary reference/direction: Immersive Garden - digital experiences studio — A luxury digital studio: a line of serif 'Innovative digital experiences studio', then a grey plaster wall with sculpted leaves and hands in relief, 'Transcend anything seen or felt before…' in a light serif, a project window (a dark conservatory with a screen) rising and growing, 'Our approach' centred, and case windows (a pink lake with a glass trunk, a quilted monogram) drifting over the relief beside short captions.
Preserve (3-5 traits): plaster relief ground; light serif statements; project windows over a sculpted wall; muted grey palette; cases as drifting framed windows.
Borrow only (1-2): Use a tactile relief as the page's ground so screens read as objects in a room
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D plaster render, WebGL project scenes
Reject: Very small captions
Token commitments: palette #C0C0C0, #384040, #9FA19F; type PSTimes, HelveticaNeueRegular; engine GSAP + Lenis linked (never vendored).
