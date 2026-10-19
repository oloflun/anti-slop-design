---
title: "inFaces - childhood photos edition"
url: https://infaces-digitalbutlers.webflow.io/
source_url: https://infaces-digitalbutlers.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: editorial
category2: "playful"
family: childhood-photo-archive-editorial
dna: "Team photo project x a wordmark that sharpens and highlighted serif statement"
register: editorial print
grammar: chaptered editorial
lane: "A team storytelling project on cream: circle and line construction drawings, a blurred 'infaces' wordmark that sharpens, 'Together with our heroes we remember the happy moments of our lives...' in condensed serif caps with lime highlight boxes, then team childhood photos drifting up with names, and a story card opening over a blurred background."
mode: read
traits: ["construction-line loader", "blurred wordmark sharpening", "lime highlight boxes on words", "childhood photos drifting", "story card modal", "cream ground"]
palette: ["#F5F3E4", "#3D443E", "#8EA170", "#CDC2B7"]
type: ["ZT Bros Oskon 90s", "PP Agrandir", "Instrument Sans Variable"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

Childhood photos of the team make an internal culture project warm and human; the highlighter boxes give the statement rhythm.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Highlight words with marker boxes as the statement reveals

## What to leave

- Modal ends the capture

## Signature move

Childhood photos of the team drifting up under a highlighted statement.

## Motion

Intro: construction lines draw (~2 s), the wordmark sharpens from blur. Wheel (Lenis): the statement reveals with lime boxes sweeping behind words; photos rise at different speeds; clicking opens a story card.

Measured (`motion/probe.json`): GSAP 3.12.7; Lenis; split text; smoothed scroll (median 127 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A editorial print page in the chaptered editorial grammar: a team storytelling project on cream: circle and line construction drawings, a blurred 'infaces' wordmark that sharpens, 'Together with our heroes we remember the happy moments of our lives...' in condensed serif caps with lime highlight boxes, then team childhood photos drifting up with names, and a story card opening over a blurred background. Type: ZT Bros Oskon 90s, PP Agrandir, Instrument Sans Variable.
Ground and ink from the measured palette (#F5F3E4, #3D443E, #8EA170). Motion carries the page through
childhood photos of the team drifting up under a highlighted statement. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — archival childhood photographs

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: archival childhood photographs

## Reference lock

Primary reference/direction: inFaces - childhood photos edition — A team storytelling project on cream: circle and line construction drawings, a blurred 'infaces' wordmark that sharpens, 'Together with our heroes we remember the happy moments of our lives...' in condensed serif caps with lime highlight boxes, then team childhood photos drifting up with names, and a story card opening over a blurred background.
Preserve (3-5 traits): construction-line loader; blurred wordmark sharpening; lime highlight boxes on words; childhood photos drifting; story card modal.
Borrow only (1-2): Highlight words with marker boxes as the statement reveals
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: archival childhood photographs
Reject: Modal ends the capture
Token commitments: palette #F5F3E4, #3D443E, #8EA170, #CDC2B7; type ZT Bros Oskon 90s, PP Agrandir, Instrument Sans Variable; engine GSAP + Lenis linked (never vendored).
