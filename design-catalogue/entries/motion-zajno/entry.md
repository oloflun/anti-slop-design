---
title: "Zajno - Motion design principles"
url: https://motion.zajno.com/
source_url: https://motion.zajno.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "portfolio"
family: pastel-chapter-motion-guide
dna: "Motion design guide x pastel chapter grounds, a black dot that hops between chapters and framed live examples"
register: modern clean
grammar: chaptered editorial
lane: "A guide to animation principles: a loader where a dot bounces, 'Principles' on black, a statement in caps with the dot hopping beside it, phone and site examples in frames, a ball pit illustrating real-time interaction, pastel chapters (the basics of easing, offset and delay, transformation, masking, parallax, zoom) each with a giant 'Implementation examples' heading and framed video examples, and a cloud close."
mode: read
traits: ["bouncing dot as guide", "pastel ground per chapter", "framed live examples", "numbered principles", "giant chapter headings"]
palette: ["#FEFCFB", "#0A0A0A", "#B3B2B2"]
type: ["Magilio-400", "Pp-neuemachina-Plain", "Pp-neuemachina-Inktrap"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each principle is shown moving in a frame next to its name, so the reader learns by watching rather than reading.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Zajno).

## What to borrow (principle)

- Show each principle running next to its definition

## What to leave

- Repetitive giant headings

## Signature move

A black dot hopping between chapters of a motion guide.

## Motion

Intro: bouncing dot (~3 s). Wheel (Lenis, 4 pins, 46 triggers): the dot travels; grounds change per chapter; example frames play video; headings slide.

Measured (`motion/probe.json`): GSAP 3.10.4; 46 ScrollTriggers; 4 pinned sections; Lenis; 52 video; smoothed scroll (median 231 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a guide to animation principles: a loader where a dot bounces, 'Principles' on black, a statement in caps with the dot hopping beside it, phone and site examples in frames, a ball pit illustrating real-time interaction, pastel chapters (the basics of easing, offset and delay, transformation, masking, parallax, zoom) each with a giant 'Implementation examples' heading and framed video examples, and a cloud close. Type: Magilio-400, Pp-neuemachina-Plain, Pp-neuemachina-Inktrap.
Ground and ink from the measured palette (#FEFCFB, #0A0A0A, #B3B2B2). Motion carries the page through
a black dot hopping between chapters of a motion guide. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — video examples, illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: video examples, illustration

## Reference lock

Primary reference/direction: Zajno - Motion design principles — A guide to animation principles: a loader where a dot bounces, 'Principles' on black, a statement in caps with the dot hopping beside it, phone and site examples in frames, a ball pit illustrating real-time interaction, pastel chapters (the basics of easing, offset and delay, transformation, masking, parallax, zoom) each with a giant 'Implementation examples' heading and framed video examples, and a cloud close.
Preserve (3-5 traits): bouncing dot as guide; pastel ground per chapter; framed live examples; numbered principles; giant chapter headings.
Borrow only (1-2): Show each principle running next to its definition
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: video examples, illustration
Reject: Repetitive giant headings
Token commitments: palette #FEFCFB, #0A0A0A, #B3B2B2; type Magilio-400, Pp-neuemachina-Plain, Pp-neuemachina-Inktrap; engine GSAP + Lenis linked (never vendored).
