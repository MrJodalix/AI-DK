# ADR 0005 – Spezifikation und Bootstrap

Status: **Accepted**  
Datum: 2026-07-29

## Kontext

Ohne klaren Einstieg bleibt AI-DK tool-spezifisch („lies irgendwelche Markdowns“). Es fehlt eine zitierbare Spezifikationsformel.

## Entscheidung

- AI-DK wird als **versionierte Spezifikation** geführt.
- `01_BOOTSTRAP.md` ist die Einstiegsschicht für Agenten.
- README trägt die kanonische KI-Anweisung inkl. Framework-Version.

## Konsequenzen

- ChatGPT, Cursor, Claude Code & Co. teilen denselben Start.
- Versionsangaben in der Formel müssen zum Release passen.
