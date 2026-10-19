---
title: "Huy Nguyen - Portfolio"
url: https://ghuynguyen.vercel.app/
source_url: https://ghuynguyen.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: chrome-ribbon-designer-folio
dna: "Product designer x chrome ribbon behind the name and an orbit of project tiles"
register: cinematic dark
grammar: chaptered editorial
lane: "A designer folio: a small portrait card grows from white, a blurred chrome ribbon shape behind 'huy nguyen' on black, a statement that fills bold words, then 'Curiosity, friction, iteration' at the centre of faint orbit rings while project screenshots fly in and out around it, and a giant 'Work - Works' marquee."
mode: read
traits: ["portrait card expanding from white", "chrome ribbon shape", "statement with bold key words", "orbit rings with tiles flying around a centre line", "giant split marquee", "Flip transitions"]
palette: ["#0A0A0A", "#FFFFFF", "#2A2A2A", "#8A8A8A"]
type: ["Geist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The orbit of project tiles around one sentence turns the work into a cloud circling the designer's principle.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fly project tiles around a fixed principle sentence

## What to leave

- Very long dark gaps
- Small type

## Signature move

Project tiles flying around 'Curiosity, friction, iteration' inside faint orbit rings.

## Motion

Intro: white, a portrait card scales up into black (~2 s). Wheel (Lenis, 1 pin, Flip): the ribbon blurs and rotates; the statement fills; the centre line pins while tiles fly in from depth and out past the camera; rings rotate; the marquee runs at the end.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; smoothed scroll (median 170 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a designer folio: a small portrait card grows from white, a blurred chrome ribbon shape behind 'huy nguyen' on black, a statement that fills bold words, then 'Curiosity, friction, iteration' at the centre of faint orbit rings while project screenshots fly in and out around it, and a giant 'Work - Works' marquee. Type: Geist.
Ground and ink from the measured palette (#0A0A0A, #FFFFFF, #2A2A2A). Motion carries the page through
project tiles flying around 'Curiosity, friction, iteration' inside faint orbit rings. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — chrome render, project screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: chrome render, project screenshots

## Reference lock

Primary reference/direction: Huy Nguyen - Portfolio — A designer folio: a small portrait card grows from white, a blurred chrome ribbon shape behind 'huy nguyen' on black, a statement that fills bold words, then 'Curiosity, friction, iteration' at the centre of faint orbit rings while project screenshots fly in and out around it, and a giant 'Work - Works' marquee.
Preserve (3-5 traits): portrait card expanding from white; chrome ribbon shape; statement with bold key words; orbit rings with tiles flying around a centre line; giant split marquee.
Borrow only (1-2): Fly project tiles around a fixed principle sentence
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: chrome render, project screenshots
Reject: Very long dark gaps; Small type
Token commitments: palette #0A0A0A, #FFFFFF, #2A2A2A, #8A8A8A; type Geist; engine GSAP + Lenis linked (never vendored).
