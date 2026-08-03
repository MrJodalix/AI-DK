# AI-DK

**AI-DK – The AI Engineering Standard**

Standards, Prozesse und Qualitätsregeln für KI-gestützte Softwareentwicklung.  
Modellunabhängig · Core technologieunabhängig · versioniert · langfristig wartbar.

> AI-DK ist der **Name**. Das Produkt ist ein **AI Engineering Standard** — eine versionierte **Spezifikation**, keine lose Regeldatei-Sammlung.

## Spezifikation (verbindlich für KI)

Dieses Projekt implementiert die AI-DK-Spezifikation in Version **2.3.1**. AI-DK ist die verbindliche Arbeitsgrundlage für Analyse, Planung, Implementierung, Tests und Dokumentation. Beginne jede neue Aufgabe mit dem Bootstrap-Prozess gemäß [`01_BOOTSTRAP.md`](.ai/01_BOOTSTRAP.md) und befolge anschließend die für die Aufgabe relevanten Core-Dokumente (und ggf. das aktive Profile).

## Aktueller Stand

| Feld | Wert |
|------|------|
| Framework-Version | **2.3.1** |
| Status | Spezifikation · Flutter-Profile · Extensions · CI · Klarstellungen Greenfield/Stack |
| Repository | https://github.com/MrJodalix/AI-DK |
| Profile-Fokus | **nur Flutter** (weitere Profiles zurückgestellt) |

Changelog: [CHANGELOG.md](CHANGELOG.md) · Stand: [`.ai/08_PROJECT_STATE.md`](.ai/08_PROJECT_STATE.md)

## Produktarchitektur

```text
AI-DK  (AI Engineering Standard / Spezifikation)
│
├── Core          Markdown-Norm `.ai/00`–`11`           ← kanonisch
├── rules/        YAML-Ableitung                         ← 1.1
├── tests/        Szenarien + check_core.py              ← 1.2
├── Profiles      derzeit: Flutter                       ← 2.0
├── docs/         Governance · ADR · Glossar · Quality   ← 2.2
├── rfcs/         Proposals                              ← 2.2
└── Extensions    Cursor · Generic                       ← 2.3
```

**Semantik der Core-Reihenfolge:** Warum (`00`) → Wie starte ich (`01`) → Wie arbeite ich (`02`) → …

**Konfliktregel:** Markdown gewinnt. YAML unter `.ai/rules/` ist abgeleitet.  
Governance: [docs/GOVERNANCE.md](docs/GOVERNANCE.md) · Extensions: [extensions/README.md](extensions/README.md)

## Dokumentenindex (Core)

| Nr. | Dokument | Zweck |
|-----|----------|--------|
| `00` | [PROJECT_CHARTER](.ai/00_PROJECT_CHARTER.md) | Grundprinzipien |
| `01` | [BOOTSTRAP](.ai/01_BOOTSTRAP.md) | Agenten-Einstieg |
| `02` | [DEVELOPMENT_WORKFLOW](.ai/02_DEVELOPMENT_WORKFLOW.md) | Ablauf |
| `03` | [CODING_STANDARDS](.ai/03_CODING_STANDARDS.md) | Codequalität |
| `04` | [TESTING](.ai/04_TESTING.md) | Tests |
| `05` | [AI_BEHAVIOR](.ai/05_AI_BEHAVIOR.md) | KI-Verhalten |
| `06` | [GIT_WORKFLOW](.ai/06_GIT_WORKFLOW.md) | Git |
| `07` | [DOCUMENTATION](.ai/07_DOCUMENTATION.md) | Projektdokumentation |
| `08` | [PROJECT_STATE](.ai/08_PROJECT_STATE.md) | Lebendiger Stand |
| `09` | [RELEASE_PROCESS](.ai/09_RELEASE_PROCESS.md) | Releases |
| `10` | [SECURITY](.ai/10_SECURITY.md) | Security |
| `11` | [VERSION](.ai/11_VERSION.md) | Versionierung |

### Flutter-Profile

| Pfad | Zweck |
|------|--------|
| [profiles/flutter/](profiles/flutter/) | Riverpod · Drift · Freezed · go_router · Material 3 |

### Extensions (2.3)

| Pfad | Zweck |
|------|--------|
| [extensions/cursor/](extensions/cursor/) | `AGENTS.md` / Cursor-Rule-Vorlagen |
| [extensions/generic/](extensions/generic/) | Chat-Session-Prompt |

### Meta & Qualität

| Pfad | Zweck |
|------|--------|
| [docs/](docs/) | Governance · Glossar · Quality · ADRs |
| [rfcs/](rfcs/) | Proposals |
| [check_core.py](.ai/tests/check_core.py) | Automatische Prüfung |
| [CI](.github/workflows/check-core.yml) | GitHub Actions |

```bash
python3 .ai/tests/check_core.py
```

## Roadmap

| Version | Fokus |
|---------|--------|
| **1.x** | Core · YAML · Checks |
| **2.0** | Flutter-Profile |
| **2.1** | Bootstrap + Spezifikation |
| **2.2** | Governance · ADR · Glossar · RFC |
| **2.3.0** | Extensions + CI |
| **2.3.1** | Klarstellungen Greenfield · Shared Core · Git-Abschluss · Flutter-Stack — **aktuell** |
| später | Weitere Profiles nur nach Bedarf |

## Verwendung

1. Spezifikationsformel an die KI / README bereitstellen.
2. Bootstrap: [`.ai/01_BOOTSTRAP.md`](.ai/01_BOOTSTRAP.md).
3. Flutter: `profiles/flutter/` aktivieren.
4. Tool verdrahten: [extensions/cursor/](extensions/cursor/) oder [extensions/generic/](extensions/generic/).
5. Vor Releases: `python3 .ai/tests/check_core.py` (PASS).
