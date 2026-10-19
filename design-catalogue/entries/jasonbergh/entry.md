---
title: "Jason Bergh - Director, Cinematographer, Producer"
url: https://www.jasonbergh.com/
source_url: https://www.jasonbergh.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "editorial"
family: director-reel-title-split
dna: "Film director x italic serif titles split around a centre video"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A director's reel: black loader with clips floating at the edges and a counter, then each project fills the screen as a muted video with its title split in italic serif left and right of a small centre player (Stand Up / Seattle Reign FC, Noted / Alicia Keys, Halftime / Jennifer Lopez) while a thumbnail strip runs along the top and bottom."
mode: experience
traits: ["italic serif title split either side of a centre frame", "full-bleed muted video per project", "floating clip loader with counter", "thumbnail strips top and bottom", "mono metadata", "Observer-driven project stepping"]
palette: ["#050505", "#202738", "#55575E"]
type: ["Editorialnew", "Monumentgrotesk", "MonumentgroteskMono", "Abcsimonmono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

Splitting the title around the player turns every project into a film poster: client on one side, film on the other, footage behind; the wheel steps through them like cuts in a reel.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Split a title either side of a centre video
- Step projects with the wheel like cuts in an edit

## What to leave

- Virtual scroll hides the URL structure
- Overlapping titles during the change

## Signature move

Italic serif titles split either side of a small centre frame over full-bleed footage.

## Motion

Intro: black, clips drift in from the edges, 'Intimate, Raw Human Storytelling' types, a counter runs to 99, then 'Jason' and 'Bergh' slide apart to reveal the first film (~3 s). Wheel (Observer, no native scroll): each tick cross-fades the background video and morphs the split titles to the next project; the centre player scales with it. Barba page transitions.

Measured (`motion/probe.json`): GSAP 3.15.0; Lenis; Locomotive; Barba page transitions; 134 video; split text; virtual scroll (window never scrolls; transform/WebGL scroller); entry gate: CLOSE, MUTE. Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a director's reel: black loader with clips floating at the edges and a counter, then each project fills the screen as a muted video with its title split in italic serif left and right of a small centre player (Stand Up / Seattle Reign FC, Noted / Alicia Keys, Halftime / Jennifer Lopez) while a thumbnail strip runs along the top and bottom. Type: Editorialnew, Monumentgrotesk, MonumentgroteskMono, Abcsimonmono.
Ground and ink from the measured palette (#050505, #202738, #55575E). Motion carries the page through
italic serif titles split either side of a small centre frame over full-bleed footage. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — music video and documentary stills

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: music video and documentary stills

## Reference lock

Primary reference/direction: Jason Bergh - Director, Cinematographer, Producer — A director's reel: black loader with clips floating at the edges and a counter, then each project fills the screen as a muted video with its title split in italic serif left and right of a small centre player (Stand Up / Seattle Reign FC, Noted / Alicia Keys, Halftime / Jennifer Lopez) while a thumbnail strip runs along the top and bottom.
Preserve (3-5 traits): italic serif title split either side of a centre frame; full-bleed muted video per project; floating clip loader with counter; thumbnail strips top and bottom; mono metadata.
Borrow only (1-2): Split a title either side of a centre video; Step projects with the wheel like cuts in an edit
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: music video and documentary stills
Reject: Virtual scroll hides the URL structure; Overlapping titles during the change
Token commitments: palette #050505, #202738, #55575E; type Editorialnew, Monumentgrotesk, MonumentgroteskMono, Abcsimonmono; engine GSAP + Lenis linked (never vendored).
