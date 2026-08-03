# AI-DK Development Workflow

Version: 1.0.0

## Ziel

Dieses Dokument definiert den verbindlichen Entwicklungsprozess innerhalb des Projekts.

Jede Aufgabe wird nach diesem Ablauf bearbeitet, um kontrollierte Entwicklung, nachvollziehbare Änderungen, geringe technische Schulden und stabile Software zu erreichen.

---

## Geltungsbereich

Gilt für alle Entwicklungsaufgaben mit KI-Unterstützung im Zielprojekt.

**Sitzungsstart:** `01_BOOTSTRAP.md` — vor Analyse und Code.

Spezialregeln (kanonisch; Matrix: `00_PROJECT_CHARTER.md`):

- Prinzipien / Entscheidungen → `00_PROJECT_CHARTER.md`
- Agenten-Einstieg → `01_BOOTSTRAP.md`
- Code → `03_CODING_STANDARDS.md`
- Tests → `04_TESTING.md`
- KI-Verhalten → `05_AI_BEHAVIOR.md`
- Git → `06_GIT_WORKFLOW.md`
- Dokumentation → `07_DOCUMENTATION.md`
- Projektstand → `08_PROJECT_STATE.md`
- Release → `09_RELEASE_PROCESS.md`
- Security → `10_SECURITY.md`
- Versionierung → `11_VERSION.md`

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Keine Änderung beginnt mit Code

Zuerst Bootstrap (`01_BOOTSTRAP.md`), dann der Ablauf:

1. Verstehen
2. Analysieren
3. Planen
4. Umsetzen
5. Prüfen
6. Dokumentieren
7. Abschließen

### Entscheidungen kanonisch

Bei mehreren Lösungen gelten die Kriterien in `00_PROJECT_CHARTER.md`.

---

## Verbindliche Regeln

### Phase 1 – Analyse

Das Problem vollständig verstehen. Vor Umsetzung prüfen:

- bestehende Implementierung
- betroffene Dateien
- Architektur
- Abhängigkeiten
- Datenfluss
- bestehende Tests
- mögliche Seiteneffekte

Vor Codeänderungen muss klar sein: Was, Warum, betroffene Komponenten, Risiken.

### Phase 2 – Planung

Die Planung enthält: vorgeschlagene Lösung, betroffene Dateien, notwendige Änderungen, Alternativen, Risiken.

Bei kleinen Änderungen kann die Planung kurz sein. Bei Architekturänderungen ist eine ausführliche Begründung erforderlich.

### Phase 3 – Umsetzung

Umsetzung gemäß Charter (kleine Änderungen) und `03_CODING_STANDARDS.md`:

- bestehende Funktionalität erhalten
- keine unnötigen Refactorings
- keine Nebenfeatures
- nur den notwendigen Bereich verändern

### Phase 4 – Qualitätssicherung

**Code:** kompiliert/ausführbar nach Projektmaßstab, Formatierung, keine bekannten Analysefehler.

**Tests:** bestehende Tests erfolgreich; neue Tests falls erforderlich (`04_TESTING.md`).

**Funktion:** gewünschtes Verhalten; keine Beschädigung bestehender Funktionen.

### Phase 5 – Dokumentation

Nach abgeschlossener Aufgabe aktualisieren: CHANGELOG, TODO, relevante Architektur-Dokumentation — gemäß `07_DOCUMENTATION.md`.

### Phase 6 – Abschluss

Abgeschlossen erst wenn: Code fertig, Tests erfolgreich, Dokumentation aktualisiert, Git-Stand **vorbereitet** (`06_GIT_WORKFLOW.md`).

**„Git-Commit vorbereitet“** bedeutet:

1. `git status` / Diff geprüft und die logische Änderung abgegrenzt
2. Commit-Nachricht (Schwerpunkt **Warum**) formuliert oder im Abschlussbericht vorgeschlagen
3. Im Abschlussbericht: Branch, commit-bereite Dateiliste bzw. Status, und ob ein Commit **ausgeführt** wurde

