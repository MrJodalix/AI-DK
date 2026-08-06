# AI-DK Flutter – Coding

Version: 2.0.1

## Ziel

Dieses Dokument vertieft `.ai/03_CODING_STANDARDS.md` für **Dart und Flutter**.

Es soll sicherstellen:

- idiomatischer, lesbarer Dart-Code
- konsistente Widget- und Riverpod-Nutzung
- sichere Freezed-/Generator-Praxis

---

## Geltungsbereich

Gilt für Dart-/Flutter-Code in Projekten mit Profile `flutter`.

Bei Konflikt:

- Formatter/Linter des Projekts (`analysis_options.yaml`) für Formatdetails
- dieses Dokument für Flutter-spezifische Struktur
- Core `03` für universelle Prinzipien

---

## Grundprinzipien

### Core zuerst

Lesbarkeit, kleine Einheiten, keine stillen Breaking Changes — wie im Core.

### Widgets sind komponierbar

Kleine Widgets mit klarer Verantwortung statt God-Widgets.

### Immutability wo der Stack es verlangt

Freezed-Models und Provider-State bevorzugt unveränderlich.

---

## Verbindliche Regeln

### Dart-Stil

- Öffentliche APIs mit klaren Namen; keine kryptischen Abkürzungen.
- `analysis_options.yaml` beachten; neue Warnungen nicht ignorieren ohne Begründung.
- `dynamic` nur mit Begründung; bevorzugte starke Typen.
- Exceptions nicht schlucken; Fehler sichtbar machen oder bewusst mappen.

### Flutter-Widgets

- `build`-Methoden schlank halten; Extraktion in private Widgets/Methoden.
- Keine teuren Synchronarbeiten in `build`.
- `const` nutzen, wo sinnvoll und korrekt.
- `BuildContext` nicht über `async`-Gaps ohne Prüfung verwenden (`mounted` / Riverpod-Äquivalente).

### Riverpod

- Provider-Typen bewusst wählen (`Provider`, `Notifier`/`AsyncNotifier`, …).
- Kein Business-Critical State nur in lokalen `StatefulWidget`-Feldern, wenn app-weit oder feature-weit nötig.
- Side-Effects nicht versteckt in `build`.

### Freezed

- Für Domänenmodelle mit Equality/Unions Freezed bevorzugen.
- Generierte Dateien nicht manuell ändern.
- Breaking Model-Änderungen inkl. Serialisierung und Tests betrachten.

### Material 3

- Themes zentral; keine wilden Hardcoded-Farben über die App verstreut ohne Theme-Bezug.
- Bestehende Design-Tokens des Projekts respektieren.
- SafeArea, Tastatur, Bottom Sheets, FAB-`heroTag`: siehe `UI.md`.

### I18N / Nutzertexte

- Core: `.ai/12_I18N.md` (technologieunabhängig).
- Flutter: keine hardcodierten nutzersichtbaren Strings in Widgets; Katalog/ARB + Zugriffs-API: siehe `I18N.md`.
- Domänendaten (Kartennamen, API-/DB-Inhalte) gehören nicht in den String-Katalog.

### Dateien und Größe

- Dateien und Widgets teilen, bevor sie unübersichtlich werden (Core-Prinzip „kleine Einheiten“).
- Eine Haupttype-Idee pro Datei anstreben (außer eng gekoppelte private Hilfstypen).

---

## Empfehlungen

- `flutter_lints` / `very_good_analysis` o. Ä. projekteinheitlich.
- Hooks nur bei bewusster Projektentscheidung (`hooks_riverpod`).
- Extension Methods sparsam und domänennah.
- Platform-Channels und `ffi` isolieren.

---

## KI-Verhalten

Die KI muss:

1. Bestehenden Code-Stil und Linter-Config lesen, bevor sie umformatiert.
2. Keine kompletten Dateien ersetzen, wenn ein gezielter Diff reicht (Core).
3. Freezed/Drift-Generator-Folgen mitdenken.
4. Keine erfundenen Flutter-APIs oder Widget-Parameter.

---

## Checkliste

- [ ] Linter/Analyzer-Issues der Änderung adressiert
- [ ] Widgets/Provider ohne versteckte Side-Effects in `build`
- [ ] Freezed/Generated konsistent
- [ ] Theme/Material-3 beachtet
- [ ] UI-Insets / Sheets gemäß `UI.md` (bei Formularen)
- [ ] Nutzertexte gemäß `I18N.md` (kein neues Literal in Widgets)
- [ ] Core-Coding-Prinzipien eingehalten

---

## Beispiele

### Gut

`AsyncNotifier` lädt über Repository; UI reagiert mit `ref.watch` und klaren Loading/Error/Data-Zweigen.

### Schlecht

`build` startet unkontrolliert Netzwerkaufrufe, setzt State über `setState` parallel zu Riverpod und ignoriert Analyzer-Warnings.

---

## Ausnahmen

Generierter oder vendorter Code kann von Stilregeln abweichen.  
Performance-kritische Stellen: Abweichung begründen und begrenzen.

---

## Version

Dokumentversion: 2.0.1

Änderung in dieser Version:

- Verweis I18N / zentrale Nutzertexte (`I18N.md`)

Verwandte Dokumente:

- `.ai/03_CODING_STANDARDS.md`
- `profiles/flutter/STACK.md`
- `profiles/flutter/ARCHITECTURE.md`
- `profiles/flutter/UI.md`
- `profiles/flutter/I18N.md`
- `.ai/12_I18N.md`
- `profiles/flutter/TESTING.md`
