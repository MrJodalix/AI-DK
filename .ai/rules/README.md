# AI-DK Rules (maschinenlesbar)

Version: 1.1.0

## Zweck

Kompakte YAML-Ableitung der Core-Markdown-Dokumente für Agenten und Tools.

## Konfliktregel (verbindlich)

1. **Markdown ist kanonisch** — bei Widerspruch gewinnen die Dateien `.ai/00`–`11` (und verwandte Core-Markdowns).
2. **YAML ist abgeleitet** — keine Pflichtregel darf nur in YAML existieren.
3. Projekte **ohne** `.ai/rules/` bleiben mit Core 1.0.x gültig.

## Schema

Pro Datei:

```yaml
aidk: "1.1"
source: "03_CODING_STANDARDS.md"   # kanonische Markdown-Quelle (eine oder primäre)
sources: []                        # optional: weitere Quellen
rules:
  - id: CS-001                     # PREFIX-NNN, stabil
    severity: must                 # must | should
    summary: "Kurztext"
    refs: ["03_CODING_STANDARDS.md"]
```

### severity

| Wert | Bedeutung |
|------|-----------|
| `must` | Verbindliche Regel aus dem Markdown |
| `should` | Empfehlung aus dem Markdown |

### ID-Präfixe

| Präfix | Datei | Quelle |
|--------|-------|--------|
| `CH` | architecture.yml (Charter-Anteil) | `00_PROJECT_CHARTER.md` |
| `BS` | architecture.yml (Bootstrap) | `01_BOOTSTRAP.md` |
| `WF` | architecture.yml (Workflow-Anteil) | `02_DEVELOPMENT_WORKFLOW.md` |
| `BH` | architecture.yml (Behavior-Anteil) | `05_AI_BEHAVIOR.md` |
| `CS` | coding.yml | `03_CODING_STANDARDS.md` |
| `TS` | testing.yml | `04_TESTING.md` |
| `GIT` | git.yml | `06_GIT_WORKFLOW.md` |
| `DOC` | documentation.yml | `07_DOCUMENTATION.md` |
| `ST` | architecture.yml (State) / documentation | `08_PROJECT_STATE.md` |
| `REL` | release.yml | `09_RELEASE_PROCESS.md` |
| `SEC` | security.yml | `10_SECURITY.md` |
| `VER` | version.yml | `11_VERSION.md` |

## Sync-Pflicht

Nach jeder inhaltlichen Änderung an einem Core-Markdown:

1. Zugehörige YAML-Datei prüfen und anpassen.
2. Keine neuen `must`-Regeln nur in YAML einfügen.
3. Vor AI-DK-Release: Stichprobe Markdown ↔ YAML.

Siehe auch `07_DOCUMENTATION.md`.

## Dateien

| Datei | Inhalt |
|-------|--------|
| [coding.yml](coding.yml) | Coding Standards |
| [testing.yml](testing.yml) | Testing |
| [git.yml](git.yml) | Git Workflow |
| [architecture.yml](architecture.yml) | Charter, Workflow, Behavior, State (verdichtet) |
| [documentation.yml](documentation.yml) | Documentation |
| [security.yml](security.yml) | Security |
| [release.yml](release.yml) | Release Process |
| [version.yml](version.yml) | Version |
