# AI-DK – Backlog nach 1.0.x (nicht implementiert)

Status: **Ideen / spätere Freigabe**  
Erfasst: 2026-07-29 · Bezug: Qualitätsrelease **1.0.2**

Dieses Dokument hält Ergänzungen fest, die **bewusst nicht** in 1.0.2 liegen.  
1.0.2 = nur Qualität am bestehenden Core. Keine neuen Feature-Dokumente hieraus ableiten, ohne Freigabe.

---

## Nach / parallel zu 1.1 (Erweiterungen)

### 1. Governance

Geplant: `docs/GOVERNANCE.md`

Inhaltsskizze:

- Wer darf Core-Regeln ändern?
- Wann ist eine Änderung Breaking?
- Wer entscheidet bei Konflikten?
- Review- und Freigabeprozess für AI-DK selbst

Orientierung: gängige Open-Source-Governance (ohne Spekulation über fremde Projekte als Norm).

### 2. Architecture Decision Records (ADRs)

Geplant: `docs/adr/`

Beispiele:

- `0001-core-layout.md`
- `0002-numbering.md`
- `0003-document-structure.md`

Zweck: **Warum** Entscheidungen gelten — nicht nur **welche**.

### 3. Glossar

Geplant: `docs/GLOSSARY.md`

Begriffe einmal definieren, z. B.:

Core · Profile · Extension · Rule · Guideline · Recommendation · Constraint · Workflow · Sprint · Verbindliche Regel · Empfehlung

### 4. Qualitätsmetriken (für AI-DK selbst)

Geplant: `docs/QUALITY.md` (oder `.ai/QUALITY.md`)

Skizze:

- Richtwerte für Dokumentgröße
- Redundanzgrenzen
- Pflicht-Checklisten
- Reviewregeln für Framework-Änderungen

Nicht Software-Produktmetriken — Meta-Qualität des Regelwerks.

---

## Ab Version 2.0

### Profiles

- **2.0:** erstes Profile **Flutter** (`profiles/flutter/`) — **umgesetzt**
- Danach weitere Technologien nach Freigabe

### RFCs / Proposals

Geplant: `rfcs/` (o. ä.)

Vor größeren Änderungen ein Proposal, z. B. `rfcs/0001-machine-readable-rules.md` (falls noch nicht über 1.1 erledigt).

---

## Abgrenzung zu 1.1

| Thema | Wo |
|-------|-----|
| YAML / `.ai/rules/` | [1.1_MACHINE_READABLE_RULES.md](1.1_MACHINE_READABLE_RULES.md) |
| Governance, ADR, Glossar, QUALITY, RFC | **dieses Backlog** — eigene Freigaben |

---

## Hinweis aus 1.0.2-Audit

Akzeptierte Ausreißer bei Dokumentlänge (kein Kürzen ohne Substanzverlust):

- `.ai/tests/SCENARIOS.md` — Prüfkatalog
- `.ai/03_CODING_STANDARDS.md` — Regelbreite
- `.ai/08_PROJECT_STATE.md` — Regeln + lebendiger Stand
