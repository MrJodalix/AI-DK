# ADR 0002 – Nummerierung `00`–`11`

Status: **Accepted**  
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

`01` war zunächst reserviert und wurde in 2.1 als Bootstrap belegt.

## Konsequenzen

- Sortierung im Dateisystem spiegelt Lern- und Startpfad.
- Umbenennungen sind Breaking ohne Migrationshinweis.
