---
title: "Stefanos Tsitsipas - official site"
url: https://tsitsipas.com/
source_url: https://tsitsipas.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: statue-to-portrait-athlete
dna: "Tennis player x a marble statue that turns into the man and photos pinned around him"
register: cinematic dark
grammar: continuous world
lane: "An athlete's site: a Greek flag loader on cream, a marble statue of the player with a racket on blue with match photos and sponsor tags pinned around it, the statue turning and cracking into the real man in a suit, a dark portrait, 'FAMILY — LEGACY' with family photos sliding, 'OFFICIAL SPONSORS' logos, and a cream closing quote over the statue."
mode: experience
traits: ["marble statue of the subject", "statue cracking into the person", "photos pinned around the figure", "blue and cream", "sponsor tags", "signature mark"]
palette: ["#323031", "#0F3462", "#0D1622", "#234F85", "#646461", "#C3CED5"]
type: ["ABC Diatype", "ABC Diatype Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The statue becoming the man is the signature transformation; it says 'legend' and 'human' in one move.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: OFF+BRAND).

## What to borrow (principle)

- Transform a sculpted version of the subject into the real one

## What to leave

- Very dark middle frames

## Signature move

A marble statue of the player cracking into the man in a suit.

## Motion

Intro: cream with a flag (~2 s). Wheel (3D): the statue rotates with photos pinning around; it turns away and cracks into the suited figure; the figure dims; a portrait frames; family photos slide; sponsors tile; the statue returns in cream.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; Taxi page transitions; WebGL canvas x1 (three.js); smoothed scroll (median 144 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the continuous world grammar: an athlete's site: a Greek flag loader on cream, a marble statue of the player with a racket on blue with match photos and sponsor tags pinned around it, the statue turning and cracking into the real man in a suit, a dark portrait, 'FAMILY — LEGACY' with family photos sliding, 'OFFICIAL SPONSORS' logos, and a cream closing quote over the statue. Type: ABC Diatype, ABC Diatype Mono.
Ground and ink from the measured palette (#323031, #0F3462, #0D1622). Motion carries the page through
a marble statue of the player cracking into the man in a suit. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D figure, photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D figure, photography

## Reference lock

Primary reference/direction: Stefanos Tsitsipas - official site — An athlete's site: a Greek flag loader on cream, a marble statue of the player with a racket on blue with match photos and sponsor tags pinned around it, the statue turning and cracking into the real man in a suit, a dark portrait, 'FAMILY — LEGACY' with family photos sliding, 'OFFICIAL SPONSORS' logos, and a cream closing quote over the statue.
Preserve (3-5 traits): marble statue of the subject; statue cracking into the person; photos pinned around the figure; blue and cream; sponsor tags.
Borrow only (1-2): Transform a sculpted version of the subject into the real one
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D figure, photography
Reject: Very dark middle frames
Token commitments: palette #323031, #0F3462, #0D1622, #234F85, #646461, #C3CED5; type ABC Diatype, ABC Diatype Mono; engine GSAP + Lenis linked (never vendored).
