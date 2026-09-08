# Generated material — Higgsfield first, measured, and never on the page's behalf

The chain generates **material**, never design. A card flip, a drawing that draws itself,
a divider that tips: those are CSS and scroll code, and no model produces them. What a
model produces is the stuff motion acts on — a cinematic still, a camera move that will
be scrubbed, a drawn system, a texture.

This file owns the route, the credit gate, the fallback ladder, who may generate, and
what has to be true before anything is vendored.

One correction it carries: `assets.md` § Generated illustration used to say *"No
animation. None of these models output multi-frame."* That is no longer true for this
vault. Kling 3.0, Seedance and Minimax are one MCP call away.

## 1 · Where it sits in Step 5b

Sources, in preference order:

1. The product's own surface, screenshotted.
2. Real photography — the contact-sheet pipeline.
3. **Generated material**, when no sourced image can carry the picture the register needs
   *and* the brief names what is to be generated.
4. A bespoke drawn identity system.
5. Curated component sources, for tech surfaces.

Generation is third, not first. A sourced photograph that holds beats a generated one,
and in a drawn register (zero photography, an identity built from line) a drawn system
beats both. "We could generate it" is not a reason; "nothing sourced can be this" is.

## 2 · Route

Run `models_explore` (`action: "recommend"`, with the goal and the input kind) before the
first call of every run. The catalogue moves, and the CLI and MCP front ends do not even
use the same model ids. The table below is the starting point, measured in r7.

Measured against the live catalogue 2026-09-08, with `get_cost` preflights (no jobs
queued). **The catalogue had already moved since r7**, which is the whole reason the
`models_explore` call is mandatory rather than advisory: `kling3_0` is now
`kling3_0_turbo` and takes a **start frame only** — the model r7 used for a locked-both-
ends clip no longer offers that role.

| Need | Model | Cost | Notes |
|---|---|---|---|
| Hero/plate still, 2K, image-to-image off a real photo | `nano_banana_pro` | **2 cr** | `image_references` role; 1k/2k/4k; 21:9 available |
| Same, cheaper, still photoreal | `nano_banana_2` / `nano_banana` | — | Both carry `supports_unlim` |
| Cinematic still, up to 4K | `cinematic_studio_2_5` | — | `image` role, not `image_references` |
| **Scrub clip, start AND end frame locked** | **`minimax_h3_max`** | **25 cr / 10 s** | Roles `start_image` + `end_image`; 5–15 s; 480p/768p; 21:9 |
| Same, longer or with audio | `flux_3_video` | — | 5–20 s, 1080p, start+end, audio (turn it off) |
| Clip from a start frame only | `kling3_0_turbo` | — | No `end_image` role — do not use where the end state matters |
| Drawn / vector system, wordmarks, line figures | Recraft V4.1 | — | The only model with production-grade SVG out |
| Seamless texture (drafting paper, grain, weave) | `gpt_image_2` via the tiling procedure | — | Verified by a seam ratio near 1.0 |
| Copy motion from a driving video | `hf_mult_motion_control` | — | Genjutsu; not the legacy `motion_control` |
| Replace an object in a video | `hf_mult_replace_object` | — | Genjutsu |

A 10-second locked-both-ends clip therefore costs **25 credits**, not the 17.5 r7 paid.
Budget from the preflight, never from this table.

### Shape rules for a clip that will be scrubbed

- **One continuous move, one direction, slower than feels right.** No cuts. The subject
  never leaves frame; nothing enters or exits.
- **Start state ≠ end state.** The first frame is the establishing shot, the last is the
  closing state. If they are the same picture the scrub has no payoff.
- **Pass the start image in the model's generic image-reference role, not a start-frame
  role**, or the clip opens frozen. r7 hit the same failure class at the other end: the
  last three seconds stood still.
- In a multi-leg clip, the next leg's start frame is the **actual decoded last frame** of
  the previous leg, extracted with a reverse filter — never a separately imagined
  "destination" still. Position continuity comes from the exact-frame handoff; velocity
  continuity comes from matching direction and speed on both sides.
- Dark, low-detail regions where copy will sit. Keep the subject away from the far edges,
  because a full-viewport clip is shown with `cover`.
- Cut phone clips portrait. A landscape clip in a portrait viewport decodes the whole
  frame and throws three quarters away — soft and stuttering on the phone, smooth on the
  desktop.
- Encode with a dense GOP before vendoring — see [`assets.md`](assets.md) § Encoding. A
  normal web encode plays perfectly and scrubs like mud.
- `count: 2–4` is for genuine variants of the *same* prompt and inputs. Every separate
  concept, emotion or camera take gets its own call.

## 3 · The credit gate

1. **A ceiling is written in `BRIEF.md` before anything is queued** (`generation budget: N
   credits`). r7 ran to 35, and Anton raised it to 36.5 with an explicit "Ja, kör pro".
2. **Read `balance` first.** If the balance is under twice the ceiling, report and ask
   before the first job.
