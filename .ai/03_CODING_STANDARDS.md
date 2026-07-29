# AI-DK Coding Standards

Version: 1.0.2

## Ziel

Dieses Dokument definiert verbindliche Regeln für die Erstellung, Änderung und Bewertung von Code.

Es soll sicherstellen:

- verständlicher Code
- wartbarer Code
- testbarer Code
- geringe technische Schulden
- langfristige Erweiterbarkeit

Code wird nicht nur für den aktuellen Entwickler geschrieben, sondern für zukünftige Entwickler und Wartung.

---

## Geltungsbereich

Gilt für:

- neuen Code
- Änderungen an bestehendem Code
- Refactorings
- Code Reviews durch die KI

Gilt nicht für:

- projektspezifische Styleguides einzelner Sprachen oder Frameworks
- Formatierungsdetails, die ein Formatter oder Linter des Projekts bereits regelt

Bei Konflikt zwischen diesem Dokument und einem projektspezifischen Styleguide gilt der projektspezifische Styleguide für sprach- oder toolbezogene Details. Die Grundprinzipien dieses Dokuments und der Charter bleiben verbindlich.

Kanonische Zuständigkeit für Code-Struktur und Stil gemäß Matrix in `00_PROJECT_CHARTER.md`.

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Lesbarkeit vor Kürze

Bevorzuge:

- klare Namen
- kleine Funktionen
- eindeutige Strukturen

Vermeide:

- schwer verständliche Abkürzungen
- übermäßig kompakte Lösungen
- cleveren, aber unlesbaren Code

---

### Einfachheit vor Komplexität

Die einfachste Lösung, die alle Anforderungen erfüllt, wird bevorzugt.

Vermeide:

- unnötige Abstraktionen
- Frameworks oder Bibliotheken ohne echten Nutzen
- vorzeitige Optimierung

---

### Single Responsibility Principle

Jede Klasse, jedes Modul und jede Funktion besitzt genau eine klare Verantwortung.

Vermeide:

- God Classes / God Modules
- riesige Services
- UI- oder Präsentationscode mit Businesslogik
- Dateien mit mehreren unabhängigen Aufgaben

---

### Konsistenz mit bestehendem Code

Neuer Code folgt den im Projekt bereits etablierten Mustern, sofern diese den Grundprinzipien nicht widersprechen.

Lokale Inkonsistenz nur erzeugen, wenn sie bewusst und begründet ist.

---

## Verbindliche Regeln

### Strukturierung – Module und Typen

Module, Klassen und vergleichbare Einheiten sollen:

- eine klare Aufgabe besitzen
- kleine öffentliche Schnittstellen haben
- einfach testbar sein

Vermeide:

- Einheiten mit sehr vielen öffentlichen Methoden
- globale veränderliche Zustände
- versteckte Seiteneffekte

---

### Strukturierung – Funktionen

Funktionen sollen:

- möglichst kurz sein
- eine Aufgabe erfüllen
- verständliche Parameter besitzen
- nachvollziehbare Rückgaben liefern

Bevorzuge sprechende Namen:

```text
calculateTotalPrice()
```

Vermeide unklare Namen:

```text
doIt()
handle()
process2()
```

---

### Benennung

Namen müssen Absicht und Inhalt ausdrücken.

Regeln:

- Namen beschreiben das Was, nicht das Wie der Implementierung.
- Boolesche Namen drücken einen Zustand oder eine Entscheidung aus.
- Vermeide bedeutungslose Präfixe und Nummerierungen.
- Halte dich an die im Projekt etablierte Namenskonvention.

---

### Abhängigkeiten und Kopplung

Regeln:

- Abhängigkeiten möglichst gering halten.
- Richtung der Abhängigkeiten klar und nachvollziehbar halten.
- Zyklische Abhängigkeiten vermeiden.
- Businesslogik nicht an UI-, I/O- oder Infrastrukturdetails koppeln.

Neue Abhängigkeiten (Bibliotheken, Module, Dienste) nur einführen, wenn Nutzen und Risiko begründet sind.

---

### Fehlerbehandlung

Regeln:

- Fehler nicht stillschweigend ignorieren.
- Fehler an der Stelle behandeln, die genug Kontext für eine sinnvolle Reaktion hat.
- Fehlermeldungen und Fehlerzustände müssen Diagnose ermöglichen.
- Keine leeren Fangblöcke ohne Begründung.

---

### Seiteneffekte

Regeln:

