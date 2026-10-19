---
title: "DINOTAENG"
url: https://en.dinotaeng.com/
source_url: https://en.dinotaeng.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "consumer-brand"
family: cloud-curtain-illustrated-town
dna: "Korean character brand x bear-shaped clouds parting over an illustrated town"
register: illustrated dark
grammar: live surface
lane: "A character-brand home page: plain sky blue, then fluffy clouds shaped like the brand's bears drift in and part like a curtain to reveal one illustrated top-down town (fountain, shops, river, trains) that serves as the navigation, with a small footer underneath."
mode: experience
traits: ["clouds shaped like mascots", "clouds part as a curtain", "isometric illustrated town as the menu", "sky blue and grass green", "tiny characters moving in the town", "short page, one scene"]
palette: ["#6BA556", "#538647", "#39B2B6", "#BEC8B0"]
type: ["Pretendard", "snushane"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The clouds carry the mascot before the map is even visible, and parting them is the whole intro: one material cause takes you from sky to town.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Duotone, FAVE®).

## What to borrow (principle)

- Clouds (or any material) in the brand's shape as the intro curtain
- An illustrated place as the navigation

## What to leave

- Almost nothing below the map
- Small footer text

## Signature move

Bear-shaped clouds parting to reveal an illustrated town.

## Motion

Intro: sky blue, bear-shaped clouds drift up and swell (~2 s), then slide apart left and right to uncover the town map. Wheel (Lenis, short page): the map lifts a little to show the footer; small characters and vehicles keep moving in the town.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the live surface grammar: a character-brand home page: plain sky blue, then fluffy clouds shaped like the brand's bears drift in and part like a curtain to reveal one illustrated top-down town (fountain, shops, river, trains) that serves as the navigation, with a small footer underneath. Type: Pretendard, snushane.
Ground and ink from the measured palette (#6BA556, #538647, #39B2B6). Motion carries the page through
bear-shaped clouds parting to reveal an illustrated town. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat illustrated town, mascots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat illustrated town, mascots

## Reference lock

Primary reference/direction: DINOTAENG — A character-brand home page: plain sky blue, then fluffy clouds shaped like the brand's bears drift in and part like a curtain to reveal one illustrated top-down town (fountain, shops, river, trains) that serves as the navigation, with a small footer underneath.
Preserve (3-5 traits): clouds shaped like mascots; clouds part as a curtain; isometric illustrated town as the menu; sky blue and grass green; tiny characters moving in the town.
Borrow only (1-2): Clouds (or any material) in the brand's shape as the intro curtain; An illustrated place as the navigation
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat illustrated town, mascots
Reject: Almost nothing below the map; Small footer text
Token commitments: palette #6BA556, #538647, #39B2B6, #BEC8B0; type Pretendard, snushane; engine GSAP + Lenis linked (never vendored).
