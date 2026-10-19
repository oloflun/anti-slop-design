---
title: "Der Baukasten"
url: https://www.der-baukasten.com/
source_url: https://www.der-baukasten.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: playful
category2: "editorial"
family: 3d-folk-toy-kit
dna: "Ukrainian folk toy kit x coloured 3D pieces that assemble into animals"
register: illustrated dark
grammar: split stage
lane: "A toy-kit concept: coloured 3D shapes assemble on black into a small animal, then scatter and the 'Der Baukasten' wordmark lands, and each animal (pivnyk the rooster, buzko the stork, konyk the horse) is built from the same pieces at left while a full-colour card (blue, red, yellow) at right gives its name, meaning and a download button."
mode: experience
traits: ["coloured 3D pieces assembling", "one kit, many animals", "full-colour info card per animal", "Cyrillic display names", "black stage", "download 3D model button"]
palette: ["#000000", "#047FFC", "#7A4441", "#063954", "#A0C3CE"]
type: ["futura-pt"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

One set of pieces reassembles into every animal, so the scroll literally demonstrates the product: a construction kit.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Tubik Studio).

## What to borrow (principle)

- Reassemble the same pieces into a new form per section

## What to leave

- Pieces fly apart a long time between animals

## Signature move

The same coloured 3D pieces reassembling into a rooster, a stork and a horse.

## Motion

Intro: black, pieces snap together into a small animal and scatter (~3 s), the wordmark rises. Wheel (Lenis ~110-150 px glide): pieces fly apart and rebuild the next animal while the side card swaps colour and name.

Measured (`motion/probe.json`): GSAP 3.13.0; Lenis; WebGL canvas x1 (three.js); smoothed scroll (median 162 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A illustrated dark page in the split stage grammar: a toy-kit concept: coloured 3D shapes assemble on black into a small animal, then scatter and the 'Der Baukasten' wordmark lands, and each animal (pivnyk the rooster, buzko the stork, konyk the horse) is built from the same pieces at left while a full-colour card (blue, red, yellow) at right gives its name, meaning and a download button. Type: futura-pt.
Ground and ink from the measured palette (#000000, #047FFC, #7A4441). Motion carries the page through
the same coloured 3D pieces reassembling into a rooster, a stork and a horse. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — 3D construction pieces

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: 3D construction pieces

## Reference lock

Primary reference/direction: Der Baukasten — A toy-kit concept: coloured 3D shapes assemble on black into a small animal, then scatter and the 'Der Baukasten' wordmark lands, and each animal (pivnyk the rooster, buzko the stork, konyk the horse) is built from the same pieces at left while a full-colour card (blue, red, yellow) at right gives its name, meaning and a download button.
Preserve (3-5 traits): coloured 3D pieces assembling; one kit, many animals; full-colour info card per animal; Cyrillic display names; black stage.
Borrow only (1-2): Reassemble the same pieces into a new form per section
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: 3D construction pieces
Reject: Pieces fly apart a long time between animals
Token commitments: palette #000000, #047FFC, #7A4441, #063954, #A0C3CE; type futura-pt; engine GSAP + Lenis linked (never vendored).
