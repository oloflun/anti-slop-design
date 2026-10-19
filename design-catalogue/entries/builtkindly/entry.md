---
title: "Built Kindly - Kind. By Design."
url: https://www.builtkindly.com/
source_url: https://www.builtkindly.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: line-illustration-kind-studio
dna: "Product studio x warm line illustrations and a drawn path"
register: illustrated dark
grammar: chaptered editorial
lane: "A product studio on cream: 'Others build fast. We build kindly.' with a green line drawing across, a line illustration of two people at a laptop, an inline-illustrated statement with tiny cartoon objects between words, a character with a bowl, a laptop that rises with the product UI, and a footer landscape with hot-air balloons drifting over hills."
mode: persuade
traits: ["warm cream and plum palette", "line illustrations with flat colour", "inline mini illustrations inside the headline", "green path line drawing through sections", "laptop rising as a product frame", "hot-air balloon landscape footer"]
palette: ["#FEFAE7", "#CEC8BE", "#898685"]
type: ["Bree Serif", "Montserrat"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Illustration does the tone work for a 'kind' studio; the inline drawings in the statement and the drifting balloons make the copy feel friendly without stock imagery.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Small illustrations set inline between words of a statement
- A drawn line that threads through every section

## What to leave

- Thin body text
- Footer repeats for a long time

## Signature move

Hot-air balloons drifting over illustrated hills in the footer.

## Motion

Intro: cream with the tagline and a green line drawing across (~1.5 s). Wheel (Lenis ~60 px glide): the hero illustration settles; the statement fills with inline drawings popping in; the line draws onward; the laptop rises and opens to the UI; the landscape slides up and balloons float.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; 1 video; smoothed scroll (median 77 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the chaptered editorial grammar: a product studio on cream: 'Others build fast. We build kindly.' with a green line drawing across, a line illustration of two people at a laptop, an inline-illustrated statement with tiny cartoon objects between words, a character with a bowl, a laptop that rises with the product UI, and a footer landscape with hot-air balloons drifting over hills. Type: Bree Serif, Montserrat.
Ground and ink from the measured palette (#FEFAE7, #CEC8BE, #898685). Motion carries the page through
hot-air balloons drifting over illustrated hills in the footer. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — line illustration, product UI

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: line illustration, product UI

## Reference lock

Primary reference/direction: Built Kindly - Kind. By Design. — A product studio on cream: 'Others build fast. We build kindly.' with a green line drawing across, a line illustration of two people at a laptop, an inline-illustrated statement with tiny cartoon objects between words, a character with a bowl, a laptop that rises with the product UI, and a footer landscape with hot-air balloons drifting over hills.
Preserve (3-5 traits): warm cream and plum palette; line illustrations with flat colour; inline mini illustrations inside the headline; green path line drawing through sections; laptop rising as a product frame.
Borrow only (1-2): Small illustrations set inline between words of a statement; A drawn line that threads through every section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: line illustration, product UI
Reject: Thin body text; Footer repeats for a long time
Token commitments: palette #FEFAE7, #CEC8BE, #898685; type Bree Serif, Montserrat; engine GSAP + Lenis linked (never vendored).
