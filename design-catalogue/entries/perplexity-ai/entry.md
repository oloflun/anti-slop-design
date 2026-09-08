---
title: "Perplexity AI"
url: https://www.perplexity.ai
source_url: https://www.perplexity.ai
captured: 2026-09-04
origin: refero
extract: blocked: designlang far en generisk blocksida (bara Arial, 5-fargspalett med default lankbla, nastan tom Section Roles) - inte riktigt innehall
category: product-focused
category2: editorial
family: botanical-parchment-camouflage
dna: "Blurred garden photography as UI camouflage x whisper-weight serif declarations"
register: warm photographic
grammar: continuous world
lane: "White flower-like cards float over 20px-blurred botanical photography as if composited onto living nature footage, with a whisper-weight serif headline reading like a caption etched onto the glass between UI and garden"
mode: experience
traits: ["40px pill nav/CTA vs 4-12px everywhere else", "warm sepia ink, never true black", "20px blur on all hero/feature photography", "weight-300 serif and sans display, tight leading", "zero drop shadow, luminance-step depth only", "serif for declarations, sans for interface, never mixed"]
palette: ["#faf8f5", "#271a00", "#d1cfc7", "#ffffff", "#0f3639", "#23291b"]
type: ["pplxSerif", "pplxSans", "pplxSansMono"]
kind: reference-style
source: anton
status: ready
refero: processed/Perplexity AI.md
---

## Why it works

Palette and type are read from Refero's extracted tokens, confirmed by the live
capture. Aged sepia `#271a00` replaces true black everywhere as primary text and
border colour — the source is explicit that this near-brown warmth is "the
brand's chromatic signature, not interchangeable with true black," reserved
absolute black strictly for the footer. That single substitution is what lets
cool digital UI sit convincingly on top of warm botanical photography without
visual conflict.

Depth is built entirely from luminance step and blur, never shadow: white cards
float on parchment canvas at a stated "2-3% luminance difference," while hero
and feature photography receives a uniform 20px blur so sharp UI elements read
as composited glass panels over out-of-focus nature footage. Radius reinforces
the same hierarchy signal used elsewhere in this catalogue — 40px pill reserved
exclusively for nav and primary CTAs, 4-12px for every other surface — so the
one loud geometric gesture always marks "you can click this."

Typography keeps two display voices in strict separation: pplxSerif for
"declaration moments" (section headlines at 48-96px) and pplxSans for interface
and hero title alike, both locked to weight 300 at display scale — "authority
through restraint, not volume," per the source. The rule against ever mixing
serif and sans within one text block is what keeps the whisper-weight
consistently readable as intentional rather than merely thin.

## What to borrow (principle)

- **Substitute a warm near-black for true black system-wide.** A single sepia
  ink used for every text and border role gives an otherwise cool digital UI a
  consistent warm register.
- **Blur photography uniformly to let sharp UI float above it.** A stated 20px
  blur (not a gradient of blur values) creates a legible "glass over nature"
  compositing effect rather than a muddled background.
- **Reserve one extreme radius for exactly two component types.** 40px only on
  nav pills and CTAs, 4-12px everywhere else, keeps the interactive signal
  unambiguous.
- **Lock both display faces to the same light weight.** Running both the serif
  and the sans at weight 300 for display sizes means switching typefaces
  changes register (editorial vs. interface) without changing volume.
- **Vignette photography into the canvas colour, not into black.** Fading image
  edges toward parchment/white rather than a dark vignette keeps a photo-heavy
  hero from ever reading as moody or dark-mode.

## What to leave

- Applying a uniform 20px blur across all hero and feature imagery is a
  significant production cost and a strong constraint — it only works if every
  photograph is genuinely usable "soft," and it forecloses ever showing crisp
  photography as a feature.
- The single teal accent, confined to "nav active states, subtle highlights,"
  is easy to lose track of in a near-monochrome sepia system; a design team
  would need to actively audit for accidental teal creep or accidental omission.
