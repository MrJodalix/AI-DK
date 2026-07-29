# AI-DK Bootstrap

Version: 2.1.0

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
3. Lies `08_PROJECT_STATE.md` (bzw. den im Projekt festgelegten Stand).
4. Prüfe `TODO.md` (falls vorhanden).
5. Ermittle die betroffenen Fachdokumente (`02`–`04`, `06`–`07`, `09`–`11`, ggf. `profiles/<name>/`).
6. Bearbeite erst dann die Aufgabe — Ablauf gemäß `02_DEVELOPMENT_WORKFLOW.md`.

Diese Reihenfolge ist für jede neue Sitzung **verbindlich**.

### Profile

Wenn das Projekt ein Profile aktiv nutzt (z. B. Flutter): nach Schritt 5 die Profile-README und die fachlich betroffenen Profile-Dokumente lesen. Core-Prinzipien bleiben vorrangig (`profiles/README.md`).

---

## Ausnahmen

Die volle Sequenz darf verkürzt werden nur bei:

- reinen Meta-/Clarifying-Fragen ohne Code- oder Dokumentänderung, oder
- Fortsetzung derselben Aufgabe in derselben Sitzung, wenn der Kontext nachweislich bereits geladen ist.

Sobald geplant, implementiert, getestet oder dokumentiert wird: Sequenz vollständig.

---

## KI-Verhalten

Die KI muss:

1. Bootstrap vor fachlicher Arbeit ausführen.
2. Die Spezifikationsformel respektieren (verbindliche Arbeitsgrundlage + Version).
3. Fachdetails in den kanonischen Dokumenten nachschlagen — Bootstrap nicht mit Norminhalt überladen.
4. Keine Behauptung, AI-DK gelesen zu haben, ohne die relevanten Dateien tatsächlich berücksichtigt zu haben.

---

## Checkliste

- [ ] Charter gelesen
- [ ] AI Behavior gelesen
- [ ] Project State gelesen
- [ ] TODO geprüft (falls vorhanden)
- [ ] Fachdokumente / Profile ermittelt
- [ ] Erst danach Umsetzung

---

## Version

Dokumentversion: 2.1.0

Änderung in dieser Version:

- Erstes Bootstrap-Dokument; Spezifikationsformel; Sitzungsstart für Agenten

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `05_AI_BEHAVIOR.md`
- `08_PROJECT_STATE.md`
- `README.md`
