# Simplify — skipped findings (re-evaluate on next /simplify)

| Datum | Fil:rad | Fynd | Varför skippat | Tas när |
|---|---|---|---|---|
| 2026-09-25 | hooks/design-vision-track.py:32 | `_MCP_TRACKED` (inspo, ui-skills) hårdkodat i hooken; borde vara data i design_hook_lib / routing-tabellen, som GEN_TOOL | Två poster; hooken kördes live av V3g-byggaren när fyndet kom | En tredje MCP-server ska spåras, eller ett servernamn byts |
| 2026-09-25 | skills/design/references/component-routing.md:114-127 | Tre identiska GSAP-regler (gsap-core, gsap-scrolltrigger, gsap-lenis) i stället för en regel med `"skills": [...]` | Kräver schemaändring i match_routes + design-route.py; delad infrastruktur, live under bygget | Nästa signal som ska routa till fler än en skill |
| 2026-09-25 | tests/hooks/test_mcp_gsap_routes.py | Subprocess per test för rena funktioner; ingen delad conftest-helper | Samma konvention som befintliga tester; ingen kanonisk helper finns | När en conftest.py med delad `_run` skrivs för tests/hooks |
| 2026-09-25 | hooks/hooks.json (mcp-matcher) | Ny pythonprocess per inspo/ui-skills-anrop | Samma kostnadsform som generation-grenen; ingen billig fix inom en-process-per-hook | Om hook-latens mäts som problem |
