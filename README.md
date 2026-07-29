# AI-DK

**AI-DK – The AI Engineering Standard**

Standards, Prozesse und Qualitätsregeln für KI-gestützte Softwareentwicklung.  
Modellunabhängig · Core technologieunabhängig · versioniert · langfristig wartbar.

> AI-DK ist der **Name**. Das Produkt ist ein **AI Engineering Standard** — kein bloßer Prompt-Werkzeugkasten.

## Aktueller Stand

| Feld | Wert |
|------|------|
| Framework-Version | **2.0.0** |
| Status | Core + rules + Checks + **Flutter-Profile** |
| Repository | https://github.com/MrJodalix/AI-DK |
| Nächste Version | weitere Profiles / Backlog — nach Freigabe |

Changelog: [CHANGELOG.md](CHANGELOG.md) · Stand: [`.ai/08_PROJECT_STATE.md`](.ai/08_PROJECT_STATE.md)

## Produktarchitektur

```text
AI-DK  (AI Engineering Standard)
│
├── Core          Markdown-Norm `.ai/00`–`11`           ← kanonisch
├── rules/        YAML-Ableitung                         ← 1.1
├── tests/        Szenarien + check_core.py              ← 1.2
├── Profiles      technologieabhängige Vertiefungen      ← 2.0 (Flutter)
└── Extensions    Anbindung an konkrete KI-Werkzeuge     ← geplant
```

**Konfliktregel:** Markdown gewinnt. YAML ist abgeleitet.  
Core vs. Profile: [profiles/README.md](profiles/README.md). Details Core-YAML: [`.ai/rules/README.md`](.ai/rules/README.md).

## Dokumentenindex (Core)

| Nr. | Dokument | Zweck |
|-----|----------|--------|
| `00` | [PROJECT_CHARTER](.ai/00_PROJECT_CHARTER.md) | Grundprinzipien und Entscheidungsgrundlagen |
| `02` | [DEVELOPMENT_WORKFLOW](.ai/02_DEVELOPMENT_WORKFLOW.md) | Verbindlicher Entwicklungsablauf |
| `03` | [CODING_STANDARDS](.ai/03_CODING_STANDARDS.md) | Codequalität |
| `04` | [TESTING](.ai/04_TESTING.md) | Teststrategie |
| `05` | [AI_BEHAVIOR](.ai/05_AI_BEHAVIOR.md) | KI-Verhalten |
| `06` | [GIT_WORKFLOW](.ai/06_GIT_WORKFLOW.md) | Git |
| `07` | [DOCUMENTATION](.ai/07_DOCUMENTATION.md) | Projektdokumentation |
| `08` | [PROJECT_STATE](.ai/08_PROJECT_STATE.md) | Lebendiger Stand |
| `09` | [RELEASE_PROCESS](.ai/09_RELEASE_PROCESS.md) | Releases |
| `10` | [SECURITY](.ai/10_SECURITY.md) | Security |
| `11` | [VERSION](.ai/11_VERSION.md) | Versionierung |

### Maschinenlesbare Regeln (1.1)

| Datei | Quelle |
|-------|--------|
| [rules/README.md](.ai/rules/README.md) | Schema & Sync |
| [coding.yml](.ai/rules/coding.yml) | `03` |
| [testing.yml](.ai/rules/testing.yml) | `04` |
| [git.yml](.ai/rules/git.yml) | `06` |
| [architecture.yml](.ai/rules/architecture.yml) | `00`/`02`/`05`/`08` |
| [documentation.yml](.ai/rules/documentation.yml) | `07` |
| [security.yml](.ai/rules/security.yml) | `10` |
| [release.yml](.ai/rules/release.yml) | `09` |
| [version.yml](.ai/rules/version.yml) | `11` |

### Flutter-Profile (2.0)

| Pfad | Zweck |
|------|--------|
| [profiles/README.md](profiles/README.md) | Profile-System & Konfliktregel |
| [profiles/flutter/](profiles/flutter/) | Stack Riverpod · Drift · Freezed · go_router · Material 3 |
| [STACK](profiles/flutter/STACK.md) | Kanonischer Stack |
| [ARCHITECTURE](profiles/flutter/ARCHITECTURE.md) | Schichten |
| [CODING](profiles/flutter/CODING.md) | Dart/Flutter |
| [TESTING](profiles/flutter/TESTING.md) | flutter_test |
| [rules/flutter.yml](profiles/flutter/rules/flutter.yml) | YAML-Ableitung |

### Framework-Qualität

| Pfad | Zweck |
|------|--------|
| [tests/SCENARIOS](.ai/tests/SCENARIOS.md) | S1–S6 Verhaltensszenarien |
| [tests/RESULTS](.ai/tests/RESULTS.md) | Desk-Review |
| [tests/check_core.py](.ai/tests/check_core.py) | Core + Flutter-Profile-Prüfung |
| [tests/reports/](.ai/tests/reports/) | Laufberichte |

```bash
python3 .ai/tests/check_core.py
```

## Roadmap

| Version | Fokus |
|---------|--------|
| **1.0.x** | Stabiler Core |
| **1.1.0** | Maschinenlesbare Regeln |
| **1.2.0** | Framework-Tests automatisieren |
| **1.x+** | Governance, ADRs, Glossar — [Backlog](.ai/plans/BACKLOG_AFTER_1.0.md) |
| **2.0.0** | Flutter-Profile — **aktuell** |
| **2.x+** | Weitere Profiles · Extensions · RFCs |

## Verwendung

1. Core-Markdown aus `.ai/` übernehmen (kanonisch).
2. Optional `.ai/rules/` für Agenten/Tools mitführen.
3. Flutter-Projekte: `profiles/flutter/` aktivieren und im Projektstand vermerken.
4. Charter, AI Behavior, Project State beachten.
5. Bei Core-/Profile-Änderungen YAML synchron halten.
6. Vor Releases: `python3 .ai/tests/check_core.py` (PASS).
