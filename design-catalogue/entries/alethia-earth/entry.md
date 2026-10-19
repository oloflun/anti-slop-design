---
title: "Alethia - climate data"
url: https://www.alethia.earth/
source_url: https://www.alethia.earth/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: moss-lens-climate-tech
dna: "Climate data x a circular moss lens opening onto a misty landscape, sensor hardware on black and lime accents"
register: cinematic dark
grammar: chaptered editorial
lane: "A climate-measurement company: a dot loader on black, a circular opening framed by moss through which a misty field of seedlings appears and widens to full screen with small data chips, a weather mast emerging from the mist, two image cards, then a black studio where the sensor head is lit piece by piece ('Scientific rigor. Commercial precision.'), blockchain claims beside an anemometer, white sections with floating data tiles and tCO2e chips, case studies, and a huge lime wordmark footer."
mode: persuade
traits: ["circular moss vignette that widens", "misty landscape video", "sensor hardware on black", "lime data chips", "floating data tiles", "huge lime wordmark"]
palette: ["#101E10", "#D4D4D4", "#000001", "#686C46", "#3B3F2B", "#A3A58E"]
type: ["Geist", "Geist Mono", "Geist Medium", "Geist Regular"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Opening through a ring of moss frames the product as looking at nature first, then the hardware arrives as the instrument for that look.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: hellohello).

## What to borrow (principle)

- Open through a natural frame that widens into the scene

## What to leave

- Generic case study cards

## Signature move

A ring of moss opening onto a misty field of seedlings.

## Motion

Intro: dot pulses on black (~2 s). Wheel (Lenis, no GSAP): the moss vignette scales open; chips fade in; the mast rises; hardware is lit with masked reveals; tiles float with parallax.

Measured (`motion/probe.json`): Lenis; 5 video; smoothed scroll (median 105 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a climate-measurement company: a dot loader on black, a circular opening framed by moss through which a misty field of seedlings appears and widens to full screen with small data chips, a weather mast emerging from the mist, two image cards, then a black studio where the sensor head is lit piece by piece ('Scientific rigor. Commercial precision.'), blockchain claims beside an anemometer, white sections with floating data tiles and tCO2e chips, case studies, and a huge lime wordmark footer. Type: Geist, Geist Mono, Geist Medium, Geist Regular.
Ground and ink from the measured palette (#101E10, #D4D4D4, #000001). Motion carries the page through
a ring of moss opening onto a misty field of seedlings. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — nature video, product photography on black

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: nature video, product photography on black

## Reference lock

Primary reference/direction: Alethia - climate data — A climate-measurement company: a dot loader on black, a circular opening framed by moss through which a misty field of seedlings appears and widens to full screen with small data chips, a weather mast emerging from the mist, two image cards, then a black studio where the sensor head is lit piece by piece ('Scientific rigor. Commercial precision.'), blockchain claims beside an anemometer, white sections with floating data tiles and tCO2e chips, case studies, and a huge lime wordmark footer.
Preserve (3-5 traits): circular moss vignette that widens; misty landscape video; sensor hardware on black; lime data chips; floating data tiles.
Borrow only (1-2): Open through a natural frame that widens into the scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: nature video, product photography on black
Reject: Generic case study cards
Token commitments: palette #101E10, #D4D4D4, #000001, #686C46, #3B3F2B, #A3A58E; type Geist, Geist Mono, Geist Medium, Geist Regular; engine GSAP + Lenis linked (never vendored).
