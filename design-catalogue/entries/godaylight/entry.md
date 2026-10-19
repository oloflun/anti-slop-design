---
title: "Daylight - home solar and battery"
url: https://godaylight.com/
source_url: https://godaylight.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "consumer-brand"
family: orange-wave-home-energy
dna: "Home energy x an orange rippled-sand loader, dusk house photography, cream panels and isometric line drawings"
register: warm photographic
grammar: chaptered editorial
lane: "A home-energy subscription: a full-screen orange rippled texture with the wordmark that wipes up to reveal a house at dusk ('Power your home for less') with an orange card standing in for the battery, cream panels with photos at the edges ('Cut your electric bill by 20 % or more', 'Keep the lights on'), a hand reaching into a warm sun-blur, a four-step sticky sequence (subscribe, install, power on) where an orange phone, an isometric house with orange panels and a line drawing of a street swap on the right, a live chart, a dark storm section about the grid, sunset photos with a serif statement about a decentralised network, and a lilac 'Step into Daylight' close."
mode: persuade
traits: ["orange rippled texture loader", "dusk house photography", "isometric line-drawn houses", "sticky numbered steps with swapping visuals", "serif statements over dark photos", "lilac close"]
palette: ["#EFE5CF", "#CD8624", "#FEF8EC", "#2E261B", "#867C64", "#735435"]
type: ["aeonikPro", "socialMono", "featureDeck"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The orange texture of the loader returns as the battery card, the phone and the panels, so the brand colour reads as the product's energy itself.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase.

## What to borrow (principle)

- Let the loader's texture become the product's material later on the page

## What to leave

- Small grey body copy on cream

## Signature move

An orange rippled texture wiping up onto a house at dusk.

## Motion

Intro: orange ripple field with the wordmark drawing (~2 s), wipe up to the hero. Wheel (Lenis, smoothed): cream panels slide over photos; the step sequence pins while visuals cross-fade; line drawings draw; the chart plots; serif statements fade over photos.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 8 video; split text; smoothed scroll (median 134 px still travelling after input stops); entry gate: Reject. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a home-energy subscription: a full-screen orange rippled texture with the wordmark that wipes up to reveal a house at dusk ('Power your home for less') with an orange card standing in for the battery, cream panels with photos at the edges ('Cut your electric bill by 20 % or more', 'Keep the lights on'), a hand reaching into a warm sun-blur, a four-step sticky sequence (subscribe, install, power on) where an orange phone, an isometric house with orange panels and a line drawing of a street swap on the right, a live chart, a dark storm section about the grid, sunset photos with a serif statement about a decentralised network, and a lilac 'Step into Daylight' close. Type: aeonikPro, socialMono, featureDeck.
Ground and ink from the measured palette (#EFE5CF, #CD8624, #FEF8EC). Motion carries the page through
an orange rippled texture wiping up onto a house at dusk. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — dusk architectural photography, isometric line drawings, UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: dusk architectural photography, isometric line drawings, UI

## Reference lock

Primary reference/direction: Daylight - home solar and battery — A home-energy subscription: a full-screen orange rippled texture with the wordmark that wipes up to reveal a house at dusk ('Power your home for less') with an orange card standing in for the battery, cream panels with photos at the edges ('Cut your electric bill by 20 % or more', 'Keep the lights on'), a hand reaching into a warm sun-blur, a four-step sticky sequence (subscribe, install, power on) where an orange phone, an isometric house with orange panels and a line drawing of a street swap on the right, a live chart, a dark storm section about the grid, sunset photos with a serif statement about a decentralised network, and a lilac 'Step into Daylight' close.
Preserve (3-5 traits): orange rippled texture loader; dusk house photography; isometric line-drawn houses; sticky numbered steps with swapping visuals; serif statements over dark photos.
Borrow only (1-2): Let the loader's texture become the product's material later on the page
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: dusk architectural photography, isometric line drawings, UI
Reject: Small grey body copy on cream
Token commitments: palette #EFE5CF, #CD8624, #FEF8EC, #2E261B, #867C64, #735435; type aeonikPro, socialMono, featureDeck; engine GSAP + Lenis linked (never vendored).
