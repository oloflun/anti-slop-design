---
title: "Filmbot"
url: https://filmbot.com/
source_url: https://filmbot.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: cinema-perforation-editorial
dna: "Indie cinema ticketing x film-strip graphics"
register: modern clean
grammar: chaptered editorial
lane: "A cinema-ticketing product that opens on a black curtain wipe into a white hero where photos sit inside film-perforation masks, then crosses into a dark red-lit auditorium half of the page with condensed headlines sliding in."
mode: persuade
traits: ["film-perforation shaped image masks", "condensed grotesque headlines in caps", "light-to-dark chapter change through a full-bleed red image", "scattered photo cluster that drifts at different speeds", "mono labels"]
palette: ["#F8F8F8", "#0C0C0D", "#871C27", "#AA9C9C"]
type: ["Font Sans Variable", "Font Mono Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The product (ticketing software) has no inherent image, so the page borrows the cinema itself: perforated mask shapes, a red neon lobby, an audience. The page runs light while it explains and turns dark when it shows the product in use, and the switch is carried by a full-bleed red motion-blurred photo rather than a hard section edge.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Eduard Bodak, Somefolk®).

## What to borrow (principle)

- Change the page ground through a full-bleed image that already contains both colours, not at a section border
- Cut images with a shape from the subject's world (film perforations) instead of rounded rectangles
- Let a cluster of photos drift at different rates so the section has depth without a pin

## What to leave

- Very small body copy in the dark half
- Condensed caps headlines cut mid-transition can read as broken on a slow scroll

## Signature move

A black-to-white curtain wipe that opens on photos masked as film-strip perforations.

## Motion

Intro: a white vertical bar wipes across black (curtain) and reveals the hero, ~1.2 s. Hero photos sit in perforation masks and shift on scroll. Statement paragraph fades from grey to ink per line. Photo cluster parallaxes at mixed speeds; a full-bleed red blur image scales up and the page turns dark. Condensed headlines ('BOLD WEBSITES', 'IPAD BOX OFFICE') slide in from below with SplitText; product screens rise in. Barba page transitions between routes.

Measured (`motion/probe.json`): GSAP 3.15.0; 25 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x1 (three.js); 3 video; split text; smoothed scroll (median 69 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a cinema-ticketing product that opens on a black curtain wipe into a white hero where photos sit inside film-perforation masks, then crosses into a dark red-lit auditorium half of the page with condensed headlines sliding in. Type: Font Sans Variable, Font Mono Variable.
Ground and ink from the measured palette (#F8F8F8, #0C0C0D, #871C27). Motion carries the page through
a black-to-white curtain wipe that opens on photos masked as film-strip perforations. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — documentary cinema photography: neon lobbies, audiences lit by the screen, motion blur, deep reds

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: documentary cinema photography: neon lobbies, audiences lit by the screen, motion blur, deep reds

## Reference lock

Primary reference/direction: Filmbot — A cinema-ticketing product that opens on a black curtain wipe into a white hero where photos sit inside film-perforation masks, then crosses into a dark red-lit auditorium half of the page with condensed headlines sliding in.
Preserve (3-5 traits): film-perforation shaped image masks; condensed grotesque headlines in caps; light-to-dark chapter change through a full-bleed red image; scattered photo cluster that drifts at different speeds; mono labels.
Borrow only (1-2): Change the page ground through a full-bleed image that already contains both colours, not at a section border; Cut images with a shape from the subject's world (film perforations) instead of rounded rectangles
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: documentary cinema photography: neon lobbies, audiences lit by the screen, motion blur, deep reds
Reject: Very small body copy in the dark half; Condensed caps headlines cut mid-transition can read as broken on a slow scroll
Token commitments: palette #F8F8F8, #0C0C0D, #871C27, #AA9C9C; type Font Sans Variable, Font Mono Variable; engine GSAP + Lenis linked (never vendored).
