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

Zielprojekte füllen die Struktur unter **Aktueller Projektstand** projektspezifisch. Die Abschnitte Ziel bis Ausnahmen bleiben als Regeln erhalten, sofern das Projekt AI-DK Core nutzt.

### Shared Core / nested AI-DK

Wenn der Core **kopiert oder verlinkt** ist (Symlink, Submodule, nested `AI-DK/`):

1. Der lebendige Stand des **Zielprojekts** muss eine **projekteigene** Datei sein — typisch `.ai/08_PROJECT_STATE.md` im Zielrepo, die **nicht** den Framework-Stand von AI-DK ersetzt oder überschreibt.
2. Alias `PROJECT_STATE.md` im Repo-Root ist erlaubt, wenn er auf denselben projekteigenen Stand zeigt.
3. Bootstrap liest den projekteigenen Stand (`01_BOOTSTRAP.md`).

Einrichtung Core/Profile: `profiles/README.md`, `extensions/cursor/README.md`.

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

2026-08-03

### Projektkurzbeschreibung

AI-DK ist der Name des **AI Engineering Standards** (versionierte Spezifikation). Core, Bootstrap, Flutter-Profile, Meta-Docs, Extensions (Cursor/Generic) und CI für `check_core.py`.

### Aktueller Fokus

Framework **2.3.1** — Klarstellungen nach Zielprojekt-Retro (Greenfield, Shared Core, Commit-Vorbereitung, Flutter Stack-Konflikte/Pre-Releases). Profile-Fokus: **nur Flutter**.

### Wichtige Entscheidungen

- Name: **AI-DK** · Spezifikation mit Bootstrap
- Nur Flutter-Profile aktiv gepflegt; keine weiteren Profiles ohne neuen Bedarf
- Extensions = Tool-Adapter, nicht Normersatz (ADR 0006)
- CI: GitHub Actions `check-core.yml`
- Vor Releases: `python3 .ai/tests/check_core.py` PASS
- Core in Zielprojekten: **kopieren oder verlinken**; Stand immer projekteigen
- Riverpod-Runtime Pflicht; Generator empfohlen mit dokumentierter Ausnahme bei Resolver-Konflikt
- AI-DK aktuell **2.3.1**

### Bekannte Risiken / Schulden

- YAML/Checks ersetzen keine S1–S6-Verhaltensprüfung
- Weitere Profiles/Tool-Adapter nur bei Bedarf

### Nächste Schritte

1. `check_core.py` PASS nach 2.3.1-Änderungen
2. Weitere Profiles nur bei explizitem Bedarf
3. Optional: weitere Tool-Extensions

### Verweise

- `.ai/01_BOOTSTRAP.md`
- `profiles/flutter/`
- `extensions/`
- `.github/workflows/check-core.yml`
- `docs/` · `rfcs/`
- `.ai/plans/2.3_EXTENSIONS_CI.md`
- `CHANGELOG.md` · `TODO.md` · `README.md`

---

## Version

Dokumentversion: 1.0.3

Änderung in dieser Version:

- Shared Core: projekteigener Stand; Alias `PROJECT_STATE.md`

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `05_AI_BEHAVIOR.md`
- `07_DOCUMENTATION.md`
- `09_RELEASE_PROCESS.md`
- `10_SECURITY.md`
- `11_VERSION.md`
