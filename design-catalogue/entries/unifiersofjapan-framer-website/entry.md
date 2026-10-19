---
title: "Unifiers of Japan"
url: https://unifiersofjapan.framer.website/
source_url: https://unifiersofjapan.framer.website/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: red-poster-warlord-illustration
dna: "History explainer x crimson ground, a flat vector warlord whose helmet descends as you scroll, cream panels with fact grids"
register: illustrated dark
grammar: typographic poster
lane: "A history piece: 'Oda Nobunaga' in huge condensed cream caps on crimson with the kanji above and a flat illustrated face peeking up behind the letters, the face rising into a full helmeted portrait as the type slides away, a cream panel with the clan crest and a fact grid (position, control, timeline, power, capital, legacy), a centred summary in red caps inside a framed card, and a map panel with the castle."
mode: read
traits: ["huge condensed name", "flat vector portrait rising through the type", "clan crest", "fact grid", "framed cream cards"]
palette: ["#DF0238", "#F4ECE3", "#E6B0B6", "#9D233C"]
type: ["Anton", "PP Nikkei Pacific Ultrabold", "F37 Blanka Trial Bold", "F37 Blanka Trial Medium"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The portrait rising out of the name turns a history page's title card into its first piece of storytelling.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Tofu Design).

## What to borrow (principle)

- Let the subject rise out of its own name

## What to leave

- Framer badge

## Signature move

A flat warlord face rising behind 'ODA NOBUNAGA' on crimson.

## Motion

Wheel (Lenis): the illustration translates up while the name slides behind; the cream panel wipes up; the fact grid fades in; cards scale.

Measured (`motion/probe.json`): GSAP 3.11.3; Lenis; smoothed scroll (median 121 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the typographic poster grammar: a history piece: 'Oda Nobunaga' in huge condensed cream caps on crimson with the kanji above and a flat illustrated face peeking up behind the letters, the face rising into a full helmeted portrait as the type slides away, a cream panel with the clan crest and a fact grid (position, control, timeline, power, capital, legacy), a centred summary in red caps inside a framed card, and a map panel with the castle. Type: Anton, PP Nikkei Pacific Ultrabold, F37 Blanka Trial Bold, F37 Blanka Trial Medium.
Ground and ink from the measured palette (#DF0238, #F4ECE3, #E6B0B6). Motion carries the page through
a flat warlord face rising behind 'ODA NOBUNAGA' on crimson. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat vector illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat vector illustration

## Reference lock

Primary reference/direction: Unifiers of Japan — A history piece: 'Oda Nobunaga' in huge condensed cream caps on crimson with the kanji above and a flat illustrated face peeking up behind the letters, the face rising into a full helmeted portrait as the type slides away, a cream panel with the clan crest and a fact grid (position, control, timeline, power, capital, legacy), a centred summary in red caps inside a framed card, and a map panel with the castle.
Preserve (3-5 traits): huge condensed name; flat vector portrait rising through the type; clan crest; fact grid; framed cream cards.
Borrow only (1-2): Let the subject rise out of its own name
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat vector illustration
Reject: Framer badge
Token commitments: palette #DF0238, #F4ECE3, #E6B0B6, #9D233C; type Anton, PP Nikkei Pacific Ultrabold, F37 Blanka Trial Bold, F37 Blanka Trial Medium; engine GSAP + Lenis linked (never vendored).
