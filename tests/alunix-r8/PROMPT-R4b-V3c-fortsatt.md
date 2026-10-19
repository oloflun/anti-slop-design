# Alunix r8, runda 4, fortsättning. Cell {{KONCEPT}}.

Din session avbröts av kontots användningsgräns mitt i runda 4 (efter 79 turer). Gränsen är
återställd. Uppdraget är oförändrat: `tests/alunix-r8/PROMPT-R4-V3c.md` i sin helhet, inklusive
leadens tillägg 2026-09-15. Ut-mapp `{{UT_MAPP}}`, port {{PORT}}.

## Var du var

`{{UT_MAPP}}/NOTES.md` § R4 bär rubriker för plan 001 till 005. Läs det avsnittet först och
kontrollera mot `{{UT_MAPP}}/index.html` att varje dom där (`verified` / `best-effort` /
`reverted`) fortfarande stämmer med filen; en plan vars Verification inte står i NOTES med
ett utfall räknas som ej körd och körs om.

## Vad som återstår, i ordning

1. Plan 006, 007, 008 (`{{UT_MAPP}}/plans/`), Verification per plan, utfall i NOTES § R4.
2. `Skill(review-animations)` i din session, rapporten i sin helhet i transkriptet (efter
   005 enligt R4-promptens § 2; 005 är gjord, så nu).
3. Hela mekaniska grinden, R4-promptens § 3, punkt 1 till 8, med kontroll- och sidtal i
   NOTES. Servern: `python ~/.claude/skills/design/scripts/serve.py --port {{PORT}} --root .`
   från repo-roten om den inte redan svarar.
4. Skärmbilderna i § 3.8, varje läst som bild, `läst: <fil>` i NOTES.
5. Låst copy 15/15 bekräftad byte för byte. Noll tankstreck.

Invarianterna i R4-promptens § 4 gäller. Kirurgiska `Edit`-anrop, aldrig `Write` av hela
filen, aldrig shell-skrivningar mot UI-filer. Rör inte heron-geometrin (span 4.8 står).
Ingen processakt i den här rundan.

Leverans som i R4-promptens § 5. Sista raden i ditt sista meddelande: `R4 klar` eller
`[PAUSED — steg X]`.