**Commit ausführen** nur, wenn ausdrücklich gefordert oder klar durch Aufgabe/Projektregel gedeckt (`06_GIT_WORKFLOW.md`). Engere User- oder Projektrechtslinien (z. B. „nur auf Anweisung committen“) haben Vorrang.

### Große Aufgaben

Große Aufgaben werden in überprüfbare Schritte zerlegt (z. B. Datenmodell → Persistenz → Zugriffsschicht → Zustand → UI → Tests → Dokumentation).

### Meilensteine / Epics (z. B. P0–Pn)

Über mehrere Lieferungen hinweg:

1. Pro Meilenstein: lauffähiger Stand + Tests + Docs (`CHANGELOG`, `TODO`, Stand).
2. SemVer-/Produktversion gemäß Projektkonvention anheben, wenn der Meilenstein nutzbaren Umfang liefert.
3. Phase-2-Planung darf bei klar abgegrenzten Meilensteinen kurz sein; Architektur- und Stack-Entscheidungen bleiben schriftlich (Stand oder Architekturdoc).

### Bestehende Projekte übernehmen

1. **Aufnahme** — keine Änderungen; Struktur, Architektur, Probleme erfassen
2. **Dokumentation** — kanonische Docs anlegen (`07_DOCUMENTATION.md`)
3. **Sanierungsplanung** — Schulden, Risiken, Prioritäten
4. **Sanierung** — nur nach Freigabe; ein Problem nach dem anderen

### Neue Features

Erst wenn Architektur verstanden, Auswirkungen geprüft und notwendige Dokumentation vorhanden ist.

### Abschlussbericht

Jede Aufgabe endet mit: Zusammenfassung, Dateien, Tests, Dokumentation, Git (Branch/Commit), nächster Schritt.

---

## Empfehlungen

- Bei Unsicherheit in der Analyse nachfragen, bevor geplant wird.
- Architekturänderungen früh und schriftlich begründen.
- Sanierung und neue Features nicht vermischen.

---

## KI-Verhalten

Die KI folgt diesem Ablauf bei jeder Aufgabe. Sie beginnt nicht mit Code, bevor Analyse (und bei Bedarf Planung) greifbar sind.

Sie zerlegt große Aufgaben selbstständig und fordert Freigabe vor Sanierung bestehender Systeme.

Weitere Verhaltensregeln: `05_AI_BEHAVIOR.md`.

---

## Checkliste

- [ ] Analyse abgeschlossen (Was / Warum / Risiken)
- [ ] Planung angemessen zum Umfang
- [ ] Umsetzung auf notwendigen Bereich begrenzt
- [ ] Qualitätssicherung (Code / Tests / Funktion)
- [ ] Dokumentation aktualisiert
- [ ] Git vorbereitet
- [ ] Abschlussbericht erstellt

---

## Beispiele

### Gut

Authentifizierung in Schritten: Modell → Persistenz → API → UI → Tests → Docs.

### Schlecht

„Komplette Authentifizierung“ in einem undifferenzierten Umbau ohne Analyse.

---

## Ausnahmen

Sehr kleine, risikoarme Korrekturen dürfen Analyse und Planung kurz halten — aber nicht auslassen.

Explizite Anweisung des Menschen kann Phasen kürzen; Risiken bleiben zu benennen.

---

## Version

Dokumentversion: 1.0.2

Änderung in dieser Version:

- Meilensteine/Epics: Docs/Tests/Version je Lieferung; Planungskürze bei klaren Schnitten

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `03_CODING_STANDARDS.md`
- `04_TESTING.md`
- `05_AI_BEHAVIOR.md`
- `06_GIT_WORKFLOW.md`
- `07_DOCUMENTATION.md`
- `08_PROJECT_STATE.md`
- `09_RELEASE_PROCESS.md`
- `10_SECURITY.md`
- `11_VERSION.md`
