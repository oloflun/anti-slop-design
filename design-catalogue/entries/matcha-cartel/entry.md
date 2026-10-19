---
title: "Matcha Cartel"
url: https://matcha-cartel.com/index
source_url: https://matcha-cartel.com/index
captured: 2026-10-03
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: matcha-dossier-archive
dna: "Matcha culture dossier x pale grey grid of specimen tiles, acid green, a leaf travelling through the production chain, and an 'obsession archive' of photos"
register: other
grammar: chaptered editorial
lane: "A matcha culture site: a pale grey grid with numbered cells filling with specimen photos, 'MatchaCartel' in condensed grey, an origin log with draggable acid-green dossier cards, 'Matcha Production Chain.' where one leaf is steamed, dried, ground into powder and sealed into a tin as you scroll, a green powder cloud for 'Effects of Matcha', 'Hyperfixation.' with drifting photos, an 'Obsession Archives' pinned panel of found photos with coordinates, preparation tools and a flashlight-lit dark step sequence."
mode: experience
traits: ["numbered specimen grid", "leaf transformed through steps", "acid green powder cloud", "dossier cards to drag", "flashlight reveal in the dark"]
palette: ["#FFFFFF", "#DAE2E9", "#48611C", "#94A881"]
type: ["Fragment Mono", "Hubot Sans Condensed Bold", "Hubot Sans Condensed Bold Placeholder"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Following one leaf through every production step makes the supply chain a single object's journey.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Agnes Andreyana, Wildy Riftian).

## What to borrow (principle)

- Follow one ingredient through every step of its making

## What to leave

- Tiny mono labels

## Signature move

One leaf turning into powder and then a sealed tin across a white page.

## Motion

Intro: grid cells fill (~2 s). Wheel (Lenis): the leaf object morphs per step; a powder cloud expands; photos drift; the archive pins; a cursor flashlight reveals steps.

Measured (`motion/probe.json`): Lenis; 9 video; split text; smoothed scroll (median 100 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A other page in the chaptered editorial grammar: a matcha culture site: a pale grey grid with numbered cells filling with specimen photos, 'MatchaCartel' in condensed grey, an origin log with draggable acid-green dossier cards, 'Matcha Production Chain.' where one leaf is steamed, dried, ground into powder and sealed into a tin as you scroll, a green powder cloud for 'Effects of Matcha', 'Hyperfixation.' with drifting photos, an 'Obsession Archives' pinned panel of found photos with coordinates, preparation tools and a flashlight-lit dark step sequence. Type: Fragment Mono, Hubot Sans Condensed Bold, Hubot Sans Condensed Bold Placeholder.
Ground and ink from the measured palette (#FFFFFF, #DAE2E9, #48611C). Motion carries the page through
one leaf turning into powder and then a sealed tin across a white page. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — product photography, found photography

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: product photography, found photography

## Reference lock

Primary reference/direction: Matcha Cartel — A matcha culture site: a pale grey grid with numbered cells filling with specimen photos, 'MatchaCartel' in condensed grey, an origin log with draggable acid-green dossier cards, 'Matcha Production Chain.' where one leaf is steamed, dried, ground into powder and sealed into a tin as you scroll, a green powder cloud for 'Effects of Matcha', 'Hyperfixation.' with drifting photos, an 'Obsession Archives' pinned panel of found photos with coordinates, preparation tools and a flashlight-lit dark step sequence.
Preserve (3-5 traits): numbered specimen grid; leaf transformed through steps; acid green powder cloud; dossier cards to drag; flashlight reveal in the dark.
Borrow only (1-2): Follow one ingredient through every step of its making
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: product photography, found photography
Reject: Tiny mono labels
Token commitments: palette #FFFFFF, #DAE2E9, #48611C, #94A881; type Fragment Mono, Hubot Sans Condensed Bold, Hubot Sans Condensed Bold Placeholder; engine GSAP + Lenis linked (never vendored).
