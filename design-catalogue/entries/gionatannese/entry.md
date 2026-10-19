---
title: "Gionatan Nese"
url: https://www.gionatannese.com/
source_url: https://www.gionatannese.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: orbiting-thumbnail-ring
dna: "Multidisciplinary designer x orbiting object ring"
register: modern clean
grammar: gallery/catalog
lane: "A white folio where small project thumbnails orbit in a loose ring around the centre like a mobile, slowly re-sorting as the wheel turns, with only a name and a role at the edges."
mode: experience
traits: ["white ground, tiny type", "project thumbnails orbiting as a ring", "depth via scale and overlap", "wheel rotates the ring (virtual)", "name and role pinned to the edges"]
palette: ["#FFFFFF", "#E4E4E3", "#141614", "#CAC9CA", "#807D80"]
type: ["LayGrotesk", "Teodor"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The folio is a single object: a ring of small things (objects, garments, posters) slowly turning in space. Everything else is withheld, so the variety of the work is read as a collection before any single piece is.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Gionatan Nese).

## What to borrow (principle)

- Show a varied body of work as one rotating object so variety reads as range
- Keep chrome to two labels at the edges when the object is the page

## What to leave

- Thumbnails are too small to read without clicking
- The ring looks the same at every wheel step: no progression

## Signature move

A ring of project thumbnails orbiting the centre like a mobile.

## Motion

Intro: white, the name and role appear at the edges, then thumbnails fly in from scattered positions and settle into a ring (~1.5 s). Wheel (virtual, WebGL): the ring rotates in 3D, items passing in front and behind; hover enlarges an item. useGSAP + CustomEase.

Measured (`motion/probe.json`): GSAP 3.15.0; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a white folio where small project thumbnails orbit in a loose ring around the centre like a mobile, slowly re-sorting as the wheel turns, with only a name and a role at the edges. Type: LayGrotesk, Teodor.
Ground and ink from the measured palette (#FFFFFF, #E4E4E3, #141614). Motion carries the page through
a ring of project thumbnails orbiting the centre like a mobile. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product and object photography cut out on white, small and varied

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product and object photography cut out on white, small and varied

## Reference lock

Primary reference/direction: Gionatan Nese — A white folio where small project thumbnails orbit in a loose ring around the centre like a mobile, slowly re-sorting as the wheel turns, with only a name and a role at the edges.
Preserve (3-5 traits): white ground, tiny type; project thumbnails orbiting as a ring; depth via scale and overlap; wheel rotates the ring (virtual); name and role pinned to the edges.
Borrow only (1-2): Show a varied body of work as one rotating object so variety reads as range; Keep chrome to two labels at the edges when the object is the page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product and object photography cut out on white, small and varied
Reject: Thumbnails are too small to read without clicking; The ring looks the same at every wheel step: no progression
Token commitments: palette #FFFFFF, #E4E4E3, #141614, #CAC9CA, #807D80; type LayGrotesk, Teodor; engine GSAP + Lenis linked (never vendored).
