---
name: designlang-tokens
description: Use when styling UI for aarke.com — references the extracted design system tokens instead of inventing colors, spacing, or typography.
---

# designlang tokens
Source: https://aarke.com
Extracted by designlang v7.0.0 on 2026-09-03T23:25:21.347Z

## Semantic tokens (use these)
- color.action.primary: #000000
- color.surface.default: #ffffff
- color.text.body: #000000
- radius.control: 12px
- typography.body.fontFamily: Body Font

## Regions
- content
- content
- content
- pricing
- content
- content
- content
- testimonials
- content
- features
- nav
- testimonials
- footer
- content
- content

## How to use
- Prefer `semantic.*` tokens over `primitive.*`.
- Never invent new tokens or hex values; reuse the ones above.
- When a value is missing, pick the closest existing semantic token and flag the gap.
- Reference tokens by their dotted path (e.g. `semantic.color.action.primary`).
