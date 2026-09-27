Alunix {{KONCEPT}}, runda 2 fortsätter. Arbetsmapp `{{UT_MAPP}}`, server-port {{PORT}}.

Leaden stoppade din session mitt i runda 2. Orsaken: webbläsarfönster öppnades synligt på Antons
skärm, staplades och kraschade maskinen. Det var leadens instruktion ("kör headed") som var fel,
inte ditt arbete. Dina ändringar i `index.html` ligger kvar. Fortsätt där du var, med de här
reglerna utan undantag:

- **Aldrig headed.** Varje webbläsare du startar, också i egna ad-hoc-skript i /tmp, är
  `headless=True`.
  - För bildrutetider: `showcase_probe.py --headed` betyder nu headless med GPU. Den är
    kalibrerad mot headed och ger samma median, 16,7 ms.
  - I egna skript, använd samma start:
    `p.chromium.launch(headless=True, channel="chromium", args=["--enable-gpu","--ignore-gpu-blocklist","--use-angle=d3d11"])`.
- **En webbläsare i taget.** Starta aldrig två Playwright-processer samtidigt och kör inget i
  bakgrunden medan en annan körning pågår.
  - `showcase_probe.py` tar låset `%TEMP%/alunix-browser.lock` själv.
  - Egna skript: vänta tills ingen annan körning pågår.
- **Stäng webbläsaren** (`browser.close()`) i `finally` i varje skript du skriver.
- Siffror jämförs bara inom samma läge och över minst två körningar. V3f-referens i samma läge:
  `tests/alunix-r8/runs/V3f/shots/lead-hgpu-1440-{1,2}/result.json` (genom-p95 50 och 33,5 ms).

Gör klart punkterna 1–4 i runda 2-instruktionen och deras verifiering. Skriv R2-sektionen i
`RAPPORT.md` med en rad om omstarten. Ingen commit.
