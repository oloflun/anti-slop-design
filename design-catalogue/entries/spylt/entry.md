---
title: "SPYLT - milk soda launch"
url: https://www.spylt.com/
source_url: https://www.spylt.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: consumer-brand
category2: "playful"
family: drink-launch-countdown
dna: "Protein milk drink x a countdown teaser and a tilted word ticker"
register: other
grammar: chaptered editorial
lane: "A drink launch teaser: a man holding a pack against orange with 'We shouldn't tell you this' in condensed caps, a live countdown, a tilted multicolour ticker ('Crack. Chug. Chill.'), then light blue 'Can't wait? Shop now / or find some IRL' with the pack and retailer logos."
mode: persuade
traits: ["live countdown", "tilted multicolour ticker", "condensed caps", "orange then sky blue", "retailer logos"]
palette: ["#73CEE6", "#CE573A", "#6F3526", "#CDE7E5", "#AF9683", "#29B6DA"]
type: ["Assistant", "tusker_grotesk4700_bold", "proxima_novaregular", "proxima_novabold"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

A teaser done simply: countdown, attitude headline, and a ticker that sounds like the product.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- A tilted ticker of the product's verbs

## What to leave

- Very short page

## Signature move

A tilted 'Crack. Chug. Chill.' ticker under a countdown.

## Motion

Intro: the hero with the countdown ticking. Wheel: the ticker slides; the blue panel rises; the pack scales; logos fade.

Measured (`motion/probe.json`): entry gate: Skip to content. Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a drink launch teaser: a man holding a pack against orange with 'We shouldn't tell you this' in condensed caps, a live countdown, a tilted multicolour ticker ('Crack. Chug. Chill.'), then light blue 'Can't wait? Shop now / or find some IRL' with the pack and retailer logos. Type: Assistant, tusker_grotesk4700_bold, proxima_novaregular, proxima_novabold.
Ground and ink from the measured palette (#73CEE6, #CE573A, #6F3526). Motion carries the page through
a tilted 'Crack. Chug. Chill.' ticker under a countdown. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — lifestyle photography, product packs

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: lifestyle photography, product packs

## Reference lock

Primary reference/direction: SPYLT - milk soda launch — A drink launch teaser: a man holding a pack against orange with 'We shouldn't tell you this' in condensed caps, a live countdown, a tilted multicolour ticker ('Crack. Chug. Chill.'), then light blue 'Can't wait? Shop now / or find some IRL' with the pack and retailer logos.
Preserve (3-5 traits): live countdown; tilted multicolour ticker; condensed caps; orange then sky blue; retailer logos.
Borrow only (1-2): A tilted ticker of the product's verbs
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: lifestyle photography, product packs
Reject: Very short page
Token commitments: palette #73CEE6, #CE573A, #6F3526, #CDE7E5, #AF9683, #29B6DA; type Assistant, tusker_grotesk4700_bold, proxima_novaregular, proxima_novabold; engine GSAP + Lenis linked (never vendored).
