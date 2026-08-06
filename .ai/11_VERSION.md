# AI-DK Version

Version: 1.0.0

## Ziel

Dieses Dokument definiert, wie Versionen für AI-DK und für Zielprojekte vergeben, dokumentiert und kommuniziert werden.

Es soll sicherstellen:

- eindeutige, vergleichbare Versionskennungen
- nachvollziehbare Sprünge (breaking / feature / fix)
- konsistente Angabe in Docs, Tags und Changelogs
- keine erfundenen oder widersprüchlichen Versionsstände

---

## Geltungsbereich

Gilt für:

- Versionskennungen von AI-DK (Framework)
- Versionskennungen von Zielprojekten, die AI-DK nutzen
- Abgleich zwischen Changelog, Release und dokumentierter Version

Gilt nicht für:

- Marketingnamen oder Store-Buildnummern jenseits der Projektkonvention
- interne Build-IDs von CI-Systemen (dürfen ergänzen, ersetzen aber nicht die Produktversion)

Bei Konflikt mit einer verbindlichen Organisations-Versionsrichtlinie gilt diese. Die Grundprinzipien dieses Dokuments und der Charter bleiben verbindlich.

Kanonische Zuständigkeit für Versionsvergabe gemäß Matrix in `00_PROJECT_CHARTER.md`.

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Eine kanonische Produktversion

Zur gleichen Zeit gibt es genau eine aktuelle kanonische Version der Hauptlinie. Ableitungen (Pre-Release, Hotfix-Zweige) sind klar gekennzeichnet.

### Semantik vor Willkür

Versionserhöhungen folgen einer erkennbaren Bedeutung — nicht dem Kalender und nicht dem Zufall.

### Version und Inhalt stimmen überein

Die deklarierte Version muss zum freigegebenen Stand und zum Changelog passen.

### Pre-1.0 ist erlaubt und ehrlich

Vor `1.0.0` dürfen sich APIs und Regeln noch ändern; das muss sichtbar sein (z. B. `0.x.y`).

---

## Verbindliche Regeln

### Versionsformat

Sofern das Projekt nichts anderes vorschreibt, gilt:

```text
MAJOR.MINOR.PATCH
```

Optional mit Pre-Release-Suffix, z. B. `1.0.0-rc.1` oder `0.3.0-draft`.

Bedeutung (übliche Semantik):

| Erhöhung | Wann |
|----------|------|
| **MAJOR** | unverträgliche Änderungen für Nutzerinnen/Nutzer der bisherigen Version |
| **MINOR** | rückwärtskompatible Funktionalität oder Regelzuwachs |
| **PATCH** | rückwärtskompatible Korrekturen oder reine Klarstellungen ohne Verhaltensbruch |

Abweichende Schemata (Kalenderversionierung u. a.) nur, wenn das Projekt sie verbindlich vorgibt — dann dokumentieren und konsequent anwenden.

### Breaking Changes

- Erfordern einen **MAJOR**-Sprung (nach `1.0.0`) oder eine klar kommunizierte unverträgliche `0.x`-Erhöhung vor `1.0.0`.
- Müssen im Changelog gekennzeichnet sein (`09_RELEASE_PROCESS.md`).

### Wo die Version steht

Mindestens eine kanonische Stelle muss die aktuelle Version tragen. Für AI-DK:

| Ort | Rolle |
|-----|--------|
| `README.md` | Framework-Version (sichtbar) |
| `08_PROJECT_STATE.md` | Arbeitskontext inkl. Versionsstand |
| einzelne Core-Docs | Dokumentversion (kann von der Framework-Version abweichen, muss aber nicht widersprechen) |
| Git-Tag | Release-Kennzeichnung gemäß `06_GIT_WORKFLOW.md` / `09_RELEASE_PROCESS.md` |

Zielprojekte legen ihre kanonische Stelle fest (z. B. Manifest, `VERSION`-Datei, Paketmetadaten) und halten Changelog dazu synchron.

### Dokumentversion vs. Framework-/Produktversion

- **Dokumentversion:** Version dieses Regeltexts.
- **Framework-/Produktversion:** Version des Gesamtstands.

