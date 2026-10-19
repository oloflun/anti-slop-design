---
title: "Dominik Kostolnik"
url: https://www.dkton.at/
source_url: https://www.dkton.at/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: "playful"
family: amber-pill-sound-folio
dna: "Film sound designer x amber equaliser pills"
register: cinematic dark
grammar: rhythmic cutlist
lane: "A black sound-design folio where amber pill shapes behave like an equaliser: they line up under the name, rise as bars behind 'SHOWREEL', and open as vertical slats over film stills, between heavy condensed German headlines."
mode: persuade
traits: ["amber/orange pill shapes as the one graphic", "heavy condensed italic grotesque", "colour-band highlight behind words (ORIGINALTON/SOUNDDESIGN/MISCHUNG)", "vertical slat mask over video", "inline portrait in a statement line", "project list with yellow active row"]
palette: ["#000000", "#46320C", "#FEB901", "#B6840A"]
type: ["Geistmono", "Gt Walsheim Condensed"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

A single shape (the rounded pill) does every job a sound brand needs to show without sound: a row of pills is a level meter under the name, the same pills grow into bars behind 'SHOWREEL', and then become vertical slats that open over the reel like blinds. Black ground, one warm gradient, condensed italic caps; the restriction makes the one shape carry the identity.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase.

## What to borrow (principle)

- Give the brand one shape and reuse it as meter, bars and mask so every section is recognisably the same hand
- Open a video behind vertical slats that widen on scroll instead of a plain fade
- Highlight a list of three disciplines with full-width colour bands that wipe in behind each word

## What to leave

- ENTER THE EXPERIENCE gate before content
- Statement lines with inline photos get crowded at small sizes

## Signature move

Amber pills that move from equaliser row to rising bars to slat-blinds opening over the showreel.

## Motion

Gate: 'Enter the experience'. Intro: name lands in condensed italic with soft pills drifting behind (~1.3 s), then pills line up as a bright row above 'AUS GESCHICHTEN WERDEN KLANGWELTEN'. Scroll (Lenis, ~100 px glide, 14 ScrollTriggers): statement reveals line by line with greyed future lines; ORIGINALTON / SOUNDDESIGN / MISCHUNG get colour bands wiping in behind; 'SHOWREEL' with pills rising as bars, then the bars become vertical slats that open to the reel; projects as full-bleed stills with condensed titles; list rows highlight yellow on the active item; FAQ accordion; photo collage close. ScrambleText on small labels.

Measured (`motion/probe.json`): GSAP 3.15.0; 14 ScrollTriggers; Lenis; 18 video; smoothed scroll (median 126 px still travelling after input stops); entry gate: Enter the experience. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A cinematic dark page in the rhythmic cutlist grammar: a black sound-design folio where amber pill shapes behave like an equaliser: they line up under the name, rise as bars behind 'SHOWREEL', and open as vertical slats over film stills, between heavy condensed German headlines. Type: Geistmono, Gt Walsheim Condensed.
Ground and ink from the measured palette (#000000, #46320C, #FEB901). Motion carries the page through
amber pills that move from equaliser row to rising bars to slat-blinds opening over the showreel. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — film and on-set stills, warm practical light, rich blacks

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: film and on-set stills, warm practical light, rich blacks

## Reference lock

Primary reference/direction: Dominik Kostolnik — A black sound-design folio where amber pill shapes behave like an equaliser: they line up under the name, rise as bars behind 'SHOWREEL', and open as vertical slats over film stills, between heavy condensed German headlines.
Preserve (3-5 traits): amber/orange pill shapes as the one graphic; heavy condensed italic grotesque; colour-band highlight behind words (ORIGINALTON/SOUNDDESIGN/MISCHUNG); vertical slat mask over video; inline portrait in a statement line.
Borrow only (1-2): Give the brand one shape and reuse it as meter, bars and mask so every section is recognisably the same hand; Open a video behind vertical slats that widen on scroll instead of a plain fade
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: film and on-set stills, warm practical light, rich blacks
Reject: ENTER THE EXPERIENCE gate before content; Statement lines with inline photos get crowded at small sizes
Token commitments: palette #000000, #46320C, #FEB901, #B6840A; type Geistmono, Gt Walsheim Condensed; engine GSAP + Lenis linked (never vendored).
