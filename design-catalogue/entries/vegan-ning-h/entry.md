---
title: "Veggie Taipei"
url: https://vegan.ning-h.com/
source_url: https://vegan.ning-h.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "editorial"
family: food-guide-sticker-scatter
dna: "Vegetarian Taipei food guide x stickers, a counter and food photos scattering around giant words"
register: warm photographic
grammar: chaptered editorial
lane: "A vegetarian food guide to Taipei: stickers (a checkered badge, a smiley, a lime triangle, a 'cuisine' tag) and a big counter, food photos (fried tofu, a sandwich, iced tea), 'WELCOME TO TAIPEI' in big pale letters with small photos around it, a full-bleed iced drink, a hexagon mask revealing 'EXPLORE CUISINE' with photos drifting, and a green 'craft your perfect Taipei eats' finale."
mode: read
traits: ["stickers as decoration", "giant pale words with photos around them", "hexagon mask reveal", "lime accents", "full-bleed food photo", "counter loader"]
palette: ["#F7F7F7", "#520F0A", "#DFE3D1", "#CB8544", "#D6C6A3", "#746555"]
type: ["PP Neue Montreal", "Swei Alias"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Stickers and drifting photos around giant words make a food guide feel like a scrapbook of a trip.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A geometric mask (hexagon) as the section reveal
- Small photos drifting around giant words

## What to leave

- Pale headline type low contrast

## Signature move

Food photos drifting around a pale 'WELCOME TO TAIPEI'.

## Motion

Intro: white, stickers pop in and a counter rolls 060 to 189 (~2 s). Wheel (23 triggers, 1 pin): photos fly in; the giant words slide; the drink fills the screen; a hexagon mask opens; photos drift around 'EXPLORE CUISINE'; the green panel rises.

Measured (`motion/probe.json`): GSAP 3.13.0; 23 ScrollTriggers; 1 pinned sections; Barba page transitions; split text; smoothed scroll (median 145 px still travelling after input stops); entry gate: SKIP TO MAIN CONTENT. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a vegetarian food guide to Taipei: stickers (a checkered badge, a smiley, a lime triangle, a 'cuisine' tag) and a big counter, food photos (fried tofu, a sandwich, iced tea), 'WELCOME TO TAIPEI' in big pale letters with small photos around it, a full-bleed iced drink, a hexagon mask revealing 'EXPLORE CUISINE' with photos drifting, and a green 'craft your perfect Taipei eats' finale. Type: PP Neue Montreal, Swei Alias.
Ground and ink from the measured palette (#F7F7F7, #520F0A, #DFE3D1). Motion carries the page through
food photos drifting around a pale 'WELCOME TO TAIPEI'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — food photography, stickers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: food photography, stickers

## Reference lock

Primary reference/direction: Veggie Taipei — A vegetarian food guide to Taipei: stickers (a checkered badge, a smiley, a lime triangle, a 'cuisine' tag) and a big counter, food photos (fried tofu, a sandwich, iced tea), 'WELCOME TO TAIPEI' in big pale letters with small photos around it, a full-bleed iced drink, a hexagon mask revealing 'EXPLORE CUISINE' with photos drifting, and a green 'craft your perfect Taipei eats' finale.
Preserve (3-5 traits): stickers as decoration; giant pale words with photos around them; hexagon mask reveal; lime accents; full-bleed food photo.
Borrow only (1-2): A geometric mask (hexagon) as the section reveal; Small photos drifting around giant words
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: food photography, stickers
Reject: Pale headline type low contrast
Token commitments: palette #F7F7F7, #520F0A, #DFE3D1, #CB8544, #D6C6A3, #746555; type PP Neue Montreal, Swei Alias; engine GSAP + Lenis linked (never vendored).
