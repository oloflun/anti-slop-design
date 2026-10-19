---
title: "Caeli Energie - Air conditioning"
url: https://www.caeli-energie.com/
source_url: https://www.caeli-energie.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: product-hero-wall-unit
dna: "French cooling unit maker x the product shrinking onto a wall in a room"
register: modern clean
grammar: chaptered editorial
lane: "A cooling product: green loader with a drop icon, 'La revolution fraiche' in big green caps behind a tall white unit that then shrinks and settles onto a wall in a living room, 'CAELI ONE' with the unit standing in the middle of the word, a performance card over the room, dark green 'Fabriquer localement / Des solutions de rafraichissement durables' statements and application photos."
mode: persuade
traits: ["product shrinking into context", "product standing inside the name", "green and cream palette", "heavy rounded caps", "statement fills on dark green", "room photography"]
palette: ["#FFFFFF", "#E4E3D9", "#727D65"]
type: ["Altform"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Shrinking the product from hero object to a small thing on a real wall shows its size and place in one move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Shrink the hero product into the room it belongs in
- Set the product inside its name

## What to leave

- Cookie panel over frames

## Signature move

A white cooling unit shrinking from hero size onto a living-room wall.

## Motion

Intro: green with a drop icon (~2 s), the hero. Wheel (Taxi): the headline fades; the unit scales down and the room fades in around it; 'CAELI ONE' letters fill around the unit; the room card slides; dark green statements fill word by word; photos slide.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a cooling product: green loader with a drop icon, 'La revolution fraiche' in big green caps behind a tall white unit that then shrinks and settles onto a wall in a living room, 'CAELI ONE' with the unit standing in the middle of the word, a performance card over the room, dark green 'Fabriquer localement / Des solutions de rafraichissement durables' statements and application photos. Type: Altform.
Ground and ink from the measured palette (#FFFFFF, #E4E3D9, #727D65). Motion carries the page through
a white cooling unit shrinking from hero size onto a living-room wall. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product render, interior photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product render, interior photography

## Reference lock

Primary reference/direction: Caeli Energie - Air conditioning — A cooling product: green loader with a drop icon, 'La revolution fraiche' in big green caps behind a tall white unit that then shrinks and settles onto a wall in a living room, 'CAELI ONE' with the unit standing in the middle of the word, a performance card over the room, dark green 'Fabriquer localement / Des solutions de rafraichissement durables' statements and application photos.
Preserve (3-5 traits): product shrinking into context; product standing inside the name; green and cream palette; heavy rounded caps; statement fills on dark green.
Borrow only (1-2): Shrink the hero product into the room it belongs in; Set the product inside its name
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product render, interior photography
Reject: Cookie panel over frames
Token commitments: palette #FFFFFF, #E4E3D9, #727D65; type Altform; engine GSAP + Lenis linked (never vendored).
