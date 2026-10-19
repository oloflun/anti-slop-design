---
title: "Die Antwoord - ZAMA ZAMA"
url: https://www.dieantwoord.com/
source_url: https://www.dieantwoord.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: sticker-bomb-orange-album
dna: "Band album site x a sticker-bombed wall and an orange plated chassis"
register: other
grammar: chaptered editorial
lane: "An album site: a wall of stickers, an orange armoured truck's rear ('Listen now'), 'ZAMA ZAMA' micro-drama card with the truck driving off, 'LORE' video cards tilting, a black and white 'ZEF' documentary card, 'LYRICS' on black plates, a tour wishlist as regional plates, a 'ZEF SHOP' tee with a circular text badge, and 'ZEF SPAM' sign-up with the duo."
mode: experience
traits: ["sticker-bombed intro", "orange and black plates", "armoured truck", "tilted video cards", "regional plates list", "circular badge text"]
palette: ["#FE5E00", "#68331D", "#000000", "#B89A7D", "#1C130F"]
type: ["Conduit ITC Pro Regular", "ArialBlackRegular Regular", "Conduit ITC Pro Regular Placeholder", "ArialBlackRegular Regular Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The plated orange chassis is the page's material; every section is a plate bolted to it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Kins).

## What to borrow (principle)

- Give the page a physical chassis and bolt sections onto it

## What to leave

- Hard to read small labels

## Signature move

An orange armoured truck's rear with 'Listen now' under it.

## Motion

Intro: the sticker wall (~2 s). Wheel: the truck drives off; cards tilt and swap; black plates slide over; the regional plates stack; the tee badge rotates; stickers drift.

Measured (`motion/probe.json`): Lenis; WebGL canvas x1; smoothed scroll (median 137 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: an album site: a wall of stickers, an orange armoured truck's rear ('Listen now'), 'ZAMA ZAMA' micro-drama card with the truck driving off, 'LORE' video cards tilting, a black and white 'ZEF' documentary card, 'LYRICS' on black plates, a tour wishlist as regional plates, a 'ZEF SHOP' tee with a circular text badge, and 'ZEF SPAM' sign-up with the duo. Type: Conduit ITC Pro Regular, ArialBlackRegular Regular, Conduit ITC Pro Regular Placeholder, ArialBlackRegular Regular Placeholder.
Ground and ink from the measured palette (#FE5E00, #68331D, #000000). Motion carries the page through
an orange armoured truck's rear with 'Listen now' under it. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D truck, stickers, video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D truck, stickers, video

## Reference lock

Primary reference/direction: Die Antwoord - ZAMA ZAMA — An album site: a wall of stickers, an orange armoured truck's rear ('Listen now'), 'ZAMA ZAMA' micro-drama card with the truck driving off, 'LORE' video cards tilting, a black and white 'ZEF' documentary card, 'LYRICS' on black plates, a tour wishlist as regional plates, a 'ZEF SHOP' tee with a circular text badge, and 'ZEF SPAM' sign-up with the duo.
Preserve (3-5 traits): sticker-bombed intro; orange and black plates; armoured truck; tilted video cards; regional plates list.
Borrow only (1-2): Give the page a physical chassis and bolt sections onto it
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D truck, stickers, video
Reject: Hard to read small labels
Token commitments: palette #FE5E00, #68331D, #000000, #B89A7D, #1C130F; type Conduit ITC Pro Regular, ArialBlackRegular Regular, Conduit ITC Pro Regular Placeholder, ArialBlackRegular Regular Placeholder; engine GSAP + Lenis linked (never vendored).
