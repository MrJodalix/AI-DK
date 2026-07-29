# Changelog

Alle wesentlichen Änderungen am AI-DK-Framework.

Format: neueste Version zuerst. Versionsregeln: `.ai/11_VERSION.md`.

## 1.0.1 – 2026-07-29

### Geändert

- `05_AI_BEHAVIOR.md`: Code-Review-Schwereordnung und Secret-Stopp vor Merge/Approve (S6-Nachzug)
- `.ai/tests/RESULTS.md`: S6 auf Bestanden aktualisiert

### Planung

- `.ai/plans/1.1_MACHINE_READABLE_RULES.md` — Planung für Version 1.1 (noch nicht implementiert)

## 1.0.0 – 2026-07-29

Erstes stabiles Core-Release (Sprint 4 abgeschlossen).

### Hinzugefügt

- Vollständiger Core `00`, `02`–`11` (Charter bis Version)
- Produktarchitektur: Core · Profiles · Extensions (Profiles/Extensions geplant)
- Einheitliche Dokumentstruktur für alle Core-Dokumente
- Zuständigkeitsmatrix (kanonische Themen ohne Duplikate)
- Framework-Testszenarien S1–S6 unter `.ai/tests/SCENARIOS.md`
- `README.md` als Einstieg und Index

### Geändert

- Pre-Release-Stände `0.1.0`–`0.3.0` und Sprint-4-Drafts zu **1.0.0** konsolidiert
- Redundanzen zwischen Charter, Workflow und AI Behavior kanonisiert
- Technologieabhängige Formulierungen aus dem Core entfernt

### Bekannt / bewusst offen

- `01` weiterhin reserviert (Overview/Quickstart)
- Profiles (2.0), YAML-Regeln (1.1), Extensions noch nicht umgesetzt
- S1–S6 Desk-Review; S6 mit 1.0.1 geschlossen
- Release lokal als Git-Tag `v1.0.0` (kein Remote-Push)

## 0.3.0

Sprint 3 – Betrieb: Release Process, Security, Version.

## 0.2.0

Sprint 2 – Projektorganisation: Git Workflow, Documentation, Project State.

## 0.1.0

Sprint 1 – Core Foundation: Charter, Workflow, Coding Standards, Testing, AI Behavior.
