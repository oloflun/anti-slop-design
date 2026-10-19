---
title: "Clay Boan - Multidisciplinary Designer"
url: https://www.clayboan.com/
source_url: https://www.clayboan.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: blackletter-tilted-cards-folio
dna: "Multidisciplinary designer x blackletter names on tilted brand-campaign cards"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A designer folio: a diamond loader with a counter, 'CLAY' in white blackletter on black with a dark sculpture, the page tilts to white, then case cards (Apple, Nike x NBA, Google, Gucci x Oura) slide in at angles and straighten, each name in a blackletter-inflected display, a 3D hand with a ring for 'Bonjour / Hallo' marquee and a phone render."
mode: read
traits: ["blackletter wordmark", "cards entering tilted and straightening", "big brand campaign imagery", "blackletter-inflected display names", "3D hand with ring", "greeting marquee"]
palette: ["#0E0E0E", "#FFFFFF", "#6A4F42", "#2F2321", "#B5A69C"]
type: ["Emeritus Display", "Aeonik Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The tilted entry of each card is a simple, repeatable transition that makes high-profile client work feel dynamic.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Enter case cards tilted and straighten them as they arrive

## What to leave

- White gaps between cards

## Signature move

Tilted brand campaign cards straightening under blackletter names.

## Motion

Intro: white diamond and counter to 99 (~2 s), black 'CLAY' with a sculpture. Wheel (smooth): the black panel tilts away; each card slides up tilted, straightens, the name rises over it and it tilts out as the next arrives; the hand rotates; the marquee runs.

Measured (`motion/probe.json`): GSAP 3.12.5; WebGL canvas x1 (three.js); 1 video; virtual scroll (window never scrolls; transform/WebGL scroller). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a designer folio: a diamond loader with a counter, 'CLAY' in white blackletter on black with a dark sculpture, the page tilts to white, then case cards (Apple, Nike x NBA, Google, Gucci x Oura) slide in at angles and straighten, each name in a blackletter-inflected display, a 3D hand with a ring for 'Bonjour / Hallo' marquee and a phone render. Type: Emeritus Display, Aeonik Pro.
Ground and ink from the measured palette (#0E0E0E, #FFFFFF, #6A4F42). Motion carries the page through
tilted brand campaign cards straightening under blackletter names. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — brand campaign photography, 3D hand

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: brand campaign photography, 3D hand

## Reference lock

Primary reference/direction: Clay Boan - Multidisciplinary Designer — A designer folio: a diamond loader with a counter, 'CLAY' in white blackletter on black with a dark sculpture, the page tilts to white, then case cards (Apple, Nike x NBA, Google, Gucci x Oura) slide in at angles and straighten, each name in a blackletter-inflected display, a 3D hand with a ring for 'Bonjour / Hallo' marquee and a phone render.
Preserve (3-5 traits): blackletter wordmark; cards entering tilted and straightening; big brand campaign imagery; blackletter-inflected display names; 3D hand with ring.
Borrow only (1-2): Enter case cards tilted and straighten them as they arrive
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: brand campaign photography, 3D hand
Reject: White gaps between cards
Token commitments: palette #0E0E0E, #FFFFFF, #6A4F42, #2F2321, #B5A69C; type Emeritus Display, Aeonik Pro; engine GSAP + Lenis linked (never vendored).
