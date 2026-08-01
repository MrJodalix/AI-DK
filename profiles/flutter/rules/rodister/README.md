# Rodister — Cursor-Rules (Consumer)

Produkt-spezifische Cursor-Rules für **Rodister**. Liegen bewusst unter `profiles/flutter/rules/rodister/`, nicht in der generischen `flutter.yml`.

## Warum hier?

- Rodister-`.cursor/` ist im App-Repo oft gitignored → Rules würden lokal bleiben.
- Versionierung und Parallelentwicklung mit AI-DK: kanonische Kopie im Submodule / AI-DK-Repo.
- Generisches Flutter-Profile (`flutter.yml`, STACK/…) bleibt frei von Produktpfaden.

## Cursor verdrahten

Im Rodister-Workspace Symlinks (oder Kopien) nach `.cursor/rules/`:

```bash
# vom Rodister-Repo-Root
mkdir -p .cursor/rules
cd .cursor/rules
for f in ../../ai-dk/profiles/flutter/rules/rodister/*.mdc; do
  ln -sfn "$f" "$(basename "$f")"
done
```

Cursor lädt Rules aus `.cursor/rules/`; die Dateien hier sind die Quelle der Wahrheit.

## Dateien

| Datei | Thema |
|-------|--------|
| `aidk.mdc` | Bootstrap-Pfade + Stack-Ausnahme Provider/Hive |
| `l10n-no-hardcoded-ui-strings.mdc` | UI nur über `AppStrings` |
| `page-help-keep-in-sync.mdc` | Seitenhilfe DE/EN |
| `lastenheft-keep-in-sync.mdc` | Lastenheft + Persistenz |
| `one-class-per-file.mdc` | Eine Klasse pro Datei / Feature-Ordner |
| `dart-doc-comments.mdc` | Doc-Kommentare Input/Output |
| `git-ssh-commits.mdc` | Commits nur auf Anfrage, Push per SSH |

## Pflege

- Inhaltliche Änderungen an Rodister-Rules: hier im AI-DK-Tree (bzw. Submodule), dann AI-DK committen/pushen und in Rodister den Submodule-Pin bumpen.
- Generische Flutter-Normen weiter in `../flutter.yml` und `profiles/flutter/*.md`.
