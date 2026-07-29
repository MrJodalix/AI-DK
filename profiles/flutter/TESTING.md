# AI-DK Flutter – Testing

Version: 2.0.0

## Ziel

Dieses Dokument vertieft `.ai/04_TESTING.md` für **Flutter-Testwerkzeuge**.

Es soll sicherstellen:

- sinnvolle Unit-, Widget- und Integrationstests
- testbare Provider und Domänenlogik
- keine Scheinabdeckung

---

## Geltungsbereich

Gilt für automatisierte Tests in Flutter-Projekten mit Profile `flutter`.

Frameworks (Defaults):

- `flutter_test` (Unit/Widget)
- Integrationstests gemäß Projektsetup (`integration_test` o. Ä.)

Stack-Bezug: Riverpod, Drift, go_router, Freezed — siehe `STACK.md`.

---

## Grundprinzipien

### Qualität vor Abdeckung

Wie Core: wenige aussagekräftige Tests schlagen viele brüchige.

### Domäne zuerst testen

Reine Dart-Logik und Notifier ohne UI sind der stabilste Kern.

### UI-Tests gezielt

Widget-Tests für kritisches Interaktionsverhalten — nicht für jedes Pixel.

---

## Verbindliche Regeln

### Mindestzuordnung (Flutter)

| Änderung | Mindesttest |
|----------|-------------|
| Domänenlogik / Freezed-Mapping | Unit (`flutter_test` / reine Dart-Tests) |
| Riverpod-Notifier mit Regeln | Unit mit Provider-Container |
| Neuer Screen mit Verhalten | Widget-Test |
| Navigation kritischer Flows | Widget- oder Integrationstest |
| Drift-Queries/Migrationen | Unit/Integration gegen Testdatenbank |

### Pflichtregeln

- Nutzerrelevante Features: mindestens ein automatisierter Test (Core).
- Bugfixes: Regressionstest.
- Tests müssen deterministisch sein (keine echten Netz-/Zeitflakes ohne Kontrolle).
- `pump` / `pumpAndSettle` bewusst einsetzen; Timeouts und Animationen beachten.
- Golden-Tests nur, wenn das Projekt sie pflegt — nicht ungefragt flächendeckend einführen.

### Riverpod testen

- `ProviderContainer` / Overrides für Dependencies.
- Keine Abhängigkeit von Produktiv-Backends in Unit-Tests.

### Drift testen

- In-Memory oder isolierte Testdb.
- Migrationen gesondert prüfen, wenn Schema geändert wird.

### go_router testen

- Kritische Redirects/Guards und Deep-Link-Ziele absichern.
- Nicht jede Route mit E2E abdecken.

---

## Empfehlungen

- Page-Objects oder Testhilfen bei wiederholten Widget-Flows.
- `integration_test` für wenige End-to-End-Pfade (Login, Kauf, Sync …).
- Fake/Mock-Infrastruktur hinter Interfaces statt Widget-interner Hardcodes.

---

## KI-Verhalten

Die KI muss:

1. Vor „Tests grün“-Behauptungen echte Ausführung oder ehrlichen Status nennen (Core).
2. Flaky Patterns (echte Timers, Netzwerk) vermeiden.
3. Keine erfundenen Test-APIs.
4. Bei UI-Änderungen bestehende Widget-Tests mitdenken.

---

## Checkliste

- [ ] Passende Testart zur Änderung
- [ ] Provider/Drift isolierbar
- [ ] Keine Secrets in Testdaten (`10_SECURITY.md`)
- [ ] Regression bei Bugfix
- [ ] Lokal/CI-ausführbar dokumentiert

---

## Beispiele

### Gut

Notifier-Test mit überschriebenem Repository; Widget-Test prüft Fehlerzustand bei `AsyncError`.

### Schlecht

Nur ein Smoke-`pumpWidget` ohne Assertion — oder E2E für jede Setter-Methode.

---

## Ausnahmen

Explorative Prototypen dürfen Tests verzögern, wenn der Projektstand das festhält und kein Release daraus wird.

Plattformkanäle: Tests so weit wie sinnvoll mocken; Rest manuell dokumentieren.

---

## Version

Dokumentversion: 2.0.0

Änderung in dieser Version:

- Erstes Flutter-Testing-Dokument (AI-DK 2.0)

Verwandte Dokumente:

- `.ai/04_TESTING.md`
- `profiles/flutter/STACK.md`
- `profiles/flutter/ARCHITECTURE.md`
- `profiles/flutter/CODING.md`
