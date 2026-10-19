---
title: "Bucks Sauce - small-batch BBQ sauce"
url: https://buckssauce.com/
source_url: https://buckssauce.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: dark-food-brand-with-flying-ingredients
dna: "BBQ sauce brand x dark brown ground, flying fruit and chilli cut-outs and a cartoon peach mascot"
register: warm photographic
grammar: chaptered editorial
lane: "A sauce shop: a red circle iris opens on the deer-skull logo, peppers, cherries and pineapple fly around the logo, 'The BBQ sauce that makes other sauces insecure' over a bottle with a peach mascot and a carousel of flavours, a manifesto line set word by word with little icons ('like it's the 1800s… act surprised when people think you can cook'), claim cards like 'No corn syrup' with ingredients drifting past. A 10 %-off modal covers the page halfway."
mode: persuade
traits: ["circle iris intro", "ingredient cut-outs flying", "condensed outline display type", "word-by-word manifesto with glyphs", "mascot on the bottle", "claim cards"]
palette: ["#0F0B08", "#35291D", "#7A614A", "#F6E7CA", "#CDB692"]
type: ["Inter Tight", "PeperoncinoSansCustom"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The ingredients drifting around every section keep the product's taste on screen even where the copy talks about something else.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Buzzworthy Studio).

## What to borrow (principle)

- Let the raw ingredients float through the page as the connecting thread

## What to leave

- Discount modal that blocks the story
- Busy carousel arrows on the hero

## Signature move

A red circle opening on a deer-skull logo while peppers and cherries fly around it.

## Motion

Intro: red circle iris (~1 s), fruit bursts outward. Wheel (Lenis, pins 2): the hero bottle pins while flavours change; the manifesto lights word by word; ingredients parallax across sections; a modal appears after ~15 s.

Measured (`motion/probe.json`): GSAP 3.14.2; 2 pinned sections; Lenis; 26 video; split text; smoothed scroll (median 107 px still travelling after input stops); entry gate: PROCEED TO CHECKOUT PROCEED TO CHECKOUT. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a sauce shop: a red circle iris opens on the deer-skull logo, peppers, cherries and pineapple fly around the logo, 'The BBQ sauce that makes other sauces insecure' over a bottle with a peach mascot and a carousel of flavours, a manifesto line set word by word with little icons ('like it's the 1800s… act surprised when people think you can cook'), claim cards like 'No corn syrup' with ingredients drifting past. A 10 %-off modal covers the page halfway. Type: Inter Tight, PeperoncinoSansCustom.
Ground and ink from the measured palette (#0F0B08, #35291D, #7A614A). Motion carries the page through
a red circle opening on a deer-skull logo while peppers and cherries fly around it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product cut-outs, ingredient photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product cut-outs, ingredient photography

## Reference lock

Primary reference/direction: Bucks Sauce - small-batch BBQ sauce — A sauce shop: a red circle iris opens on the deer-skull logo, peppers, cherries and pineapple fly around the logo, 'The BBQ sauce that makes other sauces insecure' over a bottle with a peach mascot and a carousel of flavours, a manifesto line set word by word with little icons ('like it's the 1800s… act surprised when people think you can cook'), claim cards like 'No corn syrup' with ingredients drifting past. A 10 %-off modal covers the page halfway.
Preserve (3-5 traits): circle iris intro; ingredient cut-outs flying; condensed outline display type; word-by-word manifesto with glyphs; mascot on the bottle.
Borrow only (1-2): Let the raw ingredients float through the page as the connecting thread
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product cut-outs, ingredient photography
Reject: Discount modal that blocks the story; Busy carousel arrows on the hero
Token commitments: palette #0F0B08, #35291D, #7A614A, #F6E7CA, #CDB692; type Inter Tight, PeperoncinoSansCustom; engine GSAP + Lenis linked (never vendored).
