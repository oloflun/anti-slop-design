# Accessibility audit report -- skeleton

Fill every section. An empty section is a stated `Not reviewed`, never an omission.

---

```markdown
# Accessibility Audit: [target]

**Audited:** [URL / files / screenshot set] . [date]
**Scope:** [what was covered -- one flow, one screen, the whole surface]
**Register / lane:** [the one-sentence lane from the design brief, if any]

## Coverage

| Pass | Evidence inspected | Result |
| --- | --- | --- |
| 0 Scope | -- | [verified vs. inferred, stated plainly] |
| 1 Mechanical | a11y_scan / tab_walk / reflow / contrast -- [ran / not run, and why] | [N violations / Clear] |
| 2 POUR | [what was checked] | [N findings / Clear] |
| 3 Cognitive (COGA) | [flows walked] | [N findings / Clear] |
| 4 Content | [pages/strings reviewed] | [N findings / Clear] |
| 5 Adaptive | [preferences tested] | [N findings / Clear] |
| 6 Interaction | [keyboard/pointer/gesture paths walked] | [N findings / Clear] |
| 7 Personas | [4-6 personas, tasks walked] | [barrier matrix below] |

`Clear` means inspected with no actionable finding. `Not reviewed` must say why (no browser, no source, out of scope).

## Summary

[2-3 sentences: overall accessibility posture, the worst finding, the verdict.]

## Findings

| Severity | Location | Before | After | Why | WCAG | Who |
| --- | --- | --- | --- | --- | --- | --- |
| HIGH | `path/to/file:line` or `[selector]` | current implementation | actionable replacement | violated principle + user impact | SC number | affected persona(s) |

One row per root cause. List every location a systemic finding reaches in the same row. Order by severity, then by reach. Escalation-trigger findings are `HIGH` regardless of surface size -- mark them `[escalation trigger]` in the Why cell.

With nothing to report: state "No actionable accessibility findings" and still show the coverage table.

## Persona walkthrough

| Persona | Condition type | Key task | Result | Barrier (if any) |
| --- | --- | --- | --- | --- |
| [name] | permanent / temporary / situational | [task from brief] | works / friction / workaround / fails | [specific blocker] |

## What works well

- [genuine strengths -- the audit is not only a problem list]

## Legal map

| Framework | Status | Notes |
| --- | --- | --- |
| WCAG 2.2 AA | [conformant / gaps: list SC numbers] | |
| EAA / EN 301 549 | [in scope? conformant?] | Aligned with WCAG 2.1 AA plus additional software/hardware requirements |
| ADA (US) | [risk noted?] | Case law references WCAG 2.1 AA |
| Section 508 (US gov) | [applicable?] | References WCAG 2.0 AA |

## SEO-relevant findings

[List findings tagged in the Findings table that also affect crawlability: headings, alt text, `lang`, link text, reflow. Or state "None."]

## Deferred to accessibility debt

[Items not fixed in this round, appended to `.impeccable/a11y-debt.md` in the audited project. List issue, severity, WCAG criterion, deadline, and confirmation the user acknowledged accepting the debt -- or note it's pending acknowledgement.]

## Verdict

`Block` -- one or more HIGH findings remain, do not ship until fixed.
`Approve` -- no HIGH findings remain; MEDIUM/LOW stay in the table as work to do.

Never issue `Approve` for a domain marked `Not reviewed` in the coverage table.
```
