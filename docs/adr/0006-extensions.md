# ADR 0006 – Extensions-Schicht

Status: **Accepted**  
Datum: 2026-07-29

## Kontext

Core und Profiles sind tool-agnostisch. Konkrete IDE-/Chat-Formate brauchen Adapter, ohne die Norm zu verunreinigen.

## Entscheidung

Ebene **Extensions** unter `extensions/`:

- mappt Core (+ Profile) auf Werkzeugvorlagen
- ersetzt keine kanonischen Regeln
- erste Adapter: Cursor, Generic (Chat)

CI für `check_core.py` liegt unter `.github/workflows/` (Repo-Qualität), nicht als Profile-Inhalt.

## Konsequenzen

- Zielprojekte kopieren Vorlagen, nicht die Norm umschreiben.
- Weitere Tool-Adapter nach Freigabe.
- Weitere Tech-Profiles bewusst zurückgestellt; Fokus Flutter.
