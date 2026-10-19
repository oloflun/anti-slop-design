---
title: "smllns portfolio"
url: http://smllns-portfolio.vercel.app/
source_url: http://smllns-portfolio.vercel.app/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: flower-doodle-dev-folio
dna: "Frontend developer x doodled flowers and a scalloped circle reveal"
register: illustrated dark
grammar: chaptered editorial
lane: "A small developer folio: a hand-drawn flower draws itself on black inside a wavy yellow ring that expands, colourful flowers scatter, a white circle rises with 'Frontend Developer' and a flower-framed portrait, a project list on black with flower ornaments, and a 'Let's work together' marquee over a scalloped black footer with a 'Download CV' between drawn arrows."
mode: persuade
traits: ["flower drawn line by line", "wavy ring expanding", "scattered colourful flower doodles", "slab serif uppercase", "rising white circle reveal", "scalloped footer edge"]
palette: ["#171717", "#F6F6F6", "#8C8781"]
type: ["Holtwood One SC", "Roboto"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The doodled flower is the signature object; it draws the intro, decorates the portrait and edges the footer, so a tiny folio has a full personality.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One doodle motif that draws the intro and frames the ending
- A circle that rises to flip the page from black to white

## What to leave

- Very short page
- Small project list

## Signature move

A hand-drawn flower drawing itself inside an expanding wavy ring.

## Motion

Intro: black, a flower stem draws, petals draw in, a yellow wavy ring grows around it and expands off screen (~3 s). Wheel (Lenis, short): flowers pop in around the top; a white circle rises from the bottom and grows into the about section; the project list slides; the white circle returns for the CTA; the marquee runs.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; smoothed scroll (median 129 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a small developer folio: a hand-drawn flower draws itself on black inside a wavy yellow ring that expands, colourful flowers scatter, a white circle rises with 'Frontend Developer' and a flower-framed portrait, a project list on black with flower ornaments, and a 'Let's work together' marquee over a scalloped black footer with a 'Download CV' between drawn arrows. Type: Holtwood One SC, Roboto.
Ground and ink from the measured palette (#171717, #F6F6F6, #8C8781). Motion carries the page through
a hand-drawn flower drawing itself inside an expanding wavy ring. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — doodled flowers, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: doodled flowers, portrait

## Reference lock

Primary reference/direction: smllns portfolio — A small developer folio: a hand-drawn flower draws itself on black inside a wavy yellow ring that expands, colourful flowers scatter, a white circle rises with 'Frontend Developer' and a flower-framed portrait, a project list on black with flower ornaments, and a 'Let's work together' marquee over a scalloped black footer with a 'Download CV' between drawn arrows.
Preserve (3-5 traits): flower drawn line by line; wavy ring expanding; scattered colourful flower doodles; slab serif uppercase; rising white circle reveal.
Borrow only (1-2): One doodle motif that draws the intro and frames the ending; A circle that rises to flip the page from black to white
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: doodled flowers, portrait
Reject: Very short page; Small project list
Token commitments: palette #171717, #F6F6F6, #8C8781; type Holtwood One SC, Roboto; engine GSAP + Lenis linked (never vendored).
