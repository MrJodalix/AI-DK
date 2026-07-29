# AI-DK Release Process

Version: 1.0.0

## Ziel

Dieses Dokument definiert, wie freigabefähige Stände eines Projekts vorbereitet, geprüft und veröffentlicht werden.

Es soll sicherstellen:

- kontrollierte, nachvollziehbare Releases
- stabile Hauptlinien
- vollständige Lieferartefakte (Code, Tests, Dokumentation)
- keine „stillen“ oder ungeprüften Veröffentlichungen durch die KI

---

## Geltungsbereich

Gilt für:

- Vorbereitung eines Releases
- Freigabekriterien
- Kennzeichnung eines Release-Stands
- Kommunikation der Änderung gegenüber Nutzerinnen und Nutzern des Projekts (Changelog)

Gilt nicht für:

- konkrete CI/CD-Produkte oder Hosting-Plattformen (Profiles / spätere Extensions)
- semantische Versionsnummern im Detail (siehe `11_VERSION.md`)
- vertiefte Security-Audits jenseits der Mindestregeln in `10_SECURITY.md`

Bei Konflikt mit einer engeren Organisations-Release-Richtlinie gilt die engere Richtlinie. Die Grundprinzipien dieses Dokuments und der Charter bleiben verbindlich.

Kanonische Zuständigkeit für Releases gemäß Matrix in `00_PROJECT_CHARTER.md`.

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Release ist eine bewusste Entscheidung

Ein Release entsteht nicht nebenbei aus dem letzten Commit. Es hat Kriterien, Inhalt und Verantwortlichkeit.

### Lieferbar bedeutet geprüft

Nur Stände, die die Freigabekriterien erfüllen, werden als Release behandelt.

### Nachvollziehbarkeit vor Geschwindigkeit

Jedes Release muss erklärbar sein: Was steckt drin, warum, welche Risiken bleiben.

### Keine erfundenen Releases

Die KI darf keine Veröffentlichung, kein Tag und keinen Release-Eintrag behaupten, die nicht erfolgt bzw. belegt sind.

---

## Verbindliche Regeln

### Was ein Release ist

Ein Release ist ein eindeutig gekennzeichneter, integrierter Stand der Hauptlinie (oder der im Projekt definierten Release-Linie), der:

1. die Freigabekriterien erfüllt,
2. dokumentiert ist,
3. und zur Nutzung freigegeben wurde.

### Freigabekriterien (Minimum)

Vor einem Release müssen gelten:

| Kriterium | Anforderung |
|-----------|-------------|
| Qualität | Bekannte Release-Blocker sind behoben oder ausdrücklich als akzeptiertes Risiko dokumentiert |
| Tests | Relevante automatisierte Tests gemäß `04_TESTING.md` und Projektvorgabe sind ausgeführt bzw. ihr Status ist ehrlich dokumentiert |
| Hauptlinie | Der Release-Stand ist auf der vorgesehenen Branch-/Integrationslinie |
| Dokumentation | `CHANGELOG.md` (oder Äquivalent) beschreibt das Release; betroffene Nutzerdocs sind aktualisiert (`07_DOCUMENTATION.md`) |
| Git | Historie und Kennzeichnung folgen `06_GIT_WORKFLOW.md` und der Projektkonvention |
| Secrets | Keine bekannten Secrets im Release-Stand |
| Freigabe | Explizite Freigabe durch die im Projekt vorgesehene Rolle (Mensch), sofern nicht anders dokumentiert |

### Release-Inhalt

Jedes Release dokumentiert mindestens:

- Versions- oder Release-Kennung
- Datum
- wesentliche Änderungen (Features, Fixes, Breaking Changes)
- bekannte Einschränkungen oder Migrationshinweise, falls nötig

### Breaking Changes

Breaking Changes müssen:

- im Changelog klar gekennzeichnet sein,
- eine Migrations- oder Kompatibilitätshinweis enthalten, sofern zumutbar,
- bewusst freigegeben sein — nicht „mitlaufen“.

### Kennzeichnung

- Der Release-Stand wird nach Projektkonvention gekennzeichnet (z. B. Git-Tag, Release-Eintrag, Versionsdatei).
- Die gewählte Kennzeichnung muss eindeutig und wiederauffindbar sein.
- Details zur Versionsvergabe: `11_VERSION.md`.

