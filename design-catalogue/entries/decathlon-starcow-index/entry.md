---
title: "Decathlon x Starcow - collab landing page"
url: https://decathlon-starcow.index.studio/
source_url: https://decathlon-starcow.index.studio/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "editorial"
family: collab-lookbook-grid-lines
dna: "Sportswear collab x a fine grid of product shots and a scattering product word list"
register: modern clean
grammar: chaptered editorial
lane: "A collab landing page: crosshair corner marks on a dark photo, 'Decathlon Starcow outdoors' over a campaign photo, a black band with condensed 'DECATHLON x STARCOW OUTDOOR', a white page with fine grid lines where campaign photos and cut-out product shots slide in and out of cells, a full-bleed campaign shot, product name callouts ('Veste'), 'Lookbook 1/8' and a finale where product names (veste, sac, chaussettes, chapka) scroll as a big word list over a marble background with photos inside the list."
mode: persuade
traits: ["fine grid lines on white", "campaign photos and product cut-outs side by side", "condensed caps", "crosshair corner marks", "product name word list finale", "marble texture ground"]
palette: ["#FFFFFF", "#8B8A80", "#010202", "#BBBAB6", "#464641", "#181A1D"]
type: ["Roboto Flex"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The fine grid makes a lookbook feel like a technical catalogue, which suits an outdoor collab, and the word list closes it like a packing list.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Pair each campaign photo with the product cut-out in a fine grid
- End with the product names as a big scrolling list

## What to leave

- Very small grid labels

## Signature move

Product names (veste, sac, chaussettes) scrolling as a big list with photos inside.

## Motion

Intro: dark with crosshair corners (~1.5 s), the campaign photo. Wheel: the black band slides up; grid cells fill as photos and cut-outs slide in from alternating sides; a full-bleed photo scales; the lookbook counter steps; the word list scrolls with photos popping between words.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a collab landing page: crosshair corner marks on a dark photo, 'Decathlon Starcow outdoors' over a campaign photo, a black band with condensed 'DECATHLON x STARCOW OUTDOOR', a white page with fine grid lines where campaign photos and cut-out product shots slide in and out of cells, a full-bleed campaign shot, product name callouts ('Veste'), 'Lookbook 1/8' and a finale where product names (veste, sac, chaussettes, chapka) scroll as a big word list over a marble background with photos inside the list. Type: Roboto Flex.
Ground and ink from the measured palette (#FFFFFF, #8B8A80, #010202). Motion carries the page through
product names (veste, sac, chaussettes) scrolling as a big list with photos inside. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — campaign and product photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: campaign and product photography

## Reference lock

Primary reference/direction: Decathlon x Starcow - collab landing page — A collab landing page: crosshair corner marks on a dark photo, 'Decathlon Starcow outdoors' over a campaign photo, a black band with condensed 'DECATHLON x STARCOW OUTDOOR', a white page with fine grid lines where campaign photos and cut-out product shots slide in and out of cells, a full-bleed campaign shot, product name callouts ('Veste'), 'Lookbook 1/8' and a finale where product names (veste, sac, chaussettes, chapka) scroll as a big word list over a marble background with photos inside the list.
Preserve (3-5 traits): fine grid lines on white; campaign photos and product cut-outs side by side; condensed caps; crosshair corner marks; product name word list finale.
Borrow only (1-2): Pair each campaign photo with the product cut-out in a fine grid; End with the product names as a big scrolling list
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: campaign and product photography
Reject: Very small grid labels
Token commitments: palette #FFFFFF, #8B8A80, #010202, #BBBAB6, #464641, #181A1D; type Roboto Flex; engine GSAP + Lenis linked (never vendored).
