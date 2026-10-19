---
title: "Eliot Besson - Webflow Developer"
url: https://www.eliotbesson.com/
source_url: https://www.eliotbesson.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: venn-circles-dev-folio
dna: "Webflow developer x three Venn circles that rotate and merge"
register: cinematic dark
grammar: chaptered editorial
lane: "A developer folio on black: 'Crafting bold & memorable websites' in condensed caps with a project strip, 'I build websites at the intersection of:' with three circles (aesthetic, performance, strategy) rotating and merging into a Venn, a statement with inline icons, a list of project names large in condensed caps with thumbnails, and a templates showcase."
mode: persuade
traits: ["three rotating circles merging", "condensed caps headings", "inline icons in statements", "large project name list", "project strip", "dark ground"]
palette: ["#0D0D0D", "#88817D", "#CFCBCD", "#533A3B", "#F4F3F3"]
type: ["Aeonik", "Geist Mono", "Arges"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The Venn diagram animation makes the positioning (aesthetic + performance + strategy) a visible idea.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Animate a Venn of your three pillars merging

## What to leave

- Many near-empty frames

## Signature move

Three circles labelled aesthetic, performance and strategy rotating into a Venn.

## Motion

Intro: blurred headline sharpens, project strip slides (~1.5 s). Wheel (Lenis, 24 triggers): the strip scales; circles appear and rotate around a centre, then merge; the statement fills with icons; project names stack and fade.

Measured (`motion/probe.json`): GSAP 3.12.2; 24 ScrollTriggers; Lenis; 21 video; split text; smoothed scroll (median 104 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a developer folio on black: 'Crafting bold & memorable websites' in condensed caps with a project strip, 'I build websites at the intersection of:' with three circles (aesthetic, performance, strategy) rotating and merging into a Venn, a statement with inline icons, a list of project names large in condensed caps with thumbnails, and a templates showcase. Type: Aeonik, Geist Mono, Arges.
Ground and ink from the measured palette (#0D0D0D, #88817D, #CFCBCD). Motion carries the page through
three circles labelled aesthetic, performance and strategy rotating into a Venn. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — site screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: site screenshots

## Reference lock

Primary reference/direction: Eliot Besson - Webflow Developer — A developer folio on black: 'Crafting bold & memorable websites' in condensed caps with a project strip, 'I build websites at the intersection of:' with three circles (aesthetic, performance, strategy) rotating and merging into a Venn, a statement with inline icons, a list of project names large in condensed caps with thumbnails, and a templates showcase.
Preserve (3-5 traits): three rotating circles merging; condensed caps headings; inline icons in statements; large project name list; project strip.
Borrow only (1-2): Animate a Venn of your three pillars merging
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: site screenshots
Reject: Many near-empty frames
Token commitments: palette #0D0D0D, #88817D, #CFCBCD, #533A3B, #F4F3F3; type Aeonik, Geist Mono, Arges; engine GSAP + Lenis linked (never vendored).
