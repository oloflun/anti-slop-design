# The Router, in plain English

The skill is [`skills/design/SKILL.md`](skills/design/SKILL.md). This page is the version you read first.

## The one rule

> **Brand derives direction. Skills supply craft. Themes are the last resort.**

Every failure this repo was built to fix came from inverting that: a specialist skill set the visual direction, and the brand got repainted in the skill author's palette.

## What changed, and why

The first version was a 161-line table of contents. It named skills to load and hoped the model loaded them. Three things were wrong with it.

**It didn't fire.** Guidance arrived at *turn* boundaries — once, at the start of a prompt. Design decisions happen at *edit* boundaries. Across one long build turn the agent writes twelve components over sixty tool calls, and nothing re-asserted anything. It worked at the top of a session and drifted after.

**It was a pointer, not a procedure.** Six hops from "user asks for a page" to any actual taste content, each hop a chance to skip. And because the front door carried no method, the model improvised one.

**The specialists it routed to force their own house style.** Verified by reading them:

| Skill | Hardcoded |
|---|---|
| `minimalist-ui` | Notion's palette verbatim — `#F7F6F3`, `#EAEAEA`, `#787774`, `border: 1px solid #EAEAEA` mandated |
| `industrial-brutalist-ui` | `#F4F4F0` ground, `#E61919` as "the ONLY accent color" |
| `high-end-visual-design` | Three fixed archetypes with fixed hex |

Routing to those *as direction-setters* is how a brand became beige, or hazard-red, or OLED-black, regardless of what the brand actually was.

## How it works now

### The gate

First tier with evidence wins. Lower tiers never run.

| Tier | Condition | Action | Invention |
|---|---|---|---|
| **0 · Locked** | `DESIGN.md` exists | Inherit. Pages share the system. | None |
| **1 · Derive** | Logo, brand hex, deployed site, tailwind colours, favicon | Derive the language from that evidence | Extension only |
| **2 · Reference** | A URL or screenshot was given | Study it. Borrow principle, never pixel | Recomposition |
| **3 · Invent** | Genuinely nothing, or "wing it" | Invent a named world. Themes live here | Full |

Tier 1 is the piece no upstream has as a gate, and it is the whole point. HAAJP is the reference case: `#F27722` + Afacad uppercase + black surfaces + an asymmetric rhombus derives from the mark and the product. No catalogue produces that.

**Inheritance is binding.** A section, component, feature, or state inside an established surface inherits it. A local addition never re-runs the gate and never starts a second identity.

### The hooks

Enforcement moved from turn boundaries to edit boundaries.

```
UserPromptSubmit    design-intent.py        gate order + this project's locked tokens
PreToolUse  write   design-gate.py          DENY contract violations before they land
PreToolUse  browser design-verify-gate.py   inspection discipline before the first look
PostToolUse write   design-route.py         name the right skill for what was just written
PostToolUse Skill   design-telemetry.py     attribute every skill call to its component
Stop                design-stop.py          deep detector pass + the session report
```

`design-route.py` fires after **every** UI file write and emits one line:

```
[design · Drawer] tier 0 — inherit the locked system, do not re-derive
→ emil-design-eng (interactive component or gesture)
→ copy gate (user-facing strings) — copywriting, then humanizer
```

### The telemetry

Without it there is no way to tell whether the router worked or whether a good result was luck. Every session writes `.impeccable/design-session.jsonl` and ends with a report:

1. **Component → skills, in order** — did the right skill fire on the right component
2. **Route-vs-invocation gap** — the router named a skill and nothing loaded it. **This must be zero.** It is the direct measurement of the original failure
3. Coverage · 4. Gate activity · 5. Trap firings · 6. Deep detector · 7. Timeline

A build that looks right but ships an empty or gap-heavy ledger has not passed.

## What it composes

The router invents no visual rules. It sequences other people's work — see [`attribution/UPSTREAMS.md`](attribution/UPSTREAMS.md).

- **[impeccable v4](https://github.com/pbakaus/impeccable)** is the engine. Its rule governs everything: *"The brief wins. Redirecting a clear brief toward your taste is failure."* Its detector supplies 68 deterministic rules, four of which check the build against `DESIGN.md` directly.
- **[Hallmark](https://github.com/Nutlope/hallmark)** supplies the front door's spine and all 105 reference files, ported byte-identical. Its 20-theme catalog is kept in full but demoted to Tier 3.
- **Anthropic's Claude Design prompt** supplies the Tier 1 derivation procedure, the Tier 3 invention guidance, the process and scope rules, and the options and wireframe formats.
- **[copywriting](https://github.com/coreyhaines31/marketingskills)** → **[humanizer](https://github.com/blader/humanizer)** gate every user-facing string, in every language.

## Install

```bash
cp -r skills/design skills/design-verify skills/brand-system ~/.agents/skills/
python verify-design-system.py
```

Hooks live in `~/.claude/hooks/` and are wired in `~/.claude/settings.json`.

Kill switch: `DESIGN_HOOKS_DISABLED=1`. Promote the gate from advisory to blocking: `DESIGN_GATE_BLOCKING=1`.

## Use

Type a design brief. The intent hook fires, the gate order lands in context, and the router runs. No prefix needed, in any language.

For a whole identity rather than one surface, `brand-system` builds the folder and emits it as a reusable `{brand}-design` skill.

## What this is NOT

Still a router. It writes no visual rules of its own. The taste comes from the upstreams; this repo decides which one applies, in what order, and enforces that they do not overwrite the brand on the way through.
