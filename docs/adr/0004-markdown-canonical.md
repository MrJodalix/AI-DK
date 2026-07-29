# ADR 0004 – Markdown kanonisch, YAML abgeleitet

Status: **Accepted**  
Datum: 2026-07-29

## Kontext

Agenten und Tools profitieren von maschinenlesbaren Regeln; Drift zu Markdown ist ein Risiko.

## Entscheidung

- Markdown unter `.ai/` (und Profile-Markdown) ist **kanonisch**.
- YAML unter `.ai/rules/` bzw. `profiles/*/rules/` ist **Ableitung**.
- Keine `must`-Regel nur in YAML.
- Sync-Pflicht bei inhaltlichen Markdown-Änderungen.

## Konsequenzen

- Projekte ohne YAML bleiben mit Markdown gültig.
- Checks validieren YAML-Schema, ersetzen aber nicht den Normtext.
