---
title: "Noomo Valentime - immersive story about love"
url: https://valentime.noomoagency.com/
source_url: https://valentime.noomoagency.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: valentine-myth-white-3d-world
dna: "Agency Valentine piece x a white marble world with red petals and a gold heart"
register: modern clean
grammar: continuous world
lane: "An interactive story of Saint Valentine: a drawn heart loader on blush, 'The Story' with a gold heart in an ornate mirror replacing the O, then a white misty world of marble columns over water where red petals drift, scenes of the story appear (a winged couple statue, a birdcage, swans), a gold heart shatters into fragments, and a heart customiser closes it."
mode: experience
traits: ["white marble and mist world", "drifting red petals", "gold heart in an ornate mirror", "one line of story per scene", "shattering gold heart", "heart customiser"]
palette: ["#ECEDEA", "#D5CFCE", "#C2B3B8"]
type: ["fontspring-light"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

A single white world with red petals as the constant, and the camera gliding between story props, makes a legend feel like a dream walk.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- One continuous world with a recurring particle (petals) as the thread

## What to leave

- Story text very small

## Signature move

Red petals drifting through a white world of marble columns.

## Motion

Intro: blush with a drawn heart (~3 s), the mirror heart zooms through the 'O'. Wheel: the camera glides over water past columns; each scene's prop rises with a line of text; petals drift constantly; the gold heart shatters into flying pieces; the customiser appears.

Measured (`motion/probe.json`): GSAP 3.12.7; ScrollSmoother; entry gate: BEGIN JOURNEY. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the continuous world grammar: an interactive story of Saint Valentine: a drawn heart loader on blush, 'The Story' with a gold heart in an ornate mirror replacing the O, then a white misty world of marble columns over water where red petals drift, scenes of the story appear (a winged couple statue, a birdcage, swans), a gold heart shatters into fragments, and a heart customiser closes it. Type: fontspring-light.
Ground and ink from the measured palette (#ECEDEA, #D5CFCE, #C2B3B8). Motion carries the page through
red petals drifting through a white world of marble columns. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D world

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D world

## Reference lock

Primary reference/direction: Noomo Valentime - immersive story about love — An interactive story of Saint Valentine: a drawn heart loader on blush, 'The Story' with a gold heart in an ornate mirror replacing the O, then a white misty world of marble columns over water where red petals drift, scenes of the story appear (a winged couple statue, a birdcage, swans), a gold heart shatters into fragments, and a heart customiser closes it.
Preserve (3-5 traits): white marble and mist world; drifting red petals; gold heart in an ornate mirror; one line of story per scene; shattering gold heart.
Borrow only (1-2): One continuous world with a recurring particle (petals) as the thread
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D world
Reject: Story text very small
Token commitments: palette #ECEDEA, #D5CFCE, #C2B3B8; type fontspring-light; engine GSAP + Lenis linked (never vendored).
