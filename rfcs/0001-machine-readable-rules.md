# RFC 0001 – Maschinenlesbare Regeln

Status: **Accepted**  
Datum: 2026-07-29  
Umsetzung: Framework **1.1.0**

## Zusammenfassung

Core-Regeln zusätzlich als kompakte YAML-Ableitung unter `.ai/rules/` bereitstellen; Markdown bleibt kanonisch.

## Motivation

Agenten und Tools sollen stabile IDs und Severities nutzen können, ohne den Normtext zu ersetzen.

## Vorschlag

- Schema in `.ai/rules/README.md`
- Dateien `coding.yml`, `testing.yml`, …
- Sync-Pflicht; Konfliktregel Markdown > YAML

## Alternativen

- Nur Markdown (schlechter für Tooling)
- YAML als einzige Quelle (Drift- und Lesbarkeitsrisiko)

## Auswirkungen

MINOR 1.1.0; keine Breaking für Markdown-only-Projekte.

## Entscheidung

**Accepted** — umgesetzt. Details: `.ai/plans/1.1_MACHINE_READABLE_RULES.md`, ADR [0004](../docs/adr/0004-markdown-canonical.md).
