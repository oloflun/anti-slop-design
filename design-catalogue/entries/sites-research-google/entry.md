---
title: "Google Research - Language Inclusion"
url: https://sites.research.google/languages/
source_url: https://sites.research.google/languages/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: white-research-story-globe
dna: "Research programme x white page, photo stack loader, card carousel of the pipeline and a dark particle globe"
register: modern clean
grammar: chaptered editorial
lane: "A research programme page: a percentage loader dealing a stack of portrait photos, a lede beside floating community portraits ('There are over 7,000 languages…'), photos scattering, 'How it works' with a horizontal track of cards (collecting data, preparing, model training, testing, product rollout) where the active card grows, 'Languages we support' fading to black with a particle globe, community stories with portraits and a place name, a quote, a video interview, research papers and an FAQ."
mode: read
traits: ["photo stack loader", "scattering portraits", "growing active card in a track", "particle globe on black", "community story cards"]
palette: ["#FFFFFF", "#4D4943", "#DEDFDF"]
type: ["Google Sans", "Google Sans Display", "Google Sans Text"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The pipeline as a track where only the active card is full size teaches a technical process one step at a time.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: HOOK).

## What to borrow (principle)

- Grow the active step card in a horizontal track

## What to leave

- Very pale inactive cards

## Signature move

A dark particle globe lighting the languages it supports.

## Motion

Intro: counter 0-100 with photos stacking (~3 s). Wheel (Lenis, smoothed): portraits scatter; the card track advances with the active card scaling; ground fades to black; the globe rotates; stories cross-fade.

Measured (`motion/probe.json`): Lenis; 25 video; smoothed scroll (median 168 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a research programme page: a percentage loader dealing a stack of portrait photos, a lede beside floating community portraits ('There are over 7,000 languages…'), photos scattering, 'How it works' with a horizontal track of cards (collecting data, preparing, model training, testing, product rollout) where the active card grows, 'Languages we support' fading to black with a particle globe, community stories with portraits and a place name, a quote, a video interview, research papers and an FAQ. Type: Google Sans, Google Sans Display, Google Sans Text.
Ground and ink from the measured palette (#FFFFFF, #4D4943, #DEDFDF). Motion carries the page through
a dark particle globe lighting the languages it supports. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — documentary portraits, WebGL globe, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: documentary portraits, WebGL globe, video

## Reference lock

Primary reference/direction: Google Research - Language Inclusion — A research programme page: a percentage loader dealing a stack of portrait photos, a lede beside floating community portraits ('There are over 7,000 languages…'), photos scattering, 'How it works' with a horizontal track of cards (collecting data, preparing, model training, testing, product rollout) where the active card grows, 'Languages we support' fading to black with a particle globe, community stories with portraits and a place name, a quote, a video interview, research papers and an FAQ.
Preserve (3-5 traits): photo stack loader; scattering portraits; growing active card in a track; particle globe on black; community story cards.
Borrow only (1-2): Grow the active step card in a horizontal track
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: documentary portraits, WebGL globe, video
Reject: Very pale inactive cards
Token commitments: palette #FFFFFF, #4D4943, #DEDFDF; type Google Sans, Google Sans Display, Google Sans Text; engine GSAP + Lenis linked (never vendored).
