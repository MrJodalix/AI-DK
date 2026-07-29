# AI-DK

**AI-DK – The AI Engineering Standard**

Standards, Prozesse und Qualitätsregeln für KI-gestützte Softwareentwicklung.  
Modellunabhängig · Core technologieunabhängig · versioniert · langfristig wartbar.

> AI-DK ist der **Name**. Das Produkt ist ein **AI Engineering Standard** — eine versionierte **Spezifikation**, keine lose Regeldatei-Sammlung.

## Spezifikation (verbindlich für KI)

Dieses Projekt implementiert die AI-DK-Spezifikation in Version **2.1.0**. AI-DK ist die verbindliche Arbeitsgrundlage für Analyse, Planung, Implementierung, Tests und Dokumentation. Beginne jede neue Aufgabe mit dem Bootstrap-Prozess gemäß [`01_BOOTSTRAP.md`](.ai/01_BOOTSTRAP.md) und befolge anschließend die für die Aufgabe relevanten Core-Dokumente (und ggf. das aktive Profile).

## Aktueller Stand

| Feld | Wert |
|------|------|
| Framework-Version | **2.1.0** |
| Status | Spezifikation · Core inkl. Bootstrap · rules · Checks · Flutter-Profile |
| Repository | https://github.com/MrJodalix/AI-DK |
| Nächste Version | weitere Profiles / Backlog — nach Freigabe |

Changelog: [CHANGELOG.md](CHANGELOG.md) · Stand: [`.ai/08_PROJECT_STATE.md`](.ai/08_PROJECT_STATE.md)

## Produktarchitektur

```text
AI-DK  (AI Engineering Standard / Spezifikation)
│
├── Core          Markdown-Norm `.ai/00`–`11`           ← kanonisch
├── rules/        YAML-Ableitung                         ← 1.1
├── tests/        Szenarien + check_core.py              ← 1.2
├── Profiles      technologieabhängige Vertiefungen      ← 2.0 (Flutter)
└── Extensions    Anbindung an konkrete KI-Werkzeuge     ← geplant
```

**Semantik der Core-Reihenfolge:** Warum (`00`) → Wie starte ich (`01`) → Wie arbeite ich (`02`) → Code (`03`) → Tests (`04`) → KI-Verhalten (`05`) → …

**Konfliktregel:** Markdown gewinnt. YAML ist abgeleitet.  
Core vs. Profile: [profiles/README.md](profiles/README.md). Details Core-YAML: [`.ai/rules/README.md`](.ai/rules/README.md).

## Dokumentenindex (Core)

| Nr. | Dokument | Zweck |
|-----|----------|--------|
| `00` | [PROJECT_CHARTER](.ai/00_PROJECT_CHARTER.md) | Grundprinzipien und Entscheidungsgrundlagen |
| `01` | [BOOTSTRAP](.ai/01_BOOTSTRAP.md) | Agenten-Einstieg (Sitzungs-/Aufgabenstart) |
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
| [tests/check_core.py](.ai/tests/check_core.py) | Core (inkl. Bootstrap) + Flutter-Profile |
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
| **2.0.0** | Flutter-Profile |
| **2.1.0** | Bootstrap + Spezifikations-Framing — **aktuell** |
| **1.x+ / 2.x+** | Governance, ADRs, weitere Profiles, Extensions — [Backlog](.ai/plans/BACKLOG_AFTER_1.0.md) |

## Verwendung

1. Spezifikationsformel (oben) an die KI geben bzw. README bereitstellen.
2. Agenten starten mit [`.ai/01_BOOTSTRAP.md`](.ai/01_BOOTSTRAP.md).
3. Core-Markdown aus `.ai/` übernehmen (kanonisch).
4. Optional `.ai/rules/` und bei Flutter `profiles/flutter/` mitführen.
5. Vor Releases: `python3 .ai/tests/check_core.py` (PASS).
