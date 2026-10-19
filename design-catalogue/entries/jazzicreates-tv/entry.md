---
title: "Jazmin Wong - Creative Content Strategist"
url: https://www.jazzicreates.tv/
source_url: https://www.jazzicreates.tv/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: pink-content-creator-folio
dna: "Content strategist x hot pink ground and stacking colour service cards"
register: other
grammar: chaptered editorial
lane: "A content creator's folio on hot pink: 'JAZMIN WONG' huge with a strip of photo thumbnails, a project list where client names stack over a photo, an about with stat cards, service cards in pink, blue, green and yellow that stack (UGC, Photography, Short-form video, Content strategy), and 'Let's work together' with tilted pill buttons."
mode: persuade
traits: ["hot pink ground", "client name stack over photo", "pastel stacking service cards", "numbered service labels", "tilted pill buttons", "leopard chat icon"]
palette: ["#C43770", "#F0D8E1", "#271C18", "#827264", "#D3B8B7", "#D2829B"]
type: ["Playfair Display", "saans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The pastel cards stacking on hot pink give a personal brand energy while keeping services scannable.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Stack services as pastel cards each with its own colour

## What to leave

- Generic stat cards

## Signature move

Pastel service cards stacking on hot pink.

## Motion

Intro: pink with the name rising (~1.5 s). Wheel (Lenis, 5 pins): the thumbnail strip slides; client names change over a pinned photo; stats count; service cards stack one over the other; buttons drop in tilted.

Measured (`motion/probe.json`): GSAP 3.13.0; 5 pinned sections; Lenis; 4 video; smoothed scroll (median 128 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a content creator's folio on hot pink: 'JAZMIN WONG' huge with a strip of photo thumbnails, a project list where client names stack over a photo, an about with stat cards, service cards in pink, blue, green and yellow that stack (UGC, Photography, Short-form video, Content strategy), and 'Let's work together' with tilted pill buttons. Type: Playfair Display, saans.
Ground and ink from the measured palette (#C43770, #F0D8E1, #271C18). Motion carries the page through
pastel service cards stacking on hot pink. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lifestyle and food photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lifestyle and food photography

## Reference lock

Primary reference/direction: Jazmin Wong - Creative Content Strategist — A content creator's folio on hot pink: 'JAZMIN WONG' huge with a strip of photo thumbnails, a project list where client names stack over a photo, an about with stat cards, service cards in pink, blue, green and yellow that stack (UGC, Photography, Short-form video, Content strategy), and 'Let's work together' with tilted pill buttons.
Preserve (3-5 traits): hot pink ground; client name stack over photo; pastel stacking service cards; numbered service labels; tilted pill buttons.
Borrow only (1-2): Stack services as pastel cards each with its own colour
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lifestyle and food photography
Reject: Generic stat cards
Token commitments: palette #C43770, #F0D8E1, #271C18, #827264, #D3B8B7, #D2829B; type Playfair Display, saans; engine GSAP + Lenis linked (never vendored).
