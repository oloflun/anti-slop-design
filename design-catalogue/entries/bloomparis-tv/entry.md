---
title: "Bloom - Production company Paris"
url: https://bloomparis.tv/
source_url: https://bloomparis.tv/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "institutional"
family: production-service-locations
dna: "Paris production company x yellow-accent location chapters"
register: cinematic dark
grammar: chaptered editorial
lane: "A production services company: a loading bar on grey, 'Your production partner in France' over footage, 'Full services, locations, tax incentives, talents', 'Welcome / Bienvenue - feel at home in Paris / down south / on the west coast / in the Alps' with the yellow place name swapping and location photos changing, 'Our work' split title over a football film, case grid and 'Let's collaborate'."
mode: persuade
traits: ["yellow place name swapping", "location photos per region", "condensed caps", "split 'Our work' title", "dark ground", "cookie panel"]
palette: ["#15161A", "#4E5C52", "#3A3F3B", "#E6E8EB", "#8C9391"]
type: ["PPNeueMontreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Swapping the place name in one sentence while the photos change sells 'we cover all of France' in one pinned section.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Swap one word of a pinned sentence while the image changes

## What to leave

- Cookie panel over frames

## Signature move

'Feel at home in ___' with the place name and photos swapping.

## Motion

Intro: grey with a black bar sweeping (~2 s), the footage. Wheel: the services list stacks; the welcome sentence pins while the yellow place swaps and photos cross-fade; 'Our work' splits; cases slide.

Measured (`motion/probe.json`): GSAP 3.12.2; Lenis; Taxi page transitions; 3 video; smoothed scroll (median 141 px still travelling after input stops); entry gate: CLOSE, SOUND OFF SOUND ON FULL SCREEN. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a production services company: a loading bar on grey, 'Your production partner in France' over footage, 'Full services, locations, tax incentives, talents', 'Welcome / Bienvenue - feel at home in Paris / down south / on the west coast / in the Alps' with the yellow place name swapping and location photos changing, 'Our work' split title over a football film, case grid and 'Let's collaborate'. Type: PPNeueMontreal.
Ground and ink from the measured palette (#15161A, #4E5C52, #3A3F3B). Motion carries the page through
'Feel at home in ___' with the place name and photos swapping. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial footage, location photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial footage, location photography

## Reference lock

Primary reference/direction: Bloom - Production company Paris — A production services company: a loading bar on grey, 'Your production partner in France' over footage, 'Full services, locations, tax incentives, talents', 'Welcome / Bienvenue - feel at home in Paris / down south / on the west coast / in the Alps' with the yellow place name swapping and location photos changing, 'Our work' split title over a football film, case grid and 'Let's collaborate'.
Preserve (3-5 traits): yellow place name swapping; location photos per region; condensed caps; split 'Our work' title; dark ground.
Borrow only (1-2): Swap one word of a pinned sentence while the image changes
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial footage, location photography
Reject: Cookie panel over frames
Token commitments: palette #15161A, #4E5C52, #3A3F3B, #E6E8EB, #8C9391; type PPNeueMontreal; engine GSAP + Lenis linked (never vendored).
