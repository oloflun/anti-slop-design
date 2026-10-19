---
title: "SÖM - functional elixir"
url: https://drinksom.eu/
source_url: https://drinksom.eu/
captured: 2026-10-03
origin: raw-url
extract: none
category: consumer-brand
category2: "product-focused"
family: dark-video-hero-supplement-shop
dna: "Functional drink shot x dark film hero, red packaging, grey studio cards and an aerial plantation for the origin story"
register: modern clean
grammar: chaptered editorial
lane: "A shop for a daily functional shot: a dark video hero of someone drinking the vial ('Power. Focus. Presence. In one daily shot'), a product block with the red box and subscribe options, a pinned vial beside 'Elixirs that give you clear mind, steady energy, and no crash', a rail of ritual photos, an aerial plantation for the origin, testimonial cards, a research section and journal cards, then a newsletter footer."
mode: persuade
traits: ["dark film hero with the product in use", "red packaging as the only colour", "aerial plantation as origin chapter", "rail of ritual photo cards", "journal cards at the foot"]
palette: ["#B7B7B7", "#52514A", "#292B28", "#131513", "#FDFDFD", "#868580"]
type: ["ABC Diatype", "ABC Diatype Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The product is shown being used before it is shown boxed, so the hero sells the moment and the shop block below only has to sell the format.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: .RAW).

## What to borrow (principle)

- Open on the product in use, put the boxed product one scroll later

## What to leave

- Region modal on arrival
- Standard shop blocks between the chapters

## Signature move

A vial held at the lips in a dark film hero, red cap the only colour on screen.

## Motion

Intro: region modal over the video. Wheel (native scroll): hero video plays, product and copy blocks fade up, the vial sits beside the elixir statement, ritual and testimonial rails slide sideways on arrows.

Measured (`motion/probe.json`): entry gate: CLOSE. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a shop for a daily functional shot: a dark video hero of someone drinking the vial ('Power. Focus. Presence. In one daily shot'), a product block with the red box and subscribe options, a pinned vial beside 'Elixirs that give you clear mind, steady energy, and no crash', a rail of ritual photos, an aerial plantation for the origin, testimonial cards, a research section and journal cards, then a newsletter footer. Type: ABC Diatype, ABC Diatype Mono.
Ground and ink from the measured palette (#B7B7B7, #52514A, #292B28). Motion carries the page through
a vial held at the lips in a dark film hero, red cap the only colour on screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills, product renders, aerial landscape

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills, product renders, aerial landscape

## Reference lock

Primary reference/direction: SÖM - functional elixir — A shop for a daily functional shot: a dark video hero of someone drinking the vial ('Power. Focus. Presence. In one daily shot'), a product block with the red box and subscribe options, a pinned vial beside 'Elixirs that give you clear mind, steady energy, and no crash', a rail of ritual photos, an aerial plantation for the origin, testimonial cards, a research section and journal cards, then a newsletter footer.
Preserve (3-5 traits): dark film hero with the product in use; red packaging as the only colour; aerial plantation as origin chapter; rail of ritual photo cards; journal cards at the foot.
Borrow only (1-2): Open on the product in use, put the boxed product one scroll later
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills, product renders, aerial landscape
Reject: Region modal on arrival; Standard shop blocks between the chapters
Token commitments: palette #B7B7B7, #52514A, #292B28, #131513, #FDFDFD, #868580; type ABC Diatype, ABC Diatype Mono; engine GSAP + Lenis linked (never vendored).
