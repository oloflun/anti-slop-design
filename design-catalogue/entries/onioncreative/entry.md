---
title: "Onion Creative Studio"
url: https://www.onioncreative.studio/
source_url: https://www.onioncreative.studio/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: laptop-on-desk-case-reel
dna: "Web studio x one laptop on a dark desk whose screen and setting change per case"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A studio folio on dark green: a giant 'onion' wordmark rising, then a fixed left column ('Onion Creative Studio') beside a laptop on a desk whose screen and surroundings change for each case (Effortel dashboards, Milena Alexandrova on lilac, Addifico on green glow, Xteam on blue, Handplayed on a wooden chair), with small thumbnails in a row above and the case name below."
mode: read
traits: ["one laptop as the stage", "setting colour changes per case", "fixed left column", "thumbnail row", "giant wordmark", "case name caption"]
palette: ["#222C29", "#8389A7", "#0E1111", "#C6D4D5"]
type: ["Onion Sans", "Et Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Keeping one laptop in place and changing its world per case makes a case list feel like one continuous film.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Keep one device fixed and change its screen and setting per case

## What to leave

- Repetitive after a few cases

## Signature move

A laptop on a desk whose screen and backdrop change per case.

## Motion

Intro: dark green (~1.5 s), 'onion' rises. Wheel: the wordmark sinks and fades; the laptop holds while its screen slides to the next site and the backdrop colour crossfades; thumbnails step; captions swap.

Measured (`motion/probe.json`): GSAP 3.12.7; 6 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: LAUNCH PROJECT, LAUNCH PROJECT. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a studio folio on dark green: a giant 'onion' wordmark rising, then a fixed left column ('Onion Creative Studio') beside a laptop on a desk whose screen and surroundings change for each case (Effortel dashboards, Milena Alexandrova on lilac, Addifico on green glow, Xteam on blue, Handplayed on a wooden chair), with small thumbnails in a row above and the case name below. Type: Onion Sans, Et Mono.
Ground and ink from the measured palette (#222C29, #8389A7, #0E1111). Motion carries the page through
a laptop on a desk whose screen and backdrop change per case. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — device photography, site screenshots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: device photography, site screenshots

## Reference lock

Primary reference/direction: Onion Creative Studio — A studio folio on dark green: a giant 'onion' wordmark rising, then a fixed left column ('Onion Creative Studio') beside a laptop on a desk whose screen and surroundings change for each case (Effortel dashboards, Milena Alexandrova on lilac, Addifico on green glow, Xteam on blue, Handplayed on a wooden chair), with small thumbnails in a row above and the case name below.
Preserve (3-5 traits): one laptop as the stage; setting colour changes per case; fixed left column; thumbnail row; giant wordmark.
Borrow only (1-2): Keep one device fixed and change its screen and setting per case
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: device photography, site screenshots
Reject: Repetitive after a few cases
Token commitments: palette #222C29, #8389A7, #0E1111, #C6D4D5; type Onion Sans, Et Mono; engine GSAP + Lenis linked (never vendored).
