# Scroll · Step 2b — Grammar, feeling curve, signature move, fingerprint

Where vendored scroll-craft (`../upstream/scroll-craft/`) plugs into `design`.
Runs between Step 2 (the gate) and Step 4 (build), only on a Persuade/
Experience surface whose brief actually asked for scroll choreography.

## The scope rule (verbatim)

> Persuade/Experience surfaces (landing, marketing, portfolio, campaign) MUST
> ship ≥4 device families, never the same device twice in a row, one
> engineered peak with the largest span, one signature move, and pass the
> fingerprint gate; Operate/Read surfaces (dashboards, admin, settings, docs)
> get NO scroll choreography (frequency rule: 100+/day = no animation) —
> state motion 150–250 ms only; ~~reduced motion removes travel, not content~~ (**utgår, F-011** — see below).

The Operate/Read half is not new: it's `../motion.md`'s existing scroll-
linked-motion ban (reveal-once only, no casual parallax, no scrub), restated in
scroll-craft's vocabulary. Nothing here overrides `../../SKILL.md` § Product
surfaces for an authenticated page.

The rule's closing clause — ~~"reduced motion removes travel"~~ — **utgår per F-011 (2026-09-07)**.
No build reads a motion preference at all, so
there is **no such path (F-011)** for the clause to describe. What it was
protecting survives on its own terms and is not a preference: **no device may
make content unreachable**. A `pan` rail's transform is the navigation, so
every item in it stays gettable, and that is confirmed on the contact sheet.
See [`devices.md`](devices.md) § Rail settle.

## Contract

**Reads** — the `design` Step 1 interview (scroll-craft's eight questions
fold in, not asked twice); [`grammars.md`](grammars.md) (pick one grammar
against the register); [`devices.md`](devices.md) (nine devices, cue
contract); [`feel-and-fingerprint.md`](feel-and-fingerprint.md) (curve, peak,
move, gate); the registry `VAULT/wiki/projects/_index/design-fingerprints.md`;
`../house-physics.md` Motion + `../motion.md` — output must clear both bars.

**Does** — names the grammar and states why the other seven lost; writes the
feeling curve (emotion → cause per act) and names the peak; invents one
signature move, bespoke and coded in the page, never a kit parameter tweak;
scores the journey into a device table (≥4 families, never twice running, ≤2
`scrub`); runs the fingerprint gate against every existing registry row (≥4
of 6 dimensions clear, per row).

**Writes** — `BRIEF.md` additions (feeling curve, peak sentence,
tell-someone sentence, signature move); the score table (beat → device →
why); one new registry row, appended after ship.

