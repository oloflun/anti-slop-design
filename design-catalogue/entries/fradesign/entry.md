---
title: "FRA! - Doodle Designer"
url: https://fradesign.it/
source_url: https://fradesign.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: doodle-artist-folio
dna: "Italian doodle artist x dense black-and-white doodles and lime accents"
register: illustrated dark
grammar: chaptered editorial
lane: "A doodle artist's folio: a loader with jittering condensed type, 'Benvenut* nella doodle art di FRA!' surrounded by dense doodles, a black about with lime headings, a doodle globe, a full doodle mural, tilted project cards (Xiaomi Guinness record, IKEA, WAMI), a brand marquee, a services list with doodle icons, 'LE SFIDE' with rotating stickers and a giant 'CONTATTALO!!!'."
mode: persuade
traits: ["dense black-and-white doodles", "condensed caps with lime accents", "tilted project cards", "rotating sticker badges", "doodle icons by service", "giant exclamation CTA"]
palette: ["#FFFFFF", "#020202", "#9C9C9A", "#C0C1BA", "#6B6C6A", "#E6E7DE"]
type: ["Tusker Grotesk", "Moderat Extended"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The doodles are the work and the brand; every section shows the hand.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Let the artist's own drawings frame every section

## What to leave

- Cookie panel over frames
- Very busy

## Signature move

Dense black-and-white doodles around 'Benvenut* nella doodle art di FRA!'.

## Motion

Intro: the loader word jitters (~1.5 s), doodles fill in. Wheel (Lenis, 3 pins): the black panel rises; the mural pans; cards slide in tilted; the marquee runs; service rows reveal with doodle icons; stickers rotate around 'LE SFIDE'; the CTA letters bounce.

Measured (`motion/probe.json`): GSAP 3.10.4; 3 pinned sections; Lenis; 1 video; split text; smoothed scroll (median 148 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a doodle artist's folio: a loader with jittering condensed type, 'Benvenut* nella doodle art di FRA!' surrounded by dense doodles, a black about with lime headings, a doodle globe, a full doodle mural, tilted project cards (Xiaomi Guinness record, IKEA, WAMI), a brand marquee, a services list with doodle icons, 'LE SFIDE' with rotating stickers and a giant 'CONTATTALO!!!'. Type: Tusker Grotesk, Moderat Extended.
Ground and ink from the measured palette (#FFFFFF, #020202, #9C9C9A). Motion carries the page through
dense black-and-white doodles around 'Benvenut* nella doodle art di FRA!'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — doodle illustration, project photos

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: doodle illustration, project photos

## Reference lock

Primary reference/direction: FRA! - Doodle Designer — A doodle artist's folio: a loader with jittering condensed type, 'Benvenut* nella doodle art di FRA!' surrounded by dense doodles, a black about with lime headings, a doodle globe, a full doodle mural, tilted project cards (Xiaomi Guinness record, IKEA, WAMI), a brand marquee, a services list with doodle icons, 'LE SFIDE' with rotating stickers and a giant 'CONTATTALO!!!'.
Preserve (3-5 traits): dense black-and-white doodles; condensed caps with lime accents; tilted project cards; rotating sticker badges; doodle icons by service.
Borrow only (1-2): Let the artist's own drawings frame every section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: doodle illustration, project photos
Reject: Cookie panel over frames; Very busy
Token commitments: palette #FFFFFF, #020202, #9C9C9A, #C0C1BA, #6B6C6A, #E6E7DE; type Tusker Grotesk, Moderat Extended; engine GSAP + Lenis linked (never vendored).
