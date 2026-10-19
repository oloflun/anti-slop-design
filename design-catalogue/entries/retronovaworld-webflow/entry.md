---
title: "Retronova - retro-futurist fashion concept"
url: https://retronovaworld.webflow.io/
source_url: https://retronovaworld.webflow.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: hud-scramble-retro-futurism
dna: "Retro-futurist fashion concept x HUD frames and scrambling condensed titles"
register: cinematic dark
grammar: chaptered editorial
lane: "A fashion concept on Webflow: a black screen with orange HUD frame lines and a 'system loading' progress box, a full-bleed desert city of saucer towers, 'INNOVATION' and 'A JOURNEY THROUGH TIME AND STYLE' in tall condensed caps that scramble into place letter by letter, small mono captions, a pixel marquee 'VINTAGE VISION //', 'ETHEREAL DREAMS' with tilted retro illustration cards of women in space fashion floating around, '// FUTURISTIC FLAIR' and 'EXPLORE AI WONDERS' with a card row."
mode: experience
traits: ["HUD frame lines and loader box", "titles scrambling through glyphs", "tall condensed caps", "pixel font marquee", "tilted illustration cards floating", "orange on black"]
palette: ["#0C0C0C", "#563927", "#7A6750", "#A1967D", "#E3DECC"]
type: ["OffBit [bold]", "PP Supply Mono [regular]", "PP Neue Montreal [medium]", "WT-Skrappa"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Scrambling every title through random glyphs matches the retro-computer theme and makes each heading an event.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Scramble headings through glyphs before they settle

## What to leave

- Scrambled text unreadable mid-frame

## Signature move

'ETHEREAL DREAMS' settling from scrambled glyphs with retro space-fashion cards around it.

## Motion

Intro: HUD frame, a system-loading bar (~3 s), then the desert city. Wheel (Lenis): titles scramble in; the city shrinks into a card; captions type; the pixel marquee runs; cards drift and tilt around the pinned title; the next title scrambles over.

Measured (`motion/probe.json`): GSAP 3.12.5; Barba page transitions; WebGL canvas x4 (three.js); smoothed scroll (median 166 px still travelling after input stops); entry gate: SKIP LOADING. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a fashion concept on Webflow: a black screen with orange HUD frame lines and a 'system loading' progress box, a full-bleed desert city of saucer towers, 'INNOVATION' and 'A JOURNEY THROUGH TIME AND STYLE' in tall condensed caps that scramble into place letter by letter, small mono captions, a pixel marquee 'VINTAGE VISION //', 'ETHEREAL DREAMS' with tilted retro illustration cards of women in space fashion floating around, '// FUTURISTIC FLAIR' and 'EXPLORE AI WONDERS' with a card row. Type: OffBit [bold], PP Supply Mono [regular], PP Neue Montreal [medium], WT-Skrappa.
Ground and ink from the measured palette (#0C0C0C, #563927, #7A6750). Motion carries the page through
'ETHEREAL DREAMS' settling from scrambled glyphs with retro space-fashion cards around it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — retro-futurist illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: retro-futurist illustration

## Reference lock

Primary reference/direction: Retronova - retro-futurist fashion concept — A fashion concept on Webflow: a black screen with orange HUD frame lines and a 'system loading' progress box, a full-bleed desert city of saucer towers, 'INNOVATION' and 'A JOURNEY THROUGH TIME AND STYLE' in tall condensed caps that scramble into place letter by letter, small mono captions, a pixel marquee 'VINTAGE VISION //', 'ETHEREAL DREAMS' with tilted retro illustration cards of women in space fashion floating around, '// FUTURISTIC FLAIR' and 'EXPLORE AI WONDERS' with a card row.
Preserve (3-5 traits): HUD frame lines and loader box; titles scrambling through glyphs; tall condensed caps; pixel font marquee; tilted illustration cards floating.
Borrow only (1-2): Scramble headings through glyphs before they settle
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: retro-futurist illustration
Reject: Scrambled text unreadable mid-frame
Token commitments: palette #0C0C0C, #563927, #7A6750, #A1967D, #E3DECC; type OffBit [bold], PP Supply Mono [regular], PP Neue Montreal [medium], WT-Skrappa; engine GSAP + Lenis linked (never vendored).