**Human checks** — the fingerprint result is shown, not asserted (≥4-of-6
printed against every row, not "it passed"); the feel check
([`feel-and-fingerprint.md`](feel-and-fingerprint.md) § Peak: scroll cold,
one word per act, diff against the intended curve before opening `BRIEF.md`);
the verification JSON pasted, not summarized (`scroll_verify.py`, generic, or
scroll-craft's own `shoot.mjs` on the real engine); a human reads the contact
sheet — no automated pass above substitutes for that.

### What the harness cannot tell you

Upstream `verify.md` § What the harness cannot tell you names three, and they
are *"the ones that matter most"*. Read the sheet for them; a green run says
nothing about any of the three.

- **Whether the motion is smooth.** *"Contiguous frames prove the clip
  advances; they do not prove it advances evenly."* Watch the contact sheet
  for a move that lurches, reverses, or stalls in the middle. This is the
  sentence that explains F-012: every mechanical check passed while the page
  looked cheap. The chain's answer is not to trust the sheet either — it is
  `motion_probe.py` plus a cold human scroll; see
  [`../motion-smoothness.md`](../motion-smoothness.md) and [`pace.md`](pace.md).
- **Whether the composition is any good.** Copy landing on the busiest part of
  the frame, a subject cropped at an unfortunate point, an act whose end frame
  is a dark empty corner.
- **Whether the page means anything.** *"Six acts that each work and together
  say nothing is the most expensive failure available here."*

Two more the harness structurally cannot reach: **pan overflow** (a rail
narrower than the viewport travels zero and reports `no dead scroll detected`
on every pass — measure `rail.scrollWidth - innerWidth` by hand), and **the
phone**, which is a different machine. Headless Chrome cannot reproduce an
iPhone's video decoder, autoplay policy, Low Power Mode or touch scrolling: on
one upstream build every probe reported the hero clip scrubbing perfectly for
**four consecutive rounds while the real phone showed a frozen frame**.

### The spacer is sized once, at mount

Worth knowing before blaming the motion for anything, and a live candidate
whenever a build is judged inside an embedded preview panel rather than a real
tab. In worldflight mode the engine writes the spacer height as
`(total + 1) * innerHeight` **once**, inside mount. If `innerHeight` reports 0
at that moment the spacer is set to **0 px**, the page has no scroll track,
and the flight never advances.

> *"It fails silently and it looks like success."* The engine mounted, every
> leg registered, the clips fetched and decoded, and there is nothing in the
> console. The page is simply a still image that cannot be scrolled. Embedded
> preview panes and some early loads do exactly this.

**Do not fix it in the engine** (`NOTE.md`: the engine is never edited). One
resize makes it re-measure correctly, so the *page* sends one once the window
and the fonts have settled:

```js
function relayout() { dispatchEvent(new Event('resize')); }
addEventListener('load', relayout);
if (document.fonts && document.fonts.ready) document.fonts.ready.then(relayout);
```

The `fonts.ready` half earns its place independently: a webfont swapping in
changes the measured height of every copy block, so anything sized against
those blocks is wrong until it re-measures.

Check it in one line, **before** blaming anything else:

```js
document.documentElement.scrollHeight   // ≈ (sum of weights + 1) * innerHeight
```

## Files here

- [`grammars.md`](grammars.md) — the eight grammars + register fit matrix.
- [`devices.md`](devices.md) — the nine devices + the cue contract's gotchas.
- [`feel-and-fingerprint.md`](feel-and-fingerprint.md) — curve, peak,
  tell-someone test, signature move, fingerprint gate, registry format,
  embodiment, act-page pacing.
- [`showcase-floor.md`](showcase-floor.md) — the level the GSAP/Lenis showcases set:
  seven rules, intro patterns, transition causes, measured stack.
- [`journeys/era-residence.md`](journeys/era-residence.md) — the worked journey (rank #1 in
  the catalogue): acts, mechanisms, the eight properties that make it a trip, a rebuild recipe
  on the house toolchain, and the variation slots that keep the next page from being Era.
- [`toolchain.md`](toolchain.md) — how GSAP + Lenis are linked, imported and verified here.
- [`pace.md`](pace.md) — the third "not smooth" fault: uneven rate, the
  0.21–0.22 vh/s floor, worldflight's `data-sc-lerp` 0.12 / `data-sc-seam` 0.16.
- Full upstream source for anything condensed here:
  `../upstream/scroll-craft/plugins/nateherk-design/skills/scroll-craft/`.
- Engine + starting template (copy per project, never edit it):
  `../../scripts/scroll/` — `scrollcraft.js`, `.css`, `template.html`, `NOTE.md`.
- Generic verification harness: `../../scripts/scroll_verify.py`.

**Engine is opt-in per grammar (AB06).** Use the vendored engine only when the chosen grammar needs scrub, pin or pan acts, and never in a blind one-shot: build, read the console for `[scrollcraft]` warnings, run `scroll_verify.py`, fix, repeat. Otherwise the chain's own signature set-piece + shared reveal (house-physics) is the default.

## Cited, not condensed

Read these upstream files directly when the build reaches them. Nothing below
is summarised anywhere in the chain, and each is the only place its content
exists.

| Upstream file | Read it for |
|---|---|
| `references/worldflight.md` | The markup, the scroll track and spacer maths, the **one-sided seam**, the copy contract (**windows ≤ 4 vh**), the route rail and `sc:waypoint`, and the **seam law for assets** (a leg's last frame and the next leg's first frame must match, GOP boundaries included). §§ 7b and 7c are condensed here and in [`pace.md`](pace.md); the rest is not |
| `scripts/worldflight-assert.mjs` | **The only automatic lerp-convergence and non-overshoot check in the whole corpus.** Nothing in `scroll_verify.py` or `motion_probe.py` does what it does; if a flight is being built, run it |
| `references/device-diag.html` | A standalone real-device scrub diagnostic: the suspect clip loaded two ways beside a known-good clip, MOVING / FROZEN verdict per pane, prime results and distinct-frame counts on screen. Edit its `TESTS` array and deploy it beside the site on the **first** mobile report |
| `references/verify.md` § The phone is a different machine | The iOS clip lifecycle: metadata priming, `touchend` (not `touchstart`) as the activation event, the 2 s prime-flag release, re-issuing a seek stuck past 700 ms, the 2.5 s poster-reveal timeout. All engine-side and already handled — read it to know what a frozen phone clip is *not* |
| `references/worlds.md` | The eight world preambles: what a scene is made of before any device touches it |
| `EXAMPLES.md` | Twelve filled fingerprint rows with the numbers inline. The `orrery` row is the worked example of the pace bar: ten legs, every 5 s leg at 1.08 vh and the 10 s peak at 2.25, **0.212–0.225 vh/s everywhere**, `data-sc-seam` 0.16, `data-sc-lerp` 0.12, measured spread 6% down from 36%. Treat the rows as illustration — they are someone else's builds and constrain nothing here |
| `CHANGELOG.md` | Three entries are load-bearing rules rather than history — inlined below |

**Three changelog findings, as rules:**

- **Orrery pacing** (2026-08-22). Leg weights of 0.70–0.95 vh for identical
  5-second clips: a **36% spread** in how fast the world moved per pixel, and
  the owner's word for it was "not smooth". Nothing in the skill said to hold
  `weight / clip_seconds` constant, so nothing caught it. Full rule and the
  numbers: [`pace.md`](pace.md).
- **Layered scenes** (2026-09-01). Four rounds of fixes on a live rebuild
  became six rules: planes solid below their silhouette, a shaped foreground
  so the product's button survives the scroll, a faded section floor over the
  clip line, `max-width: none` on planes, **no transform transition on a
  parallaxed element**, and a new filename for replaced art.
  [`devices.md`](devices.md) § Layered scenes.
- **The scrim `::before` bug** (2026-08-22). `shoot.mjs` hides
  `[data-sc-copy],[data-sc-copy] *` to photograph the film under a line, and
  `visibility: hidden` takes an element's `::before` with it. **A per-block
  scrim written as `.copy::before` is therefore never composited into the
  measurement**: six blocks reported 1.2–1.9:1 against means of 7–13:1, and
  *"strengthening the scrim changed the reported numbers by exactly zero,
  which is the tell."* The identical-numbers-after-a-real-change signature is
  worth knowing on its own. **Fix: the scrim is a sibling of the copy block**,
  never its pseudo-element — mount one soft plate per block into the copy
  layer and drive its opacity from the block's own inline opacity, so it
  tracks the engine's window for free.
