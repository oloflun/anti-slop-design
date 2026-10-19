---
title: "Indigo — 5 tales of being"
url: https://indigo-laboratory.it/
source_url: https://indigo-laboratory.it/
captured: 2026-10-02
origin: raw-url
extract: none
category: luxury-craft
category2: "editorial"
family: sound-tale-jewellery-house
dna: "Contemporary jewellery house x five sound-titled tales"
register: editorial print
grammar: chaptered editorial
lane: "A jewellery house told in five tales (Rhythm, Pulse, Whisper, Resonance, Sub-noise): huge distorted display words set over portraits, rings photographed on skin, and a collection strip, with a tale index pinned along the bottom."
mode: experience
traits: ["five chapter words in a distorted display face", "portrait photography with silver rings", "tale index bar along the bottom", "request-info overlays", "black, white and violet", "43,000 px long page"]
palette: ["#000000", "#FFFFFF", "#797574", "#D2D9DD", "#A5ABB0", "#514842"]
type: ["Hanken Grotesk", "Palette Mosaic", "IBM Plex Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Each collection is named after a kind of sound, and each name is set in a distorted, mosaic-like display face that looks like a sound wave rendered as type. The jewellery is always on bodies, close up, so the scale stays human between the loud words.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: FPTP Studio, Marea Studio).

## What to borrow (principle)

- Name chapters with one word each and let the word's type be the chapter's image
- Keep the product on skin, close up, between the loud typographic beats
- A pinned chapter index along the bottom for a very long page

## What to leave

- Very long page (43,000 px)
- Cookie notice and request-info overlays crowd the frames

## Signature move

Huge distorted chapter words (RHYTHM, WHISPER) set over portraits.

## Motion

Intro: violet flash, 'INDIGO' and the five tale names stacked on black, gate 'ENTER THE EXPERIENCE' (~2.5 s). Scroll (Lenis, SplitText): 'INVISIBLE ECHO' manifesto; 'RHYTHM' distorted word lands over a portrait as a ring drifts; split layouts of portraits; 'SELENE RING' over a mineral close-up; 'THE SOUND WITHIN' with a waveform; collection strip; 'WHISPER' word.

Measured (`motion/probe.json`): GSAP 3.14.2; Lenis; WebGL canvas x1; 1 video; split text; smoothed scroll (median 66 px still travelling after input stops); entry gate: ENTER THE EXPERIENCE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a jewellery house told in five tales (Rhythm, Pulse, Whisper, Resonance, Sub-noise): huge distorted display words set over portraits, rings photographed on skin, and a collection strip, with a tale index pinned along the bottom. Type: Hanken Grotesk, Palette Mosaic, IBM Plex Mono.
Ground and ink from the measured palette (#000000, #FFFFFF, #797574). Motion carries the page through
huge distorted chapter words (RHYTHM, WHISPER) set over portraits. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — close-up portrait photography with silver jewellery, cool skin tones, mineral textures

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: close-up portrait photography with silver jewellery, cool skin tones, mineral textures

## Reference lock

Primary reference/direction: Indigo — 5 tales of being — A jewellery house told in five tales (Rhythm, Pulse, Whisper, Resonance, Sub-noise): huge distorted display words set over portraits, rings photographed on skin, and a collection strip, with a tale index pinned along the bottom.
Preserve (3-5 traits): five chapter words in a distorted display face; portrait photography with silver rings; tale index bar along the bottom; request-info overlays; black, white and violet.
Borrow only (1-2): Name chapters with one word each and let the word's type be the chapter's image; Keep the product on skin, close up, between the loud typographic beats
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: close-up portrait photography with silver jewellery, cool skin tones, mineral textures
Reject: Very long page (43,000 px); Cookie notice and request-info overlays crowd the frames
Token commitments: palette #000000, #FFFFFF, #797574, #D2D9DD, #A5ABB0, #514842; type Hanken Grotesk, Palette Mosaic, IBM Plex Mono; engine GSAP + Lenis linked (never vendored).