3. **`get_cost: true` on every job before running it.** No generation without the cost
   having been read. This is why r7's log reconciles.
4. **Omit `use_unlim`** so the server may return `unlim_choice`; if a free allowance
   covers the model, put the question to Anton before spending credits. Never set
   `use_unlim: true` on your own initiative.
5. **Log every call** in `runs/<cell>/higgsfield/LOG.md`: step, model, inputs with media
   ids, cost, and your own reading of the frames. The log is the evidence, not memory.
6. **The ceiling is never passed quietly.** Reaching it means stopping, saying what
   remains and what it would cost, and continuing down the fallback ladder meanwhile.

## 4 · Fallback ladder

1. **Higgsfield** — first choice for everything generated.
2. **If credits are short: ChatGPT / Codex image generation**, per
   `impeccable/reference/codex.md` (`image_gen`, four stop points, palette before mocks).
   Codex produces **no video**; for moving material there is no ChatGPT fallback.
3. **Only then, no generation**: real photography, a drawn SVG system, or CSS art — and
   if the act needed a clip, the *device* changes rather than the quality. A `reveal` or
   `pin` built on real stills replaces a `scrub`. Shipping an empty plate because the clip
   would not generate is not an outcome.

The ladder is entered only for missing credits or an unavailable service — never because
it is faster, and never silently: the substitution gets a row in the decision ledger with
its reason.

## 5 · Who may generate

**The orchestrator, never the builder.** Builders run headless and inherit the account
connector, so the restriction is mechanical: `run.py` puts a `--disallowed-tools` pattern
for the Higgsfield tools on the builder argv, and the builder prompt says the material is
already vendored under `runs/<cell>/assets/` with `credits.json`. A builder that tries
anyway shows up in the ledger as a denied tool call.

The architect specifies material as an **asset lock**, never as a prompt:

```
Asset role:    hero plate / texture / illustration / cutout
Slot:          dimensions, aspect ratio, where on the page
Art direction: subject, palette from the lock, light, rendering, crop
Avoid:         wrong palette, text in image, people, symmetric composition,
               mesh gradient, stock-lighting
```

The lock's `Art direction` becomes the prompt and `Avoid` becomes its constraints. A
generated object with no asset lock does not get queued.

## 6 · Before anything is vendored

r7's first clip carried a hallucinated banner with unreadable characters at t=4–6 and
froze for its last three seconds. Neither is visible without looking at the frames.

1. **Contact sheet** of ten evenly spaced frames, and read every one as an image. Check
   for: hallucinated text or signage, hands and faces (never on an Alunix page), objects
   entering or leaving, motion that stops, a camera that changes direction.
2. **Track the subject** when the act depends on something staying in frame: plot its
   position across the frames and confirm it moves monotonically.
3. **Never ship a mock crop as an asset**, and never raw output: post-process per
   `assets.md` — grain, an asymmetric crop, a grade.
4. **Provenance**: a row per generated object in `credits.json` (model, prompt, media/job
   id, cost, date), a `generated: <model> · post-processed` stamp in the section comment,
   and a visible credit line where the page itself refers to the material.
5. **Encode** before the file enters `assets/`.

## 7 · Measured like every other call

`hooks/design-vision-track.py` logs Higgsfield MCP calls as `kind: generation`;
`design-gate.py` denies a `generate_*` without a budget line and a preceding `get_cost`;
`design-stop.py` reports jobs, summed cost and models, and reconciles against
`credits.json`. A generation that does not appear in the ledger is a defect, not a
convenience.

## 8 · Never

- **`sync_agents`.** It uploads Anton's own skills and a synthesised personality file to
  Higgsfield's marketplace. It installs nothing. It is not a chain step; if Anton wants
  it, it is his command.
- **`website-builder-flow`** and the game flow. They build React 19 + TanStack Start on
  Cloudflare Workers and instruct the agent to stop consulting other design guidance. The
  chain ships single-file HTML and does not deploy.
- Faces or people on an Alunix page.
- Generated UI, generated screenshots of a product, generated logos of "customers" — the
  same rule as gate 46 and gate 47, with a generator attached.
- A generated image shipped raw.
- Marketplace-style claim panels (`pain_points`, `efficacy`, `endorsement`). They are
  fabricated marketing with a rendering step in front.

## Related

[`upstream/higgsfield/scroll-scrub.md`](upstream/higgsfield/scroll-scrub.md) (the scrub production spec: start/end states, seam handoff, byte budgets, blob-seek playback) · [`upstream/higgsfield/scroll-scrub-asset-video.md`](upstream/higgsfield/scroll-scrub-asset-video.md) (the ffmpeg recipes) · [`upstream/higgsfield/game-textures.md`](upstream/higgsfield/game-textures.md) (seamless tiling, verified by seam ratio) ·
[`assets.md`](assets.md) · [`performance.md`](performance.md) ·
[`reference-lock.md`](reference-lock.md) · [`scroll/devices.md`](scroll/devices.md) ·
`impeccable/reference/codex.md` · FEEDBACK.md F-009.
