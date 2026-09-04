---
title: "Hark Capital"
url: https://www.harkcap.com
source_url: https://www.harkcap.com
captured: 2026-09-04
origin: raw-url
extract: ok
category: institutional
category2: ""
family: glass-monolith-finance
dna: "3D glass-render hero x flat institutional finance grid"
register: modern clean
grammar: split stage
lane: "A rotating 3D glass monolith fills the hero under one restrained headline, then the page drops to flat white sections of stats, story and a hoverable team roster"
mode: persuade
traits: ["3D rendered glass hero object", "steel-blue to white gradient ground", "flat white content sections", "numeric stat tiles on photographic band", "hover-reveal team photo list", "sparse dot-labelled section kickers", "expandable corner nav"]
palette: ["#F3F3F3", "#181818", "#062541", "#114167", "#235E80", "#00F2E5", "#919598", "#D4D4D4"]
type: ["Aeonikpro", "Suisseworks Webs"]
measured: designlang
kind: reference-style
source: claude
status: ready
raw: raw/5dd9960623f203e4-www-harkcap-com.webp
---

## Why it works

The hero is doing one job: a large, glossy, 3D-rendered glass volume — closer to
product-render than illustration — fills almost the entire first viewport behind
a two-line headline ("Pioneers in NAV financing") set small relative to the
object. The type stays modest deliberately; the render carries the authority
signal that a finance site usually gets from photography of a skyline or a
handshake. One typeface (Aeonikpro, a plain geometric grotesque) runs the whole
page at every size, so nothing about the type competes with the object — the
render is the only "designed" element, everything else is quiet infrastructure
around it.

Below the fold the page flattens hard: pure white ground, small dot-prefixed
kickers ("Who We Are", "Core Stats"), body copy in the same grotesque at
paragraph size. The one return to the blue-glass palette is a stat band —
2013 / $2.1B+ / 70+ / 4 — laid directly over a close crop of the same rendered
material, tying the numbers visually back to the hero object rather than
presenting them as a generic dashboard.

The team section swaps the pattern again: a plain list of names in light grey,
with the row under the cursor turned to solid black text and a portrait photo
appearing beside it. Identity is withheld until the reader engages — a quieter,
more editorial way to present a roster than the usual grid-of-headshots.

The extract also surfaces a real electric-cyan accent (`#00f2e5`, used 60
times in CSS) and a secondary display face, Suisseworks Webs, used sparingly
alongside Aeonikpro — the render's blue-grey material isn't the whole
brand palette, and the "one grotesque" read holds for scale but not for
absolute exclusivity.

## What to borrow (principle)

- **Use one 3D-rendered hero object as the entire authority signal**, and keep
  the headline small enough that the object, not the type, is what the eye
  reads first.
- **Return to the hero's exact material once, for the numbers** — stats sitting
  on the same glass-blue crop reads as "these numbers come from that thing,"
  not as a disconnected metrics widget.
- **Withhold team photos until hover** — a roster of grey names with one photo
  revealed at a time reads more restrained than a wall of headshots, and gives
  the page an interaction moment in an otherwise static list.
- **Run the whole page on one grotesque at every weight** so a heavy visual hero
  never has to fight a second typeface for attention.

## What to leave

- The stat band's numbers sit low-contrast against the glass photography in
  places (white-on-light-blue) — legibility is closer to "reads at full
  attention" than "reads on a skim."
- The expandable "Click to Expand" corner nav is a small extra interaction step
  before the reader can see the primary nav items, which are otherwise just
  three links.
- The hero object, while striking, carries no explicit metaphor tied to NAV
  financing in the copy — it's abstract polish rather than idea made visual.

## Signature move

The hover-reveal team roster: a stacked list of names in flat grey, with the
row under the pointer turning solid black and a portrait photograph appearing
beside it — identity given only to the person currently being read, not to the
whole list at once.

## Motion

(from designlang extract) The extract rates overall feel "smooth" with
confirmed scroll-linked behaviour. Duration steps run from an effectively
instant 1ms state toggle up to 300ms, almost entirely on a plain `ease-in-out`
curve (186 uses, just `ease`) rather than a custom bezier or spring — restrained
by design, in keeping with the render-carries-the-authority read above. A
`--transition-smooth: all 400ms ease-out` custom property also appears,
likely governing the hero object itself. Two named keyframes in the
stylesheet, `move-in` (a clip-path polygon wipe from a closed sliver to full
reveal) and `move-out` (opacity 1→0.4), read as the mechanism behind the
hover-reveal team roster in the Signature move below — a wipe-in for the row
gaining focus, a dim-out for the rest — though neither registers as "in use"
in the extract's runtime scan, so this is inferred from the keyframes'
definitions and names, not confirmed live. A `spin` keyframe is also defined
but unused. (inferred from image) The hero object's framing differs between
the raw screenshot and the fresh capture, still consistent with the render
rotating or the camera moving on load/scroll.

| token | duration | easing |
|---|---|---|
| `instant` | 1ms | ease-in-out (`ease`) |
| `sm` | 200ms | ease-in-out (`ease`) |
| `md` | 300ms | ease-in-out (`ease`) |
| `--transition-smooth` | 400ms | ease-out |

## Brief

Build an institutional finance hero around one large 3D-rendered glass or metal
object, ideally something evoking the firm's structure, filling most of the
first viewport in cool blue-grey tones (`#81A0B0`, `#446A87`, `#263240`) against
a light ground. Keep the headline to two short lines, set small relative to the
object, in one plain geometric grotesque used everywhere on the page. Drop to a
flat white body with small dot-prefixed section kickers and modest paragraph
copy. Present core stats as large numerals laid over a close crop of the same
hero material, not on a plain background. For a team page, list names in flat
grey and reveal a portrait photo only for the row under the pointer.

## Image recipe

Photorealistic 3D render of an abstract glass or brushed-metal geometric
volume, cool blue-grey lighting, soft studio gradient background fading from
steel blue to near-white, glossy specular highlights along hard edges, shallow
camera angle emphasising one corner or fold of the object, no text or logo
baked into the render.

## Photo search

Unsplash first, Pexels second (for the team/office secondary imagery only — the
hero itself is a bespoke 3D render, not stock photography).
- "abstract glass geometric render blue"
- "corporate team portrait studio grey background"
- "office glass architecture minimal"

## Reference lock

Primary reference/direction: Hark Capital — 3D glass-render hero, flat white
institutional body, hover-reveal team roster.
Preserve (3-5 traits): one large 3D-rendered glass/metal object filling the
hero, restrained two-line headline set small against it; one grotesque
(Aeonikpro or equivalent) at every size on the page; stat numerals laid over a
crop of the hero's own material rather than a plain background; team roster as
a list of names with photo revealed only on hover.
Borrow only (1-2): the "Click to Expand" corner nav pattern; dot-prefixed
section kickers.
Role rules: the hero object is the only large-scale visual device on the page —
no second hero-scale image competes with it; body sections stay flat white with
no gradient; stat band is the only place the hero's blue-glass material recurs.
Media strategy: 3D render (bespoke, not stock) for the hero material; plain
studio portrait photography for team headshots, revealed on hover only.
Reject: photographic skyline/handshake hero imagery in place of the rendered
object; grid-of-headshots team layout; a second display typeface.
Token commitments: ink `#181818`, ground `#F3F3F3`, glass-light `#81A0B0`,
glass-mid `#5786A6`, glass-deep `#446A87`, glass-shadow `#263240`; body/display
"Aeonikpro" throughout.
