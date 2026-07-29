# ADR 0001 – Core / Profiles / Extensions

Status: **Accepted**  
Datum: 2026-07-29

## Kontext

AI-DK braucht universelle Regeln und zugleich Stack-Vertiefungen, ohne den Core mit Flutter/Python/.NET zu verunreinigen.

## Entscheidung

Drei Ebenen:

1. **Core** (`.ai/`) — technologieunabhängig
2. **Profiles** (`profiles/<tech>/`) — stackspezifisch
3. **Extensions** — Tool-Anbindung (später)

Konflikt: Core-Prinzipien gewinnen; Profile gewinnen bei Tech-Details.

## Konsequenzen

- Core bleibt portabel.
- Flutter u. a. leben unter Profiles.
- Neue Technologien = neues Profile, kein Aufblasen des Cores.
