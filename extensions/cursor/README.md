# AI-DK Extension – Cursor

Version: 2.3.0

## Zweck

Cursor so verdrahten, dass Agenten die AI-DK-Spezifikation über Bootstrap starten.

## Konfliktregel

Core-/Profile-Markdown bleibt kanonisch. Diese Extension liefert nur **Werkzeug-Vorlagen**.

## Einrichtung (Zielprojekt)

1. AI-DK Core nach `.ai/` kopieren (inkl. `01_BOOTSTRAP.md`).
2. Bei Flutter-Projekten: `profiles/flutter/` mitführen.
3. Vorlage [AGENTS.template.md](AGENTS.template.md) als `AGENTS.md` (Repo-Root) oder in Cursor-Rules übernehmen.
4. Optional: [cursor-rule.template.mdc](cursor-rule.template.mdc) nach `.cursor/rules/aidk.mdc` legen.

## Was Cursor zuerst lesen soll

Reihenfolge unverändert aus `01_BOOTSTRAP.md`:

1. Charter → 2. AI Behavior → 3. Project State → 4. TODO → 5. Fachdocs/Profile → 6. Aufgabe

## Pflege

Nach AI-DK-Upgrades: Spezifikations-Versionsnummer in `AGENTS.md` / Rule anpassen.
