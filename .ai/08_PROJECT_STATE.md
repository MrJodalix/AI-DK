# AI-DK Project State

Version: 1.0.0

## Ziel

Dieses Dokument definiert den **aktuellen Arbeitsstand** eines Projekts für KI und Entwickler.

Es soll sicherstellen:

- schneller Einstieg in den Ist-Zustand
- keine wiederholte Neu-Entdeckung bereits bekannter Fakten
- klare Trennung zu langfristiger Architektur- und Aufgabendokumentation
- kontinuierlich gepflegter Kontext über Sitzungen hinweg

---

## Geltungsbereich

Gilt für:

- den lebendigen Projektstand unter `.ai/08_PROJECT_STATE.md` (oder dem vom Projekt festgelegten Äquivalent)
- Lesen und Aktualisieren dieses Stands durch die KI

Gilt nicht für:

- vollständige Architektur (`ARCHITECTURE.md` / `07_DOCUMENTATION.md`)
- chronologische Historie (`CHANGELOG.md`)
- offene Aufgabenliste als Führungsinstrument (`TODO.md`) — der Stand darf darauf verweisen, sie aber nicht ersetzen
- AI-DK-Core-Regeln selbst (Charter, Workflow, …)

Dieses Dokument ist technologie- und modellunabhängig. Stack-Details gehören nur als Fakten des konkreten Projekts in den Stand-Abschnitt, nicht als universelle Regeln.

Kanonische Zuständigkeit für den lebendigen Projektstand gemäß Matrix in `00_PROJECT_CHARTER.md`.

---

## Grundprinzipien

### Kurz und aktuell

Der Stand beschreibt den Ist-Zustand, nicht die Idealwelt. Veraltetes entfernen oder korrigieren.

### Belegt, nicht spekuliert

Nur aufnehmen, was aus Code, Docs oder bestätigter Abstimmung bekannt ist. Unklares als offen kennzeichnen.

### Ergänzen, nicht duplizieren

Details gehören in kanonische Docs; hier stehen Zusammenfassung, Zeiger und Arbeitskontext.

### Nach relevanten Aufgaben pflegen

Jede Aufgabe, die den Projektkontext verändert, aktualisiert den Stand.

---

## Verbindliche Regeln

### Pflichtinhalt

Der Projektstand muss mindestens enthalten:

1. **Projektkurzbeschreibung** — wozu das Projekt existiert
2. **Aktueller Fokus** — woran gerade gearbeitet wird
3. **Wichtige Entscheidungen** — kurze Liste verbindlicher Festlegungen
4. **Bekannte Risiken / Schulden** — nur die relevanten
5. **Nächste Schritte** — wenige, konkrete Punkte
6. **Stand vom** — Datum der letzten Aktualisierung

Optional:

- aktives Profile (sobald Profiles existieren)
- Branch / Release-Linie
- Verweise auf zentrale Docs und Module
- Blocker

### Abgrenzung

| Inhalt | Hier | Stattdessen |
|--------|------|-------------|
| Aktueller Fokus | ja | — |
| Lange Architektur | nein | `ARCHITECTURE.md` |
| Feature-Backlog | nein (nur Verweis) | `TODO.md` |
| Versionshistorie | nein | `CHANGELOG.md` |
| Regelwerk AI-DK | nein | Core-Dokumente |

### Aktualisierungspflicht

Die KI aktualisiert dieses Dokument, wenn:

- sich der Arbeitsfokus ändert,
- eine Architektur- oder Produktentscheidung getroffen wurde,
- Blocker entstehen oder entfallen,
- ein Sprint-/Meilenstein-Abschnitt im Projekt abgeschlossen wird.

Keine kosmetischen Umschreibungen ohne Inhaltsänderung.

### Vorlage

Zielprojekte kopieren die Struktur unter **Aktueller Projektstand** und ersetzen den Inhalt. Die Abschnitte Ziel bis Ausnahmen bleiben als Regeln erhalten, sofern das Projekt AI-DK Core nutzt.

---

## Empfehlungen

- Den Stand auf eine Bildschirmseite Kerntext begrenzen; Details verlinken.
- Nach größeren Sessions den Stand vor dem Abschlussbericht aktualisieren.
- Widersprüche zwischen Stand und Code sofort klären — Code bzw. belegte Docs gewinnen, Stand korrigieren.
- Profile-Name erst eintragen, wenn ein Profile verbindlich gewählt wurde.

---

## KI-Verhalten

Die KI muss:

1. Zu Beginn relevanter Aufgaben den Projektstand lesen.
2. Den Stand nicht als alleinige Wahrheit behandeln — bei Zweifel Code und kanonische Docs prüfen.
3. Nach relevanten Änderungen den Stand aktualisieren.
4. Fehlenden Stand benennen und Anlegen vorschlagen (Projektübernahme / Greenfield).
5. Keine erfundenen Zustände, Metriken oder Entscheidungen eintragen.

