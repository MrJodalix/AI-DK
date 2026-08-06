# ADR 0002 – Nummerierung Core-Dokumente

Status: **Accepted** (ergänzt 2026-08-06)  
Datum: 2026-07-29

## Kontext

Dokumente brauchen eine stabile, semantische Reihenfolge für Menschen und Agenten.

## Entscheidung

| Nr. | Rolle |
|-----|--------|
| `00` | Charter — Warum |
| `01` | Bootstrap — Wie starte ich (Agenten) |
| `02` | Workflow — Wie arbeite ich |
| `03`–`04` | Code / Tests |
| `05` | KI-Verhalten |
| `06`–`11` | Git, Docs, State, Release, Security, Version |
| `12` | I18N / Nutzertexte (technologieunabhängig) |

`01` war zunächst reserviert und wurde in 2.1 als Bootstrap belegt.  
`12` ergänzt den Core ab **2.3.5** für zentrale Nutzertexte / Mehrsprachigkeit (nicht Profile-spezifisch).

## Konsequenzen

- Sortierung im Dateisystem spiegelt Lern- und Startpfad.
- Umbenennungen sind Breaking ohne Migrationshinweis.
- Neue Querschnittsthemen erhalten die nächste freie Nummer, statt in Profiles zu landen, wenn sie stackübergreifend gelten.
