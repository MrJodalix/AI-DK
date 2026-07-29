# ADR 0003 – Einheitliche Dokumentstruktur

Status: **Accepted**  
Datum: 2026-07-29

## Kontext

Uneinheitliche Abschnitte erschweren Checks, Reviews und Agenten-Navigation.

## Entscheidung

Norm-Dokumente im Core folgen (soweit sinnvoll) denselben Hauptüberschriften: Ziel, Geltungsbereich, Grundprinzipien, Verbindliche Regeln, Empfehlungen, KI-Verhalten, Checkliste, Beispiele, Ausnahmen, Version.

**Ausnahme:** `01_BOOTSTRAP.md` hat eine schlankere, agentenspezifische Struktur (eigene Checklist in `check_core.py`).

## Konsequenzen

- Automatische Heading-Prüfung möglich.
- Weniger „wo steht die Pflichtregel?“-Suche.
- Spezialdocs dürfen Ausnahmen haben, wenn dokumentiert.
