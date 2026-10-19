---
title: "Abhishek Jha - Designer and Developer"
url: https://abhishekjha.me/
source_url: https://abhishekjha.me/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: calla-lily-condensed-folio
dna: "Designer-developer x a chrome calla lily and ultra-condensed headlines"
register: editorial print
grammar: chaptered editorial
lane: "A folio: a plum loader with flower photos and a line counter, a pink chrome calla lily breaking through an oval hole in a sky photo, ultra-condensed white 'Crafting unforgettable digital experiences for ambitious clients' with italic script inserts, a visual identity collage, 'Crafting legacies', green featured projects with names in condensed caps plus a script initial, thorny branches beside philosophy, a services list in condensed caps and 'Send an email' marquee."
mode: persuade
traits: ["chrome calla lily", "ultra-condensed caps with script inserts", "plum, green and cream chapters", "thorny branch illustration", "oval cut-out window", "marquee email CTA"]
palette: ["#2E1128", "#837A80", "#B2C2D1", "#F6F6F6", "#D5E0E8", "#6E4D54"]
type: ["DM Sans", "playground", "thunder", "editorial"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The calla lily and thorns give a personal folio a botanical motif, and the condensed caps with script inserts are a distinctive type system.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Mix ultra-condensed caps with italic script words inline

## What to leave

- Many chapter colours
- Small body text

## Signature move

A pink chrome calla lily breaking through an oval window.

## Motion

Intro: plum, flower photos fan out along a line as a counter runs (~3 s). Wheel (ScrollSmoother, 2 pins): the lily rises through the oval; headline words drop in; the collage assembles; project names slide in with script initials; branches grow; the services list scrolls; the email marquee runs.

Measured (`motion/probe.json`): GSAP 3.15.0; 2 pinned sections; ScrollSmoother; WebGL canvas x2 (three.js); 6 video; split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a folio: a plum loader with flower photos and a line counter, a pink chrome calla lily breaking through an oval hole in a sky photo, ultra-condensed white 'Crafting unforgettable digital experiences for ambitious clients' with italic script inserts, a visual identity collage, 'Crafting legacies', green featured projects with names in condensed caps plus a script initial, thorny branches beside philosophy, a services list in condensed caps and 'Send an email' marquee. Type: DM Sans, playground, thunder, editorial.
Ground and ink from the measured palette (#2E1128, #837A80, #B2C2D1). Motion carries the page through
a pink chrome calla lily breaking through an oval window. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D flower, botanical photos, project mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D flower, botanical photos, project mockups

## Reference lock

Primary reference/direction: Abhishek Jha - Designer and Developer — A folio: a plum loader with flower photos and a line counter, a pink chrome calla lily breaking through an oval hole in a sky photo, ultra-condensed white 'Crafting unforgettable digital experiences for ambitious clients' with italic script inserts, a visual identity collage, 'Crafting legacies', green featured projects with names in condensed caps plus a script initial, thorny branches beside philosophy, a services list in condensed caps and 'Send an email' marquee.
Preserve (3-5 traits): chrome calla lily; ultra-condensed caps with script inserts; plum, green and cream chapters; thorny branch illustration; oval cut-out window.
Borrow only (1-2): Mix ultra-condensed caps with italic script words inline
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D flower, botanical photos, project mockups
Reject: Many chapter colours; Small body text
Token commitments: palette #2E1128, #837A80, #B2C2D1, #F6F6F6, #D5E0E8, #6E4D54; type DM Sans, playground, thunder, editorial; engine GSAP + Lenis linked (never vendored).
