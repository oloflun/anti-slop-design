---
title: "Mat Voyce - type designer and animator"
url: https://matvoyce.tv/
source_url: https://matvoyce.tv/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: kinetic-type-animator-folio
dna: "Type designer and animator x giant cyan type and project names that scrub sideways"
register: other
grammar: rhythmic cutlist
lane: "A type animator's folio on cream: a counter in cyan type, 'MAT VOYCE' in giant cyan condensed type breaking apart, a tilted Olipop TV card, a rainbow and 'OUCH!' card, a grid of animated lettering pieces, 'FEATURED WORK GO!' with a sticker, then project names in condensed italic sliding horizontally across the screen (Olipop TV, Friends 30th, Let's do lunch) with small thumbnails trailing and the full piece opening."
mode: experience
traits: ["giant cyan condensed type", "letters breaking apart", "tilted project cards", "project names sliding sideways", "thumbnails trailing the title", "lime scroll indicator"]
palette: ["#FFFEFA", "#FE651F", "#117FD4", "#33D3F2", "#889B88", "#E8E4B4"]
type: ["F37Judge", "F37Judge-Extended"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Using his own kinetic type as navigation (names sliding past like titles) demonstrates the craft in the interface itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Uncommon).

## What to borrow (principle)

- Slide project names across the screen as moving titles

## What to leave

- Hard to stop on one project

## Signature move

'FRIENDS 30TH' sliding across cream with thumbnails trailing.

## Motion

Intro: cream with a counter in cyan (~2 s), the name builds from fragments. Wheel: letters break apart; tilted cards rise and swap; the grid animates; each project name slides across with a thumbnail growing behind it.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); split text; smoothed scroll (median 131 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the rhythmic cutlist grammar: a type animator's folio on cream: a counter in cyan type, 'MAT VOYCE' in giant cyan condensed type breaking apart, a tilted Olipop TV card, a rainbow and 'OUCH!' card, a grid of animated lettering pieces, 'FEATURED WORK GO!' with a sticker, then project names in condensed italic sliding horizontally across the screen (Olipop TV, Friends 30th, Let's do lunch) with small thumbnails trailing and the full piece opening. Type: F37Judge, F37Judge-Extended.
Ground and ink from the measured palette (#FFFEFA, #FE651F, #117FD4). Motion carries the page through
'FRIENDS 30TH' sliding across cream with thumbnails trailing. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lettering animation

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lettering animation

## Reference lock

Primary reference/direction: Mat Voyce - type designer and animator — A type animator's folio on cream: a counter in cyan type, 'MAT VOYCE' in giant cyan condensed type breaking apart, a tilted Olipop TV card, a rainbow and 'OUCH!' card, a grid of animated lettering pieces, 'FEATURED WORK GO!' with a sticker, then project names in condensed italic sliding horizontally across the screen (Olipop TV, Friends 30th, Let's do lunch) with small thumbnails trailing and the full piece opening.
Preserve (3-5 traits): giant cyan condensed type; letters breaking apart; tilted project cards; project names sliding sideways; thumbnails trailing the title.
Borrow only (1-2): Slide project names across the screen as moving titles
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lettering animation
Reject: Hard to stop on one project
Token commitments: palette #FFFEFA, #FE651F, #117FD4, #33D3F2, #889B88, #E8E4B4; type F37Judge, F37Judge-Extended; engine GSAP + Lenis linked (never vendored).
