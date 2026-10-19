---
title: "Tripletta - neighbourhood pizza"
url: https://www.triplettapizza.com/
source_url: https://www.triplettapizza.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "consumer-brand"
family: pizzeria-city-marquee
dna: "Paris pizzeria chain x city-name marquees and a pizza-faced mascot"
register: other
grammar: chaptered editorial
lane: "A pizzeria chain: city names flash (Paris, Versailles), the 'TRIPLETTA' wordmark with a mascot of a woman holding a pizza, a photo strip with order links, city-name marquees (Versailles, Montrouge, Rennes) in condensed caps on green and teal with a manifesto, 'Avoir du style n'est pas qu'une histoire de sapes' with merch, 'Vali of love' giant words with photos around, and 'La vie d'un quartier avec supplément d'âme'."
mode: persuade
traits: ["city names flashing as loader", "pizza mascot illustration", "city marquees", "condensed caps", "green, teal and cream", "photos around giant words"]
palette: ["#FDF9DD", "#004733", "#68846B", "#B4AE9A", "#1F302B", "#D8E0BD"]
type: ["Merriweather", "Oswald"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The city marquees turn a chain into a list of neighbourhoods, which supports the 'neighbourhood pizzeria' message.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Marquee the locations as the brand's rhythm

## What to leave

- Dense caps body text

## Signature move

City names marqueeing between pizza emoji on green.

## Motion

Intro: city names flash on alternating colours (~2 s), the wordmark. Wheel: the photo strip slides; city marquees run; text blocks rise; photos float around giant words.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; Barba page transitions; smoothed scroll (median 123 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a pizzeria chain: city names flash (Paris, Versailles), the 'TRIPLETTA' wordmark with a mascot of a woman holding a pizza, a photo strip with order links, city-name marquees (Versailles, Montrouge, Rennes) in condensed caps on green and teal with a manifesto, 'Avoir du style n'est pas qu'une histoire de sapes' with merch, 'Vali of love' giant words with photos around, and 'La vie d'un quartier avec supplément d'âme'. Type: Merriweather, Oswald.
Ground and ink from the measured palette (#FDF9DD, #004733, #68846B). Motion carries the page through
city names marqueeing between pizza emoji on green. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — restaurant and lifestyle photography, illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: restaurant and lifestyle photography, illustration

## Reference lock

Primary reference/direction: Tripletta - neighbourhood pizza — A pizzeria chain: city names flash (Paris, Versailles), the 'TRIPLETTA' wordmark with a mascot of a woman holding a pizza, a photo strip with order links, city-name marquees (Versailles, Montrouge, Rennes) in condensed caps on green and teal with a manifesto, 'Avoir du style n'est pas qu'une histoire de sapes' with merch, 'Vali of love' giant words with photos around, and 'La vie d'un quartier avec supplément d'âme'.
Preserve (3-5 traits): city names flashing as loader; pizza mascot illustration; city marquees; condensed caps; green, teal and cream.
Borrow only (1-2): Marquee the locations as the brand's rhythm
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: restaurant and lifestyle photography, illustration
Reject: Dense caps body text
Token commitments: palette #FDF9DD, #004733, #68846B, #B4AE9A, #1F302B, #D8E0BD; type Merriweather, Oswald; engine GSAP + Lenis linked (never vendored).
