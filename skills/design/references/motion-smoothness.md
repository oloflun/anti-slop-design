# Motion smoothness — why a page that renders correctly can still look cheap

Anton, r7 (FEEDBACK.md F-012): *"scrolleffekten renderade som den skulle, men det såg
hackigt och billigt gjort ut."* The measured answer is F-013. Read this before writing
any scroll-driven motion, and read it again before "fixing" motion that someone has
called janky — because **two different faults produce that same sentence**, and the cure
for one does nothing for the other.

## The two faults

| | The value steps | The page drops frames |
|---|---|---|
| What you see | Motion advances in visible notches | Motion stutters and lags the hand |
| What the clock says | 60 fps, nothing wrong | frame p95 well over 20 ms |
| Where it comes from | A raw scroll value written 1:1 | Too much work per frame |
| What fixes it | Damp the value (`--sc-ps`) | Cut the work (`performance.md`) |

Measure both before changing anything: `scripts/motion_probe.py` reports frame time and
value continuity in one run. Guessing which fault you have is how a session spends an
afternoon smoothing something that was never stepping.

## Fault 1 — the raw value

`scrollcraft.js` damps exactly two things: the video playhead (lerp 0.18, deadband,
seek coalescing) and the pointer devices `tilt` / `magnet`. Its own docstring explains
why: *"wheel events do not arrive at a constant rate and a 1:1 write reproduces every
gap in them."*

That reasoning is right, and the engine does not apply it to `--sc-p`. Everything
`read()` writes — `--sc-p` itself, cue opacity, parallax, pan, kinetic units,
`clip-path`, drift — is written 1:1 from raw scroll position, on the scroll event
behind a one-frame rAF guard. On a mouse wheel the value stands still between notches
and then jumps.

Two things make it worse:

- **`--sc-p` is an unregistered custom property.** To CSS it is a string, so it never
  interpolates, and no `@property` registration exists anywhere in the engine.
- **`scrollcraft.css` sets `transition: none`** on `[data-sc-cue]` and `[data-sc-copy]`
  once `.sc-ready` lands. That is deliberate — JS owns the value — but it means nothing
  bridges the gap between two writes.

**F-011 did not cause this.** `var reduce = false` turned the playhead lerp *on*
(rate 1.0 → 0.18). `reduce` gates ten sites in the engine and every one is a disable
branch. The stepping is architectural and predates the override.

### The rule

> **Bespoke motion reads `--sc-ps`, never raw `--sc-p`, whenever it drives something the
> eye sees move** — `transform`, `object-position`, `clip-path`, `mask-position`,
> `background-position`. Cue opacity may read `--sc-p`.

`--sc-ps` is published by `scripts/scroll/sc-smooth.js`, copied in beside the engine and
loaded after it. The engine is never edited (`scroll/NOTE.md`: copy, never edit). The
shim lerps at 0.16 per frame with a 0.0005 deadband, registers `--sc-ps` as a real
`<number>` so CSS can interpolate it, stops its own rAF loop when nothing is moving, and
sets `will-change` **only while an act is actually in motion** — correcting the engine
CSS's seven class-level promotions, which `motion.md` § Bans forbids.

A page's own rAF painters (`paintHeroPool`, `paintMotion`, a word scrub) read `--sc-ps`
too. `?preview=` modes set `window.__scFreezeMotion = true`, and the shim then tracks the
raw value exactly so a screenshot shows the formed state, not a lerp in flight.

Measured, same motion, same wheel cadence (`tests/motion/`):

| | frame p95 | staircase | largest single-frame step |
|---|---|---|---|
| `staircase.html` (raw `--sc-p` → `rotateY`) | 16.7 ms | 18 | 5.6 % |
| `smooth.html` (lerped) | 16.7 ms | **0** | **1.4 %** |

The frame clock is identical in both. The difference is entirely in the value.

## Fault 2 — the page is genuinely slow

Damping a value on a page that cannot hold 60 fps just makes a smooth curve arrive late.
V3b, measured 2026-09-08 with no CPU throttling at all: frame p95 49.9 ms, 62 frames over
33 ms, 4.9 MB transferred, 19 font files, 17 long tasks during scroll, four elements with
a resting `will-change`. See `performance.md` for the budget and `scripts/perf_probe.py`
for the measurement.

## Pace — the third thing people call "not smooth"

From upstream scroll-craft's `worldflight.md` § 7c, the only place in the corpus where
someone diagnosed the complaint to root cause: *"Two separate faults get described as
'it doesn't feel smooth', and only one of them is smoothing."*

- **Inconsistent pace is the worse one.** Across a multi-act or multi-leg sequence,
  `rate = weight / seconds` must hold within a few percent. On the `orrery` build it
  varied 36 % across ten legs and the owner's word for it was "not smooth"; evened to
  6 %, the same footage read as one continuous move.
- **Too fast reads as cheap.** For a fly-through, 0.21–0.22 vh per second of film is the
  floor. The per-8-seconds guardrail is a dead-scroll floor, not a taste target.
- **Damping and weights fix different halves.** *"The damping is what removes wheel
  judder; the weights are what remove the surging."* For a worldflight use
  `data-sc-lerp` **0.12**, not the 0.18 default, and widen `data-sc-seam` to ~0.16.

`motion_probe.py` reports `max_step` per act, so an act that surges relative to its
neighbours shows up as a spread across runs rather than as a feeling. Full port, with
the weight arithmetic and the worldflight knob values: [`scroll/pace.md`](scroll/pace.md).

## The bar

A signature act is not finished until, at 4× CPU throttling:

- `staircase = 0`
- `max_step ≤ 3 %` of the value's own range **on the damped playhead `--sc-ps`**; on a
  derived track (`transform`, `clip-path`, …) it is reported, not gated — a smoothstepped
  value peaks at ~4.4 % per frame by its own derivative, and `staircase` is the number
  that catches a step there (r8 R2: V3c's flip at 4.12 %, staircase 0, was correct)
- frame p95 ≤ 20 ms, zero frames over 33 ms
- both scroll directions measured, not just downward
- measured in a quiet window: run `tests/motion/smooth.html` first as a control; if the
  control shows any frame over 33 ms, the host is busy and the page's numbers are noise

## What the harness still cannot tell you

Upstream's `verify.md` says it plainly: *"Whether the motion is smooth. Contiguous frames
prove the clip advances; they do not prove it advances evenly."* `motion_probe.py` closes
most of that gap and does not close all of it. Watch the contact sheet for a move that
lurches, reverses, or stalls in the middle, and watch the sparkline the probe writes: a
curve with a flat shoulder is an act that stops dead mid-travel, which no single number
reports.

One known, accepted inconsistency: `scripts/scroll/scrollcraft.css` line 98 still carries
`@media (prefers-reduced-motion: reduce) { html { scroll-behavior: auto } }`. It only
disables smooth anchor jumping and touches no act, and the engine is never edited, so it
stays — documented here rather than silently tolerated.

## Related

[`scroll/devices.md`](scroll/devices.md) · [`scroll/pace.md`](scroll/pace.md) ·
[`performance.md`](performance.md) ·
[`motion.md`](motion.md) · `scripts/motion_probe.py` · `scripts/scroll/sc-smooth.js` ·
FEEDBACK.md F-011, F-012, F-013.
