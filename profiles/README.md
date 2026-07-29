# AI-DK Profiles

Version: 2.0.0

## Zweck

Profiles vertiefen den **technologieunabhängigen Core** um stackspezifische Regeln.

```text
Core (.ai/)     → gilt immer
Profile         → gilt nur, wenn das Projekt das Profile aktiv übernimmt
Extensions      → Tool-Anbindung (später)
```

## Konfliktregel (verbindlich)

1. **Core gewinnt** bei universellen Prinzipien, Workflow, Security, Git und Versionierung.
2. **Profile gewinnt** bei sprach-, framework- und paketbezogenen Details.
3. Ein Profile **darf Core-Prinzipien nicht widersprechen** — nur konkretisieren.
4. Projektspezifische Styleguides dürfen Profile-Details überschreiben; Abweichungen sind zu dokumentieren (`08_PROJECT_STATE.md` im Zielprojekt).
5. **Markdown ist kanonisch**; YAML unter `profiles/<name>/rules/` ist abgeleitet (wie Core 1.1).

## Verfügbare Profiles

| Profile | Pfad | Ab Version |
|---------|------|------------|
| Flutter | [flutter/](flutter/) | **2.0.0** |

## Nutzung in Zielprojekten

1. Core unter `.ai/` übernehmen.
2. Gewähltes Profile (z. B. `profiles/flutter/`) mitführen oder verlinken.
3. Im Projektstand vermerken: aktives Profile + Version.
4. Bei Konflikten: Core-Prinzipien + dokumentierte Projektentscheidung.

## Neues Profile

Nur nach Freigabe. Mindestinhalt:

- `README.md` (Geltung, Konfliktregel, Index)
- `STACK.md` (kanonische Technologieentscheidungen)
- Coding- und Testing-Vertiefung
- optional `rules/*.yml` (Ableitung)
