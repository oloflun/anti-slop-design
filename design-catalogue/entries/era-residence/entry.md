---
title: "ERA Residence"
url: https://era-residence.com/
source_url: https://era-residence.com/
captured: 2026-10-02
origin: raw-url
extract: none
category: hospitality
category2: "luxury-craft"
family: mediterranean-arch-residence
dna: "Costa del Sol residences x condensed serif and arched windows"
register: warm photographic
grammar: chaptered editorial
lane: "A residential development page that opens on burgundy with a condensed serif ERA RESIDENCE and script 'Estepona', then a semicircular window rises out of the bottom and grows into the full pool photograph; the rest alternates arches, bougainvillea and a drawn coastline map."
mode: persuade
traits: ["burgundy intro ground", "condensed serif caps + script word", "semicircle/arch window that grows into the photo", "text set on a curve along the arch edge", "bougainvillea cut-outs at the edges", "hand-drawn coastline route"]
palette: ["#340C25", "#7A98B7", "#3B68A9", "#B2C6D5", "#423A33", "#1A4585"]
type: ["Maison Neue Extended", "ambroise-francois-std", "sloop-script-three"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 2
---
<!-- motion_entry.py -->
## Why it works

Architecture is the transition: a half-moon window appears at the base of the intro and grows into the full photograph of the pool, and later arches carry text around their edges ('three reasons to choose ERA'). The burgundy, script and bougainvillea give a Mediterranean holiday register without a single sunset cliché.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: The First The Last).

## What to borrow (principle)

- Grow a shape from the architecture (an arch) into the full-bleed photo as the intro handoff
- Set a line of text along the curve of the shape that frames the image
- Cut-out flowers bleeding in from the frame edges as recurring ornament

## What to leave

- 132 ScrollTriggers; long page
- Condensed serif in light weights loses legibility over photos

## Signature move

A half-moon window rising from the bottom of the burgundy intro and growing into the pool photograph.

## Motion

Intro: burgundy, logo star, 'ERA RESIDENCE Estepona' with 'COSTA … DEL SOL' spaced either side (~2 s); a script line draws behind. Scroll (Lenis, 132 ScrollTriggers, Barba, Observer): a semicircle rises from the bottom and grows into the full pool photo with the title over it; 'THREE REASONS TO CHOOSE ERA' set on an arch curve; 'REAL-LIFE LOCATION' on pale blue with a small image that grows; bougainvillea frames; drawn coastline from Gibraltar to Malaga; aerial with a cloud transition; floor plans; interior pairs.

Measured (`motion/probe.json`): GSAP 3.15.0; 132 ScrollTriggers; Lenis; Barba page transitions; 8 video; smoothed scroll (median 153 px still travelling after input stops); entry gate: DECLINE DECLINE. Floor tier: **sets the floor** (`references/scroll/showcase-floor.md`).

## Brief

A warm photographic page in the chaptered editorial grammar: a residential development page that opens on burgundy with a condensed serif ERA RESIDENCE and script 'Estepona', then a semicircular window rises out of the bottom and grows into the full pool photograph; the rest alternates arches, bougainvillea and a drawn coastline map. Type: Maison Neue Extended, ambroise-francois-std, sloop-script-three.
Ground and ink from the measured palette (#340C25, #7A98B7, #3B68A9). Motion carries the page through
a half-moon window rising from the bottom of the burgundy intro and growing into the pool photograph. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — architectural renders in strong sun, pools, white walls, magenta bougainvillea

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: architectural renders in strong sun, pools, white walls, magenta bougainvillea

## Reference lock

Primary reference/direction: ERA Residence — A residential development page that opens on burgundy with a condensed serif ERA RESIDENCE and script 'Estepona', then a semicircular window rises out of the bottom and grows into the full pool photograph; the rest alternates arches, bougainvillea and a drawn coastline map.
Preserve (3-5 traits): burgundy intro ground; condensed serif caps + script word; semicircle/arch window that grows into the photo; text set on a curve along the arch edge; bougainvillea cut-outs at the edges.
Borrow only (1-2): Grow a shape from the architecture (an arch) into the full-bleed photo as the intro handoff; Set a line of text along the curve of the shape that frames the image
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: architectural renders in strong sun, pools, white walls, magenta bougainvillea
Reject: 132 ScrollTriggers; long page; Condensed serif in light weights loses legibility over photos
Token commitments: palette #340C25, #7A98B7, #3B68A9, #B2C6D5, #423A33, #1A4585; type Maison Neue Extended, ambroise-francois-std, sloop-script-three; engine GSAP + Lenis linked (never vendored).
