---
title: "Ousmane Dembele - Ne Pour Briller"
url: http://ousmaneballondor.fr/
source_url: http://ousmaneballondor.fr/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "editorial"
family: footballer-career-jersey-chapters
dna: "Ballon d'Or footballer story x one 3D jersey per club and full-colour chapters"
register: cinematic dark
grammar: chaptered editorial
lane: "A career story for Ousmane Dembele: a signature 'Ne pour briller' draws on cream, then each club is a chapter: the ground floods with the club colour (black for Evreux, red for Rennes, yellow for Dortmund, navy for Barca and PSG), the club name is brushed in script, a 3D jersey rotates in and is cut by a vertical stripe wipe, clips fly past, and a match photo shows with giant outline stats."
mode: read
traits: ["one 3D jersey per club", "club colour floods each chapter", "brush script club names", "vertical stripe wipe", "giant outline stat numerals", "signature drawn as intro"]
palette: ["#630709", "#0F0F0F", "#FCF9F1", "#D9D0BD", "#582628"]
type: ["Being", "Doner"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The jersey is the signature object that changes with the career, and every chapter uses the same choreography in a new colour, so a long biography reads as a fast, legible rhythm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One object that changes skin per chapter
- Flood the background with each chapter's colour

## What to leave

- Very long page
- Small body text

## Signature move

A 3D club jersey rotating in as the background floods with each club's colour.

## Motion

Intro: cream, the signature writes itself (~2 s). Wheel (Lenis ~150-190 px glide, 5 pins, 59 triggers, Taxi): the ground floods with the club colour; the brush name draws; a vertical stripe sweeps across as the jersey rotates in; photos fly in from the edges; the chapter ends on a full match photo with outline stats counting; then the next colour floods in.

Measured (`motion/probe.json`): GSAP 3.13.0; 59 ScrollTriggers; 5 pinned sections; Lenis; Taxi page transitions; WebGL canvas x2 (three.js); 14 video; smoothed scroll (median 184 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a career story for Ousmane Dembele: a signature 'Ne pour briller' draws on cream, then each club is a chapter: the ground floods with the club colour (black for Evreux, red for Rennes, yellow for Dortmund, navy for Barca and PSG), the club name is brushed in script, a 3D jersey rotates in and is cut by a vertical stripe wipe, clips fly past, and a match photo shows with giant outline stats. Type: Being, Doner.
Ground and ink from the measured palette (#630709, #0F0F0F, #FCF9F1). Motion carries the page through
a 3D club jersey rotating in as the background floods with each club's colour. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D jerseys, match photography, archive photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D jerseys, match photography, archive photos

## Reference lock

Primary reference/direction: Ousmane Dembele - Ne Pour Briller — A career story for Ousmane Dembele: a signature 'Ne pour briller' draws on cream, then each club is a chapter: the ground floods with the club colour (black for Evreux, red for Rennes, yellow for Dortmund, navy for Barca and PSG), the club name is brushed in script, a 3D jersey rotates in and is cut by a vertical stripe wipe, clips fly past, and a match photo shows with giant outline stats.
Preserve (3-5 traits): one 3D jersey per club; club colour floods each chapter; brush script club names; vertical stripe wipe; giant outline stat numerals.
Borrow only (1-2): One object that changes skin per chapter; Flood the background with each chapter's colour
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D jerseys, match photography, archive photos
Reject: Very long page; Small body text
Token commitments: palette #630709, #0F0F0F, #FCF9F1, #D9D0BD, #582628; type Being, Doner; engine GSAP + Lenis linked (never vendored).
