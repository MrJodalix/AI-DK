# AI-DK Governance

Version: 2.2.0

## Ziel

Dieses Dokument regelt, **wer** am AI-DK-Framework was ändern darf, **wann** eine Änderung Breaking ist und **wie** Freigaben laufen.

Es betrifft AI-DK selbst — nicht die Governance von Zielprojekten, die AI-DK nur nutzen.

---

## Rollen

| Rolle | Rechte |
|-------|--------|
| **Maintainer** | Core, Profiles, docs, Releases, Tags; finale Entscheidung bei Konflikten |
| **Contributor** | Vorschläge (PR/Patch/RFC); keine eigenmächtigen Releases |
| **KI-Agent** | Darf Änderungen **vorbereiten**; setzt Versionen/Tags/Releases nur nach ausdrücklicher Freigabe |

Aktueller Maintainer-Kontext: Repository-Owner von [AI-DK](https://github.com/MrJodalix/AI-DK).

---

## Was darf geändert werden

| Bereich | Wer | Voraussetzung |
|---------|-----|----------------|
| Core `.ai/00`–`11` | Maintainer (ggf. nach Review) | Freigabe; Changelog; SemVer |
| `.ai/rules/` YAML | Maintainer / Contributor | Sync mit Markdown; Markdown bleibt kanonisch |
| Profiles | Maintainer | Freigabe; kein Widerspruch zu Core-Prinzipien |
| `docs/` (Governance, ADR, Glossar, Quality) | Maintainer / Contributor | Nachvollziehbarkeit; bei Normwirkung Freigabe |
| `rfcs/` | jeder | RFC-Prozess einhalten |
| Releases / Tags | Maintainer (oder KI nach Freigabe) | Release-Prozess + `check_core.py` PASS |

---

## Breaking Changes

Eine Änderung am Framework ist **Breaking**, wenn sie:

1. bestehende verbindliche Regeln so ändert, dass konformes Verhalten vorher **inkonform** wird, oder
2. kanonische Dateipfade/IDs entfernt oder umbenennt ohne Migrationspfad, oder
3. die Spezifikationsformel / Bootstrap-Semantik so ändert, dass Agenten-Startsequenzen brechen.

Breaking → **MAJOR** gemäß `.ai/11_VERSION.md`, mit klarem Changelog-Abschnitt.

Nicht Breaking (typisch **MINOR**/**PATCH**):

- neue Dokumente, Profiles, ADRs, RFCs
- Klarstellungen ohne Regelumkehr
- Check-/YAML-Erweiterungen ohne Markdown-Widerspruch

---

## Entscheid bei Konflikten

1. **Markdown Core** vor YAML und vor Profile-Details zu Prinzipien.
2. **Profile** vor Ad-hoc-Stack-Ideen zu Tech-Details.
3. Bei Maintainer-Konflikt: dokumentierte Entscheidung (ADR oder Changelog) schlägt informelle Chat-Aussagen.
4. Unklarheit → nachfragen; keine stillen Normänderungen durch die KI.

---

## Review- und Freigabeprozess (AI-DK)

1. Änderung vorschlagen (Issue, RFC bei größeren Themen, oder direkter Diff bei kleinen Fixes).
2. Betroffene kanonische Docs + YAML-Sync prüfen.
3. `python3 .ai/tests/check_core.py` → PASS.
4. **Ausdrückliche Freigabe** durch Maintainer (Chat, Review-Approve, o. Ä.).
5. Commit · ggf. Tag · Push nur nach Freigabe (KI: keine eigenmächtigen Releases).

Kleine typo-/Link-Fixes: verkürzter Weg erlaubt, wenn kein Regelinhalt kippt — trotzdem Changelog bei Release bündeln.

---

## RFC-Pflicht

Ein RFC unter `rfcs/` ist **empfohlen** vor:

- neuen Core-Dokumenten mit Normwirkung
- Breaking Changes
- neuen Profile-Familien oder Architektur-Ebenen (z. B. Extensions)

Ein RFC ist **nicht nötig** für:

- reine Qualitäts-/Klarstellungspatches
- ADR-Nachzüge bereits getroffener Entscheidungen
- Profile-Inhaltsupdates innerhalb eines freigegebenen Profiles

Details: `rfcs/README.md`.

---

## Verwandte Dokumente

- `.ai/11_VERSION.md`
- `.ai/09_RELEASE_PROCESS.md`
- `.ai/01_BOOTSTRAP.md`
- `docs/QUALITY.md`
- `rfcs/README.md`
