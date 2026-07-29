# AI-DK Documentation

Version: 1.0.0

## Ziel

Dieses Dokument definiert, welche Projektdokumentation erforderlich ist, wann sie aktualisiert wird und wie die KI damit umgeht.

Es soll sicherstellen:

- nachvollziehbarer Projektstand
- klare Verantwortlichkeiten der Dokumente
- keine veraltete oder doppelte Dokumentation
- Dokumentation als fester Bestandteil der Entwicklung

---

## Geltungsbereich

Gilt für:

- projektspezifische Markdown-Dokumentation im Zielprojekt
- Aktualisierungspflichten nach Aufgaben
- Abgrenzung zwischen Dokumenttypen

Gilt nicht für:

- AI-DK-Core-Dokumente unter `.ai/` (werden über die AI-DK-Version gesteuert)
- reine Code-Kommentare (siehe `03_CODING_STANDARDS.md`)
- technologieabhängige API-Doku-Generatoren (gehören in Profiles)

Bei Konflikt mit einer bestehenden Projekt-Dokumentationsstruktur gilt die vorhandene Struktur. Die KI übernimmt etablierte Namen und Orte und erfindet keine parallele Dokumentationslandschaft.

Kanonische Zuständigkeit für Projektdokumentation gemäß Matrix in `00_PROJECT_CHARTER.md`.

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Dokumentation ist Teil der Lieferung

Eine Aufgabe ohne aktualisierte, notwendige Dokumentation gilt als unvollständig.

### Ein Thema, ein kanonisches Dokument

Dieselbe Information nicht an mehreren Stellen pflegen. Querverweise statt Duplikate.

### Aktuell vor vollständig

Lieber kurze, korrekte Dokumentation als umfangreiche, veraltete Texte.

### Bestehende Struktur respektieren

Vorhandene Dokumente erweitern statt neue Parallelwelten anzulegen.

---

## Verbindliche Regeln

### Kanonische Projektdokumente

Sofern das Projekt keine abweichenden Namen vorgibt, gelten folgende Rollen:

| Dokument | Rolle |
|----------|--------|
| `PROJECT.md` | Zweck, Umfang, Kontext, wichtige Einstiege |
| `ARCHITECTURE.md` | Struktur, Grenzen, zentrale Entscheidungen |
| `TODO.md` | offene Aufgaben, Prioritäten, bekannte Lücken |
| `CHANGELOG.md` | chronologische, für Menschen lesbare Änderungsübersicht |
| `08_PROJECT_STATE.md` bzw. projektspezifischer Stand | aktueller Arbeitsstand für die KI (siehe `08_PROJECT_STATE.md`) |

Optional, wenn zutreffend:

| Dokument | Rolle |
|----------|--------|
| Daten-/Persistenzdokumentation (z. B. `DATABASE.md`) | Schema, Speicher, Migrationen, Datenflüsse |
| weitere Fachdokumente | nur wenn ein klares, eigenes Thema existiert |

Die KI legt optionale Dokumente nur an, wenn der Bedarf besteht oder der Entwicklungsworkflow es verlangt (z. B. Projektübernahme).

### Wann aktualisieren

Nach jeder abgeschlossenen Aufgabe prüfen und bei Relevanz aktualisieren:

1. `CHANGELOG.md` — was geändert wurde und warum (kurz)
2. `TODO.md` — erledigte Punkte entfernen oder abhaken; neue offene Punkte ergänzen
3. Architektur- oder Fachdokumentation — nur wenn Struktur, Schnittstellen oder Entscheidungen betroffen sind
4. Projektstand-Dokument — gemäß `08_PROJECT_STATE.md`

Keine Schein-Updates: unveränderte Dokumente nicht „der Vollständigkeit halber“ umformulieren.

### Was wohin gehört

- **Warum einer Änderung (kurz, chronologisch)** → `CHANGELOG.md`
- **Was noch offen ist** → `TODO.md`
- **Wie das System aufgebaut ist** → `ARCHITECTURE.md`
- **Worum es im Projekt geht** → `PROJECT.md`
- **Woran gerade gearbeitet wird / aktueller Kontext** → Projektstand (`PROJECT_STATE`)
- **Lokales Warum im Code** → Kommentare gemäß Coding Standards