Ein einzelnes Dokument darf eine ältere Dokumentversion behalten, solange der Inhalt zur aktuellen Framework-Version kompatibel ist. Widersprüchliche Aussagen („Framework 0.3.0“ vs. Doc „nur bis 0.1 gültig“ ohne Hinweis) sind unzulässig.

### KI-Verhalten bei Versionen

Die KI darf:

- Versionsvorschläge anhand der Semantik unterbreiten,
- Changelog und Tags **vorbereiten**.

Die KI darf nicht:

- Versionsnummern erfinden, die nicht zum Stand passen,
- eigenmächtig MAJOR-Sprünge ohne Freigabe setzen,
- behaupten, eine Version sei released/getaggt, ohne Beleg.

### AI-DK-Roadmap (Framework)

| Version | Bedeutung |
|---------|-----------|
| `1.0.x` | Stabiler Core |
| `1.1.x` | Maschinenlesbare Regeln (YAML), Markdown kanonisch |
| `1.2.x` | Framework-Tests automatisieren |
| `1.x+` | Governance, ADRs, Glossar, QUALITY (Backlog) |
| `2.0.x` | Erstes Profile: Flutter |
| `2.1.x` | Bootstrap + Spezifikations-Framing |
| `2.2.x` | Governance · ADR · Glossar · Quality · RFC |
| `2.3.x` | Extensions + CI; Klarstellungen Greenfield/Stack/Offline/UI; Core I18N; Shell-Invalidierung / Shared-Core-Upgrade (**aktuell 2.3.6**); Profile-Fokus Flutter |
| später | Weitere Profiles nur bei Bedarf |

---

## Empfehlungen

- Vor größeren Umbauten nach `1.0.0` die Semantik (MAJOR/MINOR/PATCH) bewusst wählen.
- Pre-Releases (`-alpha`, `-beta`, `-rc`, `-draft`) für unfertige Stände verwenden.
- Nach jedem Release README, Projektstand und Changelog in demselben Arbeitsgang aktualisieren.
- Abhängige Systeme (Paketindex, Container-Tags) dieselbe Semantik spiegeln lassen.

---

## KI-Verhalten

Die KI muss:

1. Vor Versionsvorschlägen Changelog und Art der Änderung prüfen.
2. Bei Unklarheit (breaking oder nicht?) nachfragen.
3. Framework- und Dokumentversion nicht stillschweigend vermischen.
4. `README.md` und `08_PROJECT_STATE.md` nach Versionswechseln des Frameworks mitpflegen, wenn sie AI-DK selbst bearbeitet.

---

## Checkliste

### Vor einem Versionssprung

- [ ] Art der Änderung klassifiziert (MAJOR / MINOR / PATCH / Pre-Release)
- [ ] Changelog vorbereitet
- [ ] Kanonische Versionsstelle identifiziert
- [ ] Breaking Changes gekennzeichnet (falls vorhanden)
- [ ] Freigabe für Sprung und Release geklärt

### Nach dem Setzen der Version

- [ ] README / Manifest / Tag konsistent
- [ ] Projektstand aktualisiert
- [ ] Keine widersprüchlichen Versionsangaben in geänderten Docs

---

## Beispiele

### Gut

Neues Core-Dokument ohne Regelbruch: `0.2.0` → `0.3.0` (MINOR im Pre-1.0-Rahmen der Roadmap).

### Schlecht

Beliebige Nummer `3.7.9` setzen, obwohl zuvor `0.2.0` kommuniziert wurde und kein Release existiert.

### Gut

Unverträgliche Regelumstellung nach `1.0.0`: `1.0.0` → `2.0.0` mit Changelog-Hinweis.

### Schlecht

Breaking Change als PATCH `1.0.1` verstecken.

---

## Ausnahmen

- Forks oder Vendoring dürfen eigene Versionslinien führen, müssen sie aber kennzeichnen.
- Notfall-Hotfixes dürfen PATCH auf einer Release-Linie sein, auch wenn parallel eine höhere Entwicklungsversion existiert — Linie klar benennen.

Unklarheit über die Semantik ist keine Ausnahme: nachfragen.

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Framework-Release **1.0.0**
- Roadmap-Kennzeichnung „aktuell“ für 1.0.0

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `07_DOCUMENTATION.md`
- `08_PROJECT_STATE.md`
- `09_RELEASE_PROCESS.md`
- `10_SECURITY.md`
- `README.md`
