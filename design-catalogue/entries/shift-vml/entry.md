---
title: "Shift by VML - experimental lab"
url: https://shift.vml.dev/
source_url: https://shift.vml.dev/
captured: 2026-10-03
origin: raw-url
extract: none
category: portfolio
category2: ""
family: halftone-silhouette-lab
dna: "Agency lab x a halftone silhouette and floating project thumbnails around words"
register: modern clean
grammar: chaptered editorial
lane: "An agency lab: a peach screen with a percent counter over a halftone dot field, 'At VML, there's a place where creativity and technology become one', 'Where we experiment' with small project thumbnails scattered around, a halftone profile silhouette with a VR headset growing in yellow, 'We amplify creativity', 'Our machines are our accomplices' with a row of capability words (Artificial Intelligence, WebGL, Casual Games) where thumbnails float and the active word lights, a full-bleed pink and orange blurred portrait 'We create emotions' and a closing line."
mode: experience
traits: ["halftone dot field", "profile silhouette with headset", "scattered floating thumbnails", "capability word row lighting up", "pastel then hot pink", "thin grotesk"]
palette: ["#E5DEE5", "#FEC7B3", "#D9ABA2"]
type: ["Snowflake"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Floating thumbnails around a single line and a lit word row make a capability list feel like a live lab.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
lenis showcase (credits: VML).

## What to borrow (principle)

- Light one capability word at a time while its thumbnails float around

## What to leave

- Very light text on pastel

## Signature move

A halftone silhouette with a VR headset in yellow.

## Motion

Intro: peach counter 25 to 100 % over halftone (~3 s). Wheel: text fades between grounds; thumbnails drift in from edges; the silhouette grows and fills yellow; words slide in a row as the active one colours; the blurred portrait scales; the ground clears to pale blue.

Measured (`motion/probe.json`): GSAP 3.14.2; 1 pinned sections; Lenis; WebGL canvas x7; split text; smoothed scroll (median 158 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: an agency lab: a peach screen with a percent counter over a halftone dot field, 'At VML, there's a place where creativity and technology become one', 'Where we experiment' with small project thumbnails scattered around, a halftone profile silhouette with a VR headset growing in yellow, 'We amplify creativity', 'Our machines are our accomplices' with a row of capability words (Artificial Intelligence, WebGL, Casual Games) where thumbnails float and the active word lights, a full-bleed pink and orange blurred portrait 'We create emotions' and a closing line. Type: Snowflake.
Ground and ink from the measured palette (#E5DEE5, #FEC7B3, #D9ABA2). Motion carries the page through
a halftone silhouette with a VR headset in yellow. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — project thumbnails, portrait

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: project thumbnails, portrait

## Reference lock

Primary reference/direction: Shift by VML - experimental lab — An agency lab: a peach screen with a percent counter over a halftone dot field, 'At VML, there's a place where creativity and technology become one', 'Where we experiment' with small project thumbnails scattered around, a halftone profile silhouette with a VR headset growing in yellow, 'We amplify creativity', 'Our machines are our accomplices' with a row of capability words (Artificial Intelligence, WebGL, Casual Games) where thumbnails float and the active word lights, a full-bleed pink and orange blurred portrait 'We create emotions' and a closing line.
Preserve (3-5 traits): halftone dot field; profile silhouette with headset; scattered floating thumbnails; capability word row lighting up; pastel then hot pink.
Borrow only (1-2): Light one capability word at a time while its thumbnails float around
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: project thumbnails, portrait
Reject: Very light text on pastel
Token commitments: palette #E5DEE5, #FEC7B3, #D9ABA2; type Snowflake; engine GSAP + Lenis linked (never vendored).
