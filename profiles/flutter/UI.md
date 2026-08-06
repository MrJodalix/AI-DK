# AI-DK Flutter – UI

Version: 1.0.1

## Ziel

Mobile- und Desktop-UI-Konventionen für Flutter-Projekte unter diesem Profile (SafeArea, Tastatur, Bottom Sheets, FAB, Material 3).

Ergänzt `CODING.md` (Widgets/Theme) und `ARCHITECTURE.md` (Presentation-Schicht).

---

## Geltungsbereich

Gilt für Presentation-Code (`*Screen`, Sheets, Shell).  
Gilt nicht für Domain-/Application-Logik.

---

## Grundprinzipien

1. **Touch-Ziele und System-Insets bleiben erreichbar** (Gestenleiste, Notch, Tastatur).
2. **`viewInsets` ≠ `viewPadding`:** Tastatur = `viewInsets`; Systemleisten = `viewPadding` (typisch über `SafeArea`).
3. **Ein Muster pro Screen-Typ** — nicht „fixierter Button“ und „alles in ListView“ mischen, ohne den Konflikt zu lösen.

---

## Verbindliche Regeln

### Formular-Screens (Import, Editor, Einstellungen)

1. `SafeArea` um den Screen-`body`.
2. **Standardmuster (kurze Formulare):**  
   `SafeArea` → `Column` → `Expanded(ListView(...))` + unten fixiertes `Padding` mit Primäraktion/Status.  
   Unteres Padding: `16 + MediaQuery.viewInsetsOf(context).bottom`.
3. **Wenn die Tastatur Felder oder Labels verdeckt** (langer Inhalt, Kamera-Preview, viele Felder):  
   - gesamte Oberfläche scrollbar (`ListView` inkl. Primäraktion), **oder**  
   - sekundären Block (z. B. Kamera) bei offener Tastatur ausblenden, **und**  
   - fokussiertes Feld per `Scrollable.ensureVisible` sichtbar halten.
4. Primäraktion **nicht** nur ans Ende einer langen `ListView` hängen, **wenn** darunter Gestenleiste/Keyboard sie dauerhaft verdecken würde — dann Muster 2 oder 3.

### Bottom Sheets

1. `showModalBottomSheet(..., isScrollControlled: true, useSafeArea: true)`.
2. Sheet-Inhalt: `SafeArea(top: false)` **und** `padding.bottom += MediaQuery.viewInsetsOf(context).bottom`.
3. Bei mehr als wenigen Feldern: `SingleChildScrollView` (sonst verdeckt Gestenleiste den Speichern-Button).

### FloatingActionButtons

- Mehrere FABs in Shell + Push-Routen: **eindeutige `heroTag`s** (sonst Hero-Crash bei `IndexedStack` / parallelen Scaffolds).

### Navigation (go_router)

- Nach `go()` auf Unterrouten kann die Shell-Navigation verschwinden — für Detail-/Editor-Flows `push` / `pushReplacement` bevorzugen.

### Material 3

- Themes zentral (`core/theme/` o. Ä.); keine wilden Hardcoded-Farben ohne Theme-Bezug.
- Fehler/Hinweise als `SnackBar` oder Inline-Text — nicht als unbehandelte Exceptions in der UI.
- Texte für Titel, Labels, Buttons, SnackBars, Tooltips: zentrale Ressourcen laut `I18N.md` (keine Literale im Widget).

---

## Checkliste

- [ ] SafeArea am Screen-Body
- [ ] Primäraktion mit Tastatur + Gestenleiste erreichbar
- [ ] Bottom Sheet: `useSafeArea` + `viewInsets` + ggf. Scroll
- [ ] FABs: eindeutige `heroTag`s
- [ ] Nutzertexte über L10n/Katalog (`I18N.md`)
- [ ] Device-/Emulator-Smoke bei Layout-Änderungen (siehe `DEV_SETUP.md`)

---

## Version

Dokumentversion: 1.0.1

Änderung in dieser Version:

- Verweis auf `I18N.md` für nutzersichtbare Texte

Verwandte Dokumente:

- `profiles/flutter/CODING.md`
- `profiles/flutter/ARCHITECTURE.md`
- `profiles/flutter/I18N.md`
- `profiles/flutter/DEV_SETUP.md`
- `profiles/flutter/TESTING.md`
