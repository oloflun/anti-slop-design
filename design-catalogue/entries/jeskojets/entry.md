---
title: "Jesko Jets - Private Jet Charter"
url: http://jeskojets.com/
source_url: http://jeskojets.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "hospitality"
family: through-the-window-jet-charter
dna: "Private jet charter x flight through the cabin window into clouds"
register: warm photographic
grammar: filmic one-shot
lane: "A private jet charter: brown intro, then you look through a cabin window at clouds and fly through it into the sky, a blue statement fades over the clouds, the sky pales to cream, 'Fly in Luxury' splits as a top-down jet descends between the words, the jet becomes a spec sheet and seating plan, then interior photos, a departures board ('Fly anywhere > Doha') and a dark 'Global' section with a globe and a boarding-pass card."
mode: persuade
traits: ["push through the cabin window", "sky that warms from blue to cream", "jet descending between split words", "jet becomes a seating plan", "departures board ticker", "boarding-pass card over a globe"]
palette: ["#31271E", "#AAC7DC", "#5C98C4", "#3C84B6", "#6D635A", "#8E9091"]
type: ["GT America Expanded", "GT America Extended"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Every section is a step of a flight (window, sky, aircraft, cabin, destination, global) and each change has a physical cause, so the page reads as one continuous trip.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: The First The Last).

## What to borrow (principle)

- Enter the page through a window
- Let the hero object turn into its own diagram

## What to leave

- Small spec text
- Brown-black ending is heavy

## Signature move

Flying through a cabin window into clouds before a jet descends between 'Fly in' and 'Luxury'.

## Motion

Intro: brown ground, 'Private jet charter worldwide' fades in (~2 s), then the cabin window. Wheel (Lenis ~110 px glide, 59 triggers): the camera pushes through the window into clouds; the statement fills word by word; clouds thin to cream; the jet drops top-down between the split words and scales up until its wings fill the frame, then fades to a seating plan with specs; interior images slide in; the board ticks destinations; the globe rises with a boarding pass card. Barba page transitions.

Measured (`motion/probe.json`): GSAP 3.13.0; 59 ScrollTriggers; Lenis; Barba page transitions; WebGL canvas x1 (three.js); split text; smoothed scroll (median 141 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: a private jet charter: brown intro, then you look through a cabin window at clouds and fly through it into the sky, a blue statement fades over the clouds, the sky pales to cream, 'Fly in Luxury' splits as a top-down jet descends between the words, the jet becomes a spec sheet and seating plan, then interior photos, a departures board ('Fly anywhere > Doha') and a dark 'Global' section with a globe and a boarding-pass card. Type: GT America Expanded, GT America Extended.
Ground and ink from the measured palette (#31271E, #AAC7DC, #5C98C4). Motion carries the page through
flying through a cabin window into clouds before a jet descends between 'Fly in' and 'Luxury'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — aviation renders, cloud footage, cabin photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: aviation renders, cloud footage, cabin photography

## Reference lock

Primary reference/direction: Jesko Jets - Private Jet Charter — A private jet charter: brown intro, then you look through a cabin window at clouds and fly through it into the sky, a blue statement fades over the clouds, the sky pales to cream, 'Fly in Luxury' splits as a top-down jet descends between the words, the jet becomes a spec sheet and seating plan, then interior photos, a departures board ('Fly anywhere > Doha') and a dark 'Global' section with a globe and a boarding-pass card.
Preserve (3-5 traits): push through the cabin window; sky that warms from blue to cream; jet descending between split words; jet becomes a seating plan; departures board ticker.
Borrow only (1-2): Enter the page through a window; Let the hero object turn into its own diagram
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: aviation renders, cloud footage, cabin photography
Reject: Small spec text; Brown-black ending is heavy
Token commitments: palette #31271E, #AAC7DC, #5C98C4, #3C84B6, #6D635A, #8E9091; type GT America Expanded, GT America Extended; engine GSAP + Lenis linked (never vendored).
