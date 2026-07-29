# AI-DK

**AI Development Kit** — AI Engineering Standard für KI-gestützte Softwareentwicklung.

Regelwerk aus Prinzipien, Workflows und Dokumentation. Modellunabhängig · Core technologieunabhängig · versioniert · langfristig wartbar.

## Aktueller Stand

| Feld | Wert |
|------|------|
| Framework-Version | **1.0.0** |
| Status | Stabiler Core (Sprint 1–4 abgeschlossen) |
| Nächste geplante Version | **1.1** (maschinenlesbare Regeln) |

Changelog: [CHANGELOG.md](CHANGELOG.md) · Projektstand: [`.ai/08_PROJECT_STATE.md`](.ai/08_PROJECT_STATE.md)

## Produktarchitektur

```text
AI-DK
│
├── Core          universelle Regeln für jedes Projekt   ← 1.0.0
├── Profiles      technologieabhängige Vertiefungen      ← geplant ab 2.0
└── Extensions    Anbindung an konkrete KI-Werkzeuge     ← geplant
```

### Ebene 1 – Core

Universelle Regeln unter [`.ai/`](.ai/). Gelten für jedes Projekt. Keine Stack-, Framework- oder Vendor-Zwänge.

Profile und Extensions dürfen den Core **verfeinern**, ihm aber **nicht widersprechen**.

### Ebene 2 – Profiles (geplant, ab 2.0)

Austauschbare technologieabhängige Regeln, z. B. `profiles/flutter/`, `profiles/python/`, `profiles/dotnet/`, `profiles/react/`, `profiles/rust/`.

### Ebene 3 – Extensions (geplant)

Dünne Adapter auf Werkzeuge wie Cursor, Claude Code, Gemini CLI, GitHub Copilot, Windsurf. Extensions definieren keine eigenen Grundregeln.

## Dokumentenindex (Core)

| Nr. | Dokument | Zweck |
|-----|----------|--------|
| `00` | [PROJECT_CHARTER](.ai/00_PROJECT_CHARTER.md) | Grundprinzipien und Entscheidungsgrundlagen |
| `02` | [DEVELOPMENT_WORKFLOW](.ai/02_DEVELOPMENT_WORKFLOW.md) | Verbindlicher Entwicklungsablauf |
| `03` | [CODING_STANDARDS](.ai/03_CODING_STANDARDS.md) | Regeln für Codequalität und Struktur |
| `04` | [TESTING](.ai/04_TESTING.md) | Teststrategie und Testpflichten |
| `05` | [AI_BEHAVIOR](.ai/05_AI_BEHAVIOR.md) | Verhaltensregeln für die KI |
| `06` | [GIT_WORKFLOW](.ai/06_GIT_WORKFLOW.md) | Versionskontrolle und Commit-Disziplin |
| `07` | [DOCUMENTATION](.ai/07_DOCUMENTATION.md) | Projektdokumentation und Aktualisierungspflichten |
| `08` | [PROJECT_STATE](.ai/08_PROJECT_STATE.md) | Aktueller Arbeitsstand (lebendig) |
| `09` | [RELEASE_PROCESS](.ai/09_RELEASE_PROCESS.md) | Release-Vorbereitung und Freigabe |
| `10` | [SECURITY](.ai/10_SECURITY.md) | Sicherheits-Mindestregeln |
| `11` | [VERSION](.ai/11_VERSION.md) | Versionsvergabe und Semantik |

### Framework-Qualität

| Pfad | Zweck |
|------|--------|
| [tests/SCENARIOS](.ai/tests/SCENARIOS.md) | Testszenarien zur Prüfung von AI-DK (S1–S6) |
| [tests/RESULTS](.ai/tests/RESULTS.md) | Ergebnisprotokoll Desk-Review S1–S6 |

### Nummerierung

- Präfix `NN_` = Reihenfolge und Themengruppe.
- **`01` ist reserviert** (z. B. Overview/Quickstart).
- Core 1.0.0: `00`, `02`–`11`.
- Framework-Tests: `.ai/tests/` (kein Core-Nummernkreis).

## Verwendung

1. Core-Dokumente aus `.ai/` in das Zielprojekt übernehmen oder verlinken.
2. KI auf Charter, AI Behavior und Project State verpflichten; übrige Core-Docs mitführen.
3. Project State projektspezifisch füllen und aktuell halten.
4. Qualität des Frameworks bei Bedarf mit S1–S6 prüfen.
5. Später optional Profile und Extension ergänzen.
6. Änderungen an AI-DK versionieren (`11_VERSION.md`, `CHANGELOG.md`).

## Dokumentationsprinzip

Ziel · Geltungsbereich · Grundprinzipien · Verbindliche Regeln · Empfehlungen · KI-Verhalten · Checkliste · Beispiele · Ausnahmen · Version

`08_PROJECT_STATE.md` ergänzt um **Aktueller Projektstand**.

### Kernzuständigkeiten (keine Duplikate)

| Dokument | Kanonisch für |
|----------|----------------|
| `00_PROJECT_CHARTER` | Prinzipien, Entscheidungskriterien, Unsicherheit |
| `02_DEVELOPMENT_WORKFLOW` | Phasen, Zerlegung, Abschlussbericht |
| `05_AI_BEHAVIOR` | Priorität, Konflikte, Kontextpflicht, Handlungsgrenzen |
| Spezialdocs `03`–`04`, `06`–`11` | ihr jeweiliges Fachthema |
| `.ai/tests/SCENARIOS` | Qualitätsprüfung des Frameworks |

## Roadmap

| Version | Fokus |
|---------|--------|
| **0.1.0** | Sprint 1 – Core Foundation |
| **0.2.0** | Sprint 2 – Projektorganisation |
| **0.3.0** | Sprint 3 – Betrieb |
| **1.0.0** | Sprint 4 – Konsolidierung (aktuell) |
| **1.1** | Maschinenlesbare Regeln (z. B. `.ai/rules/*.yml`); Markdown bleibt kanonisch |
| **2.0** | Profiles |
| **2.x+** | Extensions, CI/CD-Vertiefung, ADRs, weitere Profile |
