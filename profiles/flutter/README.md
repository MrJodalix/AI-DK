# AI-DK Flutter Profile

Version: 2.0.0

**Profile-ID:** `flutter`  
**Gilt ab Framework:** AI-DK **2.0.0**  
**Baut auf:** Core `.ai/00`–`11` (unverändert kanonisch für universelle Regeln)

## Ziel

Technologieabhängige Regeln für **Flutter / Dart**-Projekte, ohne den Core zu verunreinigen.

## Kanonischer Stack

| Bereich | Entscheidung | Dokument |
|---------|--------------|----------|
| State Management | **Riverpod** | [STACK.md](STACK.md), [CODING.md](CODING.md) |
| Persistenz | **Drift** | [STACK.md](STACK.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| Modelle / Immutability | **Freezed** | [STACK.md](STACK.md), [CODING.md](CODING.md) |
| Navigation | **go_router** | [STACK.md](STACK.md), [ARCHITECTURE.md](ARCHITECTURE.md) |
| UI | **Material 3** | [STACK.md](STACK.md), [CODING.md](CODING.md) |

Abweichungen vom Stack nur mit Begründung im Projektstand.

## Dokumentenindex

| Dokument | Zweck |
|----------|--------|
| [STACK.md](STACK.md) | Verbindliche Stack-Wahl und Alternativen |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Schichten, Abhängigkeiten, Feature-Schnitt |
| [CODING.md](CODING.md) | Dart/Flutter-Codequalität |
| [TESTING.md](TESTING.md) | flutter_test, Widget-/Integrationstests |
| [rules/](rules/) | YAML-Ableitung (optional für Agenten) |

## Konfliktregel

Siehe [profiles/README.md](../README.md). Kurz:

- Core = Prinzipien & Prozess
- dieses Profile = Flutter/Dart/Stack
- bei Widerspruch der Prinzipien: **Core**

## KI-Verhalten (Profile)

Die KI muss:

1. Vor Flutter-Vorschlägen prüfen, ob dieses Profile aktiv ist.
2. Den kanonischen Stack bevorzugen (keine parallelen State-/Router-/DB-Lösungen ohne Freigabe).
3. Core-Workflow (kleine Schritte, Tests, Security) weiter einhalten.
4. Keine erfundenen Package-APIs; bei Unsicherheit nachfragen.

## Checkliste (Einstieg)

- [ ] Core `.ai/` vorhanden und beachtet
- [ ] Flutter-Profile übernommen / verlinkt
- [ ] Stack-Abweichungen dokumentiert (falls vorhanden)
- [ ] `ARCHITECTURE.md` / Feature-Schnitt verstanden
