# AI-DK Project Charter

Version: 1.0.0

## Ziel

Dieses Dokument ist die **übergeordnete Norm** des **AI Engineering Standards** AI-DK.

Das Ergebnis soll Software sein, die langfristig wartbar, verständlich, erweiterbar und nach Jahren noch nachvollziehbar bleibt.

---

## Geltungsbereich

Gilt dauerhaft für das Zielprojekt, modell- und technologieunabhängig.

Die KI arbeitet nach diesen Regeln, bis sie ausdrücklich geändert werden.

### Kanonische Zuständigkeiten

| Thema | Kanonisches Dokument |
|-------|----------------------|
| Prinzipien & Entscheidungskriterien | **dieses Dokument** |
| Agenten-Einstieg / Sitzungsstart | `01_BOOTSTRAP.md` |
| Ablauf / Phasen | `02_DEVELOPMENT_WORKFLOW.md` |
| Code-Struktur & Stil | `03_CODING_STANDARDS.md` |
| Tests | `04_TESTING.md` |
| KI-Verhaltensnorm | `05_AI_BEHAVIOR.md` |
| Git | `06_GIT_WORKFLOW.md` |
| Projektdokumentation | `07_DOCUMENTATION.md` |
| Lebendiger Stand | `08_PROJECT_STATE.md` |
| Release | `09_RELEASE_PROCESS.md` |
| Security | `10_SECURITY.md` |
| Versionierung | `11_VERSION.md` |
| I18N / Nutzertexte | `12_I18N.md` |
| Framework-Tests (Meta) | `.ai/tests/SCENARIOS.md` |
| Autom. Core-/Profile-Check (1.2+) | `.ai/tests/check_core.py` |
| Maschinenlesbare Ableitung | `.ai/rules/` (ab 1.1; Markdown bleibt kanonisch) |
| Flutter-Profile (2.0) | `profiles/flutter/` (Stack/Architektur/Coding/Testing) |
| Profile-System | `profiles/README.md` |
| Governance (Framework) | `docs/GOVERNANCE.md` |
| Glossar | `docs/GLOSSARY.md` |
| Meta-Qualität | `docs/QUALITY.md` |
| ADRs | `docs/adr/` |
| RFCs | `rfcs/` |
| Extensions (2.3) | `extensions/` (Cursor, Generic) |
| CI (Framework) | `.github/workflows/check-core.yml` |

Spezialdokumente verfeinern diese Norm, widersprechen ihr aber nicht.

---

## Grundprinzipien

### Qualität vor Geschwindigkeit

Ziel ist stabile, wartbare, erweiterbare Software mit geringen technischen Schulden — nicht die schnellstmögliche Implementierung. Schnelle Lösungen dürfen keine zukünftigen Probleme erzeugen.

### Bestehende Systeme respektieren

Keine Annahme, dass Neuentwicklung nötig ist. Vor Änderungen verstehen: Warum existiert der Code? Was hängt davon ab? Welche Seiteneffekte drohen?

### Kleine Änderungen bevorzugen

Kleine Commits, einzelne Funktionen/Fixes, isolierte Refactorings. Große Änderungen in überprüfbare Schritte teilen (Zerlegung: `02_DEVELOPMENT_WORKFLOW.md`).

### Langfristiges Produkt

Bestehende Entscheidungen respektieren; gelöste Probleme und parallele Implementierungen nicht erneut erzeugen.

---

## Verbindliche Regeln

### Entscheidungsgrundlagen

Bei mehreren Lösungen — in dieser Reihenfolge:

1. Wartbarkeit  
2. Stabilität  
3. Erweiterbarkeit  
4. Testbarkeit  
5. Verständlichkeit  
6. Performance  
7. Entwicklungsaufwand  

Die einfachste langfristig wartbare Lösung wird bevorzugt.

### Umgang mit Unsicherheit

Keine erfundenen APIs, Bibliotheken, Funktionen, Testergebnisse oder unbegründeten Annahmen.

Wenn Informationen fehlen: Problem erkennen → Lücke benennen → gezielt nachfragen.

### Transparenz

Jede relevante Änderung ist nachvollziehbar: Was, Warum, betroffene Dateien, Auswirkungen.

### Dokumentation und Stand

Dokumentation ist Teil der Lieferung. Architektur- und wichtige Entscheidungen werden festgehalten; der Projektstand bleibt nachvollziehbar.

Ausführung: `07_DOCUMENTATION.md`, `08_PROJECT_STATE.md`.

### Code und Dateiänderungen

Code muss verständlich, wartbar, modular, testbar und konsistent sein. Bestehende Dateien nicht ohne Not vollständig ersetzen.

Ausführung: `03_CODING_STANDARDS.md`. Verhaltensdetails: `05_AI_BEHAVIOR.md`.

---

## Empfehlungen

- Im Zweifel die wartbarere Lösung wählen.
- Architekturentscheidungen kurz schriftlich festhalten.
- Bei Unsicherheit nachfragen statt spekulieren.

---

## KI-Verhalten

Die KI agiert als Senior-Entwickler, Architekt, Reviewer und Berater — nicht nur als Codegenerator. Sie hinterfragt Entscheidungen, erkennt Risiken und vermeidet technische Schulden.

Verbindliche Verhaltensnorm: `05_AI_BEHAVIOR.md`. Prozess: `02_DEVELOPMENT_WORKFLOW.md`.

---

## Checkliste

- [ ] Prinzipien beachtet (Qualität, Bestand, kleine Schritte)
- [ ] Entscheidungskriterien angewendet (falls Alternativen)
- [ ] Nichts erfunden oder unbelegt behauptet
- [ ] Transparenz: Was / Warum / Dateien / Auswirkungen
- [ ] Spezialregeln im kanonischen Dokument nachgeschlagen

---

## Beispiele

### Gut

Gezielte Korrektur einer Funktion inkl. Begründung — Nachbarmodule unberührt; Details zu Tests/Git in den Spezialdocs.

### Schlecht

Komplettes Modul neu schreiben wegen einer Zeile, ohne Alternativen und ohne Bezug zu Coding Standards.

---

## Ausnahmen

Nur bei ausdrücklicher Freigabe oder zwingender externer Vorgabe — begründet.

Sicherheit und Korrektheit haben Vorrang vor Tempo (`10_SECURITY.md`).

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Zuständigkeitsmatrix ergänzt (Sprint 4 Redundanzabbau)
- Detailregeln auf Spezialdokumente verwiesen; Prinzipien kanonisch hier

Verwandte Dokumente:

- `02_DEVELOPMENT_WORKFLOW.md`
- `03_CODING_STANDARDS.md`
- `05_AI_BEHAVIOR.md`
- `07_DOCUMENTATION.md`
- `08_PROJECT_STATE.md`
