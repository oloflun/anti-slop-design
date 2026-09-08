# Runda 2: fold + signaturakten, inget mer

Orkestreraren har läst din BRIEF.md. Svar på dina öppna frågor och korrigeringar står under
"Från orkestreraren" längst ned. Allt annat i BRIEF.md gäller.

## Bygg nu

`{{UT_MAPP}}/index.html` (CSS och JS inuti eller bredvid) med **bara** första skärmen och
signaturakten enligt BRIEF.md och målbilden: heron i vila, resan, avslöjandet, och det hårda
klippet till nästa akts första rad (en rubrik räcker som platshållare för resten). Motorn
(`~/.agents/skills/design/scripts/scroll/scrollcraft.js` + `.css`) kopieras in oförändrad om
din device-tabell använder scrub, pin eller pan; bespoke rörelse läser `--sc-p`. Ingen
tredjepartskod utöver motorn och Google Fonts.

Krav som kontrolleras i pixlar:
- I vila förhandsvisas inte slutläget (FEEDBACK F-002).
- Signaturakten fungerar i båda scrollriktningarna och är mjukt lerpad.
- `?preview=<läge>` tvingar fram varje formad vy du listade i BRIEF.md.
- Reduced motion visar de formade lägena i ordning som egna sektioner (F-001), ingen tumnagel.
- Ramen till `/sites/…` är otransformerad och otonad när den visas; dokumentet i ramen har en `<title>`.
- Inget horisontellt överflöde vid 320/390/768/1440.

## Server och skärmbilder

Starta `python ~/.agents/skills/design/scripts/serve.py --port {{PORT}} --root .` från
repo-roten i bakgrunden och öppna `http://127.0.0.1:{{PORT}}/{{UT_MAPP}}/index.html`.
Skjut med Playwright till `{{UT_MAPP}}/shots/`, **i båda lägena** (`reduced_motion=
"no-preference"` respektive `"reduce"`): fold 1440×900; sex rutor genom signaturakten
(0/10/20/30/40/60 % av scrollhöjden) i rörelseläge; varje `?preview=`-läge; fold och 50 % under
reduced motion (filnamn med `rm-`); 390×844 fold. **Läs varje bild med Read** och skriv i
`NOTES.md` vad du såg och ändrade. Läs konsolen efter fel och `[scrollcraft]`-varningar.

Avsluta med: vilka bilder du läste, vad som avviker från BRIEF.md och varför, öppna frågor.

## Från orkestreraren

{{FEEDBACK}}
