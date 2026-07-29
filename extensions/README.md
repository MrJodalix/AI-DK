# AI-DK Extensions

Version: 2.3.0

## Zweck

Extensions mappen **Core (+ optionales Profile)** auf konkrete KI-Werkzeugformate.

```text
Core / Profile     = Norm (kanonisch)
Extension          = Adapter / Vorlage für ein Tool
```

Extensions **ersetzen** keine Core- oder Profile-Regeln. Bei Konflikt gewinnt Markdown-Core (Prinzipien) bzw. Profile (Stack).

## Verfügbare Extensions

| Extension | Pfad | Werkzeug |
|-----------|------|----------|
| Cursor | [cursor/](cursor/) | Cursor IDE / Agent |
| Generic | [generic/](generic/) | ChatGPT, Claude.ai, andere Chat-Agenten |

## Nutzung

1. Core (und ggf. `profiles/flutter/`) ins Zielprojekt übernehmen.
2. Passende Extension-Vorlage kopieren oder verlinken.
3. Framework-Version in der Spezifikationsformel aktuell halten (`README.md`).

## Neue Extensions

Nur nach Freigabe. Mindestinhalt: `README.md` mit Mapping-Hinweis und Startinstruktion (Bootstrap).

## Aktiver Profile-Fokus

Aktuell wird nur das **Flutter-Profile** gepflegt. Weitere Profiles sind nicht Bestandteil dieser Extension-Lieferung.
