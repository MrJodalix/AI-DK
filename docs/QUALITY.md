# AI-DK Quality (Meta)

Version: 2.2.0

## Ziel

Qualitätsmaßstäbe für das **AI-DK-Regelwerk selbst** — nicht für Software-Produktmetriken von Zielprojekten.

---

## Dokumentgröße (Richtwerte)

| Art | Orientierung | Aktion bei Überschreitung |
|-----|--------------|---------------------------|
| Typisches Core-Normdokument | bis ~350 Zeilen | Aufspaltung oder Verweis statt Wiederholung prüfen |
| Bootstrap / kurze Spec-Docs | deutlich kürzer | so lassen |
| Prüfkataloge (`SCENARIOS`) | länger erlaubt | Ausreißer akzeptiert |
| Lebendiger Stand (`08`) | länger erlaubt | Regeln vs. Stand klar trennen |

Akzeptierte Ausreißer (historisch): `SCENARIOS.md`, `03_CODING_STANDARDS.md`, `08_PROJECT_STATE.md` — kein Kürzen ohne Substanzverlust.

---

## Redundanz

1. **Eine kanonische Zuständigkeit** pro Thema (Charter-Matrix).
2. Andere Docs **verweisen**, wiederholen keine parallelen Muss-Regeln.
3. YAML ist Ableitung — keine Pflichtregel nur in YAML.
4. Profiles wiederholen Core-Prinzipien nicht als neue Norm.

---

## Pflicht vor Framework-Änderung

- [ ] Betroffene kanonische Datei identifiziert
- [ ] Keine Doppelpflege eingeführt
- [ ] YAML-Sync geprüft (falls Rules betroffen)
- [ ] `python3 .ai/tests/check_core.py` → PASS
- [ ] Changelog-Eintrag vorbereitet (bei Release)
- [ ] Freigabe eingeholt (`docs/GOVERNANCE.md`)

---

## Reviewregeln (Framework)

Reviewer / Maintainer prüfen:

1. Widerspricht die Änderung der Charter oder dem Bootstrap?
2. Ist die SemVer-Klassifikation plausibel?
3. Bleibt der Core tech-agnostisch?
4. Sind Beispiele und Checklisten noch wahr?

Schweregrad analog AI Behavior: Security/Korrektheit der Norm > Wartbarkeit > Stil.

---

## Verwandte Dokumente

- `docs/GOVERNANCE.md`
- `.ai/00_PROJECT_CHARTER.md`
- `.ai/tests/check_core.py`
- `.ai/09_RELEASE_PROCESS.md`
