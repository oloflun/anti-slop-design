---
title: "Electra Filmworks"
url: https://electrafilmworks.com/
source_url: https://electrafilmworks.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: production-reel-bolt-logo
dna: "Production company x a reel with an orange bolt logo fixed in the centre"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A production company home: a hand icon loader, then full-bleed commercial clips (a fighter jet with a pilot, a girl with a snow globe, Jeep coins, a hand plating food) cutting one after another, with a small orange bolt logo fixed in the centre, the 'ELECTRA' wordmark bottom left and a four-project index along the bottom."
mode: experience
traits: ["fixed orange bolt in centre", "full-bleed commercial clips", "project index along the bottom", "hand-icon loader", "condensed wordmark", "dark cuts between clips"]
palette: ["#1A1615", "#3E4D4F", "#768581"]
type: ["PP Pangram Sans", "Monument Extended"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The fixed bolt is a constant against fast cuts; the index makes the reel navigable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Fix a small brand mark at centre while the reel cuts

## What to leave

- Dark frames between cuts

## Signature move

An orange bolt fixed in the centre of cutting commercial clips.

## Motion

Intro: dark with a hand icon (~1.5 s). Scroll (Lenis): the reel steps clip by clip; the index item highlights; the bolt stays fixed.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; 1 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a production company home: a hand icon loader, then full-bleed commercial clips (a fighter jet with a pilot, a girl with a snow globe, Jeep coins, a hand plating food) cutting one after another, with a small orange bolt logo fixed in the centre, the 'ELECTRA' wordmark bottom left and a four-project index along the bottom. Type: PP Pangram Sans, Monument Extended.
Ground and ink from the measured palette (#1A1615, #3E4D4F, #768581). Motion carries the page through
an orange bolt fixed in the centre of cutting commercial clips. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — commercial film stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: commercial film stills

## Reference lock

Primary reference/direction: Electra Filmworks — A production company home: a hand icon loader, then full-bleed commercial clips (a fighter jet with a pilot, a girl with a snow globe, Jeep coins, a hand plating food) cutting one after another, with a small orange bolt logo fixed in the centre, the 'ELECTRA' wordmark bottom left and a four-project index along the bottom.
Preserve (3-5 traits): fixed orange bolt in centre; full-bleed commercial clips; project index along the bottom; hand-icon loader; condensed wordmark.
Borrow only (1-2): Fix a small brand mark at centre while the reel cuts
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: commercial film stills
Reject: Dark frames between cuts
Token commitments: palette #1A1615, #3E4D4F, #768581; type PP Pangram Sans, Monument Extended; engine GSAP + Lenis linked (never vendored).
