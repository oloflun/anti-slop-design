---
title: "ZapConnect 2026 - Zapier conference"
url: https://zapier.com/zapconnect
source_url: https://zapier.com/zapconnect
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "editorial"
family: illustrated-city-event
dna: "Product conference x an illustrated city at sunset with a walker on a hill"
register: warm photographic
grammar: chaptered editorial
lane: "A conference site: 'Rethink. Rebuild. Refound.' in serif over an illustrated city of towers with an orange sun and clouds, the camera pulling down to a figure walking up a sandy hill, a dark band 'ZapConnect 2026 has ended' with words brightening, a registration form over the city illustration, speakers in a grid of portraits, 'What to expect', 'Can AI transform a business in a single afternoon?' with an orange 'Build-Off' card, and awards."
mode: persuade
traits: ["illustrated city skyline", "orange sun", "figure walking up a hill", "serif headlines", "words brightening", "speaker portrait grid"]
palette: ["#1F1614", "#423C44", "#6C7BBF", "#875B4B", "#A7949E"]
type: ["Tiempos Headline Light", "Tiempos Text Regular", "Inter", "Degular Display"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The illustrated city with a lone walker gives a SaaS conference a story; the rest is a clean event page.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Adriano Reis).

## What to borrow (principle)

- Pan an illustrated scene down to one small figure

## What to leave

- Long speaker list

## Signature move

An illustrated city at sunset with a figure walking up a hill.

## Motion

Intro: the illustrated city. Wheel: the scene pans down to the hill and walker; the headline fades; the dark band rises; words brighten; the form slides; portraits stagger.

Measured (`motion/probe.json`): Lenis; 4 video; smoothed scroll (median 151 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a conference site: 'Rethink. Rebuild. Refound.' in serif over an illustrated city of towers with an orange sun and clouds, the camera pulling down to a figure walking up a sandy hill, a dark band 'ZapConnect 2026 has ended' with words brightening, a registration form over the city illustration, speakers in a grid of portraits, 'What to expect', 'Can AI transform a business in a single afternoon?' with an orange 'Build-Off' card, and awards. Type: Tiempos Headline Light, Tiempos Text Regular, Inter, Degular Display.
Ground and ink from the measured palette (#1F1614, #423C44, #6C7BBF). Motion carries the page through
an illustrated city at sunset with a figure walking up a hill. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — illustration, speaker portraits

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: illustration, speaker portraits

## Reference lock

Primary reference/direction: ZapConnect 2026 - Zapier conference — A conference site: 'Rethink. Rebuild. Refound.' in serif over an illustrated city of towers with an orange sun and clouds, the camera pulling down to a figure walking up a sandy hill, a dark band 'ZapConnect 2026 has ended' with words brightening, a registration form over the city illustration, speakers in a grid of portraits, 'What to expect', 'Can AI transform a business in a single afternoon?' with an orange 'Build-Off' card, and awards.
Preserve (3-5 traits): illustrated city skyline; orange sun; figure walking up a hill; serif headlines; words brightening.
Borrow only (1-2): Pan an illustrated scene down to one small figure
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: illustration, speaker portraits
Reject: Long speaker list
Token commitments: palette #1F1614, #423C44, #6C7BBF, #875B4B, #A7949E; type Tiempos Headline Light, Tiempos Text Regular, Inter, Degular Display; engine GSAP + Lenis linked (never vendored).
