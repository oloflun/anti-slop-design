---
title: "Nothin'"
url: https://noth.in/
source_url: https://noth.in/
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: chrome-objects-paris-studio
dna: "Paris creative studio x chrome 3D objects and giant wordmark"
register: modern clean
grammar: chaptered editorial
lane: "A studio page that opens on N' with a chrome heart in place of the apostrophe, cuts to a white page filled edge to edge by NOTHIN', then shows its work as mockups on black and a short film of a silver figure in a hospital waiting room."
mode: persuade
traits: ["chrome 3D objects (heart, star, crumpled foil)", "full-width black wordmark on white", "black work section with device mockups", "film still: silver creature in waiting room", "Neue Montreal + Plex Mono", "Taxi transitions"]
palette: ["#000000", "#FFFFFF", "#121417", "#3F6FDA", "#253046", "#374B7B"]
type: ["Ppneuemontreal", "Ppneuemontreal Book", "IBM Plex Mono"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap+lenis
motion_floor: 1
---
<!-- motion_entry.py -->
## Why it works

The name (Nothin') is played straight: a blank white page with only the word, edge to edge. Personality comes from glossy chrome objects (a heart, a star, crumpled foil) that appear between sections like props, and from a surreal film, so a minimal layout has strange, tactile moments.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap and lenis showcase (credits: Nothin', Thomas Carré).

## What to borrow (principle)

- Replace a glyph in the wordmark with a 3D object during the intro
- A wordmark set to the full page width as a hero
- Use a few odd 3D props as recurring punctuation between plain sections

## What to leave

- Work mockups are generic device renders
- Black-to-white switch is abrupt

## Signature move

A chrome heart standing in for the apostrophe of N' in the loader.

## Motion

Intro: black, 'N'' appears, a chrome heart spins in as the apostrophe, then out (~1.5 s); a black panel lifts to white and NOTHIN' fills the width. Scroll (Lenis, 1 pin, Taxi, Flip, SplitText): 'Most brands produce content. We prefer ideas.' with chrome objects rising; black 'WORKS' section with mockups sliding in; the waiting-room film scales up from a frame inside a gallery space; studio text; 'Forms follow perspective.' with the objects scattered.

Measured (`motion/probe.json`): GSAP 3.13.0; 1 pinned sections; Lenis; Taxi page transitions; 4 video; split text; smoothed scroll (median 139 px still travelling after input stops). Floor tier: **solid** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a studio page that opens on N' with a chrome heart in place of the apostrophe, cuts to a white page filled edge to edge by NOTHIN', then shows its work as mockups on black and a short film of a silver figure in a hospital waiting room. Type: Ppneuemontreal, Ppneuemontreal Book, IBM Plex Mono.
Ground and ink from the measured palette (#000000, #FFFFFF, #121417). Motion carries the page through
a chrome heart standing in for the apostrophe of N' in the loader. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — chrome 3D props, surreal staged film stills, device mockups

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: chrome 3D props, surreal staged film stills, device mockups

## Reference lock

Primary reference/direction: Nothin' — A studio page that opens on N' with a chrome heart in place of the apostrophe, cuts to a white page filled edge to edge by NOTHIN', then shows its work as mockups on black and a short film of a silver figure in a hospital waiting room.
Preserve (3-5 traits): chrome 3D objects (heart, star, crumpled foil); full-width black wordmark on white; black work section with device mockups; film still: silver creature in waiting room; Neue Montreal + Plex Mono.
Borrow only (1-2): Replace a glyph in the wordmark with a 3D object during the intro; A wordmark set to the full page width as a hero
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: chrome 3D props, surreal staged film stills, device mockups
Reject: Work mockups are generic device renders; Black-to-white switch is abrupt
Token commitments: palette #000000, #FFFFFF, #121417, #3F6FDA, #253046, #374B7B; type Ppneuemontreal, Ppneuemontreal Book, IBM Plex Mono; engine GSAP + Lenis linked (never vendored).
