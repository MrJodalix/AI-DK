# AI-DK Flutter – Stack

Version: 2.0.0

## Ziel

Dieses Dokument legt den **kanonischen Technologie-Stack** für Flutter-Projekte unter diesem Profile fest.

Es soll sicherstellen:

- eine klare Default-Wahl statt Tool-Wildwuchs
- nachvollziehbare Abweichungen
- konsistente KI-Empfehlungen

---

## Geltungsbereich

Gilt für Flutter/Dart-Zielprojekte, die das Profile `flutter` aktiv nutzen.

Gilt nicht für:

- Core-Regeln (`.ai/`)
- andere Profiles
- Hosting-/CI-Produkte (Extensions / spätere Vertiefung)

---

## Grundprinzipien

### Eine kanonische Wahl pro Problemklasse

Pro Problemklasse (State, Persistenz, Routing, UI-System, Immutable Models) gibt es genau eine Profile-Default-Lösung.

### Abweichung ist Entscheidung, kein Zufall

Andere Pakete sind erlaubt, wenn begründet und im Projektstand dokumentiert — nicht „nebenbei“ parallel eingeführt.

### Core bleibt unberührt

Stack-Wahl ersetzt keine Coding-/Test-/Security-Prinzipien des Cores.

---

## Verbindliche Regeln

### Kanonischer Stack

| Problemklasse | Muss (Default) | Darf nicht ohne Begründung parallel |
|---------------|----------------|-------------------------------------|
| State Management | **Riverpod** (`flutter_riverpod` / `hooks_riverpod` nach Projektwahl) | Provider, Bloc/Cubit, GetX, MobX als Zweit-System |
| Lokale Persistenz / SQL | **Drift** | parallele ORM-/SQL-Stacks für dieselbe Domäne |
| Immutable Models / Unions | **Freezed** (+ `json_serializable` wo nötig) | handgeschriebene `copyWith`-Wälder ohne Not |
| Navigation | **go_router** | parallele Navigator-2.0-Stacks / auto_route ohne Migration |
| Design-System | **Material 3** (`useMaterial3: true` bzw. aktuelles Flutter-Default) | paralleles zweites Design-System ohne Theme-Strategie |

### Paketwahl

- Bevorzuge **aktive, gut dokumentierte** Pakete aus dem kanonischen Stack.
- Keine neuen Abhängigkeiten „auf Verdacht“.
- Vor Aufnahme: Nutzen, Wartung, Lizenz, Konflikt mit bestehendem Stack prüfen (`10_SECURITY.md` für Secrets/Supply-Chain-Mindestmaß).

### Codegenerierung

Freezed / Drift / json_serializable:

- Generierte Dateien (`*.g.dart`, `*.freezed.dart`) nicht von Hand editieren.
- Generator-Lauf ist Teil der Lieferpflicht vor Commit, wenn neue Annotierungen hinzukamen.
- Breaking Generator-Upgrades bewusst und mit Changelog.

### Flutter-/Dart-SDK

- SDK-Constraints in `pubspec.yaml` müssen zum Projekt passen.
- Keine erfundenen SDK- oder Package-Versionen in Vorschlägen.

---

## Empfehlungen

- `hooks_riverpod` nur, wenn das Projekt Hooks bereits nutzt oder bewusst einführt.
- Feature-first Ordnerstruktur (siehe `ARCHITECTURE.md`).
- Theme über `ThemeData` / `ColorScheme.fromSeed` zentral halten.
- Deep Links und Navigator-APIs über `go_router` bündeln.

---

## KI-Verhalten

Die KI muss:

1. Bei State/DB/Router/UI zuerst den kanonischen Stack vorschlagen.
2. Alternativen nur mit Begründung und Migrationsaufwand nennen.
3. Keine zweiten State- oder Router-Lösungen „kurz zwischendurch“ einführen.
4. Package-Namen und APIs nicht erfinden.

---

## Checkliste

- [ ] State = Riverpod (oder dokumentierte Ausnahme)
- [ ] Persistenz = Drift (oder dokumentierte Ausnahme)
- [ ] Models = Freezed wo Immutability/Unions nötig
- [ ] Navigation = go_router
- [ ] UI = Material 3
- [ ] Keine parallelen Stacks ohne Stand-Eintrag

---

## Beispiele

### Gut

Neues Feature mit `ConsumerWidget`, Drift-DAO, Freezed-Model, Route in `go_router`, Material-3-Widgets.

### Schlecht

Dasselbe Feature mit Provider „nur hier“, plus `Navigator.push`, plus manuellem `copyWith`, parallel zu bestehendem Riverpod/go_router.

---

## Ausnahmen

Abweichungen vom kanonischen Stack sind erlaubt, wenn:

- Altcode eine Migration erzwingt (zeitlich begrenzt dokumentieren), oder
- eine ausdrückliche Projektentscheidung vorliegt, oder
- Plattform-/Kundenanforderungen entgegenstehen.

Jede Ausnahme: Begründung im Projektstand.

---

## Version

Dokumentversion: 2.0.0

Änderung in dieser Version:

- Erstes Flutter-Stack-Dokument (AI-DK 2.0)

Verwandte Dokumente:

- `profiles/flutter/README.md`
- `profiles/flutter/ARCHITECTURE.md`
- `profiles/flutter/CODING.md`
- `.ai/03_CODING_STANDARDS.md`
- `.ai/10_SECURITY.md`
