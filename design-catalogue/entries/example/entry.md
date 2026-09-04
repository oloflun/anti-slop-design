---
title: "EXAMPLE"
url: https://www.weareexample.com
source_url: https://www.weareexample.com
captured: 2026-09-04
origin: raw-url
raw: raw/24ad4c5cd6218a7f-www-weareexample-com.webp
extract: ok
category: portfolio
category2: hospitality
family: condensed-marquee-agency
dna: "Culture-agency manifesto poster x hotel-lounge marquee reel"
register: modern clean
grammar: typographic poster
lane: "A giant condensed black headline wedges small client photos into its own letterforms, then a full-bleed hotel-lounge photo carries a horizontal scrolling marquee of the same copy"
mode: persuade
traits: ["off-white ground", "ultra-bold condensed display sans", "photos wedged into headline letterforms", "italic script sub-tagline", "horizontal marquee text over photo", "warm red-lit interior photography", "numbered slide counter", "minimal single-line nav"]
palette: ["#F3F3F3", "#7A4B2E", "#380907", "#0F141B", "#730909", "#907663"]
type: ["American Grotesk Compressed", "Ppeditorialnew"]
measured: designlang
kind: reference-style
source: claude
status: ready
---

## Why it works

The page opens with one device doing double duty: an oversized, ultra-bold condensed
headline ("AN EARNED-LED CULTURE AGENCY") that reads as pure typography from a distance,
but has two small client-work photographs wedged directly into its negative space, tucked
between letters at an angle. The headline is the hero image and the proof point at once —
there's no separate "our work" gallery competing for the same attention in the first
screen.

Directly beneath it, a full-bleed, warm red-lit hotel-lounge photograph carries a second
typographic device: a horizontal marquee of oversized white type ("...AND HOTELS TRAVEL
...") scrolling across the image at a scale that partially exceeds the viewport, with a
small `02/03` counter centred at the top. Because both the headline and the marquee use
the same ultra-condensed, ultra-bold face, the page reads as one continuous typographic
voice even though the mechanism (static wedge vs. scrolling band) changes.

An italic script line — "We Make It Happen" — sits alone in the quiet gap between the two
loud sections, functioning as the page's only soft, humanising mark against two very hard
typographic devices. The restraint of introducing a second type voice exactly once, at the
lowest-intensity moment, keeps it from diluting the condensed system.

## What to borrow (principle)

- **Wedge real work photography into the negative space of giant type**, rather than
  running a headline and a portfolio grid as separate zones — the credibility and the
  hook arrive in the same glance.
- **Reuse one condensed, ultra-bold voice across both a static headline and a moving
  marquee.** The mechanism can change (static vs. scrolling) as long as the type doesn't.
- **Save a second, softer typeface for exactly one low-intensity moment** — a tagline, a
  closing line — so it reads as a considered break, not a second system.
- **Let a full-bleed photo carry oversized type that exceeds the frame.** Type running off
  both edges signals scale and confidence without needing more copy.

## What to leave

- Tucking a small square photo behind a headline letter at a rotated angle (top left) is
  legible here only because the photo has a light background matching the page ground —
  it would fail against a busier client photo.
- The marquee band's line-height and the interior photo's horizon line nearly collide
  (visible in the raw capture), leaving little breathing room above the scrolling text —
  worth a fixed minimum contrast scrim behind the marquee band.
- This entry's `fold.webp`/`shot.webp` are derived from the archived raw capture, not a
  fresh render — the live page returned HTTP 200 but did not reach network-idle within the
  capture budget (likely continuous marquee/video network activity), so treat exact crops
  and any since-changed copy as approximate.

## Signature move

The marquee band: a strip of oversized type scrolling horizontally across a full-bleed
photograph, with a slide counter (`02/03`) marking it as one frame in a sequence rather
than a one-off flourish — turning a scrolling ticker, usually a low-craft device, into a
structured, numbered chapter.

## Motion

Overall feel reads as mixed — quick UI-chrome transitions layered under a page that is
otherwise scroll-linked. Interaction states run on two short durations: a `sm` 200ms for
opacity fades (link/nav hover) and a `md` 300ms for border-color changes (form-input focus
rings). Neither transition declares an explicit easing function, so both fall through to
the browser's plain default ease — nothing here signals a spring or overshoot curve. The
only keyframe animation the extract captured is a plain 360° `spin`, almost certainly a
loading-icon rotation rather than the hero/marquee effect; the extract's DOM/CSS pass
doesn't confirm how the marquee band itself is driven (likely a scroll-triggered script
rather than a declared `@keyframes` rule), and no stagger/choreography pattern is
documented. (from designlang extract)

| Token | Value | Curve |
|---|---|---|
| `sm` (opacity) | 200ms | default ease (unspecified) |
| `md` (border-color) | 300ms | default ease (unspecified) |
| `spin` keyframe | rotate 0deg → 360deg | unspecified (loader) |

## Brief

Build a culture/PR-agency landing page anchored on one oversized, ultra-condensed bold
headline set on an off-white ground, with one or two small real-work photographs wedged
into the headline's negative space at a slight rotation. Beneath it, run a full-bleed,
warm-lit interior or lifestyle photograph carrying a horizontal marquee of oversized white
type in the same condensed face, scrolling past the frame edges, with a small numbered
counter (`NN/total`) marking it as one of several sequential slides. Use an italic script
line as the only second typeface, reserved for a single soft tagline between the two loud
sections. Keep the palette to off-white, near-black and one warm red/brown drawn from the
photography — no separate brand accent colour.

## Image recipe

Warm, red-lit interior photograph of [SUBJECT] — a hotel lounge, a members' club, a
destination bar — shot at dusk or with practical warm lighting, saturated reds and ambers,
real furniture and real guests or staff in soft focus, composed with a clear horizontal
band through the middle third so scrolling marquee type can run across it without losing
legibility.

## Photo search

Unsplash first, Pexels second.
- "hotel lounge red lighting interior"
- "members club warm ambient interior"
- "rooftop bar dusk skyline"
- "boutique hotel lobby evening light"

## Reference lock

Primary reference/direction: EXAMPLE — condensed manifesto headline with photos wedged
into letterforms, marquee band over a red-lit hotel photo.
Preserve (3-5 traits): off-white ground with near-black condensed display type as the
dominant voice; small work photography wedged into the headline's negative space rather
than shown in a separate grid; a full-bleed warm interior photograph carrying an oversized
scrolling marquee in the same face; a numbered slide counter marking sequential content; a
single italic script line as the only second typeface, used once.
Borrow only (1-2): the slight rotation on wedged photos; the thin horizontal progress
line beneath the marquee photo.
Role rules: the condensed display face is used for both static headlines and the marquee,
never mixed with a third face; the italic script appears at most once per page; accent
colour is drawn only from the photography (warm red/brown), never a separate brand hue.
Media strategy: photo:unsplash — warm, saturated interior/hospitality photography with a
clear horizontal band for marquee-type legibility; never a flat, evenly-lit product shot.
Reject: a conventional separate "our work" grid competing with the hero; more than one
accent colour; a second display typeface; centred, static (non-scrolling) proof sections.
Token commitments: bg `#F3F3F3`, ink `#0F141B`, warm-deep `#380907`, warm-red `#730909`,
warm-mid `#7A4B2E`, warm-tint `#907663`; display: ultra-condensed bold grotesque for
headline and marquee; script/italic serif for the single soft tagline; marquee type scaled
to exceed the viewport edges.