### Verbotene Praktiken

- parallele Dokumente mit gleichem Zweck unter neuem Namen
- Copy-Paste ganzer Abschnitte zwischen Dokumenten
- Spekulation als dokumentierte Tatsache
- Geheimnisse, Tokens oder Zugangsdaten in Dokumentation

### Projektübernahme

Bei bestehenden Projekten ohne Dokumentation gilt der Ablauf in `02_DEVELOPMENT_WORKFLOW.md` (Phase B). Dokumente werden dort angelegt, nicht erfunden befüllt: Unbekanntes als offen kennzeichnen.

---

## Empfehlungen

- Dokumente kurz halten; Details bei Bedarf in verlinkte Abschnitte oder ADR-ähnliche Notizen auslagern (ADRs vertieft in späteren Versionen).
- In `ARCHITECTURE.md` Entscheidungen mit kurzer Begründung festhalten, nicht nur Ist-Zustände listen.
- In `TODO.md` priorisieren und erledigte Einträge regelmäßig bereinigen.
- Dateiorte im Repository-Root oder unter `docs/` der Projektkonvention folgen; nicht mischen ohne Grund.
- Screenshots und binäre Anhänge sparsam und nur mit klarem Nutzen verwenden.

---

## KI-Verhalten

Die KI muss:

1. Vor Aufgaben bestehende Dokumentation lesen, soweit vorhanden und relevant.
2. Nach Aufgaben die Aktualisierungspflicht prüfen (CHANGELOG, TODO, Architektur, Stand).
3. Fehlende notwendige Dokumentation benennen und gezielt vorschlagen — nicht stillschweigend weglassen.
4. Keine Dokumentationsinhalte erfinden (APIs, Entscheidungen, Zustände).
5. Bei Unklarheit über kanonische Dateinamen nachfragen oder die vorhandene Struktur übernehmen.
6. AI-DK-Core-Regeln nicht in Projektdokumente kopieren; bei Bedarf darauf verweisen.

---

## Checkliste

### Nach einer Aufgabe

- [ ] `CHANGELOG.md` bei relevanter Änderung aktualisiert
- [ ] `TODO.md` an den neuen Stand angepasst
- [ ] Architektur-/Fachdokumente nur bei echtem Bedarf geändert
- [ ] Keine Duplikate oder Widersprüche eingeführt
- [ ] Keine Secrets dokumentiert
- [ ] Unbekanntes als offen gekennzeichnet, nicht erfunden

### Bei Projektübernahme

- [ ] Vorhandene Docs inventarisiert
- [ ] Lücken benannt
- [ ] Nur notwendige kanonische Docs angelegt
- [ ] Inhalt auf Belegen aus dem Code gestützt

---

## Beispiele

### Gut

Kleine API-Änderung: Eintrag in `CHANGELOG.md`, betroffenen TODO-Punkt schließen, `ARCHITECTURE.md` unverändert lassen.

### Schlecht

Dieselbe API-Änderung ausführlich in `PROJECT.md`, `ARCHITECTURE.md` und `CHANGELOG.md` wiederholen und zusätzlich eine neue Datei `API_NOTES.md` anlegen.

### Gut

Unklarheit über Persistenz: In der Dokumentation „offen / zu klären“ vermerken und nachfragen.

### Schlecht

Ein `DATABASE.md` mit vermutetem Schema schreiben, das im Code nicht belegt ist.

---

## Ausnahmen

Abweichungen sind erlaubt, wenn:

- das Projekt verbindliche andere Dokumentnamen oder -orte vorgibt, oder
- regulatorische/organisatorische Vorlagen Vorrang haben, oder
- ein Dokumenttyp für das Projekt nachweislich irrelevant ist (dann nicht anlegen).

Die Abwesenheit von Dokumentation ist keine Ausnahme für abgeschlossene Aufgaben, wenn CHANGELOG/TODO oder Architektur von der Änderung betroffen sind.

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Querverweis auf Charter-Matrix (Sprint 4 Konsistenz)

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `03_CODING_STANDARDS.md`
- `05_AI_BEHAVIOR.md`
- `06_GIT_WORKFLOW.md`
- `08_PROJECT_STATE.md`
- `09_RELEASE_PROCESS.md`
- `11_VERSION.md`
