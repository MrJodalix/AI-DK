# Changelog

Alle wesentlichen Änderungen am AI-DK-Framework.

Format: neueste Version zuerst. Versionsregeln: `.ai/11_VERSION.md`.

## 2.3.5 – 2026-08-06

I18N als Core-Querschnittsthema (nicht nur Flutter-Profile). Kein Breaking Change.

### Hinzugefügt

- `.ai/12_I18N.md` — technologieunabhängige Nutzertexte / Mehrsprachigkeit
- `.ai/rules/i18n.yml` — I18N-001…005

### Geändert

- `profiles/flutter/I18N.md` — als Konkretisierung von Core `12` ausgerichtet
- Charter-Matrix, Bootstrap-Fachdocs, Coding Standards, ADR 0002 (Nummer `12`)
- `check_core.py` — Core-Datei + YAML `i18n.yml`

## 2.3.4 – 2026-08-06

I18N / zentrale Nutzertexte im Flutter-Profile. Kein Breaking Change.

### Hinzugefügt

- `profiles/flutter/I18N.md` — gen-l10n (ARB), Zugriff über API/Getter, Übergangskatalog, Domänendaten vs. Copy

### Geändert

- `profiles/flutter/STACK.md` — Problemklasse I18N / UI-Texte
- `profiles/flutter/CODING.md` / `UI.md` / `README.md` — Verweise auf I18N
- `profiles/flutter/rules/flutter.yml` — FL-ST-009, FL-I18N-*

## 2.3.3 – 2026-08-05

Klarstellungen aus Zielprojekt-Retro (Flutter UI/Insets, Dev-Setup/Device-Smoke, undokumentierte HTTP). Kein Breaking Change.

### Hinzugefügt

- `profiles/flutter/UI.md` — SafeArea, Formulare, Bottom Sheets, FAB-`heroTag`, viewInsets vs. viewPadding
- `profiles/flutter/DEV_SETUP.md` — SDK/Gerät, Drift-Bump-Checkliste, Device-Smoke

### Geändert

- `profiles/flutter/ARCHITECTURE.md` — undokumentierte/Community-APIs; Verweis Drift-Checkliste
- `profiles/flutter/CODING.md` / `README.md` — Verweise auf UI/DEV_SETUP
- `profiles/flutter/rules/flutter.yml` — FL-UI-*, FL-DS-001, FL-AR-006

## 2.3.2 – 2026-08-03

Klarstellungen aus Zielprojekt-Retro P0–P4 (Offline/HTTP, Migrations-Tests, Fortsetzungssitzung, optionale Integrationen). Kein Breaking Change.

### Geändert

- `.ai/01_BOOTSTRAP.md` — Fortsetzungssitzung: verkürzter Start bei aktuellem Stand
- `.ai/02_DEVELOPMENT_WORKFLOW.md` — Meilensteine/Epics (Docs/Tests/Version je Lieferung)
- `.ai/05_AI_BEHAVIOR.md` — Stack-Ausnahmen vs. Feature-Blockade; Port + Unavailable-Stub
- `profiles/flutter/ARCHITECTURE.md` — Offline-First-Netzgrenze; HTTP-Client-Mindeststandard
- `profiles/flutter/TESTING.md` — Upgrade-Migrationstest bei `schemaVersion`-Bump
- `profiles/flutter/STACK.md` — Pre-Release vs. Blockade; Verweise Offline/HTTP
- YAML: `architecture.yml`, `profiles/flutter/rules/flutter.yml`

## 2.3.1 – 2026-08-03


Klarstellungen aus Zielprojekt-Retro (Greenfield, Shared Core, Git-Abschluss, Flutter-Stack-Konflikte). Kein Breaking Change.

### Geändert

- `.ai/01_BOOTSTRAP.md` — Zielprojekt-Greenfield; Shared Core (Kopie/Verlinkung); projekteigener Stand / Alias `PROJECT_STATE.md`
- `.ai/02_DEVELOPMENT_WORKFLOW.md` — Phase 6: „Commit vorbereitet“ vs. ausführen
- `.ai/06_GIT_WORKFLOW.md` — Abschluss vorbereitet; Commit nur bei Freigabe/Aufgabendeckung
- `.ai/08_PROJECT_STATE.md` — Shared Core / nested AI-DK
- `profiles/README.md` — Core **kopieren oder verlinken**; Stand-Pflicht
- `extensions/cursor/README.md` — gleiche Einbindungsregel wie Profiles
- `profiles/flutter/STACK.md` — Riverpod Runtime vs. Generator; Pub-Konflikte; Pre-Release-Regel
- YAML-Ableitung: `architecture.yml`, `git.yml`, `profiles/flutter/rules/flutter.yml`

## 2.3.0 – 2026-07-29

Extensions und CI. Profile-Fokus bleibt **Flutter only**.

### Hinzugefügt

- `extensions/` — Cursor- und Generic-Adapter (Vorlagen)
- `.github/workflows/check-core.yml` — CI für `check_core.py`
- `requirements.txt` — PyYAML
- ADR [0006](docs/adr/0006-extensions.md)
- Plan [`.ai/plans/2.3_EXTENSIONS_CI.md`](.ai/plans/2.3_EXTENSIONS_CI.md)

### Nicht enthalten

- Weitere Tech-Profiles (Python, .NET, …) — bewusst zurückgestellt

## 2.2.0 – 2026-07-29

Backlog-Meta: Governance, ADR, Glossar, Quality, RFC.

### Hinzugefügt

- `docs/GOVERNANCE.md`, `docs/GLOSSARY.md`, `docs/QUALITY.md`
- `docs/adr/` — ADR 0001–0005
- `rfcs/` — Prozess, Template, RFC 0001 (Accepted / 1.1)
- Plan [`.ai/plans/2.2_BACKLOG_META.md`](.ai/plans/2.2_BACKLOG_META.md)

### Geändert

- `check_core.py` prüft Meta-Docs und ADRs
- Backlog als weitgehend umgesetzt markiert

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
