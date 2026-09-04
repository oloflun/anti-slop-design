---
title: "Shepherd"
url: https://www.withshepherd.com/
source_url: https://www.withshepherd.com/
captured: 2026-09-04
origin: raw-url
extract: ok
raw: raw/f6be4ef22ba3d66f-screenshot-upload.webp
category: product-focused
category2: ""
family: yellow-frictionless-underwriting
dna: "Insurtech dashboard proof x construction safety photography"
register: modern clean
grammar: live surface
lane: "A saturated yellow ground carries a serif headline broken up by inline icon glyphs and a small photo, then a warm construction-site photograph pairs with a tan product panel, closing on an icon-illustrated module grid"
mode: persuade
traits: ["saturated yellow ground", "serif headline with inline icon/photo glyphs breaking the sentence", "brokerage trust-logo row", "warm documentary construction photography", "tan info panel paired with photo", "black pill CTAs", "small folded-paper brand mark", "icon-illustrated product grid"]
palette: ["#F0BE2C", "#111111", "#D8C9A8", "#FFFFFF", "#E8752B"]
type: ["Magister", "GT Planar"]
measured: designlang (confirmed)
kind: reference-style
source: anton
status: ready
---

## Why it works

The headline is a single serif sentence interrupted four times by small inline
glyphs — a double-chevron, an upward arrow, a folded-paper icon, a tiny photo
thumbnail — set at cap-height inside the running text: "Making risk
*frictionless* ▶▶ Insurance ▲ for the builders and operators shaping ◆ our
physical [photo] world." It reads first as playful punctuation, then, on a
second look, as a small system: each glyph marks a concept (speed, elevation,
brand, the physical world) without needing a separate icon legend.

A fully saturated construction-safety yellow covers the entire hero — an
unusual, confident choice for an insurance company, where the category default
is navy-and-white credibility signalling. The yellow instead borrows directly
from job-site signage (hard hats, warning tape, machinery), which is a more
honest colour association for a company insuring physical construction risk
than a generic financial-services palette would be.

Below the fold, real documentary photography — a worker on scaffolding in
safety gear — sits beside a tan info panel making a specific, numbers-adjacent
claim ("rewarding builders who invest in technology to deliver safer and
better"). The photography is doing credibility work a financial-services stock
photo of a boardroom couldn't: it shows the actual risk being insured.

## What to borrow (principle)

- **Break a headline sentence with small inline glyphs at cap-height**, each
  marking one concept, as a lightweight alternative to a separate icon legend.
- **Borrow your category's own signage colour**, not the finance-default navy,
  when your product insures or serves a specific physical industry.
- **Pair documentary photography of the actual insured risk** (a worker on
  site, in gear) with the value-proposition panel, not generic office stock.
- **Run a brokerage/partner trust-logo row directly under the hero** when your
  buyer is a broker, not a consumer — sell to the actual audience reading the
  page.

## What to leave

- Breaking a single sentence with four different glyph types risks reading as
  cluttered rather than systemic if a reader doesn't immediately parse the
  glyph-as-concept logic — it needs to work even skimmed.
- A fully saturated yellow ground this large, sustained through the entire
  first fold, can fatigue on longer scroll sessions without a lighter section
  to rest the eye soon after.

## Signature move

The glyph-interrupted headline: a single plain sentence with inline icons and a
tiny inset photo standing in for select words, so the headline reads as both
a sentence and a small system of marks — a device that rewards a second,
closer read.

## Motion

(from designlang extract) Feel is "mixed" with scroll-linked motion confirmed.
Durations run a plain `100–600ms` ladder with no eased curve captured for the
common transitions (opacity, transform, grid-template-rows all use the
browser default). The real motion system lives in the Mantine-framework
keyframes: a `menuClose` clip-path wipe for the mobile nav, a `scroll`
slide-x for a marquee/logo strip, plus stock scale/opacity pulse and rotate
utilities (spinner, badge-ping style pulse) that read as UI chrome rather
than bespoke choreography — consistent with the entry's "no motion visible"
read for the hero glyphs and photography themselves.

| token | value | role |
|---|---|---|
| `xs`–`sm` | 100–200ms | UI state changes |
| `md` | 300ms | default transitions |
| `lg` | 600ms | larger transform/grid transitions |
| `scroll` (keyframe) | slide-x | marquee/logo-row scroll |

## Brief

Build a category-honest insurtech page for a physical-risk industry. Cover the
hero in your industry's own signage colour (not a generic finance palette),
and set a serif headline where 3-4 words are replaced or accompanied by small
inline glyphs at cap-height, each marking one underlying concept. Run a
brokerage/partner trust-logo row directly beneath. Pair documentary photography
of the real insured activity (a worker, a site, the actual risk) with a
tan or neutral info panel making one specific, numbers-adjacent claim. Close
with an icon-illustrated grid of product modules, black pill CTAs throughout.

## Image recipe

Documentary photograph of a worker in [SUBJECT] — construction, industrial, or
field-safety gear, genuine job-site setting, natural or work-light lighting,
mid-task rather than posed, colour grading left mostly natural with the
industry's signage colour as an accent nearby.

## Photo search

Unsplash first, Pexels second.
- "construction worker safety gear job site documentary"
- "scaffolding worker steel beam candid"
- "industrial site safety equipment natural light"

## Reference lock

Primary reference/direction: Shepherd — construction-signage yellow hero with a glyph-interrupted serif headline, documentary job-site photography paired with a claims panel.
Preserve (3-5 traits): the industry's own signage colour (not finance-default navy) as the dominant hero ground; a serif headline broken by small inline glyphs at cap-height, each marking one concept; documentary photography of the actual insured activity paired directly with the value-proposition panel; a brokerage/partner trust-logo row placed immediately under the hero.
Borrow only (1-2): the icon-illustrated product-module grid; the small folded-paper brand mark.
Role rules: inline glyphs capped at 4 per headline, each must map to a real concept, never pure decoration; hero photography always documents the real insured activity, never generic office stock.
Media strategy: photo:unsplash — documentary, real-industry photography only; no boardroom or handshake stock imagery.
Reject: a generic navy-and-white finance palette; more than one full-bleed saturated-colour section in a row with no visual rest between them; decorative glyphs with no conceptual mapping.
Token commitments: signage-yellow `#F0BE2C`, ink `#111111`, tan `#D8C9A8`, white `#FFFFFF`, icon-orange `#E8752B`; serif display for the headline, sans for UI and body.
