---
title: "Glyphic Biotechnologies - protein sequencing"
url: https://www.glyphic.bio/
source_url: https://www.glyphic.bio/
captured: 2026-10-03
origin: raw-url
extract: none
category: product-focused
category2: "institutional"
family: pale-bead-molecule-science
dna: "Biotech x pale grey-green, molecules modelled as soft beads and glass rings, Swiss rules"
register: modern clean
grammar: chaptered editorial
lane: "A protein-sequencing startup: a line loader, a sticky three-step method (sample preparation, molecular expansion, amino acid sequencing) where a bead chain coils, threads a glass ring and expands, a long statement underlined in links, a field of drifting bead chains, amino-acid letters falling in columns, 'Glyphic Biotechnologies' with a bead ring through the wordmark, patents in a ruled table, careers cards and a contact form."
mode: persuade
traits: ["soft bead molecules", "glass ring", "sticky three-step method", "falling letter columns", "Swiss ruled tables", "pale grey-green"]
palette: ["#FFFFFF", "#DFE4E6", "#949896"]
type: ["fontPrimary"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Turning an invisible process into soft physical beads makes the science tangible and calm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: Obys Agency).

## What to borrow (principle)

- Model the invisible process as one soft physical object that changes per step

## What to leave

- Very small labels

## Signature move

A chain of pale green beads threading through a glass ring.

## Motion

Intro: line loader (~2 s). Wheel (Lenis): the WebGL bead chain morphs per step while the step list highlights; a bead field drifts with depth of field; letters fall; the ring rotates through the wordmark.

Measured (`motion/probe.json`): GSAP 3.12.5; Lenis; WebGL canvas x1 (three.js); 1 video; split text; smoothed scroll (median 153 px still travelling after input stops). Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a protein-sequencing startup: a line loader, a sticky three-step method (sample preparation, molecular expansion, amino acid sequencing) where a bead chain coils, threads a glass ring and expands, a long statement underlined in links, a field of drifting bead chains, amino-acid letters falling in columns, 'Glyphic Biotechnologies' with a bead ring through the wordmark, patents in a ruled table, careers cards and a contact form. Type: fontPrimary.
Ground and ink from the measured palette (#FFFFFF, #DFE4E6, #949896). Motion carries the page through
a chain of pale green beads threading through a glass ring. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — WebGL molecular renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: WebGL molecular renders

## Reference lock

Primary reference/direction: Glyphic Biotechnologies - protein sequencing — A protein-sequencing startup: a line loader, a sticky three-step method (sample preparation, molecular expansion, amino acid sequencing) where a bead chain coils, threads a glass ring and expands, a long statement underlined in links, a field of drifting bead chains, amino-acid letters falling in columns, 'Glyphic Biotechnologies' with a bead ring through the wordmark, patents in a ruled table, careers cards and a contact form.
Preserve (3-5 traits): soft bead molecules; glass ring; sticky three-step method; falling letter columns; Swiss ruled tables.
Borrow only (1-2): Model the invisible process as one soft physical object that changes per step
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: WebGL molecular renders
Reject: Very small labels
Token commitments: palette #FFFFFF, #DFE4E6, #949896; type fontPrimary; engine GSAP + Lenis linked (never vendored).
