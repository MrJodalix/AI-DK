# AI-DK Security

Version: 1.0.0

## Ziel

Dieses Dokument definiert verbindliche Mindestsicherheitsregeln für Projekte, die AI-DK nutzen.

Es soll sicherstellen:

- Schutz von Geheimnissen und Zugangsdaten
- bewusstes Risiko statt blinder Änderungen
- keine Scheinsicherheit durch unbelegte Aussagen der KI
- Vorrang von Sicherheit vor Bequemlichkeit und Tempo

---

## Geltungsbereich

Gilt für:

- Umgang mit Secrets und sensiblen Daten
- sichere Änderungs- und Review-Praxis durch die KI
- grundlegende Vertrauensgrenzen in Software
- Abhängigkeiten und Konfiguration auf Prinzipienebene

Gilt nicht für:

- produkt-, branchen- oder zertifizierungsspezifische Compliance-Kataloge
- Stack-spezifische Hardening-Guides (gehören in Profiles)
- vollständige Penetrationstests oder Audit-Methodiken

Bei Konflikt mit einer engeren Organisations-Sicherheitsrichtlinie gilt die engere Richtlinie. Die Grundprinzipien dieses Dokuments und der Charter bleiben verbindlich.

Kanonische Zuständigkeit für Security-Mindestregeln gemäß Matrix in `00_PROJECT_CHARTER.md`.

Dieses Dokument ist technologie- und modellunabhängig.

---

## Grundprinzipien

### Sicherheit vor Tempo

Sicherheitsrisiken werden nicht zugunsten schneller Lieferungen ignoriert.

### Minimale Angriffsfläche

Nur notwendige Rechte, Daten und Exposition. Standard: so wenig wie möglich freigeben.

### Keine Scheinsicherheit

Ungeprüfte Behauptungen („ist sicher“, „verschlüsselt“, „nicht angreifbar“) sind unzulässig.

### Verteidigung in der Tiefe

Eine einzelne Kontrolle reicht nicht; kritische Pfade brauchen mehrere sinnvolle Absicherungen, soweit im Projektkontext möglich.

---

## Verbindliche Regeln

### Secrets und sensible Daten

- Keine Secrets in Quellcode, Commits, Logs, Screenshots, Issues oder Dokumentation.
- Keine Secrets in Prompts an die KI einfügen, sofern vermeidbar; vorhandene Lecks sofort melden.
- Konfiguration mit Geheimnissen über vom Projekt vorgesehene sichere Mechanismen (z. B. Umgebung, Secret-Store) — nicht hardcoden.
- Bei Verdacht auf Leak: betroffene Systeme/Zugänge als kompromittiert behandeln, rotieren und dokumentieren; Git-Historie gemäß `06_GIT_WORKFLOW.md` und Freigabe bereinigen.

### Vertrauensgrenzen

- Eingaben von außerhalb der Vertrauensgrenze (Benutzer, Netz, Dateien, Drittsysteme) nicht blind vertrauen.
- Authentifizierung und Autorisierung nicht „nebenbei“ weglassen, wenn das Feature sie erfordert.
- Öffentliche Schnittstellen und Debug-Endpunkte nicht unbeabsichtigt exponieren.

### Abhängigkeiten und Werkzeuge

- Neue Abhängigkeiten nur mit begründetem Nutzen und kurzer Risikoabschätzung.
- Keine undokumentierten oder unbekannten Paketquellen.
- Keine erfundenen Bibliotheken, Tools oder Sicherheitsfeatures.
- Sicherheitsrelevante Updates und bekannte kritische Schwachstellen im bearbeiteten Bereich nicht ignorieren; Status ehrlich benennen.

### Änderungen und Reviews

- Sicherheitsrelevante Änderungen klein, nachvollziehbar und reviewfähig halten.
- Sicherheitsprobleme haben hohe Priorität (siehe `05_AI_BEHAVIOR.md`).
- Bestehende Schutzmaßnahmen (Validierung, Rechteprüfung, Verschlüsselung an Ort und Stelle) nicht ohne Ersatz entfernen.

