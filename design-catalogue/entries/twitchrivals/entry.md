---
title: "Twitch Rivals - creator competitions"
url: https://twitchrivals.com/
source_url: https://twitchrivals.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: black-white-sticker-event-site
dna: "Esports event brand x black/white blocks with photos and stickers thrown in"
register: other
grammar: chaptered editorial
lane: "An event brand: a counter 012 to 100 on black with a glyph, a white page with 'what_is_____twitch_rivals' and a video window that grows, 'Winning is only part of the story…' with event photos and sticker glyphs flying in around a black caption card, three series cards (alt_arcade yellow, hard_mode orange, casual_quest blue) sliding across with a progress rule, 'Showing up is more than…', an FAQ laid out as a cascading tree, and partner logos."
mode: persuade
traits: ["counter with a glyph", "mono underscore titles", "photos and stickers thrown around a card", "three colour series cards", "cascading FAQ tree", "black and white halves"]
palette: ["#050505", "#FBFBFB", "#323138", "#857C8B", "#E3E3E2"]
type: ["roobert"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The photos and stickers flying in around one caption card give an event page the chaos of a tournament without losing the message.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Jesse Martinez).

## What to borrow (principle)

- Throw supporting photos in around one fixed caption card

## What to leave

- Mono labels very small

## Signature move

Event photos and sticker glyphs flying in around a black caption card.

## Motion

Intro: black counter (~2 s). Wheel (Lenis): the video window grows; photos and stickers fly in from the edges with rotation; the series cards slide sideways with the rule advancing; the FAQ branches draw; logos fade.

Measured (`motion/probe.json`): Lenis; WebGL canvas x4 (three.js); 2 video; smoothed scroll (median 123 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: an event brand: a counter 012 to 100 on black with a glyph, a white page with 'what_is_____twitch_rivals' and a video window that grows, 'Winning is only part of the story…' with event photos and sticker glyphs flying in around a black caption card, three series cards (alt_arcade yellow, hard_mode orange, casual_quest blue) sliding across with a progress rule, 'Showing up is more than…', an FAQ laid out as a cascading tree, and partner logos. Type: roobert.
Ground and ink from the measured palette (#050505, #FBFBFB, #323138). Motion carries the page through
event photos and sticker glyphs flying in around a black caption card. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — event photography, glyph stickers

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: event photography, glyph stickers

## Reference lock

Primary reference/direction: Twitch Rivals - creator competitions — An event brand: a counter 012 to 100 on black with a glyph, a white page with 'what_is_____twitch_rivals' and a video window that grows, 'Winning is only part of the story…' with event photos and sticker glyphs flying in around a black caption card, three series cards (alt_arcade yellow, hard_mode orange, casual_quest blue) sliding across with a progress rule, 'Showing up is more than…', an FAQ laid out as a cascading tree, and partner logos.
Preserve (3-5 traits): counter with a glyph; mono underscore titles; photos and stickers thrown around a card; three colour series cards; cascading FAQ tree.
Borrow only (1-2): Throw supporting photos in around one fixed caption card
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: event photography, glyph stickers
Reject: Mono labels very small
Token commitments: palette #050505, #FBFBFB, #323138, #857C8B, #E3E3E2; type roobert; engine GSAP + Lenis linked (never vendored).