---

## Checkliste

### Vor einer Aufgabe

- [ ] Projektstand gelesen
- [ ] Fokus und Risiken zur Aufgabe passend verstanden
- [ ] Bei Widerspruch zu Code/Docs nachgefragt oder verifiziert

### Nach einer relevanten Aufgabe

- [ ] Fokus / nächste Schritte aktualisiert
- [ ] Neue Entscheidungen kurz notiert
- [ ] Erledigte oder obsolette Punkte entfernt
- [ ] Datum gesetzt
- [ ] Keine Duplikate zu CHANGELOG/TODO/ARCHITECTURE erzeugt

---

## Beispiele

### Gut

Kurz: „Fokus: Auth-Token-Refresh. Entscheidung: Refresh serverseitig. Risiko: fehlende Tests. Nächster Schritt: Regressionstest.“

### Schlecht

Komplette API-Referenz und alle TODOs in den Stand kopieren.

---

## Ausnahmen

- Sehr kleine Einmal-Skripte ohne Fortbestand brauchen keinen gepflegten Stand.
- Organisationsvorlagen dürfen Abschnitte umbenennen, solange die Pflichtinhalte abgedeckt sind.

Fehlender Stand in einem fortlaufenden Produktprojekt ist keine Dauerausnahme.

---

## Aktueller Projektstand

> Lebendiger Stand **dieses** Repositorys (AI-DK). In Zielprojekten diesen Abschnitt projektspezifisch füllen.

### Stand vom

2026-07-29

### Projektkurzbeschreibung

AI-DK (AI Development Kit) ist ein AI Engineering Standard: versioniertes Framework aus Regeln, Workflows und Dokumentation für KI-gestützte Softwareentwicklung. **Core 1.0.0** ist freigegeben; Profiles und Extensions sind geplant.

### Aktueller Fokus

Framework **1.0.0** (Tag `v1.0.0`). S1–S6 Desk-Review abgeschlossen (`.ai/tests/RESULTS.md`: 5× bestanden, S6 teilweise). Nächste Optionen: S6-Nachzug oder Planung **1.1** (jeweils Freigabe).

### Wichtige Entscheidungen

- Drei Ebenen: Core · Profiles · Extensions
- Markdown ist bis 1.1 kanonisch; YAML-Regeln erst in 1.1
- Profiles erst ab 2.0; keine Tech-Stacks im Core
- Einheitliche Dokumentstruktur für alle Core-Dokumente
- Kanonisch: Charter = Prinzipien; Workflow = Prozess; AI Behavior = Verhalten; Spezialdocs = Fachthema
- Framework-Qualität über Szenarien S1–S6; Erstprotokoll 2026-07-29
- Versions Semantik: MAJOR.MINOR.PATCH; AI-DK aktuell **1.0.0**
- Releases nur nach Freigabekriterien; KI veröffentlicht nicht eigenmächtig
- Security: Secrets, Vertrauensgrenzen, keine Scheinsicherheit; Stack-Details → Profiles

### Bekannte Risiken / Schulden

- S6 nur teilweise: fehlende explizite Review-Schwereordnung / Secret-Stopp-vor-Merge im Core-Wortlaut
- `01` reserviert, noch ohne Dokument
- Profiles, YAML (1.1), Extensions noch nicht umgesetzt
- Tag `v1.0.0` lokal; kein Remote-Push

### Nächste Schritte

1. Optional: S6-Lücke in `05_AI_BEHAVIOR.md` schließen (Freigabe)
2. Planung **1.1** (YAML-Regeln, Markdown bleibt kanonisch)
3. Später **2.0** Profiles

### Verweise

- `README.md` — Produktarchitektur, Index
- `CHANGELOG.md` — Versionshistorie
- `TODO.md` — offene Nacharbeiten
- `00_PROJECT_CHARTER.md` — Zuständigkeitsmatrix
- `.ai/tests/SCENARIOS.md` — Framework-Tests
- `.ai/tests/RESULTS.md` — Ergebnisprotokoll S1–S6
- `11_VERSION.md` — Versionsvergabe
- Git-Tag `v1.0.0` — Release-Kennzeichnung

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Framework-Release **1.0.0** (Sprint 4 abgeschlossen)
- Lebendiger Stand auf stabilen Core aktualisiert

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `05_AI_BEHAVIOR.md`
- `07_DOCUMENTATION.md`
- `09_RELEASE_PROCESS.md`
- `10_SECURITY.md`
- `11_VERSION.md`
