# AI-DK Glossar

Version: 2.2.0

Begriffsdefinitionen für die AI-DK-Spezifikation. Bei Konflikt mit einem Core-Dokument gilt das Core-Dokument; dieses Glossar vereinheitlicht die Sprache.

| Begriff | Bedeutung |
|---------|-----------|
| **AI-DK** | Name des Standards („AI Engineering Standard“). |
| **Spezifikation** | Versionierter, verbindlicher Normstand von AI-DK (nicht nur eine Dateisammlung). |
| **Core** | Universelle Regeln unter `.ai/00`–`11`; technologie- und modellunabhängig. |
| **Bootstrap** | Agenten-Einstieg (`01_BOOTSTRAP.md`); verbindliche Startsequenz je Sitzung/Aufgabe. |
| **Profile** | Technologieabhängige Vertiefung unter `profiles/<name>/`; konkretisiert den Core, widerspricht ihm nicht. |
| **Extension** | Geplante Anbindung an konkrete KI-Werkzeuge/Formate (noch nicht ausgearbeitet). |
| **Rule / Verbindliche Regel** | Muss-Anforderung (`must`); Abweichung nur mit begründeter Ausnahme. |
| **Empfehlung / Recommendation** | Soll-Hinweis (`should`); Preferenz ohne harten Block. |
| **Guideline** | Orientierungshilfe ohne denselben Verbindlichkeitsgrad wie eine Rule. |
| **Constraint** | Harte Einschränkung (z. B. „kein Tech-Stack im Core“). |
| **Workflow** | Verbindlicher Ablauf (`02_DEVELOPMENT_WORKFLOW.md`). |
| **Sprint** | Abgegrenzter Arbeitsabschnitt am Framework oder Zielprojekt (Kommunikationsbegriff). |
| **Freigabe** | Ausdrückliche Zustimmung des Maintainers vor Umsetzung/Release. |
| **Kanonisch** | Maßgebliche Quelle bei Konflikten (i. d. R. Core-Markdown). |
| **ADR** | Architecture Decision Record — dokumentiert *warum* eine Entscheidung gilt (`docs/adr/`). |
| **RFC** | Request for Comments — Vorschlag vor größeren Änderungen (`rfcs/`). |
| **Framework-Version** | SemVer des AI-DK-Gesamtstands (README / Tags). |
| **Dokumentversion** | Version eines einzelnen Regeltexts; darf hinter der Framework-Version zurückbleiben, wenn kompatibel. |

## Verwandte Dokumente

- `README.md`
- `docs/GOVERNANCE.md`
- `.ai/11_VERSION.md`
- `.ai/rules/README.md`
