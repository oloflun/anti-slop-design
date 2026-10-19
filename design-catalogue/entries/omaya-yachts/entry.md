---
title: "OMAYA Yachts - Next-Gen Power Catamarans"
url: https://www.omaya-yachts.com/
source_url: https://www.omaya-yachts.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "consumer-brand"
family: shell-logo-yacht-film
dna: "Power catamaran maker x shell logo loader and a cinematic lifestyle film"
register: warm photographic
grammar: filmic one-shot
lane: "A yacht builder: a teal shell logo on cream with a counter, a shell photo that dissolves into a boy on deck, then a full-bleed lifestyle film (sunset, friends sunbathing, dolphins, swimming, aerial deck, helm) under 'OMAYA - Your shell of comfort', which becomes 'Next generation power catamarans', 'Space for thought', 'Comfort without clutter' and 'Freedom to move' as the boat moves."
mode: persuade
traits: ["shell logo and shell photo", "full-bleed lifestyle film", "line of copy changing over film", "aerial drone shots", "quick anchors nav", "SKIP INTRO"]
palette: ["#604B40", "#487E8D", "#1A282A", "#A8BCBE", "#6CA9BE", "#C5A586"]
type: ["Sourcesans 3", "Ppgatwick", "PT Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The film is the page: one continuous sequence of a day at sea with the copy changing over it, so the brand sells a feeling before any spec.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Branda Studio).

## What to borrow (principle)

- Run one film under the hero and change the line of copy as it plays
- A real object (the shell) dissolving into the first shot

## What to leave

- Cookie bar over the film
- Long before any product information

## Signature move

A shell dissolving into a lifestyle film of a day at sea under 'Your shell of comfort'.

## Motion

Intro: cream with the shell logo and a counter (~2 s), then a shell photo cross-dissolves into the film. ENTER WITHOUT SOUND (unlocked). Wheel (Lenis, 7 pins, 36 triggers): the film keeps playing pinned while the headline changes; the aerial shot sets the boat in the centre and copy appears below; the stern shot holds as lines fade between; it cuts to the interior and then to black for 'Freedom to move'.

Measured (`motion/probe.json`): GSAP 3.15.0; 36 ScrollTriggers; 7 pinned sections; Lenis; 6 video; split text; smoothed scroll (median 208 px still travelling after input stops); entry gate: ENTER WITHOUT SOUND. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the filmic one-shot grammar: a yacht builder: a teal shell logo on cream with a counter, a shell photo that dissolves into a boy on deck, then a full-bleed lifestyle film (sunset, friends sunbathing, dolphins, swimming, aerial deck, helm) under 'OMAYA - Your shell of comfort', which becomes 'Next generation power catamarans', 'Space for thought', 'Comfort without clutter' and 'Freedom to move' as the boat moves. Type: Sourcesans 3, Ppgatwick, PT Sans.
Ground and ink from the measured palette (#604B40, #487E8D, #1A282A). Motion carries the page through
a shell dissolving into a lifestyle film of a day at sea under 'Your shell of comfort'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — yacht lifestyle film

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: yacht lifestyle film

## Reference lock

Primary reference/direction: OMAYA Yachts - Next-Gen Power Catamarans — A yacht builder: a teal shell logo on cream with a counter, a shell photo that dissolves into a boy on deck, then a full-bleed lifestyle film (sunset, friends sunbathing, dolphins, swimming, aerial deck, helm) under 'OMAYA - Your shell of comfort', which becomes 'Next generation power catamarans', 'Space for thought', 'Comfort without clutter' and 'Freedom to move' as the boat moves.
Preserve (3-5 traits): shell logo and shell photo; full-bleed lifestyle film; line of copy changing over film; aerial drone shots; quick anchors nav.
Borrow only (1-2): Run one film under the hero and change the line of copy as it plays; A real object (the shell) dissolving into the first shot
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: yacht lifestyle film
Reject: Cookie bar over the film; Long before any product information
Token commitments: palette #604B40, #487E8D, #1A282A, #A8BCBE, #6CA9BE, #C5A586; type Sourcesans 3, Ppgatwick, PT Sans; engine GSAP + Lenis linked (never vendored).
