---
title: "MindMarket - real human insights"
url: https://mindmarket.com/
source_url: https://mindmarket.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "playful"
family: green-blob-illustrated-research
dna: "Market research agency x lime green blob ground, a flat illustrated crowd of characters and cream cards"
register: illustrated dark
grammar: continuous world
lane: "A qualitative research agency: a doodle loader, 'Real human insights' on lime with a flying crowd of flat characters, the ground becoming a winding green blob path that the camera follows down past cards ('No more chaos', 'One brief. One team.', 'Speak their language') with characters running, juggling and talking along it, 'Ready when you are', a photo of a parent and child with a yellow ribbon looping round 'connecting you to your audience', numbers as stacked coloured cards, case photos and a logo wall."
mode: persuade
traits: ["flat illustrated characters", "winding green blob path", "cards placed along the path", "yellow ribbon looping round a photo", "stacked number cards"]
palette: ["#8DD561", "#F6F1E5", "#98A991", "#E2E7AE"]
type: ["Inter"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Following a winding path past illustrated people makes a research process feel like meeting people, which is what the agency sells.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Deven Caron, KOKI-KIKO, Louis Paquet, Pier-Luc Cossette).

## What to borrow (principle)

- Lay the chapters along one winding path the camera follows

## What to leave

- Cream cards with small text over busy illustration

## Signature move

A crowd of flat characters flying over a lime ground under 'Real human insights'.

## Motion

Intro: doodle draws (~1.5 s). Wheel (Lenis, swup): the blob path scrolls with characters animating along it; cards pin briefly; the ribbon draws around the photo; number cards stack up.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; Swup page transitions; smoothed scroll (median 104 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the continuous world grammar: a qualitative research agency: a doodle loader, 'Real human insights' on lime with a flying crowd of flat characters, the ground becoming a winding green blob path that the camera follows down past cards ('No more chaos', 'One brief. One team.', 'Speak their language') with characters running, juggling and talking along it, 'Ready when you are', a photo of a parent and child with a yellow ribbon looping round 'connecting you to your audience', numbers as stacked coloured cards, case photos and a logo wall. Type: Inter.
Ground and ink from the measured palette (#8DD561, #F6F1E5, #98A991). Motion carries the page through
a crowd of flat characters flying over a lime ground under 'Real human insights'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat illustration, documentary photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat illustration, documentary photography

## Reference lock

Primary reference/direction: MindMarket - real human insights — A qualitative research agency: a doodle loader, 'Real human insights' on lime with a flying crowd of flat characters, the ground becoming a winding green blob path that the camera follows down past cards ('No more chaos', 'One brief. One team.', 'Speak their language') with characters running, juggling and talking along it, 'Ready when you are', a photo of a parent and child with a yellow ribbon looping round 'connecting you to your audience', numbers as stacked coloured cards, case photos and a logo wall.
Preserve (3-5 traits): flat illustrated characters; winding green blob path; cards placed along the path; yellow ribbon looping round a photo; stacked number cards.
Borrow only (1-2): Lay the chapters along one winding path the camera follows
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat illustration, documentary photography
Reject: Cream cards with small text over busy illustration
Token commitments: palette #8DD561, #F6F1E5, #98A991, #E2E7AE; type Inter; engine GSAP + Lenis linked (never vendored).