### Logging und Diagnostik

- Keine Passwörter, Tokens, Session-IDs oder personenbezogene Rohdaten ungeschützt loggen.
- Fehlermeldungen nach außen keine internen Details leaken, die Angriffe erleichtern.

### Releases

- Release-Stände ohne bekannte, ungeklärte kritische Sicherheitsblocker (siehe `09_RELEASE_PROCESS.md`).
- Sicherheitspatches dürfen beschleunigt werden, Dokumentation wird nachgezogen.

---

## Empfehlungen

- Sensible Operationen hinter explizite Bestätigung oder zusätzliche Prüfungen legen, wenn das Projekt das vorsieht.
- Geheimnisse regelmäßig rotieren, besonders nach Mitarbeitendenwechsel oder Leak-Verdacht.
- Sicherheitsrelevante Entscheidungen kurz im Changelog oder in der Architektur dokumentieren.
- Stack-spezifische Maßnahmen (Header, ORM-Schutz, Mobile-Keystore, …) im jeweiligen Profile vertiefen — nicht den Core aufblähen.

---

## KI-Verhalten

Die KI muss:

1. Sicherheitsrisiken in Vorschlägen aktiv benennen.
2. Keine Sicherheitszusagen ohne Beleg machen.
3. Keine Backdoors, versteckten Fernzugriffe oder absichtliche Schwachstellen einbauen.
4. Keine Anleitungen liefern, die eindeutig der Schädigung fremder Systeme dienen; defensive Absicherung und Fixen eigener Systeme bleiben erlaubt.
5. Bei unklarer Bedrohungslage nachfragen statt zu raten.
6. Secrets, die sie im Kontext sieht, nicht wiederholen oder in neue Dateien kopieren.

---

## Checkliste

### Vor einer sicherheitsrelevanten Änderung

- [ ] Vertrauensgrenze und betroffene Daten klar
- [ ] Bestehende Schutzmaßnahmen verstanden
- [ ] Keine Secrets in Diff oder Docs
- [ ] Rechte/Validierung nicht abgeschwächt ohne Ersatz

### Vor Abschluss / Release

- [ ] Bekannte kritischen Risiken dokumentiert oder behoben
- [ ] Logs und Fehlermeldungen geprüft
- [ ] Neue Abhängigkeiten begründet
- [ ] Keine unbelegten Sicherheitsclaims

---

## Beispiele

### Gut

Token aus Umgebungsvariable lesen; in der Doku nur den Variablennamen nennen.

### Schlecht

API-Key in Quellcode oder Beispiel-`.env` mit echtem Wert committen.

### Gut

„Auth-Bypass-Risiko in diesem Handler; Fix vorschlagen und testen.“

### Schlecht

„Die API ist jetzt sicher.“ — ohne Prüfung und ohne konkrete Maßnahmen.

---

## Ausnahmen

- Temporäre Debug-Hilfen mit abgeschwächtem Schutz nur in nicht-produktiven Umgebungen, zeitlich begrenzt und dokumentiert.
- Organisatorische Security-Baselines können strengere Regeln setzen.

Bequemlichkeit, Demo-Druck oder fehlende Testumgebung sind keine Ausnahmen für Secrets in der Historie oder produktive Schutzlosigkeit.

---

## Version

Dokumentversion: 1.0.0

Änderung in dieser Version:

- Querverweis auf Charter-Matrix (Sprint 4 Konsistenz)

Verwandte Dokumente:

- `00_PROJECT_CHARTER.md`
- `05_AI_BEHAVIOR.md`
- `06_GIT_WORKFLOW.md`
- `07_DOCUMENTATION.md`
- `09_RELEASE_PROCESS.md`
- `11_VERSION.md`
