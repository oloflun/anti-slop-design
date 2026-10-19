---
title: "SoulStride - mental wellbeing app"
url: https://soulstridee.webflow.io/
source_url: https://soulstridee.webflow.io/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "playful"
family: illustrated-wellbeing-cards
dna: "Mental wellbeing app x a pink character in a snowy forest and saboteur cards"
register: other
grammar: chaptered editorial
lane: "A wellbeing app on Webflow: a faded 'SoulStride' logo, 'Welcome to SoulStride / Guide to mental wellbeing' with a pink illustrated character in a snowy forest that zooms down, a trusted-by logo row, an app UI card 'Defeat the saboteurs', 'Meet the saboteurs' as a horizontal row of illustrated cards (Ruminator, Slacker, Oblivious, Appeaser, The Pessimist, Resentful, Impulsive, Anxious), then 'Cultivate inner strength with Valor, Empathy and Insight' where three character cards fly in and fan over a green landscape."
mode: persuade
traits: ["flat illustrated characters", "horizontal card row", "cards flying in and fanning", "snowy forest scene", "pink, mint and cream", "condensed caps"]
palette: ["#FFFFFF", "#B1ABA0", "#E1F0E9"]
type: ["Satoshi", "Obviouslydemo"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Naming each inner obstacle as a character turns a wellbeing pitch into a cast you can recognise yourself in.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Cast the problems as named characters on cards
- Fan the solution cards in over the scene

## What to leave

- Webflow badge

## Signature move

Three pink character cards (Valor, Empathy, Insight) fanning over a green landscape.

## Motion

Intro: the logo fades from white (~2 s). Wheel: the forest scene zooms; logos slide; the UI card slides; the saboteur row scrolls sideways; the landscape rises; cards fly in one by one and rotate into a fan.

Measured (`motion/probe.json`): GSAP 3.12.5; 2 pinned sections; smoothed scroll (median 130 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a wellbeing app on Webflow: a faded 'SoulStride' logo, 'Welcome to SoulStride / Guide to mental wellbeing' with a pink illustrated character in a snowy forest that zooms down, a trusted-by logo row, an app UI card 'Defeat the saboteurs', 'Meet the saboteurs' as a horizontal row of illustrated cards (Ruminator, Slacker, Oblivious, Appeaser, The Pessimist, Resentful, Impulsive, Anxious), then 'Cultivate inner strength with Valor, Empathy and Insight' where three character cards fly in and fan over a green landscape. Type: Satoshi, Obviouslydemo.
Ground and ink from the measured palette (#FFFFFF, #B1ABA0, #E1F0E9). Motion carries the page through
three pink character cards (Valor, Empathy, Insight) fanning over a green landscape. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — flat illustration

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: flat illustration

## Reference lock

Primary reference/direction: SoulStride - mental wellbeing app — A wellbeing app on Webflow: a faded 'SoulStride' logo, 'Welcome to SoulStride / Guide to mental wellbeing' with a pink illustrated character in a snowy forest that zooms down, a trusted-by logo row, an app UI card 'Defeat the saboteurs', 'Meet the saboteurs' as a horizontal row of illustrated cards (Ruminator, Slacker, Oblivious, Appeaser, The Pessimist, Resentful, Impulsive, Anxious), then 'Cultivate inner strength with Valor, Empathy and Insight' where three character cards fly in and fan over a green landscape.
Preserve (3-5 traits): flat illustrated characters; horizontal card row; cards flying in and fanning; snowy forest scene; pink, mint and cream.
Borrow only (1-2): Cast the problems as named characters on cards; Fan the solution cards in over the scene
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: flat illustration
Reject: Webflow badge
Token commitments: palette #FFFFFF, #B1ABA0, #E1F0E9; type Satoshi, Obviouslydemo; engine GSAP + Lenis linked (never vendored).
