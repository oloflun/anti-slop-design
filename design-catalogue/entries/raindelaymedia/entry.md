---
title: "Rain Delay Media - sports podcasts"
url: https://www.raindelaymedia.com/
source_url: https://www.raindelaymedia.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "editorial"
family: sports-podcast-show-grid
dna: "Sports podcast network x stacked show cards and accordion services"
register: modern clean
grammar: chaptered editorial
lane: "A podcast network: a blue wipe, 'RAIN DELAY' split heavy condensed with partner logos between, a video, show cards that stack as you scroll (Road Trippin', Club 30, Kickin' It) with hosts cut out, 'Other shows' as a grid of cover art, services as a vertical accordion (Consultation, Development, Production, Packaging, Promotion) and 'Advantages'."
mode: persuade
traits: ["split heavy condensed title", "stacked show cards", "host cut-outs", "cover art grid", "vertical tab accordion", "blue nav pill"]
palette: ["#EEEDF2", "#131113", "#6E696C", "#4F4136", "#B8B4B7"]
type: ["Pprightgrotesk", "Ppradiogrotesk", "Ppformula"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The show cards stacking like a deck keeps the flagship shows in focus before the grid.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stack the flagship cards, then open the full grid

## What to leave

- Empty dark video frames

## Signature move

Show cards with host cut-outs stacking over each other.

## Motion

Intro: a blue wipe (~1 s), the split title. Wheel (Lenis): logos cycle; the video card rises; show cards stack; the grid slides in; accordion tabs open sideways.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; smoothed scroll (median 101 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a podcast network: a blue wipe, 'RAIN DELAY' split heavy condensed with partner logos between, a video, show cards that stack as you scroll (Road Trippin', Club 30, Kickin' It) with hosts cut out, 'Other shows' as a grid of cover art, services as a vertical accordion (Consultation, Development, Production, Packaging, Promotion) and 'Advantages'. Type: Pprightgrotesk, Ppradiogrotesk, Ppformula.
Ground and ink from the measured palette (#EEEDF2, #131113, #6E696C). Motion carries the page through
show cards with host cut-outs stacking over each other. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — host photography, cover art

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: host photography, cover art

## Reference lock

Primary reference/direction: Rain Delay Media - sports podcasts — A podcast network: a blue wipe, 'RAIN DELAY' split heavy condensed with partner logos between, a video, show cards that stack as you scroll (Road Trippin', Club 30, Kickin' It) with hosts cut out, 'Other shows' as a grid of cover art, services as a vertical accordion (Consultation, Development, Production, Packaging, Promotion) and 'Advantages'.
Preserve (3-5 traits): split heavy condensed title; stacked show cards; host cut-outs; cover art grid; vertical tab accordion.
Borrow only (1-2): Stack the flagship cards, then open the full grid
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: host photography, cover art
Reject: Empty dark video frames
Token commitments: palette #EEEDF2, #131113, #6E696C, #4F4136, #B8B4B7; type Pprightgrotesk, Ppradiogrotesk, Ppformula; engine GSAP + Lenis linked (never vendored).
