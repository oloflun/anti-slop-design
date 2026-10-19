---
title: "Emily in Paris Experiences - Tours in Paris and Rome"
url: https://www.parisbyemily.com/
source_url: https://www.parisbyemily.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "consumer-brand"
family: two-city-card-chooser
dna: "Emily in Paris tours x two tilted video cards for Paris and Rome"
register: warm photographic
grammar: split stage
lane: "A tour brand tied to the TV series: black 'Where will your Emily story begin?', then two tall rounded video cards side by side, 'Paris' and 'Rome', slightly tilted on a peach ground, each cycling clips (champagne, boat, cafe) in serif lettering, as the choice between two experiences."
mode: persuade
traits: ["two tilted video cards", "serif city names", "peach ground", "clips cycling inside cards", "question as the headline", "cookie decline"]
palette: ["#EED5BB", "#000000", "#584B3F", "#281817", "#ACA091"]
type: ["Roslindaledisplaycondensed", "Ppneuemontreal", "Mangogrotesque"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

The whole page is one choice; two moving cards make the decision visual and playful, like picking a postcard.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: LOOP).

## What to borrow (principle)

- Make the main choice two tilted moving cards

## What to leave

- Nothing else on scroll
- Small card labels

## Signature move

Two tilted video cards, Paris and Rome, cycling clips side by side.

## Motion

Intro: black, the question appears in serif (~2 s); the two cards slide up tilted and the ground turns peach. Wheel (virtual): the cards cycle through clips and shift tilt slightly; hover would enlarge one.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; 2 video; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: Decline. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the split stage grammar: a tour brand tied to the TV series: black 'Where will your Emily story begin?', then two tall rounded video cards side by side, 'Paris' and 'Rome', slightly tilted on a peach ground, each cycling clips (champagne, boat, cafe) in serif lettering, as the choice between two experiences. Type: Roslindaledisplaycondensed, Ppneuemontreal, Mangogrotesque.
Ground and ink from the measured palette (#EED5BB, #000000, #584B3F). Motion carries the page through
two tilted video cards, Paris and Rome, cycling clips side by side. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — travel and lifestyle video

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: travel and lifestyle video

## Reference lock

Primary reference/direction: Emily in Paris Experiences - Tours in Paris and Rome — A tour brand tied to the TV series: black 'Where will your Emily story begin?', then two tall rounded video cards side by side, 'Paris' and 'Rome', slightly tilted on a peach ground, each cycling clips (champagne, boat, cafe) in serif lettering, as the choice between two experiences.
Preserve (3-5 traits): two tilted video cards; serif city names; peach ground; clips cycling inside cards; question as the headline.
Borrow only (1-2): Make the main choice two tilted moving cards
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: travel and lifestyle video
Reject: Nothing else on scroll; Small card labels
Token commitments: palette #EED5BB, #000000, #584B3F, #281817, #ACA091; type Roslindaledisplaycondensed, Ppneuemontreal, Mangogrotesque; engine GSAP + Lenis linked (never vendored).
