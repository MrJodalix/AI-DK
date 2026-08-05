# AI-DK Flutter – Architecture

Version: 2.0.1

## Ziel

Dieses Dokument definiert die **Schichten- und Abhängigkeitsregeln** für Flutter-Projekte unter diesem Profile.

Es soll sicherstellen:

- klare Feature- und Schichtgrenzen
- testbare Domänenlogik
- nachvollziehbare Navigation und Persistenz

---

## Geltungsbereich

Gilt für Struktur und Abhängigkeiten in Flutter-Apps und -Packages, die das Profile `flutter` nutzen.

Gilt nicht für:

- universelle Architekturprinzipien des Cores (Charter)
- CI/Hosting-Details

Stack-Wahl: `STACK.md`.

---

## Grundprinzipien

### Abhängungen zeigen nach innen

UI hängt von Application/Domain ab — nicht umgekehrt.  
Infrastructure (Drift, APIs) implementiert Ports/Interfaces der inneren Schichten.

### Features schneiden vertikal

Bevorzuge feature-orientierte Module gegenüber rein technischen Großordnern ohne Feature-Bezug.

### Wenige globale Singletons

App-weite Zustände bewusst und über Riverpod bereitstellen — keine versteckten Service-Locator-Netzwerke.

---

## Verbindliche Regeln

### Empfohlene Schichtensicht

| Schicht | Verantwortung | Typische Artefakte |
|---------|---------------|--------------------|
| Presentation | Widgets, Routing-UI, Riverpod-Consumer | `*Screen`, `*View`, Provider-Wiring |
| Application | Use-Cases, Orchestrierung | Notifier/Controller, Commands |
| Domain | Regeln, Entities, Policies | Freezed-Models, reine Dart-Logik |
| Infrastructure | Drift, HTTP, Platform-Channels | DAOs, APIs, Adapter |

### Abhängigkeitsregeln

1. **Domain** darf Flutter-UI und Infrastruktur-Details nicht importieren.
2. **Presentation** spricht Domain/Application über stabile APIs an — nicht direkt SQL/HTTP-Details streuen.
3. **Drift**-Tabellen/DAOs bleiben in Infrastructure (oder einem klar benannten `data/`-Bereich).
4. **go_router**-Routen zentral oder feature-lokal, aber **eine** Router-Konfiguration als Quelle der Wahrheit.
5. Keine zyklischen Imports zwischen Features.

### Riverpod

- Provider nach Feature gruppieren.
- Side-Effects (Schreiben, Navigation nach Save) klar von reinem Lesen trennen.
- Keine Businessregeln nur in Widgets verstecken, wenn sie wiederverwendbar/testbar sein müssen.

### go_router

- Routen-Namen/Pfade konsistent und dokumentiert halten.
- Auth-/Guard-Logik an einer Stelle, nicht kopiert in jedem Screen.
- Kein wildes Mischen von `Navigator.push` und `go_router` für dieselbe Navigationsdomäne.

### Drift

- Schema-Änderungen versioniert (Migrationen).
- Queries in DAOs/Repositories — nicht in Widgets.
- Transaktionen für zusammengehörige Schreibvorgänge.
- Bei `schemaVersion`-Bump: Kurz-Checkliste in `DEV_SETUP.md`; Upgrade-Test in `TESTING.md`.

### Offline-First und Netzgrenze

Wenn das Projekt Offline-First vorgibt (Produkt/Stand):

1. **Lokale Persistenz ist Primärquelle** für Kernfunktionen (Lesen/Schreiben ohne Netz).
2. HTTP/Netz gehört in Infrastructure (Client/Adapter) hinter Application-Services — **nicht** in Widgets und nicht in Domain-Policies.
3. Online nur für explizit genannte Fälle (z. B. Katalog-Laden, Bilddownload, Sync/Backup). Kernpfade müssen ohne Netz nutzbar bleiben bzw. klar degradieren.
4. Fehler aus dem Netz dürfen Offline-Daten nicht zerstören (kein stilles Überschreiben ohne Absicht).

