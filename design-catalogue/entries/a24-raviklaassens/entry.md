---
title: "A24 Films (concept)"
url: https://a24.raviklaassens.com/
source_url: https://a24.raviklaassens.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: disc-carousel-catalogue
dna: "Film studio catalogue x physical DVD discs"
register: modern clean
grammar: gallery/catalog
lane: "A pale-grey film catalogue where every title is a printed DVD disc in a tilted 3D row that you drag and fling, with a small serif title and credits updating in the corner."
mode: experience
traits: ["films as 3D printed discs", "drag and inertia carousel", "counter preloader 0 to 100", "small high-contrast serif titles", "credits block with hairlines", "press quotes with star ratings"]
palette: ["#F0F0F0", "#211F1E", "#7C7359", "#9D9A93", "#5E4835", "#D4D4D3"]
type: ["Ppneuemontreal", "Ppmuseum", "Ppeiko"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The catalogue turns a list of films into objects you can handle: each film is its disc, printed with its key art, sitting in a tilted row with real perspective. The chrome is almost nothing (tiny serif titles, a hairline credits table), so the discs are the interface.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Ravi Klaassens).

## What to borrow (principle)

- Make catalogue items physical objects with depth and let the visitor drag through them with inertia
- Keep chrome to a small serif title and a credits table so the objects carry the page
- Counter preloader whose last number hands straight to the first object

## What to leave

- No scroll path: the content lives in drag only, invisible to a wheel user
- Discs at the edges are cropped hard with no hint of how many remain

## Signature move

Films as printed DVD discs in a tilted 3D row you drag and fling.

## Motion

Intro: counter 0→100 at the bottom, 'A24' in serif, then a single disc spins in centre and the row slides in from the right (~2.5 s). Interaction (Observer/Draggable + Inertia, WebGL): dragging or wheeling moves the disc row horizontally with momentum; the active title and credits swap in the top-left; reviews fade in under the active disc. Barba transitions to film pages; Flip used between list and detail.

Measured (`motion/probe.json`): GSAP 3.15.0; 1 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x1 (three.js); virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the gallery/catalog grammar: a pale-grey film catalogue where every title is a printed DVD disc in a tilted 3D row that you drag and fling, with a small serif title and credits updating in the corner. Type: Ppneuemontreal, Ppmuseum, Ppeiko.
Ground and ink from the measured palette (#F0F0F0, #211F1E, #7C7359). Motion carries the page through
films as printed DVD discs in a tilted 3D row you drag and fling. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — key art printed on a physical object, product-shot lighting, pale neutral ground

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: key art printed on a physical object, product-shot lighting, pale neutral ground

## Reference lock

Primary reference/direction: A24 Films (concept) — A pale-grey film catalogue where every title is a printed DVD disc in a tilted 3D row that you drag and fling, with a small serif title and credits updating in the corner.
Preserve (3-5 traits): films as 3D printed discs; drag and inertia carousel; counter preloader 0 to 100; small high-contrast serif titles; credits block with hairlines.
Borrow only (1-2): Make catalogue items physical objects with depth and let the visitor drag through them with inertia; Keep chrome to a small serif title and a credits table so the objects carry the page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: key art printed on a physical object, product-shot lighting, pale neutral ground
Reject: No scroll path: the content lives in drag only, invisible to a wheel user; Discs at the edges are cropped hard with no hint of how many remain
Token commitments: palette #F0F0F0, #211F1E, #7C7359, #9D9A93, #5E4835, #D4D4D3; type Ppneuemontreal, Ppmuseum, Ppeiko; engine GSAP + Lenis linked (never vendored).
