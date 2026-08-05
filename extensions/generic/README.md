# AI-DK Extension – Generic (Chat-Agenten)

Version: 2.3.3

## Zweck

Einstieg für ChatGPT, Claude.ai und ähnliche Agenten **ohne** IDE-spezifisches Rule-Format.

## Nutzung

Zu Beginn einer Sitzung die Datei [SESSION_PROMPT.template.md](SESSION_PROMPT.template.md) (oder ihren Inhalt) als ersten Kontext senden, danach bei Bedarf:

- `.ai/01_BOOTSTRAP.md`
- `.ai/00_PROJECT_CHARTER.md`
- `.ai/05_AI_BEHAVIOR.md`
- projekteigener Stand (`.ai/08_PROJECT_STATE.md` / `PROJECT_STATE.md`)
- Fachdokumente / `profiles/flutter/` (wenn Flutter)

## Hinweis

Lange Chats: Bootstrap bei Themenwechsel erneut anstoßen. Version in der Prompt-Vorlage an die Framework-Version anpassen.
