# Changelog

Alle wesentlichen Änderungen am AI-DK-Framework.

Format: neueste Version zuerst. Versionsregeln: `.ai/11_VERSION.md`.

## 2.1.0 – 2026-07-29

Bootstrap und Spezifikations-Framing.

### Hinzugefügt

- `.ai/01_BOOTSTRAP.md` — verbindlicher Agenten-Einstieg (Sitzungs-/Aufgabenstart)
- Plan [`.ai/plans/2.1_BOOTSTRAP.md`](.ai/plans/2.1_BOOTSTRAP.md)

### Geändert

- README: AI-DK als versionierte **Spezifikation**; kanonische KI-Anweisung
- Charter-Matrix, Workflow, AI Behavior: Verweise auf Bootstrap
- `check_core.py`: prüft `01_BOOTSTRAP.md` (eigene Heading-Liste)

## 2.0.0 – 2026-07-29

Erstes Profile: **Flutter**.

### Hinzugefügt

- `profiles/README.md` — Profile-System und Konfliktregel Core vs. Profile
- `profiles/flutter/` — README, STACK, ARCHITECTURE, CODING, TESTING
- `profiles/flutter/rules/flutter.yml` — YAML-Ableitung (`aidk: "2.0"`)
- Plan [`.ai/plans/2.0_FLUTTER_PROFILE.md`](.ai/plans/2.0_FLUTTER_PROFILE.md)

### Kanonischer Flutter-Stack

Riverpod · Drift · Freezed · go_router · Material 3

### Geändert

- `check_core.py` prüft Flutter-Profile-Dateien, Strukturüberschriften und Profile-YAML
- README / STATE / Roadmap auf **2.0.0**

## 1.2.0 – 2026-07-29

### Hinzugefügt

- `.ai/tests/check_core.py` — Core-Struktur, Markdown-Verweise, YAML-Regeln
- `.ai/tests/reports/` — Laufberichte (`latest.txt`)

### Geändert

- Plan 1.2 als umgesetzt markiert
- Release-/Szenario-Hinweise auf automatischen Check

### Nutzung

```bash
python3 .ai/tests/check_core.py
```

Exit 0 = PASS. Benötigt PyYAML.

## 1.1.0 – 2026-07-29

Maschinenlesbare Regeln unter `.ai/rules/`.

## 1.0.3 – 2026-07-29

Positioning: AI-DK – The AI Engineering Standard.

## 1.0.2 / 1.0.1 / 1.0.0

Qualität, S6-Nachzug, erstes Core-Release.

Repository: https://github.com/MrJodalix/AI-DK
