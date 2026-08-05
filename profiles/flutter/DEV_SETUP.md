# AI-DK Flutter – Dev Setup

Version: 1.0.0

## Ziel

Kurze Checkliste, damit Agenten und Entwickler Flutter-Apps **lokal bauen und auf Gerät/Emulator** laufen lassen können — ohne spekulative SDK-Pfade.

---

## Pflicht vor erstem Debug-Lauf

1. **Flutter SDK** installiert und erreichbar (`flutter doctor`).
2. Im Projekt dokumentieren (falls nicht im PATH): z. B. `.vscode/settings.json` → `dart.flutterSdkPath`, `launch.json`.
3. **Android:** SDK, JDK, USB-Debugging / Emulator; Gerät mit `adb devices` sichtbar (`device`, nicht `unauthorized`).
4. **Linux-Desktop:** benötigte GTK-/CMake-Abhängigkeiten laut Flutter-Docs.
5. `flutter pub get` erfolgreich; Generatoren (`build_runner`) wenn Drift/Freezed genutzt werden.

Keine erfundenen SDK-Pfade — im Zweifel im Projektstand / README des Zielprojekts nachlesen oder nachfragen.

---

## Drift-Schema-Bump (Kurz-Checkliste)

Bei Änderung von Tabellen / `schemaVersion`:

1. Tabelle(n) in Drift-Definitionen anpassen
2. `schemaVersion` erhöhen
3. `onUpgrade`-Migration schreiben (kein stilles Datenlöschen ohne Absicht)
4. `dart run build_runner build -d` (oder Projektäquivalent)
5. Upgrade-Migrationstest (nicht nur `onCreate`) — siehe `TESTING.md`

---

## Device-Smoke (vor UX-/Release-Feinschliff)

Kurz auf physischem Gerät oder Emulator prüfen:

- [ ] Primärformulare: Button mit **offener Tastatur** erreichbar
- [ ] Bottom Sheets: Speichern über der **Gesten-/Navigationsleiste**
- [ ] Shell-FABs: kein Hero-Crash beim Wechsel Tab ↔ Detail
- [ ] Offline-Kern ohne Netz startfähig (falls Offline-First)

Details zu Tests: `TESTING.md` und Core `.ai/04_TESTING.md`.

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Erstes Dev-Setup-/Smoke-Dokument (Zielprojekt-Retro)

Verwandte Dokumente:

- `profiles/flutter/UI.md`
- `profiles/flutter/TESTING.md`
- `profiles/flutter/STACK.md`
- `.ai/01_BOOTSTRAP.md`
