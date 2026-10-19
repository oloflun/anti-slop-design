---
title: "Capitolium - club shirt collaboration"
url: https://www.collabcapitolium.fr/
source_url: https://www.collabcapitolium.fr/
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "luxury-craft"
family: arcade-chapters-shirt-launch
dna: "Club shirt launch x a city hall's arcades and council chamber, gold engraved caps CAPITOLIUM, script chapter titles, cream paper ground"
register: historical art
grammar: chaptered editorial
lane: "A club's shirt launch staged inside a historic city hall: an aerial dusk shot of the old town with a gold CAPITOLIUM wordmark and a script motto, a pan down to the building's facade, then chapters on cream paper ('Les arcades', 'Salle du conseil'), each opening through arched windows that grow into full-bleed photographs of painted ceilings and the chamber, with the shirt on plinths, on a player and folded as an object between the rooms."
mode: persuade
traits: ["gold engraved caps wordmark over every chapter", "arched windows that grow into the room photograph", "script chapter title set across the bottom of the photo", "cream paper ground between rooms", "shirt recurring as plinth object, worn, folded"]
palette: ["#0E0A0D", "#553C2F", "#362724", "#F7F7F6", "#8A7F71"]
type: ["gin", "Edwardian Script", "Times"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

The building is the argument: every chapter opens through the arch shape of the architecture the shirt borrows from, so the product reads as part of the place rather than placed in front of it.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Jonas Reymondin, Local Studio, Supercolor).

## What to borrow (principle)

- Open each chapter through a shape taken from the subject's architecture (an arch) that grows to full bleed
- Let the product recur in three states between chapters: displayed, worn, held

## What to leave

- Cookie and sound prompts over the intro

## Signature move

Three arched windows on cream that widen into the painted council chamber.

## Motion

Intro: aerial dusk shot with wordmark, ENTRER, then a slow drop to the facade. Wheel (Lenis): arches grow to full bleed, script titles slide in under the photo, shirt cards and portraits drift at different speeds on the paper ground, chapter bar updates at the foot.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; 11 video; split text; smoothed scroll (median 131 px still travelling after input stops); entry gate: Non merci, Entrer. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A historical art page in the chaptered editorial grammar: a club's shirt launch staged inside a historic city hall: an aerial dusk shot of the old town with a gold CAPITOLIUM wordmark and a script motto, a pan down to the building's facade, then chapters on cream paper ('Les arcades', 'Salle du conseil'), each opening through arched windows that grow into full-bleed photographs of painted ceilings and the chamber, with the shirt on plinths, on a player and folded as an object between the rooms. Type: gin, Edwardian Script, Times.
Ground and ink from the measured palette (#0E0A0D, #553C2F, #362724). Motion carries the page through
three arched windows on cream that widen into the painted council chamber. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural photography and product shots

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural photography and product shots

## Reference lock

Primary reference/direction: Capitolium - club shirt collaboration — A club's shirt launch staged inside a historic city hall: an aerial dusk shot of the old town with a gold CAPITOLIUM wordmark and a script motto, a pan down to the building's facade, then chapters on cream paper ('Les arcades', 'Salle du conseil'), each opening through arched windows that grow into full-bleed photographs of painted ceilings and the chamber, with the shirt on plinths, on a player and folded as an object between the rooms.
Preserve (3-5 traits): gold engraved caps wordmark over every chapter; arched windows that grow into the room photograph; script chapter title set across the bottom of the photo; cream paper ground between rooms; shirt recurring as plinth object, worn, folded.
Borrow only (1-2): Open each chapter through a shape taken from the subject's architecture (an arch) that grows to full bleed; Let the product recur in three states between chapters: displayed, worn, held
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural photography and product shots
Reject: Cookie and sound prompts over the intro
Token commitments: palette #0E0A0D, #553C2F, #362724, #F7F7F6, #8A7F71; type gin, Edwardian Script, Times; engine GSAP + Lenis linked (never vendored).
