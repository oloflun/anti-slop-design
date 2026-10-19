---
title: "The GSAP Field - a motion playground by BYQ"
url: https://the-gsap-field.webflow.io/
source_url: https://the-gsap-field.webflow.io/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: scout-film-scribble-showcase
dna: "Motion showcase x scouts in a field and yellow hand-drawn scribbles"
register: warm photographic
grammar: chaptered editorial
lane: "A motion studio showcase: a yellow serif 'The GSAP Field' on black that becomes a film of kids in scout uniforms in a meadow, then cream sections where words ('More than motion', 'A field of expression', 'Built on GSAP', 'Rooted in real joy') get yellow scribbles drawn around them while small photos float, full-bleed character titles ('The Quiet One', 'The Watcher', 'The Sellers'), stats and a ring of photos for 'We'll see the smoke'."
mode: persuade
traits: ["yellow hand-drawn scribbles on words", "scout film photography", "serif yellow titles over film", "floating small photos", "character chapter titles", "photo ring finale"]
palette: ["#EAE7DA", "#4E452A", "#312C18", "#705D3C", "#827556", "#D2C48E"]
type: ["Raveo Display", "Geist Mono Variable", "LT Superior Serif", "Instrument Sans"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The scribbles are drawn live on each statement (DrawSVG in action) and the scout characters make a tech demo feel like a story.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Draw a scribble around the key word as it arrives
- Name chapters after characters

## What to leave

- Small stats labels

## Signature move

Yellow scribbles drawing themselves around words beside floating scout photos.

## Motion

Intro: black, the serif title fills yellow (~2 s), the film fades in. Wheel (15 triggers): words arrive with a scribble drawing around them; small photos drift; character titles slide over full-bleed film; stats count; photos arrange into a rotating ring.

Measured (`motion/probe.json`): GSAP 3.15.0; 15 ScrollTriggers; 5 video; split text. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a motion studio showcase: a yellow serif 'The GSAP Field' on black that becomes a film of kids in scout uniforms in a meadow, then cream sections where words ('More than motion', 'A field of expression', 'Built on GSAP', 'Rooted in real joy') get yellow scribbles drawn around them while small photos float, full-bleed character titles ('The Quiet One', 'The Watcher', 'The Sellers'), stats and a ring of photos for 'We'll see the smoke'. Type: Raveo Display, Geist Mono Variable, LT Superior Serif, Instrument Sans.
Ground and ink from the measured palette (#EAE7DA, #4E452A, #312C18). Motion carries the page through
yellow scribbles drawing themselves around words beside floating scout photos. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film photography, hand-drawn scribbles

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film photography, hand-drawn scribbles

## Reference lock

Primary reference/direction: The GSAP Field - a motion playground by BYQ — A motion studio showcase: a yellow serif 'The GSAP Field' on black that becomes a film of kids in scout uniforms in a meadow, then cream sections where words ('More than motion', 'A field of expression', 'Built on GSAP', 'Rooted in real joy') get yellow scribbles drawn around them while small photos float, full-bleed character titles ('The Quiet One', 'The Watcher', 'The Sellers'), stats and a ring of photos for 'We'll see the smoke'.
Preserve (3-5 traits): yellow hand-drawn scribbles on words; scout film photography; serif yellow titles over film; floating small photos; character chapter titles.
Borrow only (1-2): Draw a scribble around the key word as it arrives; Name chapters after characters
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film photography, hand-drawn scribbles
Reject: Small stats labels
Token commitments: palette #EAE7DA, #4E452A, #312C18, #705D3C, #827556, #D2C48E; type Raveo Display, Geist Mono Variable, LT Superior Serif, Instrument Sans; engine GSAP + Lenis linked (never vendored).
