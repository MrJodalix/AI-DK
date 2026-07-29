# AI-DK

**AI-DK – The AI Engineering Standard**

Standards, Prozesse und Qualitätsregeln für KI-gestützte Softwareentwicklung.  
Modellunabhängig · Core technologieunabhängig · versioniert · langfristig wartbar.

> AI-DK ist der **Name**. Das Produkt ist ein **AI Engineering Standard** — kein bloßer Prompt-Werkzeugkasten.

## Aktueller Stand

| Feld | Wert |
|------|------|
| Framework-Version | **1.0.3** |
| Status | Stabiler Core + Positioning |
| Repository | https://github.com/MrJodalix/AI-DK |
| Nächste Version | **1.1** — maschinenlesbare Regeln ([Plan](.ai/plans/1.1_MACHINE_READABLE_RULES.md)) |

Changelog: [CHANGELOG.md](CHANGELOG.md) · Stand: [`.ai/08_PROJECT_STATE.md`](.ai/08_PROJECT_STATE.md) · Pläne: [`.ai/plans/`](.ai/plans/)

## Produktarchitektur

```text
AI-DK  (AI Engineering Standard)
│
├── Core          universelle Regeln für jedes Projekt   ← 1.0.x
├── Profiles      technologieabhängige Vertiefungen      ← ab 2.0 (Flutter zuerst)
└── Extensions    Anbindung an konkrete KI-Werkzeuge     ← geplant
```

### Ebene 1 – Core

Universelle Regeln unter [`.ai/`](.ai/). Gelten für jedes Projekt. Keine Stack-, Framework- oder Vendor-Zwänge.

Profile und Extensions dürfen den Core **verfeinern**, ihm aber **nicht widersprechen**.

### Ebene 2 – Profiles (ab 2.0)

Erstes geplantes Profile: **Flutter**. Weitere (Python, .NET, React, Rust, …) folgen.

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
| [tests/SCENARIOS](.ai/tests/SCENARIOS.md) | Testszenarien S1–S6 |
| [tests/RESULTS](.ai/tests/RESULTS.md) | Desk-Review-Protokoll |

### Nummerierung

- **`01` ist reserviert** (z. B. Overview/Quickstart) — absichtlich leer in 1.0.x.
- Core: `00`, `02`–`11` · Tests: `.ai/tests/` · Pläne: `.ai/plans/`

## Verwendung

1. Core aus `.ai/` übernehmen oder verlinken.
2. KI auf Charter, AI Behavior und Project State verpflichten.
3. Project State aktuell halten.
4. Qualität mit S1–S6 prüfen.
5. Später Profile / Extension ergänzen.
6. Änderungen versionieren (`11_VERSION.md`, `CHANGELOG.md`).

## Dokumentationsprinzip

Ziel · Geltungsbereich · Grundprinzipien · Verbindliche Regeln · Empfehlungen · KI-Verhalten · Checkliste · Beispiele · Ausnahmen · Version

### Begriffe (kurz)

| Begriff | Bedeutung |
|---------|-----------|
| **AI-DK** | Name |
| **AI Engineering Standard** | Produktkategorie / Untertitel |
| **Verbindliche Regeln** | Muss-Verhalten |
| **Empfehlungen** | Soll-Verhalten |
| **Core** | Universelle Norm `.ai/00`–`11` |
| **Profile** | Technologievertiefung (ab 2.0) |
| **Extension** | Tool-Adapter (geplant) |

## Roadmap

| Version | Fokus |
|---------|--------|
| **1.0.x** | Stabiler Core (aktuell **1.0.3**) |
| **1.1** | Maschinenlesbare Regeln (YAML) — [Plan](.ai/plans/1.1_MACHINE_READABLE_RULES.md) |
| **1.2** | Framework-Tests automatisieren — [Plan](.ai/plans/1.2_TEST_AUTOMATION.md) |
| **1.x+** | Governance, ADRs, Glossar, QUALITY — [Backlog](.ai/plans/BACKLOG_AFTER_1.0.md) |
| **2.0** | Erstes Profile: **Flutter** |
| **2.x+** | Weitere Profiles · Extensions · RFCs |
