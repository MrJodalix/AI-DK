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

AI-DK ist der Name des **AI Engineering Standards**. Core, `.ai/rules/` (1.1), `check_core.py` (1.2) und erstes Profile **Flutter** (2.0).

### Aktueller Fokus

Framework **2.0.0**. Flutter-Profile unter `profiles/flutter/` aktiv.  
Als Nächstes: weitere Profiles oder Backlog — nach Freigabe.

### Wichtige Entscheidungen

- Name: **AI-DK** · Produktkategorie: **AI Engineering Standard**
- Roadmap: 1.1 YAML → 1.2 Checks → **2.0 Flutter** (erledigt)
- Markdown kanonisch; YAML abgeleitet; Sync-Pflicht
- Core vs. Profile: Core gewinnt bei Prinzipien; Profile bei Stack-Details
- Flutter-Stack: Riverpod · Drift · Freezed · go_router · Material 3
- Vor AI-DK-Releases: `python3 .ai/tests/check_core.py` PASS
- AI-DK aktuell **2.0.0**

### Bekannte Risiken / Schulden

- `01` reserviert
- YAML ist Stichprobe; Auto-Check deckt Struktur/Links/YAML-Schema, nicht S1–S6-Verhalten
- Weitere Profiles / Governance-Backlog offen

### Nächste Schritte

1. Weitere Profiles (nach Freigabe)
2. Optional: Backlog (Governance, ADR, …)
3. Optional: GitHub Actions für `check_core.py`

### Verweise

- `profiles/flutter/`
- `.ai/tests/check_core.py`
- `.ai/tests/reports/latest.txt`
- `.ai/rules/README.md`
- `.ai/plans/2.0_FLUTTER_PROFILE.md`
- `.ai/plans/BACKLOG_AFTER_1.0.md`
- `CHANGELOG.md` · `TODO.md` · `README.md`

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
