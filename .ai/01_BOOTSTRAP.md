# AI-DK Bootstrap

Version: 2.1.2

## Ziel

Dieses Dokument ist die **Einstiegsschicht für KI-Agenten**.

Es definiert den verbindlichen Start jeder neuen Sitzung und jeder neuen Aufgabe.  
Es ist **nicht** das Primärdokument für menschliche Entwickler (dafür: Charter, Workflow, Projektstand).

---

## Geltungsbereich

Gilt für:

- jede neue Agenten-Sitzung
- jede neue Aufgabe (Analyse, Planung, Implementierung, Review, Dokumentation)

Gilt nicht als Ersatz für:

- Prinzipien (`00_PROJECT_CHARTER.md`)
- Ablaufphasen (`02_DEVELOPMENT_WORKFLOW.md`)
- Verhaltensdetails (`05_AI_BEHAVIOR.md`)

Werkzeuge (ChatGPT, Cursor, Claude Code u. a.) sollen diese Datei **zuerst** erhalten bzw. einlesen.

---

## Spezifikation

AI-DK ist eine **versionierte Spezifikation**, keine lose Dokumentensammlung.

Kanonische Anweisung an jede KI:

> Dieses Projekt implementiert die AI-DK-Spezifikation in Version **X.Y.Z** (siehe `README.md` / Framework-Version). AI-DK ist die verbindliche Arbeitsgrundlage für Analyse, Planung, Implementierung, Tests und Dokumentation. Beginne jede neue Aufgabe mit dem Bootstrap-Prozess gemäß `01_BOOTSTRAP.md` und befolge anschließend die für die Aufgabe relevanten Core-Dokumente (und ggf. das aktive Profile).

`X.Y.Z` ist die aktuelle Framework-Version — nicht erfinden, aus README oder Release-Stand lesen.

---

## Verbindliche Startsequenz

Bevor die Aufgabe bearbeitet wird:

1. Lies `00_PROJECT_CHARTER.md`.
2. Lies `05_AI_BEHAVIOR.md`.
3. Lies `08_PROJECT_STATE.md` (bzw. den im Projekt festgelegten Stand — siehe Shared Core unten).
4. Prüfe `TODO.md` (falls vorhanden).
5. Ermittle die betroffenen Fachdokumente (`02`–`04`, `06`–`07`, `09`–`12`, ggf. `profiles/<name>/`).
6. Bearbeite erst dann die Aufgabe — Ablauf gemäß `02_DEVELOPMENT_WORKFLOW.md`.

Diese Reihenfolge ist für jede neue Sitzung **verbindlich**.

### Profile

Wenn das Projekt ein Profile aktiv nutzt (z. B. Flutter): nach Schritt 5 die Profile-README und die fachlich betroffenen Profile-Dokumente lesen. Core-Prinzipien bleiben vorrangig (`profiles/README.md`).

### Zielprojekt-Greenfield

Bei **neuen** Zielprojekten (noch kein Produktcode / keine Fach-Features):

1. AI-DK verdrahten: Core unter `.ai/` **kopieren oder verlinken**; Profile und optional Extensions gemäß `profiles/README.md` / `extensions/`.
2. Kanonische Projektdocs anlegen (`07_DOCUMENTATION.md`): `PROJECT.md`, `ARCHITECTURE.md`, `TODO.md`, `CHANGELOG.md`, **projekteigener** Stand.
3. Scaffold und Ordnerstruktur laut aktivem Profile — **ohne** Fach-Features.
4. Erst danach Features gemäß Workflow und TODO-Priorität.

**Init gilt als erledigt**, wenn: Verdrahtung + kanonische Docs + lauffähiges Scaffold + dokumentierter Stack vorhanden sind. Fach-Features sind dafür **nicht** erforderlich.

### Shared Core (Kopie oder Verlinkung)

- Core darf nach `.ai/` **kopiert oder verlinkt** werden (Kopie, Symlink, Submodule/nested Checkout) — siehe `profiles/README.md` und Cursor-Extension.
- Ist der Core geteilt oder verlinkt, darf der lebendige Stand **nicht** der Framework-Stand von AI-DK sein.
- Pflicht: **projekteigene** Stand-Datei (typisch `.ai/08_PROJECT_STATE.md` als Datei des Zielprojekts). Alias `PROJECT_STATE.md` im Repo-Root ist erlaubt, wenn er auf denselben projekteigenen Stand zeigt (`08_PROJECT_STATE.md`).

---

## Ausnahmen

Die volle Sequenz darf verkürzt werden bei:

- reinen Meta-/Clarifying-Fragen ohne Code- oder Dokumentänderung, oder
- Fortsetzung derselben Aufgabe in derselben Sitzung, wenn der Kontext nachweislich bereits geladen ist, oder
- **Fortsetzungssitzung im selben Zielprojekt**, wenn der projekteigene Stand (`08_PROJECT_STATE.md` / Alias) **aktuell** ist und die Aufgabe keine Architektur-/Stack-Entscheidung neu aufwirft.

### Fortsetzungssitzung (verkürzter Start)

Mindestens lesen/prüfen:

1. projekteigener Stand
2. `TODO.md` (falls vorhanden)
3. fachlich betroffene Core-/Profile-Dokumente der konkreten Aufgabe

Charter und AI Behavior müssen nicht jedes Mal vollständig neu gelesen werden, bleiben aber verbindlich. Bei Unsicherheit, Stack-Konflikt oder Architekturänderung: volle Startsequenz.

---

## KI-Verhalten

Die KI muss:

1. Bootstrap vor fachlicher Arbeit ausführen.
2. Die Spezifikationsformel respektieren (verbindliche Arbeitsgrundlage + Version).
3. Fachdetails in den kanonischen Dokumenten nachschlagen — Bootstrap nicht mit Norminhalt überladen.
4. Keine Behauptung, AI-DK gelesen zu haben, ohne die relevanten Dateien tatsächlich berücksichtigt zu haben.
5. Bei Greenfield die Init-Reihenfolge einhalten und Shared-Core-Stand projekteigen halten.

---

## Checkliste

- [ ] Charter gelesen
- [ ] AI Behavior gelesen
- [ ] Project State gelesen (projekteigen bei Shared Core)
- [ ] TODO geprüft (falls vorhanden)
- [ ] Fachdokumente / Profile ermittelt
- [ ] Bei Greenfield: Init-Reihenfolge beachtet
- [ ] Erst danach Umsetzung

---

## Version

Dokumentversion: 2.1.2

Änderung in dieser Version:

- Fortsetzungssitzung: verkürzter Start bei aktuellem Stand

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `05_AI_BEHAVIOR.md`
- `08_PROJECT_STATE.md`
- `profiles/README.md`
- `extensions/cursor/README.md`
- `README.md`
