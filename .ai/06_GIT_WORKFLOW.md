# AI-DK Git Workflow

Version: 1.0.0

## Ziel

Dieses Dokument definiert verbindliche Regeln für Versionskontrolle mit Git innerhalb von Projekten, die AI-DK nutzen.

Es soll sicherstellen:

- nachvollziehbare Historie
- kleine, überprüfbare Änderungen
- stabile Hauptbranches
- kein Verlust oder Verfälschung von Projektgeschichte durch die KI

---

## Geltungsbereich

Gilt für:

- Branch-Strategie
- Commits
- Push und Integration in gemeinsame Branches
- Umgang der KI mit Git-Status und Historie

Gilt nicht für:

- Hosting-Plattformen (GitHub, GitLab, Bitbucket usw.) als Pflicht
- CI/CD-Produkte als Pflicht (Profiles / Extensions); Qualitätsgates vor Releases: `09_RELEASE_PROCESS.md`
- technologieabhängige Hook- oder Toolketten (gehören in Profiles)

Bei Konflikt mit einer engeren projekt- oder organisationsspezifischen Git-Richtlinie gilt die engere Richtlinie. Die Grundprinzipien dieses Dokuments und der Charter bleiben verbindlich.

Kanonische Zuständigkeit für Git gemäß Matrix in `00_PROJECT_CHARTER.md`.

Dieses Dokument ist hosting- und modellunabhängig. Es setzt Git als Versionskontrollsystem voraus.

---

## Grundprinzipien

### Historie ist Dokumentation

Die Commit-Historie erklärt, warum sich das System verändert hat. Sie muss für Menschen lesbar und für Reviews nutzbar bleiben.

### Atomare Änderungen

Ein Commit enthält genau eine logische Änderung. Unzusammenhängende Änderungen gehören in getrennte Commits.

### Hauptlinie bleibt stabil

Gemeinsame Hauptbranches (z. B. `main` oder `master`) nehmen nur geprüfte, integrierbare Zustände auf.

### Keine erfundenen Git-Zustände

Die KI darf Git-Aktionen und -Ergebnisse nicht behaupten, die sie nicht ausgeführt oder verifiziert hat.

---

## Verbindliche Regeln

### Branches

- Für thematisch abgegrenzte Arbeit einen eigenen Branch verwenden, sofern das Projekt Branches nutzt.
- Branchnamen kurz, verständlich und konsistent zur Projektkonvention wählen.
- Direktes Arbeiten auf dem Hauptbranch nur, wenn das Projekt das ausdrücklich so vorgibt.

### Vor dem Commit

- Relevante Tests und statische Checks gemäß `04_TESTING.md` und Projektvorgaben beachten.
- Ein Commit mit bekannten fehlschlagenden Tests ist nicht zulässig.
- Nur Dateien stagen, die zur logischen Änderung gehören.
- Keine Secrets, Zugangsdaten oder privaten Schlüssel committen.

### Commit-Nachrichten

- Beschreiben vorwiegend das **Warum**, nicht nur das Was.
- Eine klare, knappe Zusammenfassung; bei Bedarf ein erklärender Textkörper.
- Projektkonventionen für Präfixe oder Issue-Bezüge einhalten, falls vorhanden.

### Historie schützen

- Öffentliche oder geteilte Historie nicht ohne ausdrückliche Freigabe umschreiben.
- Force-Push auf gemeinsame Hauptbranches ist verboten.
- Force-Push auf andere geteilte Branches nur nach ausdrücklicher Freigabe.
- `commit --amend` und vergleichbare Geschichtsänderungen nur, wenn alle folgenden Punkte gelten:
  1. ausdrückliche Erlaubnis oder klare Projektregel,
  2. Commit wurde in diesem Arbeitskontext erstellt und ist noch nicht veröffentlicht, oder die Projektregel erlaubt den Fall ausdrücklich,
  3. keine Hooks oder Prüflogik werden umgangen, sofern nicht ausdrücklich erlaubt.

### Push und Integration

- Push nur nach Projektkonvention oder ausdrücklicher Anweisung.
- Integration in den Hauptbranch über den im Projekt üblichen Weg (Merge, Rebase, Review-Verfahren).
- Bei Unklarheit nachfragen statt eine Integrationsstrategie zu erfinden.

### Abschluss einer Aufgabe

