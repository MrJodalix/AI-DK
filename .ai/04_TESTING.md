# AI-DK Testing Strategy

Version: 1.0.0

## Ziel

Tests dienen nicht dazu, eine hohe Testabdeckung zu erreichen.

Tests dienen dazu:

- Fehler frühzeitig zu erkennen
- Regressionen zu verhindern
- Refactorings sicher zu machen
- Vertrauen in Änderungen zu schaffen

Jede Änderung am Projekt soll mit möglichst geringem Risiko erfolgen.

---

## Geltungsbereich

Gilt für automatisierte und manuell dokumentierte Prüfungen im Zielprojekt.

Gilt nicht für stackspezifische Test-Frameworks oder Runner (Profiles).

Kanonische Zuständigkeit für Tests gemäß Matrix in `00_PROJECT_CHARTER.md`.

Commit- und Release-Bezüge: `06_GIT_WORKFLOW.md`, `09_RELEASE_PROCESS.md`.

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Qualität vor Abdeckung

Reihenfolge:

1. Wenige, hochwertige Tests
2. Aussagekräftige Tests
3. Wartbare Tests
4. Hohe Testabdeckung

Testabdeckung ist kein Selbstzweck.

### Vertrauen durch Wiederholbarkeit

Tests sollen deterministisch und verständlich sein.

---

## Verbindliche Regeln

### Testarten

**Unit Tests** — einzelne Module oder Funktionen isoliert (Berechnungen, Parser, Services, Businesslogik, Utilities). Anforderungen: schnell, deterministisch, unabhängig.

**Integration Tests** — Zusammenspiel mehrerer Komponenten (Persistenz, APIs, Nachrichtenaustausch, Synchronisation).

**UI-Tests** — Verhalten der Benutzeroberfläche (Interaktion, Navigation, Formulare, Dialoge).

**End-to-End Tests** — komplette kritische Benutzerabläufe; sparsam einsetzen.

### Wann Tests erstellen

| Änderung | Mindesttest |
|----------|-------------|
| Neue Businesslogik | Unit Test |
| Neue UI | UI-Test |
| Neue Schnittstelle | Integration Test |
| Kritischer Workflow | End-to-End Test |

### Pflichtregeln

- Jede vom Benutzer nutzbare Funktion besitzt mindestens einen automatisierten Test.
- Neue Features dürfen bestehende Tests nicht brechen.
- Bugfixes erhalten einen Regressionstest.
- Jeder behobene Fehler erhält einen Test.

### Testqualität

Ein guter Test besitzt genau einen Zweck, verständliche Namen, keine Seiteneffekte und keine versteckte Logik.

### Testdaten

Reproduzierbar, klein, verständlich. Keine zufälligen Daten als alleinige Grundlage.

### Mocking

Nur wenn notwendig. Bevorzugt echte Domänenobjekte und Modelle. Mocks vor allem für Netzwerk, Datenbanken und externe Systeme.

### Vor jedem Commit

Tests, statische Analyse und Formatierung gemäß Projektvorgabe erfolgreich. Ein Commit mit fehlschlagenden Tests ist nicht zulässig.

---

## Empfehlungen

- Vorhandene Tests erweitern, bevor neue parallele Tests entstehen.
- Instabile Tests zeitnah reparieren oder bewusst quarantänisieren und dokumentieren.
- E2E auf die wertvollsten Pfade begrenzen.

---

## KI-Verhalten

Bei jeder Änderung prüfen:

- Welche bestehenden Tests sind betroffen?
- Welche neuen Tests werden benötigt?
- Existiert bereits ein ähnlicher Test?
- Kann ein vorhandener Test erweitert werden?

Die KI darf niemals behaupten, Tests erfolgreich ausgeführt zu haben, wenn sie diese nicht tatsächlich ausführen konnte.

---

## Checkliste

Vor Abschluss einer Aufgabe:

- [ ] Alle relevanten Tests vorhanden
- [ ] Regressionen berücksichtigt
- [ ] Neue Logik getestet
- [ ] Bestehende Tests bleiben gültig
- [ ] Testnamen verständlich
- [ ] Testdaten nachvollziehbar
- [ ] Keine doppelten Tests
- [ ] Keine instabilen Tests

---

## Beispiele

### Gut

Bugfix inkl. Test, der den Fehler reproduziert und nach dem Fix grün ist.

### Schlecht

Hohe Abdeckung durch aussagelose Tests ohne Verhaltensprüfung.

---

## Ausnahmen

Explorative Spikes ohne Produktivpfad dürfen Tests kurzfristig schuldig bleiben — Übergang in den Hauptpfad nur mit Tests.

Organisatorische Testmindeststandards können strenger sein.

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Einheitliche Dokumentstruktur (Sprint 4)
- Inhalt der Teststrategie beibehalten
- Verweis auf Charter-Zuständigkeitsmatrix

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `03_CODING_STANDARDS.md`
- `05_AI_BEHAVIOR.md`
- `06_GIT_WORKFLOW.md`
- `09_RELEASE_PROCESS.md`
