---
title: "Real Food (US dietary guidelines)"
url: https://realfood.gov/
source_url: https://realfood.gov/
captured: 2026-10-03
origin: raw-url
extract: none
category: institutional
category2: "editorial"
family: food-cutout-public-campaign
dna: "Public health campaign x green and near-black grounds, falling food cut-outs, red stat bars, a new pyramid built of food"
register: warm photographic
grammar: chaptered editorial
lane: "A government nutrition campaign: broccoli, a milk carton and a steak falling on green, 'Real Food Wins' on black over a close-up face, 'America is sick. The data is clear.' with red stat bars, the old food pyramid image, a long statement lighting word by word, an inverted pyramid built from photographed food on cream, categories (protein, vegetables, whole grains) as food piles, resources cards, a checklist of actions and 'Eat Real Food. Spread the word.'."
mode: persuade
traits: ["falling food cut-outs", "red stat bars", "words lighting in a long statement", "pyramid built of real food", "cream and black alternation"]
palette: ["#100001", "#F6F6F1", "#6B605E", "#403B3A", "#2B2221", "#B0AAA4"]
type: ["Geist Mono", "Die Grotesk A", "Die Grotesk B", "Die Grotesk D"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Rebuilding the food pyramid from real photographed food turns a policy change into a picture people already recognise.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: National Design Studio).

## What to borrow (principle)

- Rebuild a familiar diagram from real objects

## What to leave

- Political copy blocks

## Signature move

An inverted food pyramid built from photographed meat, vegetables and grains.

## Motion

Intro: food cut-outs fall on green (~2 s). Wheel: bars grow; the statement fills word by word; food pieces drop into the pyramid; cards stack.

Measured (`motion/probe.json`): Lenis; 3 video; smoothed scroll (median 150 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a government nutrition campaign: broccoli, a milk carton and a steak falling on green, 'Real Food Wins' on black over a close-up face, 'America is sick. The data is clear.' with red stat bars, the old food pyramid image, a long statement lighting word by word, an inverted pyramid built from photographed food on cream, categories (protein, vegetables, whole grains) as food piles, resources cards, a checklist of actions and 'Eat Real Food. Spread the word.'. Type: Geist Mono, Die Grotesk A, Die Grotesk B, Die Grotesk D.
Ground and ink from the measured palette (#100001, #F6F6F1, #6B605E). Motion carries the page through
an inverted food pyramid built from photographed meat, vegetables and grains. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — food cut-out photography, documentary photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: food cut-out photography, documentary photography

## Reference lock

Primary reference/direction: Real Food (US dietary guidelines) — A government nutrition campaign: broccoli, a milk carton and a steak falling on green, 'Real Food Wins' on black over a close-up face, 'America is sick. The data is clear.' with red stat bars, the old food pyramid image, a long statement lighting word by word, an inverted pyramid built from photographed food on cream, categories (protein, vegetables, whole grains) as food piles, resources cards, a checklist of actions and 'Eat Real Food. Spread the word.'.
Preserve (3-5 traits): falling food cut-outs; red stat bars; words lighting in a long statement; pyramid built of real food; cream and black alternation.
Borrow only (1-2): Rebuild a familiar diagram from real objects
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: food cut-out photography, documentary photography
Reject: Political copy blocks
Token commitments: palette #100001, #F6F6F1, #6B605E, #403B3A, #2B2221, #B0AAA4; type Geist Mono, Die Grotesk A, Die Grotesk B, Die Grotesk D; engine GSAP + Lenis linked (never vendored).