### KI darf nicht eigenmächtig veröffentlichen

Ohne ausdrückliche Anweisung oder klare Projektregel darf die KI:

- keine Release-Tags erstellen,
- keine Store-/Registry-/Plattform-Veröffentlichung auslösen,
- keine produktiven Deployments starten.

Vorbereitung (Checkliste, Changelog-Entwurf, Versionsvorschlag) ist erlaubt und erwünscht.

### Hotfixes

Dringende Korrekturen:

- so klein wie möglich halten,
- Regressionstest anstreben,
- denselben Dokumentations-Mindeststandard erfüllen (Changelog-Eintrag),
- danach wieder in die normale Integrationslinie überführen.

---

## Empfehlungen

- Vor dem Release einen kurzen Freeze nur für Release-relevante Fixes nutzen.
- Release Notes aus dem Changelog ableiten, nicht parallel erfinden.
- Pre-Releases (alpha/beta/rc) klar als solche kennzeichnen.
- Automatisierte Pipelines als Unterstützung nutzen, wenn vorhanden — sie ersetzen nicht die Freigabekriterien.
- Nach dem Release den Projektstand (`08_PROJECT_STATE.md`) aktualisieren.

---

## KI-Verhalten

Die KI muss:

1. Vor Release-Arbeit den gewünschten Zielstand und die Projektkonvention klären.
2. Freigabekriterien systematisch prüfen und Lücken benennen.
3. Changelog und Dokumentation vorbereiten, ohne Inhalte zu erfinden.
4. Veröffentlichungsschritte nur auf Anweisung oder nach klarer Regel ausführen.
5. Testergebnisse und Release-Status nur behaupten, wenn belegt.
6. Bei Unsicherheit über Breaking Changes oder Versionssprung nachfragen.

---

## Checkliste

### Release-Vorbereitung

- [ ] Release-Inhalt und Zielkennung geklärt
- [ ] Blocker bekannt und adressiert
- [ ] Tests/Checks ausgeführt oder Status dokumentiert
- [ ] Changelog aktualisiert (inkl. Breaking Changes)
- [ ] Nutzerrelevante Docs aktualisiert
- [ ] Keine Secrets im Stand
- [ ] Git-Stand entspricht der Release-Linie

### Vor der Veröffentlichung

- [ ] Menschliche Freigabe liegt vor (falls erforderlich)
- [ ] Kennzeichnung (Tag/Eintrag) geplant
- [ ] KI hat explizite Erlaubnis für Tag/Publish/Deploy, falls sie das ausführen soll

### Nach dem Release

- [ ] Kennzeichnung erfolgt und verifizierbar
- [ ] Projektstand aktualisiert
- [ ] Offene Nacharbeiten in `TODO.md` erfasst

---

## Beispiele

### Gut

Version vorbereiten: Tests grün, Changelog mit Breaking-Change-Hinweis, Tag erst nach ausdrücklicher Freigabe.

### Schlecht

„Release ist raus“, obwohl nur lokal committed wurde und kein Tag/Publish belegt ist.

### Gut

Hotfix: ein Commit, Regressionstest, Changelog-Zeile, danach Rückführung in die Hauptlinie.

### Schlecht

Hotfix plus unzusammenhängendes Refactoring und neue Features im selben Release ohne Kennzeichnung.

---

## Ausnahmen

- Interne Experimentier-Branches sind keine Releases.
- Rein private Lernprojekte dürfen den Prozess kürzen, wenn das dokumentiert ist — produktive oder geteilte Artefakte nicht.
- Notfall-Releases (z. B. kritischer Sicherheitspatches) dürfen beschleunigt werden, müssen aber nachgezogen dokumentiert werden.

Sicherheitsanforderungen haben Vorrang vor Release-Tempo.

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Querverweis auf Charter-Matrix (Sprint 4 Konsistenz)

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `02_DEVELOPMENT_WORKFLOW.md`
- `04_TESTING.md`
- `05_AI_BEHAVIOR.md`
- `06_GIT_WORKFLOW.md`
- `07_DOCUMENTATION.md`
- `08_PROJECT_STATE.md`
- `10_SECURITY.md`
- `11_VERSION.md`