- Weight-300 display type at both serif and sans sizes depends on both
  typefaces having genuinely well-drawn light cuts; a heavier substitute for
  either face would collapse the "whisper-weight authority" effect the system
  is built around.

## Signature move

The frosted-glass floating card: a translucent white surface at 60% opacity,
1px hairline border, sitting directly on blurred botanical photography — UI
rendered as a physical pane of glass laid over a garden rather than a flat
rectangle on a background image.

## Motion

No motion or interaction tokens are captured in the Refero export beyond the
static `backdrop-filter: blur(20px)` treatment on photography and the nav pill's
morph "into pill shape on hover/active." The live capture shows an active
building/query demo animating a monospace progress line ("BUILDING...") beneath
the hero — indicating the homepage runs a live, animated product demonstration
rather than a static hero, though no specific easing or duration is documented
beyond that observed behavior.

## Brief

Build an AI-product marketing page with a botanical-camouflage aesthetic.
Canvas is parchment `#faf8f5`; primary text, borders and icons use aged sepia
`#271a00` — never true black, which is reserved for the footer only. Apply a
uniform 20px blur to all hero and feature photography (close-up wildflower and
garden scenes), vignetting edges into white/parchment via a gradient. Float
white `#ffffff` cards and frosted-glass buttons (60% opacity white, 1px sepia-
tint border) directly over the blurred imagery. Use 40px pill radius
exclusively for the navigation bar and primary CTA; keep every other card,
badge and input at 4-12px. Set the hero title and section declarations at
weight 300, 72-96px, alternating between pplxSerif (editorial declarations) and
pplxSans (interface/hero title) — never mixed within one text block, and
pplxSans always carrying -0.028em tracking. Reserve teal `#0f3639` for nav
active states only. No drop shadows anywhere — depth comes from a 2-3%
luminance step between white cards and parchment canvas.

## Image recipe

Close-up botanical photograph of [SUBJECT] — wildflowers, ornamental grasses or
garden foliage in soft natural daylight, photorealistic (never illustrated or
abstracted), shot with genuine shallow depth of field, then processed with a
uniform 20px gaussian blur so the entire frame reads as consistently
out-of-focus, edges fading to white via a 200px linear gradient.

## Photo search

Unsplash first, Pexels second.
- "wildflower garden close up soft focus"
- "ornamental grass natural light bokeh"
- "botanical foliage blurred background"
- "forget-me-not flowers close up"

## Reference lock

Primary reference/direction: Perplexity AI (Computer) — botanical-camouflage
AI product page, blurred garden photography beneath frosted UI cards.
Preserve (3-5 traits): parchment `#faf8f5` canvas with aged sepia `#271a00`
ink, never true black outside the footer; uniform 20px blur on all hero/feature
photography with edges vignetting to white; 40px pill radius reserved for nav
and CTAs only, 4-12px elsewhere; weight-300 display type on both serif and sans
faces, never mixed in one block; zero drop shadow, depth from luminance step
only.
Borrow only (1-2): the frosted-glass 60%-opacity button over blurred imagery;
the monospace live-build progress indicator.
Role rules: serif never sets UI/interface text; teal accent confined to nav
active states, never a large fill; pplxSansMono reserved for code-adjacent
badges only.
Media strategy: photo:unsplash — close-up, photorealistic botanical photography
processed with a uniform blur filter; never illustrated or abstract, never
sharp in a UI-adjacent context.
Reject: drop shadows on any card; sharp (non-blurred) hero photography; a
second saturated accent beyond teal; 40px radius on cards or content
containers; body text below 15px.
Token commitments: bg `#faf8f5`, card `#ffffff`, border `#d1cfc7`, ink
`#271a00`, muted `#7c7464`, accent `#0f3639`, dark-overlay `#23291b`; display
weight 300 at 48-96px/leading 1.0-1.12/-0.028em (sans only); body pplxSans 400
at 15-16px/leading 1.5; radius 4px inputs/badges, 12px cards, 40px nav/CTA;
section gap 28-40px, card padding 40px.