### Externer HTTP-/API-Client (Mindeststandard)

Bei Anbindung einer dokumentierten Fremd-API:

1. Nur **belegte** Endpoints/Felder (Doku/OpenAPI) — nichts erfinden.
2. Eigenen Client hinter einem Port oder Application-Service (DTO-Mapping getrennt von Drift-Entities).
3. Rate-Limits / Throttle und identifikationsfähiger User-Agent, wenn die API das verlangt.
4. Unit-Tests mit gemocktem HTTP-Client; keine echten Netzcalls in Unit-Tests.
5. Optionale Cloud: siehe Core `05_AI_BEHAVIOR.md` (Port + Unavailable-Stub).

### Undokumentierte / Community-APIs (optional)

Wenn eine Integration **ohne stabile öffentliche Doku** nötig ist (z. B. Drittanbieter-Web-Export):

1. Eigenen Client + DTO-Parser hinter Application-Service; Annahmen im Code und Projektstand dokumentieren.
2. Throttle, User-Agent, klare Fehlerklassen (Netz / Parse / Not Found).
3. Unit-Tests mit Fixtures/Mocks; kein stilles „Raten“ von Endpoints in der UI.
4. Produktverhalten (Match → Nachladen → Besitz) in `PROJECT.md` / Stand festhalten — nicht nur in Architecture.

---

## Empfehlungen

- `lib/features/<feature>/…` plus `lib/core/` für Querschnitt.
- Shared UI-Komponenten ohne Feature-Businesslogik.
- Deep Links und Web-URL-Strategien früh mit `go_router` planen.
- Codegenerierung (Freezed/Drift) in der Architektur als Grenze akzeptieren: Generated gehört zur implementierenden Schicht.

---

## KI-Verhalten

Die KI muss:

1. Vor Strukturvorschlägen bestehende Ordner und Abhängungen lesen.
2. Keine neue Parallelarchitektur neben einer klaren bestehenden legen.
3. Domänenlogik nicht in Widgets verschieben, nur weil es schneller tippt.
4. Migrationen und Router-Änderungen als risikoreich behandeln (Tests, kleine Schritte).

---

## Checkliste

- [ ] Schichten/Features ohne Zyklen
- [ ] Domain ohne UI-/Drift-Imports
- [ ] Eine Router-Quelle der Wahrheit
- [ ] Persistenz hinter DAO/Repository
- [ ] Riverpod-Wiring nachvollziehbar
- [ ] Offline-Kern ohne Netz nutzbar (falls Offline-first)
- [ ] HTTP nur hinter Client/Service; gemockte Tests

---

## Beispiele

### Gut

`features/deck/domain/` mit Freezed-Entity; `data/` mit Drift-DAO; `presentation/` mit `ConsumerWidget` und Route in zentralem `GoRouter`.

### Schlecht

Widget öffnet Drift-Datenbank direkt, baut SQL-Strings und navigiert per `Navigator.push` an `go_router` vorbei.

---

## Ausnahmen

Bestehende Legacy-Apps dürfen schrittweise migrieren. Jede Dauerabweichung dokumentieren.

Plattformplugins mit Zwangskopplung an UI: eng begrenzen und isolieren.

---

## Version

Dokumentversion: 2.0.2

Änderung in dieser Version:

- Undokumentierte HTTP-Integrationen; Verweis Drift-Checkliste / DEV_SETUP

Verwandte Dokumente:

- `profiles/flutter/STACK.md`
- `profiles/flutter/CODING.md`
- `profiles/flutter/UI.md`
- `profiles/flutter/DEV_SETUP.md`
- `profiles/flutter/TESTING.md`
- `.ai/00_PROJECT_CHARTER.md`
- `.ai/03_CODING_STANDARDS.md`
