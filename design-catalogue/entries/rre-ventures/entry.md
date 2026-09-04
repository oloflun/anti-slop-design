---
title: "RRE Ventures"
url: https://rre.com/
source_url: https://rre.com/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/b6ce36ab26cc9b9e-screenshot-upload.webp
category: institutional
category2: ""
family: satellite-abstraction-fund
dna: "Satellite ocean photography x boutique-fund credibility panel"
register: cinematic dark
grammar: split stage
lane: "Abstract satellite ocean photography runs continuously behind the page, interrupted by alternating pale-blue credibility panels carrying stats, thesis and testimonials"
mode: persuade
traits: ["full-bleed abstract satellite/ocean photography as continuous ground", "alternating dark-photo/light-panel bands", "small geometric logomark", "plain stat trio", "sector tag grid", "quoted testimonial close", "minimal caps labels"]
palette: ["#0B2540", "#1C5F6B", "#C9A15C", "#D7E6EF", "#FFFFFF"]
type: ["RRE Monument Grotesk"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

A single abstract satellite photograph — swirling ocean currents in navy, teal
and sand — runs continuously as the page's visual ground, with content panels
laid on top of it rather than replacing it. Because the image is abstract
(no recognisable landmark, no people, no product), it can carry a VC firm's
entire visual identity without ever competing for meaning against the text on
top of it — it's mood without message, which is exactly what a fund's
background needs to be.

The page alternates between full-photo bands and pale-blue opaque panels: hero
claim on photo, then a stats panel on solid pale blue, then investment-area tags
back on photo, then a "our difference" panel on pale blue again, closing with a
testimonial quote back on the photograph. The rhythm of exposure-then-cover,
exposure-then-cover, keeps the page visually alive without needing any
additional imagery — one photograph, reused as a through-line, does the work of
several.

Content itself stays plain and confident: three round numbers (`$2.5B+ AUM`,
`125+ Exits`, `400+ Companies`), a sector tag grid (AI, Crypto, Fintech,
Consumer...) and one closing founder quote. Nothing is illustrated or iconified —
the restraint is the credibility signal for a firm this established.

## What to borrow (principle)

- **Use one abstract, non-literal photograph as a continuous through-line**,
  alternating between full exposure and being covered by opaque content panels,
  rather than sourcing a new image per section.
- **Alternate photo bands and solid-colour panels rhythmically** to keep a long
  page visually alive with a single image asset.
- **State fund/firm metrics as three bare round numbers**, no icons, no charts —
  for an established institutional audience, plainness reads as confidence.
- **Close on one real, attributed testimonial quote** rather than a logo wall,
  when relationship depth (not volume) is the actual sales pitch.

## What to leave

- Relying on a single background photograph for the entire page means any
  section that needs to add new visual information (a portfolio grid, a team
  photo) will need to break the pattern eventually — the system needs a defined
  exit point.
- Pale-blue opaque panels directly against a dark, saturated photograph can
  create a harsh edge at the panel boundary if not softened with a gradient or
  consistent margin.

## Signature move

The single continuous background: one abstract satellite/ocean photograph runs
the full length of the page, alternately exposed behind photo-band content and
covered by opaque pale-blue panels — one image asset doing the visual work of
an entire long-scroll page.

## Motion

(from designlang extract) Feel is "responsive" with scroll-linked motion
confirmed. Transitions sit on a quick `200–300ms` pair, riding a single
ease-out curve (`cubic-bezier(0.25,1,0.5,1)`, 12 uses) for hover/colour state
changes — filter, height, background and opacity moves on links and panel
edges. No parallax or fixed-background keyframe was captured for the
satellite photograph itself, so the "photo drifts behind the panels" read
stays inferred from the image, not confirmed by the extract.

| token | value | role |
|---|---|---|
| `sm` | 200ms | link/filter/height transitions |
| `md` | 300ms | panel/background transitions |
| ease-out | `cubic-bezier(0.25,1,0.5,1)` | only family found (12 uses) |

## Brief

Build an institutional, credibility-first fund or firm page. Choose one
abstract, non-literal photograph (satellite imagery, aerial water, geological
texture) in a limited navy/teal/sand palette, and run it continuously behind
the entire page. Alternate full-photo content bands (hero claim, sector tags,
closing quote) with opaque pale-blue panels (stats, thesis, differentiators) so
the single image is rhythmically exposed and covered rather than replaced.
State metrics as bare round numbers with no icons or charts. Close on one
attributed testimonial quote rather than a logo wall. Keep type to a single
plain grotesk sans throughout, small tracked caps for section labels.

## Image recipe

Abstract satellite or aerial photography of [SUBJECT] — ocean currents,
coastline, or geological terrain — shot from directly above, saturated navy,
teal and warm sand tones, no recognisable landmark or scale reference, texture
and colour carrying the entire image.

## Photo search

Unsplash first, Pexels second.
- "satellite ocean current abstract aerial"
- "aerial coastline texture navy teal"
- "earth from above abstract water"

## Reference lock

Primary reference/direction: RRE Ventures — one continuous abstract satellite photograph alternately exposed and covered by pale-blue credibility panels.
Preserve (3-5 traits): a single abstract, non-literal photograph used continuously as the page's visual ground; alternating rhythm of full-photo bands and opaque pale-blue content panels; metrics stated as bare round numbers with no icons or charts; one attributed testimonial quote as the closing device, not a logo wall.
Borrow only (1-2): the sector/investment-area tag grid; the small geometric logomark.
Role rules: only one background photograph per page, no substitutions mid-scroll; opaque panels always pale blue, never a second photo or gradient; stat trio capped at three numbers, never more.
Media strategy: photo:unsplash — abstract aerial/satellite imagery only, no people, no literal office or handshake photography anywhere on the page.
Reject: swapping in a second background image; icon-illustrated stat tiles; a logo wall in place of the attributed quote.
Token commitments: navy `#0B2540`, teal `#1C5F6B`, sand `#C9A15C`, panel-blue `#D7E6EF`, white `#FFFFFF`; single grotesk sans for all type, small tracked caps for section labels.
