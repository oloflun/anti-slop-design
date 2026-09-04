---
title: "Contra Labs"
url: https://contralabs.com
source_url: https://contralabs.com
captured: 2026-09-04
origin: raw-url
extract: ok
category: product-focused
category2: editorial
family: old-master-halftone-collage
dna: "Renaissance oil portraiture x halftone-dithered tech device"
register: illustrated dark
grammar: gallery/catalog
lane: "A classical oil-painting figure works a halftone-dithered laptop in the hero, then the page scatters more of the same device — dot-matrix phones and laptops collaged into old-master portraits — around short serif claims"
mode: persuade
traits: ["renaissance oil painting portraiture", "halftone/dither-textured device overlays", "serif display headlines", "scattered mosaic image layout", "pill-shaped nav CTAs", "cream paper ground", "sage green logo mark"]
palette: ["#FBFAF6", "#A5BEBA", "#2B2B29", "#918F66", "#C8BCAE", "#494444"]
type: ["Source Serif 4 Variable", "GT Standard L Regular"]
measured: designlang (confirmed)
kind: reference-style
source: claude
status: ready
raw: raw/be685599d2e16631-contralabs-com.webp
---

## Why it works

The whole identity rests on one collage device: a classical oil-painting
figure — the kind you'd find captioned in a museum — is shown using a modern
device that's been rendered as a coarse halftone dot-matrix, as if it were
printed on newsprint rather than painted. The contrast is the argument made
visual without saying it: old human expertise (the painting) meeting new
machine texture (the dithered object), which is exactly what an "AI eval lab
for human creativity" is selling. Because the device is reused — laptop in the
hero, phones and tablets in the portraits further down — it reads as a system,
not a one-off hero trick.

Type stays out of the way of that device. A warm serif (Source Serif 4)
carries every headline and claim in plain sentence case, sized generously but
never competing visually with the collage; a plain grotesque (GT Standard L)
handles body copy and UI labels. Below the fold, the page changes composition
strategy entirely — instead of one large hero image, it scatters a dozen small
portrait cards at irregular sizes and positions around a centred serif
headline, like pinned photographs on a wall, which keeps the "gallery of
evidence" feeling going without repeating the hero's exact framing.

The palette is almost silent — cream paper, near-black ink, one sage-green
accent on the logo mark and page furniture — so every bit of colour interest in
the page comes from the paintings themselves, not from applied brand colour.

## What to borrow (principle)

- **Invent one visual collage device that literalises the pitch**, and reuse it
  across the page rather than confining it to the hero — a single trick used
  once reads as decoration; used five times it reads as a visual language.
- **Keep type completely neutral (one serif, one grotesque, sentence case)**
  when the imagery itself is doing all the conceptual work — competing display
  type would fight the collage for attention.
- **Scatter proof images at irregular sizes instead of a grid** to keep a
  photo-heavy section from reading as a stock gallery.
- **Reserve brand colour for the smallest elements** (logo mark, hairlines)
  and let sourced/generated imagery carry all the visual richness.

## What to leave

- Nav copy and CTA labels changed between two captures of the same page
  ("Request partnership" / "Research" vs. "Join network" / "Get in touch"),
  suggesting active A/B testing or fast iteration — fine for a young company,
  worth knowing before treating any single state as final.
- The scattered mosaic layout risks feeling cluttered at narrower viewports;
  it depends on generous whitespace that a smaller screen won't have.
- The halftone/dither texture on devices is a specific, hard-to-reproduce
  effect — it needs either a real filter pipeline or bespoke asset prep, not a
  quick CSS trick.

## Signature move

Classical oil-painting portraits photoshopped to hold a modern device rendered
in a coarse black-and-white halftone dot pattern — human craft and machine
texture occupying the same frame, reused across the hero and every proof
section as the page's one recurring idea.

## Motion

(from designlang extract) The extract rates overall feel "responsive" with
confirmed scroll-linked behaviour, though the token set itself is unusually
minimal: just two duration steps (an effectively-instant 1ms and a single
320ms `md`) and one ease-out curve (`cubic-bezier(0.22, 1, 0.36, 1)`, 6 uses)
driving width and transform changes. This scarcity matches the page's overall
restraint — colour and type stay quiet so the collage imagery carries
attention, and motion follows the same discipline rather than adding its own
flourish. The only keyframe defined is Framer's built-in loading spinner, not
a bespoke animation; there's no evidence of a custom stagger or reveal
choreography for the scattered mosaic section beyond what a generic
scroll-reveal utility would add.

| kind | tokens |
|---|---|
| durations | instant 1ms · md 320ms |
| easing | ease-out `cubic-bezier(0.22, 1, 0.36, 1)` (6×) |

## Brief

Build a product/lab landing page around one bespoke visual collage device that
makes the pitch literal without copy — here, classical oil portraiture paired
with a modern object rendered in coarse halftone dither, standing in for "human
expertise meets machine." Reuse the device across the hero and every proof
section rather than once. Keep typography completely quiet: one warm serif for
headlines in plain sentence case, one grotesque for body and UI, both
generously sized but never competing with the imagery. Ground the page in cream
paper with near-black ink and exactly one small accent colour reserved for the
logo mark and hairlines. Below the fold, break from the hero's single-image
composition into a scattered mosaic of small proof images at irregular sizes
around a centred serif claim.

## Image recipe

Classical oil-painting portrait of [SUBJECT] in Renaissance or Baroque style,
warm varnished tones, holding or interacting with a modern device (laptop,
phone, tablet) that has been re-rendered in a coarse black-and-white halftone
dot pattern as if printed separately and composited in, sharp tonal contrast
between the painted figure and the dithered object, museum-plate lighting and
colour grading on the portrait itself.

## Photo search

Unsplash first, Pexels second (for supporting texture only — the signature
collage imagery is bespoke composite work, not sourced stock).
- "renaissance oil painting portrait classical"
- "museum painting detail hands"
- "old master portrait warm tone"

## Reference lock

Primary reference/direction: Contra Labs — old-master portraiture collaged
with halftone-dithered devices, scattered mosaic proof layout.
Preserve (3-5 traits): the halftone-dithered device held by a classical
oil-painting figure, reused across hero and every proof section; one warm
serif for headlines in plain sentence case, one grotesque for body/UI, neither
competing with the imagery; cream paper ground with near-black ink and a single
small accent colour; scattered mosaic of irregularly-sized proof images below
the fold instead of a uniform grid.
Borrow only (1-2): the pill-shaped nav CTA pair (outline + filled); the small
ribbon/diamond logo mark.
Role rules: the halftone-dither treatment applies only to modern devices
inserted into classical paintings, never to full images or to UI chrome;
accent colour never used for large fills, only marks and hairlines.
Media strategy: bespoke composite (painting + halftone device) as the sole
hero-scale device across the page; no separate stock photography competing
for hero attention.
Reject: a second display typeface; full-colour brand fills competing with the
paintings; a uniform image grid in place of the scattered mosaic.
Token commitments: paper `#F1F0EC`, ink `#41352B`, sage `#C3DAD7`, stone
`#B7BBAD`, olive `#6C6B55`; headline serif "Source Serif 4 Variable", body/UI
"GT Standard L Regular".
