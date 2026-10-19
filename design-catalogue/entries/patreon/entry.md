---
title: "Patreon (Swedish)"
url: https://www.patreon.com/
source_url: https://www.patreon.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: creator-collage-statement
dna: "Creator platform x huge light grotesk statements split across the screen with creator photos and video tucked between words, on periwinkle and dark"
register: warm photographic
grammar: chaptered editorial
lane: "Patreon in Swedish: 'Platsen där poddar växer' split into three lines across a podcast studio video, 'Din vildaste kreativa verklighet' on periwinkle, 'Kreativitet drivs av fandom' with creator portraits scattered between the words, a close-up of a musician with a quote, 'Komplett kreativ kontroll' with phone screens, 'Skapare. Fans. Inget i mellan.' beside a community feed, 'Förvandla passioner till företag' with an earnings card, and a creator portrait close."
mode: persuade
traits: ["huge light grotesk split across the frame", "creator photos between words", "periwinkle and dark alternation", "product UI beside statements"]
palette: ["#3641AA", "#0D0909", "#97ABC9", "#5E4F63", "#FDFDFE", "#D9D8DA"]
type: ["Oracle", "Noto Sans Regular", "Noto Sans JP", "Noto Sans KR"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Splitting each statement across the screen with creators in the gaps keeps the people and the promise in the same frame.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Active Theory).

## What to borrow (principle)

- Tuck the people into the gaps of the statement

## What to leave

- Cookie bar on every frame

## Signature move

'Platsen där poddar växer' split across a podcast studio video.

## Motion

Wheel: statement lines slide in from opposite sides; photos scale into the gaps; grounds switch.

Measured (`motion/probe.json`): GSAP 3.11.5; Lenis; WebGL canvas x1; 4 video; split text; smoothed scroll (median 95 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: patreon in Swedish: 'Platsen där poddar växer' split into three lines across a podcast studio video, 'Din vildaste kreativa verklighet' on periwinkle, 'Kreativitet drivs av fandom' with creator portraits scattered between the words, a close-up of a musician with a quote, 'Komplett kreativ kontroll' with phone screens, 'Skapare. Fans. Inget i mellan.' beside a community feed, 'Förvandla passioner till företag' with an earnings card, and a creator portrait close. Type: Oracle, Noto Sans Regular, Noto Sans JP, Noto Sans KR.
Ground and ink from the measured palette (#3641AA, #0D0909, #97ABC9). Motion carries the page through
'Platsen där poddar växer' split across a podcast studio video. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — creator photography, video, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: creator photography, video, UI

## Reference lock

Primary reference/direction: Patreon (Swedish) — Patreon in Swedish: 'Platsen där poddar växer' split into three lines across a podcast studio video, 'Din vildaste kreativa verklighet' on periwinkle, 'Kreativitet drivs av fandom' with creator portraits scattered between the words, a close-up of a musician with a quote, 'Komplett kreativ kontroll' with phone screens, 'Skapare. Fans. Inget i mellan.' beside a community feed, 'Förvandla passioner till företag' with an earnings card, and a creator portrait close.
Preserve (3-5 traits): huge light grotesk split across the frame; creator photos between words; periwinkle and dark alternation; product UI beside statements.
Borrow only (1-2): Tuck the people into the gaps of the statement
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: creator photography, video, UI
Reject: Cookie bar on every frame
Token commitments: palette #3641AA, #0D0909, #97ABC9, #5E4F63, #FDFDFE, #D9D8DA; type Oracle, Noto Sans Regular, Noto Sans JP, Noto Sans KR; engine GSAP + Lenis linked (never vendored).
