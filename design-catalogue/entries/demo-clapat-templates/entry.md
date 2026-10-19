---
title: "Hayler (Clapat template)"
url: https://demo.clapat-templates.com/hayler
source_url: https://demo.clapat-templates.com/hayler
captured: 2026-10-02
origin: raw-url
extract: none
category: portfolio
category2: ""
family: lilac-counter-template-agency
dna: "Agency HTML template x lilac counter and block wipes"
register: modern clean
grammar: chaptered editorial
lane: "A commercial agency template: a lilac screen counts 000 → 100 in the corner, the page opens on a two-line statement with images sliding in from the bottom edge, projects drift in a staggered grid, and black stepped blocks wipe between light and dark chapters."
mode: persuade
traits: ["full-screen lilac counter loader", "staggered project grid with parallax", "black stepped-block wipe between chapters", "client logo marquee on black", "feature list with active row", "giant name in the footer"]
palette: ["#F7F7F7", "#B980FF", "#7C4061", "#C6B6A2"]
type: ["FunnelDisplayWeb", "Inter Tight"]
measured: "palette quantized from motion captures; type from document.fonts; stack from motion/probe.json"
kind: reference-style
source: claude
status: ready
showcase: gsap
motion_floor: 0
---
<!-- motion_entry.py -->
## Why it works

It packages the showcase vocabulary as a template: counter loader, image parallax, a stepped black block wipe that changes the ground, a marquee, a list that lights one row. Useful as a baseline of what is now standard, not as a signature.

Read from the scroll captures in `motion/sheet.webp` (intro strip, then one frame per wheel
step). Palette quantized from those frames; type from the fonts the page loaded. Listed in the
gsap showcase (credits: Clapat Studio).

## What to borrow (principle)

- A stepped-block wipe (staircase of black rectangles) to change ground between chapters

## What to leave

- Generic template content and structure
- Everything is a known move; no single idea carries the page

## Signature move

Black stepped blocks wiping the page from light to dark.

## Motion

Intro: white, then lilac with '000' counting to '100' bottom-right (~2.5 s), lilac lifts. Scroll (Lenis, ~140 px glide, 73 ScrollTriggers, 2 pins): statement lines; images rise in a staggered grid; 'See all Projects'; black stepped blocks grow up the frame; client marquee and logo grid on black; blocks step back to white; features list with one active row; 'Digital Experiences' next-page link; footer name.

Measured (`motion/probe.json`): GSAP 3.13.0; 73 ScrollTriggers; 2 pinned sections; Lenis; 1 video; smoothed scroll (median 128 px still travelling after input stops). Floor tier: **one move worth keeping** (`references/scroll/showcase-floor.md`).

## Brief

A modern clean page in the chaptered editorial grammar: a commercial agency template: a lilac screen counts 000 → 100 in the corner, the page opens on a two-line statement with images sliding in from the bottom edge, projects drift in a staggered grid, and black stepped blocks wipe between light and dark chapters. Type: FunnelDisplayWeb, Inter Tight.
Ground and ink from the measured palette (#F7F7F7, #B980FF, #7C4061). Motion carries the page through
black stepped blocks wiping the page from light to dark. Build it on the linked GSAP + Lenis toolchain
(`references/scroll/toolchain.md`), one Lenis instance, every trigger created in page order.

## Image recipe

[SUBJECT] — high-saturation fashion/product photos and abstract 3D renders

## Photo search

own production or commissioned; the page's motion depends on the imagery's art direction: high-saturation fashion/product photos and abstract 3D renders

## Reference lock

Primary reference/direction: Hayler (Clapat template) — A commercial agency template: a lilac screen counts 000 → 100 in the corner, the page opens on a two-line statement with images sliding in from the bottom edge, projects drift in a staggered grid, and black stepped blocks wipe between light and dark chapters.
Preserve (3-5 traits): full-screen lilac counter loader; staggered project grid with parallax; black stepped-block wipe between chapters; client logo marquee on black; feature list with active row.
Borrow only (1-2): A stepped-block wipe (staircase of black rectangles) to change ground between chapters
Role rules: motion serves reading order; every reveal fails toward visible; headings stand still while they are read (house rule).
Media strategy: high-saturation fashion/product photos and abstract 3D renders
Reject: Generic template content and structure; Everything is a known move; no single idea carries the page
Token commitments: palette #F7F7F7, #B980FF, #7C4061, #C6B6A2; type FunnelDisplayWeb, Inter Tight; engine GSAP + Lenis linked (never vendored).