Eine Aufgabe ist git-seitig erst **vorbereitet**, wenn:

- gewünschte Änderungen **committed** oder klar als **commit-bereit** beschrieben sind (Message + abgegrenzte Dateiliste),
- Branch und — falls committed — Commit-Referenz im Abschlussbericht genannt werden können; sonst explizit „noch nicht committed“ (siehe `02_DEVELOPMENT_WORKFLOW.md` Phase 6).

**Commit ausführen** nur bei ausdrücklicher Freigabe oder klarer Aufgabendeckung (siehe KI-Verhalten unten). „Vorbereitet“ allein ist kein Auftrag zum Committen.

Details zum Entwicklungsablauf stehen in `02_DEVELOPMENT_WORKFLOW.md`. Testpflichten vor dem Commit stehen in `04_TESTING.md`.

---

## Empfehlungen

- Feature- oder Fix-Branches gegenüber lang laufenden Sammelbranches bevorzugen.
- Commits klein halten, damit Reviews und Reverts einfach bleiben.
- Vor Merge/Rebase lokalen Stand mit dem Remote abgleichen, wenn ein Remote genutzt wird.
- Generierte Artefakte und lokale Umgebungswerte nicht versionieren, sofern das Projekt nichts anderes verlangt.
- Pull-/Merge-Requests nutzen, wenn das Projekt sie einsetzt.

---

## KI-Verhalten

Die KI muss:

1. `git status`, Diff und relevante Historie prüfen, bevor sie Git-Aktionen vorschlägt oder ausführt.
2. Nur committen, wenn ausdrücklich gefordert oder klar durch die Aufgabe gedeckt.
3. Keine destruktiven Git-Befehle ausführen (Hard Reset, Force-Push auf Hauptbranches, Historien-Rewrite), sofern nicht ausdrücklich verlangt.
4. Keine Hooks oder Signaturprüfungen umgehen, sofern nicht ausdrücklich erlaubt.
5. Nicht behaupten, ein Commit, Push oder Merge sei erfolgt, wenn das nicht verifiziert wurde.
6. Bei widersprüchlichen Git-Anforderungen den Konflikt benennen und nachfragen.

---

## Checkliste

### Vor dem Commit

- [ ] Logische Einheit der Änderung ist klar
- [ ] Nur zugehörige Dateien gestaged
- [ ] Keine Secrets in der Änderung
- [ ] Tests/Checks laut Projekt und `04_TESTING.md` berücksichtigt
- [ ] Commit-Nachricht erklärt den Grund

### Vor dem Push / der Integration

- [ ] Branch ist der vorgesehene Zielbranch
- [ ] Kein Force-Push auf Hauptbranches
- [ ] Projektkonvention für Review/Merge beachtet
- [ ] Push ist erlaubt oder angeordnet

---

## Beispiele

### Gut: atomarer Commit

Eine Fehlerkorrektur in der Preisberechnung inkl. Regressionstest, Nachricht erklärt die Ursache des Fehlers.

### Schlecht: Sammelcommit

Bugfix, Formatierung vieler Dateien und ein neues Feature in einem Commit ohne klaren Fokus.

### Gut: Branch-Arbeit

`fix/price-rounding` vom Hauptbranch, kleiner Commit, Integration nach Prüfung.

### Schlecht: Historie riskieren

Force-Push auf `main`, um lokale Experimente zu erzwingen.

---

## Ausnahmen

Abweichungen sind nur erlaubt, wenn:

- eine verbindliche Projekt- oder Organisationsrichtlinie entgegensteht, oder
- eine Notfallmaßnahme (z. B. Entfernen geleakter Secrets) dokumentiert und freigegeben ist, oder
- das Repository bewusst ohne Branch-Modell betrieben wird und das dokumentiert ist.

Jede Ausnahme muss begründet werden.

Sicherheitsanforderungen (keine Secrets in der Historie) haben Vorrang vor Bequemlichkeit.

---

## Version

Dokumentversion: 1.0.1

Änderung in dieser Version:

- „Commit vorbereitet“ vs. ausführen; Abschlussbericht darf „noch nicht committed“ nennen

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `04_TESTING.md`
- `05_AI_BEHAVIOR.md`
- `07_DOCUMENTATION.md`
- `09_RELEASE_PROCESS.md`
- `10_SECURITY.md`
