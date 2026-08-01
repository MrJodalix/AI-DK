# AI-DK Flutter Rules (YAML)

Version: 2.0.0

## Zweck

Kompakte Ableitung der Flutter-Profile-Markdowns für Agenten und Tools.

## Konfliktregel

1. Markdown unter `profiles/flutter/*.md` ist kanonisch.
2. YAML hier ist abgeleitet.
3. Core-YAML (`.ai/rules/`) und Core-Markdown bleiben für universelle Regeln maßgeblich.

## Schema

Wie Core 1.1, zuzüglich:

```yaml
aidk: "2.0"
profile: "flutter"
source: "profiles/flutter/CODING.md"
rules:
  - id: FL-CS-001
    severity: must
    summary: "Kurztext"
    refs: ["profiles/flutter/CODING.md"]
```

### ID-Präfixe (Flutter)

| Präfix | Quelle |
|--------|--------|
| `FL-ST` | STACK.md |
| `FL-AR` | ARCHITECTURE.md |
| `FL-CS` | CODING.md |
| `FL-TS` | TESTING.md |

## Dateien

| Datei | Inhalt |
|-------|--------|
| [flutter.yml](flutter.yml) | verdichtete must/should-Regeln (generisches Flutter-Profile) |
| [rodister/](rodister/) | **Consumer-Rules** für das Produkt Rodister (Cursor `.mdc`) |

Produkt-spezifische Cursor-Rules gehören nach `rodister/`, nicht in `flutter.yml`.

