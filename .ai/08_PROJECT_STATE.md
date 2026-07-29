# AI-DK Project State

Version: 1.0.2

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

AI-DK ist der Name des **AI Engineering Standards**: versioniertes Framework aus Regeln, Workflows und Dokumentation für KI-gestützte Softwareentwicklung. **Core 1.0.x** ist freigegeben; nächste Ausbaustufen: 1.1 (YAML), 1.2 (Test-Automation), 2.0 (Flutter-Profile).

### Aktueller Fokus

Framework **1.0.3** (Positioning + Roadmap).  
Als Nächstes: **1.1** maschinenlesbare Regeln.

### Wichtige Entscheidungen

- Name: **AI-DK** · Produktkategorie: **AI Engineering Standard** (nicht als bloßer „Development Kit“ vermarkten)
- Drei Ebenen: Core · Profiles · Extensions
- Roadmap: **1.1** YAML → **1.2** Test-Automation → **2.0** Flutter-Profile
- Markdown ist bis 1.1 kanonisch; YAML erst ab 1.1 als Ableitung
- Profiles: Flutter zuerst (2.0); keine Tech-Stacks im Core
- Code Review: Security > Korrektheit > Wartbarkeit > Stil; Secrets blockieren Merge/Approve
- AI-DK aktuell **1.0.3**; Tags `v1.0.0`–`v1.0.2` vorhanden

### Bekannte Risiken / Schulden

- `01` reserviert, noch ohne Dokument
- 1.1 / 1.2 / 2.0 noch nicht implementiert (nur Pläne/Backlog)
- Governance/ADR/Glossar nur im Backlog

### Nächste Schritte

1. ~~Commit Positioning (1.0.3)~~  
2. **1.1 implementieren** (Schema + YAML)  
3. Danach **1.2** Test-Automation  
4. Danach **2.0** Flutter-Profile

### Verweise

- `README.md` — Branding und Roadmap
- `.ai/plans/1.1_MACHINE_READABLE_RULES.md`
- `.ai/plans/1.2_TEST_AUTOMATION.md`
- `.ai/plans/BACKLOG_AFTER_1.0.md`
- `CHANGELOG.md` · `TODO.md`

---

## Version

Dokumentversion: 1.0.2

Änderung in dieser Version:

- Stand auf Qualitätsrelease **1.0.2**; Backlog-Verweis

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `05_AI_BEHAVIOR.md`
- `07_DOCUMENTATION.md`
- `09_RELEASE_PROCESS.md`
- `10_SECURITY.md`
- `11_VERSION.md`
