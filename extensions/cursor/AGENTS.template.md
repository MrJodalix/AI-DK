# AGENTS.md — AI-DK (Vorlage)

Dieses Projekt implementiert die AI-DK-Spezifikation in Version **2.3.3**.
AI-DK ist die verbindliche Arbeitsgrundlage für Analyse, Planung, Implementierung, Tests und Dokumentation.

## Start jeder Aufgabe

1. Lies `.ai/01_BOOTSTRAP.md` und führe die Startsequenz aus.
2. Lies `.ai/00_PROJECT_CHARTER.md`, `.ai/05_AI_BEHAVIOR.md`, `.ai/08_PROJECT_STATE.md` (projekteigener Stand; ggf. Alias `PROJECT_STATE.md`).
3. Prüfe `TODO.md` (falls vorhanden).
4. Ermittle betroffene Fachdokumente unter `.ai/` und — falls aktiv — `profiles/flutter/`.
5. Arbeite danach gemäß `.ai/02_DEVELOPMENT_WORKFLOW.md`.

## Regeln

- Markdown unter `.ai/` ist kanonisch; `.ai/rules/*.yml` ist abgeleitet.
- Keine erfundenen APIs, Testergebnisse oder Releases.
- Freigaben und Releases nur nach Maintainer-Vorgabe (`docs/GOVERNANCE.md`, falls vorhanden).
- Flutter: kanonischer Stack laut `profiles/flutter/STACK.md` (Riverpod, Drift, Freezed, go_router, Material 3).
- Core darf kopiert oder verlinkt sein; bei Shared Core Stand immer projekteigen.
- Commit vorbereiten ≠ Commit ausführen (`02` / `06`).

## Qualität

Vor AI-DK-Framework-Änderungen (falls dieses Repo AI-DK selbst ist):

```bash
python3 .ai/tests/check_core.py
```
