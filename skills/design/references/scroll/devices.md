# The device kit, condensed

Nine ways scroll can drive the page. Pick per beat, never per page: ≥4 device
families, never the same one twice running. Every act publishes `--sc-p` (0–1)
on itself, so bespoke CSS can ride the same value the kit devices use. Full
depth, worked examples, and every trap: `upstream/scroll-craft/.../references/devices.md`.

| # | Device | Syntax | Span / rate | One-line rule |
|---|---|---|---|---|
| 1 | `scrub` | `data-sc-act="scrub" data-sc-span="2.6" data-sc-dwell="0.35"` on the section; `data-sc-scrub data-sc-src="…"` on the `<video>` | span 2.2–3.0 for a hero | ≤2 per page. The wheel scrubs a pre-rendered clip; spend it on the open |
| 2 | `pin` | `data-sc-act="pin" data-sc-span="3"` | span ≥1.2 (below that, progress jumps 0→1 in one notch) | The frame holds, copy states cross over inside it |
| 3 | `pan` | `data-sc-act="pan" data-sc-span="3.2"`; rail gets `data-sc-pan="0.08"` | ~1vh per item + 1 | Lateral = breadth, not hierarchy. Overflow must be measured, not assumed |
| 4 | `reveal` | `data-sc-reveal="up|down|left|right|iris" data-sc-reveal-at="0.15 0.55"` | — | `clip-path` wipe = change of state. `iris` once per page at most |
| 5 | `kinetic` | `data-sc-kinetic="lines|words|chars"` on a cued heading | — | Lines almost always right, chars ~never. One kinetic headline per act |
| 6 | `parallax` | `data-sc-parallax="-0.6"` | rate is **hundreds of px total travel**, not a fraction — usable range 0.3–1.5 (framed), 1–2 (full-bleed) | Never on body copy. 3 layers is plenty |
| 7 | `count` | `data-sc-count="0 4,200" data-sc-count-at="0.1 0.5"` | 1.2–1.8s outside an act (`data-sc-count-ms`) | Only real numbers. No verified figure, no counter |
| 8 | `flow` + `in` | `data-sc-in data-sc-stagger="70"` on the wrap | stagger 30–80ms | The rest of the page. Fires once, opacity+14px rise, ~620ms ease-out |
| 9 | pointer: `tilt` / `magnet` / `spotlight` | `data-sc-tilt="7"` (5–9°), `data-sc-magnet="0.28"` (0.2–0.35, CTA only), `data-sc-spotlight` (publishes `--sc-mx`/`--sc-my`) | — | Gated to `(hover:hover) and (pointer:fine)`, off under reduced motion |

`drift` (`data-sc-drift="#0A0806"` on an act) is not a device, it's a
property: the page ground interpolates toward it while the act is live. 3–5
stops, one theme family. On a page of many *short* acts several can be
part-way through at once — paint grounds per section instead of drifting; see
upstream §10.

## The cue contract — what verification actually catches you on

`data-sc-cue="from [to [rampIn [rampOut]]]"`, all in act progress 0–1.

| Form | Behaviour |
|---|---|
| `"0.2"` | fades in at 0.2, **holds to the end of the act** |
| `"0.1 0.6"` | in, plateau, out (ramps default 30% of window each) |
| `"0 0.78 0"` | **greet**: full opacity at act start, then fades — the hero form |
| `"0 1 0 0"` | **greet and hold**: full at p=0, no ramp either end |

Five rules, each one a real bug this fixture has caught:

- **A hero cue needs the greet form.** A plain `"0 0.7"` means the first
  screen every visitor sees has no headline on it.
- **The last act's cue must hold** (one value). A two-value close cue fades
  the CTA out before the page ends.
- **Only the last act may hold.** A one-value cue on a *middle* pinned act
  stays lit through the whole un-pin slide — the line travels a full viewport
  up, crosses fixed chrome, overlaps the next section. Invisible until
  measured; shows up as a contrast failure nobody meant.
- **Ground or greet.** A pinned stage is fully visible ~1vh *before* its own
  progress leaves 0. A plain two-value first cue shows an empty stage for
  that whole travel — give the act a ground (image/colour already doing
  work) or open with a greet cue.
- **Clip time ≠ cue time.** A `scrub` clip is mapped across the stage's
  *entire visible life* (default), not across the pinned travel, because the
  stage is on screen for a viewport before the pin starts and after it ends.
  Cues keep using `p` (they belong to the pin); the clip uses a separately
  computed `vp`. Reaching for `data-sc-clip-map="travel"` reintroduces the
  freeze — there's almost no reason to.

Two more that a harness will not catch by itself:

- **Pan overflow must be measured, not assumed.** The rail travels exactly
  `scrollWidth - viewport`; a rail narrower than the viewport travels **zero**
  and the act reads as a still. `rail.scrollWidth - innerWidth` — check it,
  don't guess.
- **Parallax rate is hundreds of pixels total, not a viewport fraction** — see
  the table above. A rate of 0.35 across three viewport-heights of scroll is
  35px: invisible.

Composing an act: devices stack (a pinned stage can hold a scrub clip, a
parallax layer, a kinetic headline, a spotlight at once), but one thing is the
reason the act exists — say that thing in one sentence or the act has none.

## Never restyle the engine's classes (AB06, 2026-09-03)

Theme the engine only through its six colour tokens and two fonts. A project rule on
`.sc-stage`, `.sc-copy`, `.sc-scrim` or any other `.sc-*` class silently wins over the
engine: the console then says `[scrollcraft] act "…" will not pin: its stage computes
position:relative` and every pinned act scrolls away, leaving its spacer as dead scroll.
Read the console for `[scrollcraft]` warnings before anything else in Step 5, and run
`scripts/scroll_verify.py` — a blind one-shot cannot see either. The engine is opt-in per
grammar (scrub, pin, pan); a page that keeps the chain's own single set-piece + shared
reveal does not need it.
