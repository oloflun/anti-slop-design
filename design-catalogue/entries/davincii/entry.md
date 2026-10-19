---
title: "DaVincii"
url: https://davincii.com/
source_url: https://davincii.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: ""
family: occult-engraving-intelligence
dna: "Intelligence platform x Renaissance occult engravings"
register: historical art
grammar: chaptered editorial
lane: "A dark platform page dressed as an occult manuscript: a ritual clock dial as loader, an eye-shaped portal with 'Signal Domains', astrological engravings around an 'Intelligence Engine' compass, case cards that fan out like tarot, and a parchment chapter with large italic numbers."
mode: persuade
traits: ["ritual clock dial loader", "eye-shaped mask", "astrological engravings (sun, moon, compass)", "case studies as tarot-like cards fanning out", "italic serif headings", "parchment chapter with huge italic numerals"]
palette: ["#444443", "#292929", "#787878"]
type: ["DaVinci", "Kessler", "Inter", "DaVinci-PIXI"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

An abstract AI product gets a mythology: engravings of suns and moons, a compass rose engine, an eye that opens onto the 'signal domains'. Case studies are dealt as cards with circular emblems, so browsing work feels like a reading.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last Agency).

## What to borrow (principle)

- Deal case studies as a fanned stack of cards with emblems
- An eye-shaped mask as a portal into a chapter
- Give an abstract product a visual mythology (engravings) instead of UI screenshots

## What to leave

- Thin serif on dark is hard to read
- Very dark midsection

## Signature move

Case studies dealt like tarot cards, each with a circular emblem.

## Motion

Intro: dark with a ritual clock dial drawing its ticks (~1.5 s). Scroll (Lenis, ~100 px glide, three.js): 'Our quest' paragraph; eye-shaped portal opens with 'Signal Domains'; 'Intelligence System' with three engraved dials; case cards fan out one by one from a stack (strategy, Avant Protocol, Nakoa, Core, QuadraX); 'Connect with DaVincii'; marquee 'Case Studies From Vision to Reality'; parchment chapter 'DaVincii Cipher' with 3 / 5 / 13 / 33 / 60 / ∞.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; smoothed scroll (median 114 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the chaptered editorial grammar: a dark platform page dressed as an occult manuscript: a ritual clock dial as loader, an eye-shaped portal with 'Signal Domains', astrological engravings around an 'Intelligence Engine' compass, case cards that fan out like tarot, and a parchment chapter with large italic numbers. Type: DaVinci, Kessler, Inter, DaVinci-PIXI.
Ground and ink from the measured palette (#444443, #292929, #787878). Motion carries the page through
case studies dealt like tarot cards, each with a circular emblem. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — antique engravings, astrological symbols, emblem badges

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: antique engravings, astrological symbols, emblem badges

## Reference lock

Primary reference/direction: DaVincii — A dark platform page dressed as an occult manuscript: a ritual clock dial as loader, an eye-shaped portal with 'Signal Domains', astrological engravings around an 'Intelligence Engine' compass, case cards that fan out like tarot, and a parchment chapter with large italic numbers.
Preserve (3-5 traits): ritual clock dial loader; eye-shaped mask; astrological engravings (sun, moon, compass); case studies as tarot-like cards fanning out; italic serif headings.
Borrow only (1-2): Deal case studies as a fanned stack of cards with emblems; An eye-shaped mask as a portal into a chapter
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: antique engravings, astrological symbols, emblem badges
Reject: Thin serif on dark is hard to read; Very dark midsection
Token commitments: palette #444443, #292929, #787878; type DaVinci, Kessler, Inter, DaVinci-PIXI; engine GSAP + Lenis linked (never vendored).
