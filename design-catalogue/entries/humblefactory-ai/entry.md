---
title: "Humble - factory operations OS"
url: https://humblefactory.ai/
source_url: https://humblefactory.ai/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: illustrated-factory-saas
dna: "Factory software x painted illustration panels and tilted checklist cards"
register: warm photographic
grammar: chaptered editorial
lane: "A B2B page: a red mountain painting, 'Your factory's next 10 years of productivity' beside an illustrated engineer over an orange band, 'Is Humble right for you?' as a tilted checklist card, 'What we need from you' cards, 'Time at a glance' stats, a black card 'How we de-risk fast change', 'Ready to run the numbers?' over a painted factory at dusk, and 'On demand factory OS, delivered overnight' footer."
mode: persuade
traits: ["painted illustration panels", "tilted checklist card", "orange arc shapes", "stat tiles", "black feature card", "serif headline"]
palette: ["#FAFAFA", "#060505", "#2B2321", "#C18C79"]
type: ["Atkinson Hyperlegible Mono", "Kode Mono", "Bricolage Grotesque", "Geist"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The painted factory and engineer give an operations tool a human scale; the cards are plain.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Lee Jay Robertson).

## What to borrow (principle)

- Open and close with the same painted scene at different times of day

## What to leave

- Generic card stack

## Signature move

A painted factory at dusk under 'Ready to run the numbers?'.

## Motion

Intro: the red mountain (~1 s), the hero. Wheel: cards tilt and settle; stat tiles rise; the black card slides; the factory painting rises and holds.

Measured (`motion/probe.json`): Lenis; split text; smoothed scroll (median 122 px still travelling after input stops); entry gate: Start my 24h Build. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a B2B page: a red mountain painting, 'Your factory's next 10 years of productivity' beside an illustrated engineer over an orange band, 'Is Humble right for you?' as a tilted checklist card, 'What we need from you' cards, 'Time at a glance' stats, a black card 'How we de-risk fast change', 'Ready to run the numbers?' over a painted factory at dusk, and 'On demand factory OS, delivered overnight' footer. Type: Atkinson Hyperlegible Mono, Kode Mono, Bricolage Grotesque, Geist.
Ground and ink from the measured palette (#FAFAFA, #060505, #2B2321). Motion carries the page through
a painted factory at dusk under 'Ready to run the numbers?'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustration

## Reference lock

Primary reference/direction: Humble - factory operations OS — A B2B page: a red mountain painting, 'Your factory's next 10 years of productivity' beside an illustrated engineer over an orange band, 'Is Humble right for you?' as a tilted checklist card, 'What we need from you' cards, 'Time at a glance' stats, a black card 'How we de-risk fast change', 'Ready to run the numbers?' over a painted factory at dusk, and 'On demand factory OS, delivered overnight' footer.
Preserve (3-5 traits): painted illustration panels; tilted checklist card; orange arc shapes; stat tiles; black feature card.
Borrow only (1-2): Open and close with the same painted scene at different times of day
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustration
Reject: Generic card stack
Token commitments: palette #FAFAFA, #060505, #2B2321, #C18C79; type Atkinson Hyperlegible Mono, Kode Mono, Bricolage Grotesque, Geist; engine GSAP + Lenis linked (never vendored).
