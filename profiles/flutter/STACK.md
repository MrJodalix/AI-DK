# AI-DK Flutter – Stack

Version: 2.0.3

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
| I18N / UI-Texte | **Flutter `gen-l10n`** (`.arb` + generierte Localizations) — konkretisiert Core `12_I18N.md` | Hardcodierte Nutzer-Strings in Widgets; paralleles i18n-Paket ohne Stand-Eintrag |

### Riverpod Runtime vs. Codegenerierung

- **Kanonisch und Pflicht:** Riverpod-Runtime (`flutter_riverpod` bzw. projektgewähltes Äquivalent).
- **Empfohlen:** `riverpod_annotation` + `riverpod_generator` für neue Provider, sofern der Resolver es zulässt.
- **Erlaubte Ausnahme:** manuelle Provider ohne Generator, wenn Pub-Resolver-Konflikte mit anderen kanonischen Paketen (z. B. Drift/Freezed) bestehen — Begründung und geplanter Upgrade-Pfad im **Projektstand**.
- Kein zweites State-System als „Ausweg“ aus einem Generator-Konflikt.

### Paketwahl

- Bevorzuge **aktive, gut dokumentierte, stabile** Releases aus dem kanonischen Stack.
- Keine neuen Abhängigkeiten „auf Verdacht“.
- Vor Aufnahme: Nutzen, Wartung, Lizenz, Konflikt mit bestehendem Stack prüfen (`10_SECURITY.md` für Secrets/Supply-Chain-Mindestmaß).

### Pre-Release-Abhängigkeiten

- Pre-Releases (`-dev`, `-alpha`, `-beta`, `-rc`) sind **nicht Default**.
- Zulässig nur mit Begründung und Eintrag im Projektstand (Risiko, Warum, Ausstiegskriterium).
- Vor Feature-Arbeit Stabilität erneut prüfen; sobald ein stabiles Release den Bedarf deckt, umstellen.
- Pre-Releases **blockieren** Feature-Arbeit nicht dauerhaft (siehe `05_AI_BEHAVIOR.md`), solange Stand und Ausstiegskriterium gepflegt sind — aber Upgrade-Druck bleibt.

### Pub-Resolver-Konflikte im kanonischen Stack

Wenn zwei kanonische Pakete nicht gemeinsam auflösbar sind:

1. Konflikt und betroffene Pakete dokumentieren (Projektstand).
2. Optionen bewerten in Charter-Reihenfolge: Wartbarkeit → Stabilität → …  
   typisch: Version pinnen, bewusstes Major-Upgrade einer Seite, oder Generator/Neben-Dep vorübergehend aussetzen.
3. Gewählte Ausnahme im Stand + Changelog festhalten; paralleles Zweit-System bleibt verboten.
4. Keine erfundenen Package-Versionen oder „force“-Overrides ohne Beleg.

### Codegenerierung

Freezed / Drift / json_serializable (und ggf. Riverpod-Generator):

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
- Nach Stack-Upgrades (z. B. Riverpod 3) Generator-Nutzung erneut prüfen.
- Nutzertexte: Core `.ai/12_I18N.md`; Flutter-Mechanismus `gen-l10n` (siehe `I18N.md`); Domänendaten nicht in ARB spiegeln.

---

## KI-Verhalten

Die KI muss:

1. Bei State/DB/Router/UI zuerst den kanonischen Stack vorschlagen.
2. Alternativen nur mit Begründung und Migrationsaufwand nennen.
3. Keine zweiten State- oder Router-Lösungen „kurz zwischendurch“ einführen.
4. Package-Namen und APIs nicht erfinden.
5. Resolver-Konflikte und Pre-Releases dokumentieren statt stillschweigend hinzunehmen.
6. Fremd-HTTP nur hinter belegtem Client (siehe `ARCHITECTURE.md`); optionale Cloud als Port + Stub.

---

## Checkliste

- [ ] State = Riverpod-Runtime (oder dokumentierte Ausnahme)
- [ ] Riverpod-Generator genutzt oder Ausnahme im Stand
- [ ] Persistenz = Drift (oder dokumentierte Ausnahme)
- [ ] Models = Freezed wo Immutability/Unions nötig
- [ ] Navigation = go_router
- [ ] UI = Material 3
- [ ] I18N = gen-l10n (oder dokumentierter Übergangskatalog laut `I18N.md`)
- [ ] Keine parallelen Stacks ohne Stand-Eintrag
- [ ] Pre-Releases nur mit Stand-Eintrag

---

## Beispiele

### Gut

Neues Feature mit `ConsumerWidget`, Drift-DAO, Freezed-Model, Route in `go_router`, Material-3-Widgets.

### Gut (dokumentierte Ausnahme)

`riverpod_generator` zurückgestellt wegen Pub-Konflikt mit Drift/Freezed; manuelle Provider; Stand nennt Upgrade auf Riverpod 3 + Generator als nächsten Schritt.

### Schlecht

Dasselbe Feature mit Provider „nur hier“, plus `Navigator.push`, plus manuellem `copyWith`, parallel zu bestehendem Riverpod/go_router.

### Schlecht

Pre-Release von Freezed ohne Stand-Eintrag und ohne Ausstiegskriterium.

---

## Ausnahmen

Abweichungen vom kanonischen Stack sind erlaubt, wenn:

- Altcode eine Migration erzwingt (zeitlich begrenzt dokumentieren), oder
- eine ausdrückliche Projektentscheidung vorliegt, oder
- Plattform-/Kundenanforderungen entgegenstehen, oder
- ein belegter Pub-Resolver-Konflikt die volle Generator-Suite blockiert (siehe oben).

Jede Ausnahme: Begründung im Projektstand.

---

## Version

Dokumentversion: 2.0.3

Änderung in dieser Version:

- I18N / `gen-l10n` als kanonische Problemklasse (siehe `I18N.md`)

Verwandte Dokumente:

- `profiles/flutter/README.md`
- `profiles/flutter/ARCHITECTURE.md`
- `profiles/flutter/CODING.md`
- `profiles/flutter/I18N.md`
- `.ai/12_I18N.md`
- `.ai/03_CODING_STANDARDS.md`
- `.ai/10_SECURITY.md`
