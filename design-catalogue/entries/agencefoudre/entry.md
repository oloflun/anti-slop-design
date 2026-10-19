---
title: "Agence Foudre - social media agency"
url: https://www.agencefoudre.com/
source_url: https://www.agencefoudre.com/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: lightning-pink-social-agency
dna: "Social media agency x a lightning bolt wipe and stacked colour service cards"
register: other
grammar: chaptered editorial
lane: "A French agency on pink: a manifesto line, a cream lightning bolt that grows to wipe the screen, 'FOUDRE / HUMAN SOCIAL CLUB' with the team photo, 'Nous électrisons vos réseaux', case cards in a horizontal row with tilted phone frames on changing grounds, 'C'est l'impact de votre sincérité', a diagonal panel 'Et frapper fort', 'Raisonner pour mieux résonner' with a photo stack, numbered service cards stacking (01 to 05) in pink and green, 'Pourquoi choisir Foudre' with cards fanning, FAQ."
mode: persuade
traits: ["lightning bolt wipe", "condensed caps in pink and green", "numbered stacking cards", "diagonal panel", "horizontal case row", "persistent mini card bottom right"]
palette: ["#F29FBD", "#FAE8E2", "#B7C0C7", "#AB6388", "#9EA4B3"]
type: ["Clash Grotesk", "Beni"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The bolt wipe is the name made into a transition; the stacked numbered cards make the method feel tangible.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Troa).

## What to borrow (principle)

- Turn the name's symbol into the screen wipe

## What to leave

- Persistent card overlaps content

## Signature move

A cream lightning bolt growing to wipe a pink screen.

## Motion

Intro: pink with a manifesto (~2 s), a bolt grows and wipes. Wheel: the team photo rises; case cards slide; grounds change per case; a diagonal panel sweeps; service cards stack one on another; cards fan out.

Measured (`motion/probe.json`): Lenis; Barba page transitions; 1 video; smoothed scroll (median 168 px still travelling after input stops); entry gate: Play. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a French agency on pink: a manifesto line, a cream lightning bolt that grows to wipe the screen, 'FOUDRE / HUMAN SOCIAL CLUB' with the team photo, 'Nous électrisons vos réseaux', case cards in a horizontal row with tilted phone frames on changing grounds, 'C'est l'impact de votre sincérité', a diagonal panel 'Et frapper fort', 'Raisonner pour mieux résonner' with a photo stack, numbered service cards stacking (01 to 05) in pink and green, 'Pourquoi choisir Foudre' with cards fanning, FAQ. Type: Clash Grotesk, Beni.
Ground and ink from the measured palette (#F29FBD, #FAE8E2, #B7C0C7). Motion carries the page through
a cream lightning bolt growing to wipe a pink screen. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — team and case photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: team and case photography

## Reference lock

Primary reference/direction: Agence Foudre - social media agency — A French agency on pink: a manifesto line, a cream lightning bolt that grows to wipe the screen, 'FOUDRE / HUMAN SOCIAL CLUB' with the team photo, 'Nous électrisons vos réseaux', case cards in a horizontal row with tilted phone frames on changing grounds, 'C'est l'impact de votre sincérité', a diagonal panel 'Et frapper fort', 'Raisonner pour mieux résonner' with a photo stack, numbered service cards stacking (01 to 05) in pink and green, 'Pourquoi choisir Foudre' with cards fanning, FAQ.
Preserve (3-5 traits): lightning bolt wipe; condensed caps in pink and green; numbered stacking cards; diagonal panel; horizontal case row.
Borrow only (1-2): Turn the name's symbol into the screen wipe
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: team and case photography
Reject: Persistent card overlaps content
Token commitments: palette #F29FBD, #FAE8E2, #B7C0C7, #AB6388, #9EA4B3; type Clash Grotesk, Beni; engine GSAP + Lenis linked (never vendored).
