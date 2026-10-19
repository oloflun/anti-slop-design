---
title: "Ben Hays - Creative Developer"
url: https://benhays.dev/
source_url: https://benhays.dev/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: magician-poster-folio
dna: "Creative developer x a vintage magician poster world"
register: historical art
grammar: chaptered editorial
lane: "A folio framed like an antique picture: a magician with a glowing crystal ball, 'Ventures from the Digital Atelier' with tarot-style cards, a gold 'Client Archive' banner with sun and moon faces, work history, 'The Pursuit of Perfection' with a haunted house in green smoke, tools list and a green-and-gold fire finale 'Awww, Hell.' with a museum label."
mode: read
traits: ["ornate picture frame around the page", "vintage magician illustration", "tarot card project cards", "gold banner with sun and moon", "green smoke", "fire finale"]
palette: ["#7B6E41", "#020202", "#2D2416", "#493D28", "#D6BC8D", "#8FA284"]
type: ["Benguiat Bold Condensed BT", "Dolly Roman"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Committing fully to a magic-show theme (frame, tarot cards, smoke, fire) makes a developer CV memorable and coherent.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Frame the whole page as an object (a framed painting)
- Present projects as a deck of themed cards

## What to leave

- Dense small text
- Theme over readability

## Signature move

A magician with a glowing crystal ball inside an ornate frame.

## Motion

Intro: black inside the frame (~2 s), the magician fades up. Wheel (smoothed ~120 px): sections slide up inside the frame; cards fan; the banner swings; smoke drifts; the fire animates at the end; the frame stays fixed.

Measured (`motion/probe.json`): GSAP 3.12.7; WebGL canvas x3; 5 video; smoothed scroll (median 120 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the chaptered editorial grammar: a folio framed like an antique picture: a magician with a glowing crystal ball, 'Ventures from the Digital Atelier' with tarot-style cards, a gold 'Client Archive' banner with sun and moon faces, work history, 'The Pursuit of Perfection' with a haunted house in green smoke, tools list and a green-and-gold fire finale 'Awww, Hell.' with a museum label. Type: Benguiat Bold Condensed BT, Dolly Roman.
Ground and ink from the measured palette (#7B6E41, #020202, #2D2416). Motion carries the page through
a magician with a glowing crystal ball inside an ornate frame. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — vintage illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: vintage illustration

## Reference lock

Primary reference/direction: Ben Hays - Creative Developer — A folio framed like an antique picture: a magician with a glowing crystal ball, 'Ventures from the Digital Atelier' with tarot-style cards, a gold 'Client Archive' banner with sun and moon faces, work history, 'The Pursuit of Perfection' with a haunted house in green smoke, tools list and a green-and-gold fire finale 'Awww, Hell.' with a museum label.
Preserve (3-5 traits): ornate picture frame around the page; vintage magician illustration; tarot card project cards; gold banner with sun and moon; green smoke.
Borrow only (1-2): Frame the whole page as an object (a framed painting); Present projects as a deck of themed cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: vintage illustration
Reject: Dense small text; Theme over readability
Token commitments: palette #7B6E41, #020202, #2D2416, #493D28, #D6BC8D, #8FA284; type Benguiat Bold Condensed BT, Dolly Roman; engine GSAP + Lenis linked (never vendored).
