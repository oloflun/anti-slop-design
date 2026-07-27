#!/usr/bin/env python
"""UserPromptSubmit — detect design intent and inject the gate order.

Deliberately a SIBLING of carl-hook.py rather than an edit to it. Claude Code
runs every hook registered for an event, so this achieves the same injection
with zero regression risk to a 921-line file that carries the user's whole
CARL setup.

What it adds that CARL's static DESIGN rules cannot: the *current project's*
state — which tier is in force and what the locked tokens actually are. That
turns "derive from the brand" from advice into a specific instruction naming
specific values.

Turn-boundary injection is the weakest link in the chain by design; the
per-edit hooks are what actually hold across a long session. This exists so
the gate order is in context before the first edit, not to carry the session.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

try:
    import design_hook_lib as L
except Exception:
    sys.exit(0)


# Multilingual. Swedish included because the user works in it.
INTENT = re.compile(
    r"\b("
    r"design|designa|redesign|omdesign|g(ö|o)r om|"
    r"ui|ux|frontend|front-end|"
    r"landing\s*page|landningssida|hero|cta|bento|pricing\s*page|"
    r"styl|style|styling|css|tailwind|"
    r"layout|typograf|typograph|font|palette|palett|f(ä|a)rg|colou?r|"
    r"animation|animera|animate|motion|transition|"
    r"polish|polera|premium|premiumk(ä|a)nsla|"
    r"komponent|component|nav|header|footer|modal|drawer|carousel|karusell|"
    r"mockup|wireframe|skiss|"
    r"bygg en sida|build a (page|site|landing)|make it look"
    r")\b",
    re.I,
)


def main() -> None:
    if L.disabled():
        return
    event = L.read_event()

    prompt = (event.get("prompt") or event.get("userInput")
              or event.get("message") or event.get("input") or "")
    if not prompt or not INTENT.search(prompt):
        return

    root = L.project_root(event)
    if not L.once_per_session(root, "design-gate-order"):
        return

    lines = ["<design-gate>",
             "Design intent detected. Load Skill(design) before any UI decision.",
             ""]

    dm = L.design_md(root)
    if dm:
        tokens = L.design_tokens(root)
        lines.append(f"TIER 0 — LOCKED. {dm.name} exists at the project root.")
        lines.append("Inherit the system. Do not re-derive, do not invent, do not "
                     "rotate a theme. Pages SHARE the system.")
        if tokens.get("colors"):
            lines.append("  colors: " + ", ".join(
                f"{k}={v}" for k, v in list(tokens["colors"].items())[:10]))
        if tokens.get("fonts"):
            lines.append("  fonts : " + ", ".join(tokens["fonts"][:5]))
        if tokens.get("radii"):
            lines.append("  radii : " + ", ".join(tokens["radii"][:8]))
        lines.append("Every colour and face in your output references one of these.")
    else:
        lines.append("No DESIGN.md — run the gate before picking anything:")
        lines.append("  Tier 1 DERIVE   logo/wordmark, brand hex, deployed site, "
                     "tailwind colours, favicon → derive from that evidence")
        lines.append("  Tier 2 REFERENCE a URL or screenshot was given → study it, "
                     "borrow principle not pixel")
        lines.append("  Tier 3 INVENT    genuinely nothing, or the user said "
                     "'wing it' → only then invent or reach for a theme")
        lines.append("First tier with evidence wins. Say which tier you are in "
                     "before picking a token.")

    lines.append("")
    lines.append("NEVER let minimalist-ui, industrial-brutalist-ui, or "
                 "high-end-visual-design set direction — each hardcodes a full "
                 "palette. Gate 60 denies their hex values in a locked project.")
    lines.append("</design-gate>")

    L.log(root, event="intent", tier=L.tier(root), detail="gate order injected")
    L.emit("UserPromptSubmit", "\n".join(lines))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
