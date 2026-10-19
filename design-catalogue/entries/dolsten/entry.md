---
title: "Dolsten and Co. - AI-first creative studio"
url: https://dolsten.com/
source_url: https://dolsten.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "luxury-craft"
family: blooming-flower-ai-studio
dna: "AI creative studio x a peony that blooms as the tagline word changes"
register: modern clean
grammar: chaptered editorial
lane: "An AI studio on blush: a dark bud that opens into a cream peony as 'We make AI ___' changes word (come alive, beautiful, emotional, larger than life, engaging, drive business), a featured tennis film, a statement, logos, a giant '1' for awards, work films (Starlink, a red panda), services and the flower returning at the end."
mode: persuade
traits: ["flower blooming with scroll", "tagline word swap", "blush ground", "award laurels", "giant numeral", "flower returns at the end"]
palette: ["#ECDDD3", "#17233F", "#070C23", "#716F81"]
type: ["PP Neue Montreal", "IBM Plex Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The bloom is tied to the tagline: each word appears as the flower opens a little more, so the hero is one scrubbed growth.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Scrub a growth (a bloom) in step with a changing tagline word

## What to leave

- Mid-section is conventional

## Signature move

A peony blooming as 'We make AI ___' swaps its last word.

## Motion

Intro: a dark bud on blush. Wheel (Lenis ~110 px glide, 93 triggers): the bud opens and grows over several screens while the right-hand word swaps; the flower lifts away to the featured film; the statement fills; the giant 1 rises; films slide; the flower returns behind the CTA.

Measured (`motion/probe.json`): GSAP 3.13.0; 93 ScrollTriggers; Lenis; 8 video; split text; smoothed scroll (median 85 px still travelling after input stops); entry gate: CLOSE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an AI studio on blush: a dark bud that opens into a cream peony as 'We make AI ___' changes word (come alive, beautiful, emotional, larger than life, engaging, drive business), a featured tennis film, a statement, logos, a giant '1' for awards, work films (Starlink, a red panda), services and the flower returning at the end. Type: PP Neue Montreal, IBM Plex Mono.
Ground and ink from the measured palette (#ECDDD3, #17233F, #070C23). Motion carries the page through
a peony blooming as 'We make AI ___' swaps its last word. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D flower, AI films

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D flower, AI films

## Reference lock

Primary reference/direction: Dolsten and Co. - AI-first creative studio — An AI studio on blush: a dark bud that opens into a cream peony as 'We make AI ___' changes word (come alive, beautiful, emotional, larger than life, engaging, drive business), a featured tennis film, a statement, logos, a giant '1' for awards, work films (Starlink, a red panda), services and the flower returning at the end.
Preserve (3-5 traits): flower blooming with scroll; tagline word swap; blush ground; award laurels; giant numeral.
Borrow only (1-2): Scrub a growth (a bloom) in step with a changing tagline word
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D flower, AI films
Reject: Mid-section is conventional
Token commitments: palette #ECDDD3, #17233F, #070C23, #716F81; type PP Neue Montreal, IBM Plex Mono; engine GSAP + Lenis linked (never vendored).