- Seiteneffekte sichtbar und begrenzt halten.
- Reine Berechnungen von I/O und Zustandsänderungen trennen, soweit sinnvoll.
- Globale oder implizite Zustandsänderungen vermeiden.

---

### Kommentare und Code-Dokumentation

Regeln:

- Code soll sich möglichst selbst erklären.
- Kommentare erklären Warum und Einschränkungen, nicht das offensichtliche Was.
- Veraltete oder irreführende Kommentare korrigieren oder entfernen.
- Bestehende Kommentare nicht ohne Grund löschen.

---

### Änderungen an bestehendem Code

Regeln:

- Nur notwendige Bereiche ändern.
- Bestehende Funktionalität erhalten.
- Keine unnötigen Komplett-Neuschreibungen.
- Keine gleichzeitigen, unzusammenhängenden Refactorings in derselben Änderung.

Wenn eine komplette Neuschreibung notwendig erscheint:

1. Ursache erklären.
2. Auswirkungen beschreiben.
3. Alternativen prüfen.

---

### Testbarkeit

Code muss so gestaltet sein, dass er testbar ist.

Regeln:

- Logik von schwer testbaren Randbereichen (UI, Netzwerk, Dateisystem) entkoppeln, soweit sinnvoll.
- Versteckte globale Zustände vermeiden.
- Öffentliche Verhaltensweisen klar und prüfbar halten.

Detaillierte Testpflichten stehen in `04_TESTING.md`.

---

## Empfehlungen

- Bevorzuge flache, nachvollziehbare Aufrufketten gegenüber tiefer Verschachtelung.
- Bevorzuge explizite Datenflüsse gegenüber implizitem Shared State.
- Extrahiere wiederkehrende Logik erst, wenn Wiederverwendung oder Klarheit es rechtfertigen.
- Optimiere erst nach nachgewiesenem Bedarf.
- Halte öffentliche APIs stabiler als interne Hilfsfunktionen.

---

## KI-Verhalten

Die KI muss bei Codeänderungen:

1. Bestehende Struktur und Namenskonventionen prüfen.
2. Nur den notwendigen Bereich ändern.
3. Keine neuen Abstraktionen ohne konkreten Nutzen einführen.
4. Keine erfundenen APIs, Typen oder Bibliotheken verwenden.
5. Abweichungen von diesen Standards begründen.
6. Bei Unsicherheit nachfragen statt raten.

Die KI bewertet vorgeschlagenen Code anhand dieses Dokuments und der Entscheidungsgrundlagen in `00_PROJECT_CHARTER.md`.

---

## Checkliste

### Vor dem Schreiben neuen Codes

- [ ] Verantwortung der Einheit ist klar
- [ ] Bestehende ähnliche Implementierung geprüft
- [ ] Namenskonvention des Projekts bekannt
- [ ] Testbarkeit berücksichtigt

### Vor Abschluss einer Codeänderung

- [ ] Nur notwendige Bereiche geändert
- [ ] Namen sind verständlich
- [ ] Keine versteckten Seiteneffekte eingeführt
- [ ] Fehlerbehandlung vorhanden und sinnvoll
- [ ] Kommentare aktuell und nicht irreführend
- [ ] Keine unnötige neue Abhängigkeit
- [ ] Änderung bleibt klein und nachvollziehbar

---

## Beispiele

### Gut: klare Verantwortung

```text
calculateTotalPrice(items, taxRate) -> money
```

Eine Funktion, ein Zweck, sprechender Name.

### Schlecht: unklare Verantwortung

```text
handle(data)
```

Name und Parameter verraten weder Zweck noch Ergebnis.

### Gut: gezielte Änderung

Nur die fehlerhafte Berechnungsfunktion und den zugehörigen Test anpassen.

### Schlecht: ungezielte Änderung

Dieselbe Berechnung „nebenbei“ umbenennen, formatieren und in ein neues Modul verschieben.

---

## Ausnahmen

Abweichungen sind nur erlaubt, wenn:

- eine projektspezifische Vorgabe entgegensteht, oder
- externe Schnittstellen oder Altcode die Abweichung erzwingen, oder
- die Abweichung zeitlich begrenzt und dokumentiert ist.

Jede Ausnahme muss begründet werden.

Sicherheits- oder Korrektheitsanforderungen haben Vorrang vor Stilpräferenzen.

---

## Version

Dokumentversion: 1.0.2

Änderung in dieser Version:

- Abschnittstitel `Checkliste` vereinheitlicht (Qualitätsrelease 1.0.2)

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `04_TESTING.md`
- `05_AI_BEHAVIOR.md`
- `10_SECURITY.md`
