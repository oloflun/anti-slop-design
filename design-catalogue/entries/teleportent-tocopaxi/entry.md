---
title: "Teleportent - Short Film"
url: https://teleportent.tocopaxi.com/
source_url: https://teleportent.tocopaxi.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "consumer-brand"
family: short-film-tent-story
dna: "Short film site x a yellow tent as the portal between room and mountain"
register: warm photographic
grammar: chaptered editorial
lane: "A short film's site: a yellow ground with a tent icon, a still of the protagonist in a tent, the condensed yellow 'TELEPORTENT' title with laurels, a 3D tent object, the synopsis over the tent doorway opening onto a mountain, 'That's when he teleported', story beats over film stills with yellow panels, 'True achievement changes him' on a tablet still, 'The best view awaits' and a storyboard grid."
mode: read
traits: ["yellow tent as portal", "condensed yellow display title", "synopsis over film stills", "yellow panels sliding in", "3D tent object", "storyboard grid finale"]
palette: ["#54270F", "#C5CFD6", "#79797B", "#29160E", "#904B1F", "#B98C57"]
type: ["Figtree", "Anton", "Crimson Pro"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The tent is the signature object: it is the loader, the 3D object and the doorway that opens onto the mountain, so the site tells the film's premise physically.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Use the story's key object as loader, 3D object and doorway

## What to leave

- Small body text on stills

## Signature move

A yellow tent doorway opening from a bedroom onto a mountain summit.

## Motion

Intro: yellow with the tent icon (~2 s). Wheel (Lenis ~140 px glide, 3 pins): the still slides up; the title spaces in; a word scrambles; the 3D tent turns; the camera passes through the tent door onto the mountain; text splits in; yellow panels slide over stills; the storyboard grid scrolls.

Measured (`motion/probe.json`): GSAP 3.13.0; 3 pinned sections; Lenis; WebGL canvas x1 (three.js); 4 video; split text; smoothed scroll (median 156 px still travelling after input stops); entry gate: Mute audio. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a short film's site: a yellow ground with a tent icon, a still of the protagonist in a tent, the condensed yellow 'TELEPORTENT' title with laurels, a 3D tent object, the synopsis over the tent doorway opening onto a mountain, 'That's when he teleported', story beats over film stills with yellow panels, 'True achievement changes him' on a tablet still, 'The best view awaits' and a storyboard grid. Type: Figtree, Anton, Crimson Pro.
Ground and ink from the measured palette (#54270F, #C5CFD6, #79797B). Motion carries the page through
a yellow tent doorway opening from a bedroom onto a mountain summit. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film stills, 3D tent

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film stills, 3D tent

## Reference lock

Primary reference/direction: Teleportent - Short Film — A short film's site: a yellow ground with a tent icon, a still of the protagonist in a tent, the condensed yellow 'TELEPORTENT' title with laurels, a 3D tent object, the synopsis over the tent doorway opening onto a mountain, 'That's when he teleported', story beats over film stills with yellow panels, 'True achievement changes him' on a tablet still, 'The best view awaits' and a storyboard grid.
Preserve (3-5 traits): yellow tent as portal; condensed yellow display title; synopsis over film stills; yellow panels sliding in; 3D tent object.
Borrow only (1-2): Use the story's key object as loader, 3D object and doorway
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film stills, 3D tent
Reject: Small body text on stills
Token commitments: palette #54270F, #C5CFD6, #79797B, #29160E, #904B1F, #B98C57; type Figtree, Anton, Crimson Pro; engine GSAP + Lenis linked (never vendored).
