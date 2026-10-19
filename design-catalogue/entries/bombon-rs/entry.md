---
title: "Bombon"
url: https://bombon.rs/
source_url: https://bombon.rs/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: lilac-candy-kingdom-shop
dna: "Swedish candy shop x lilac fairy-tale kingdom"
register: other
grammar: continuous world
lane: "A candy shop set in a lilac cloud kingdom: sweets spill out of an open bag in the hero, letters of 'Welcome to the kingdom of Bombon' tumble into place out of the clouds, a 3D castle road appears, and product cards drift over cloud banks with candies floating around them."
mode: persuade
traits: ["lilac/purple single-hue world", "3D candies floating and spilling", "letters tumbling into a headline", "clouds as section transitions", "rounded heavy display type", "play-a-game badge"]
palette: ["#EDE7F2", "#BC9FA0", "#5C485B", "#D4CAD5"]
type: ["akina", "manrope", "roundo"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Every section sits on the same cloud bank and the candies themselves move between them, so the shop reads as one world. Headlines are built letter by letter falling out of the sky, and the castle road gives the shop a destination, which turns a product grid into a place.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Square43 Studio).

## What to borrow (principle)

- Clouds (or any recurring atmosphere) as the seam between sections instead of hard edges
- Let the product (candies) float across section boundaries
- Headline letters that fall into place from scattered positions

## What to leave

- Heavy smoothing (~180 px glide) on a shop
- Many fonts (rounded, slab, script)

## Signature move

Letters of 'Welcome to the kingdom of Bombon' tumbling out of the clouds into a headline.

## Motion

Intro: 'BOMBON ROYAL SWEDISH CANDY' assembles while candies spring out of an open bag (~1.5 s). Scroll (Lenis, ~180 px glide, 1 pin, SplitText, Draggable): clouds drift up and the headline letters fall into place; 3D castle and purple road; realm cards (Sugar Rush, Sour Power, Cocoa Bliss, Licorizz); a draggable product shelf; bag cards with candies orbiting; 'twist, Bombon attitude' scattered letters; testimonials as tilted cards; newsletter.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; split text; smoothed scroll (median 183 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the continuous world grammar: a candy shop set in a lilac cloud kingdom: sweets spill out of an open bag in the hero, letters of 'Welcome to the kingdom of Bombon' tumble into place out of the clouds, a 3D castle road appears, and product cards drift over cloud banks with candies floating around them. Type: akina, manrope, roundo.
Ground and ink from the measured palette (#EDE7F2, #BC9FA0, #5C485B). Motion carries the page through
letters of 'Welcome to the kingdom of Bombon' tumbling out of the clouds into a headline. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D candy renders and soft clouds in one lilac hue

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D candy renders and soft clouds in one lilac hue

## Reference lock

Primary reference/direction: Bombon — A candy shop set in a lilac cloud kingdom: sweets spill out of an open bag in the hero, letters of 'Welcome to the kingdom of Bombon' tumble into place out of the clouds, a 3D castle road appears, and product cards drift over cloud banks with candies floating around them.
Preserve (3-5 traits): lilac/purple single-hue world; 3D candies floating and spilling; letters tumbling into a headline; clouds as section transitions; rounded heavy display type.
Borrow only (1-2): Clouds (or any recurring atmosphere) as the seam between sections instead of hard edges; Let the product (candies) float across section boundaries
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D candy renders and soft clouds in one lilac hue
Reject: Heavy smoothing (~180 px glide) on a shop; Many fonts (rounded, slab, script)
Token commitments: palette #EDE7F2, #BC9FA0, #5C485B, #D4CAD5; type akina, manrope, roundo; engine GSAP + Lenis linked (never vendored).
