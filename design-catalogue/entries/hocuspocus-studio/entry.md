---
title: "Hocus Pocus Studio - VFX and 3D animation"
url: https://hocuspocus-studio.fr/en/
source_url: https://hocuspocus-studio.fr/en/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: vfx-studio-creature-reel
dna: "VFX studio x a creature close-up and a horizontal service word strip"
register: cinematic dark
grammar: chaptered editorial
lane: "A VFX studio: a dot that becomes the scribble logo, a copper 3D scribble on black, a full-bleed alien creature close-up zooming into its skin, 'HOCUS POCUS STUDIO' in gold over the texture, a white intro paragraph where gold words colour in, a horizontal strip of services ('3D . VFX . Motion design . Post Production') with frames sliding behind, 'Our creations' as full-bleed project films (Nike Air Max DN, a motorbike, a UFO showcase) with underlined titles, client logos and contact."
mode: persuade
traits: ["creature close-up zoom", "gold display type", "words colouring in", "horizontal service word strip", "full-bleed project films", "3D scribble logo"]
palette: ["#000000", "#FFFFFF", "#A6968B", "#E2DBCA", "#5E413B", "#202020"]
type: ["Agrandir Wide", "Neue Montreal"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Opening on a creature close-up proves the VFX quality instantly; the service strip and full-bleed films carry the rest.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Open on an extreme close-up of your best render

## What to leave

- Small labels

## Signature move

An alien creature close-up zooming into skin under 'HOCUS POCUS'.

## Motion

Intro: a dot draws the scribble logo (~2 s), the copper scribble rotates. Wheel (Lenis, SplitText 205): the creature zooms; the title reveals; words colour gold one by one; the service strip slides sideways with frames; project films crossfade with titles drawing their underlines.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; split text; smoothed scroll (median 189 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the chaptered editorial grammar: a VFX studio: a dot that becomes the scribble logo, a copper 3D scribble on black, a full-bleed alien creature close-up zooming into its skin, 'HOCUS POCUS STUDIO' in gold over the texture, a white intro paragraph where gold words colour in, a horizontal strip of services ('3D . VFX . Motion design . Post Production') with frames sliding behind, 'Our creations' as full-bleed project films (Nike Air Max DN, a motorbike, a UFO showcase) with underlined titles, client logos and contact. Type: Agrandir Wide, Neue Montreal.
Ground and ink from the measured palette (#000000, #FFFFFF, #A6968B). Motion carries the page through
an alien creature close-up zooming into skin under 'HOCUS POCUS'. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — VFX stills and films

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: VFX stills and films

## Reference lock

Primary reference/direction: Hocus Pocus Studio - VFX and 3D animation — A VFX studio: a dot that becomes the scribble logo, a copper 3D scribble on black, a full-bleed alien creature close-up zooming into its skin, 'HOCUS POCUS STUDIO' in gold over the texture, a white intro paragraph where gold words colour in, a horizontal strip of services ('3D . VFX . Motion design . Post Production') with frames sliding behind, 'Our creations' as full-bleed project films (Nike Air Max DN, a motorbike, a UFO showcase) with underlined titles, client logos and contact.
Preserve (3-5 traits): creature close-up zoom; gold display type; words colouring in; horizontal service word strip; full-bleed project films.
Borrow only (1-2): Open on an extreme close-up of your best render
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: VFX stills and films
Reject: Small labels
Token commitments: palette #000000, #FFFFFF, #A6968B, #E2DBCA, #5E413B, #202020; type Agrandir Wide, Neue Montreal; engine GSAP + Lenis linked (never vendored).
