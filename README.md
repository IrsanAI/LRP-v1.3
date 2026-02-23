# IrsanAI-LRP v1.3 🚀

> **Revolutionäres Meta-Protokoll für robustes Prompt Engineering.**
> Ein client-seitiges System zur strukturierten Generierung hochwertiger LRP-Protokolle für LLM-Workflows in Produkt-, Code- und Strategieprojekten.

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.3-blue.svg)](https://github.com/IrsanAI/LRP-v1.3)

## Warum dieses Projekt?
IrsanAI-LRP v1.3 geht über klassische Prompt-Generatoren hinaus:
- **Intent-Analyse statt reiner Textvorlage**
- **Entscheidungslogik für Ausführungswege** (direkt vs. OS/HW-bewusst)
- **Fallback- und Kompatibilitätsmechaniken** für robuste Nutzung
- **Token-orientierte Strukturierung** für produktive LLM-Sessions
- **Mehrsprachige Landingpage** (EN, DE, BS, ES, TR, IT, FR, ZH) für internationales Onboarding

## Projektstatus
- ✅ Produktiv nutzbar (Single-File HTML App)
- ✅ Dokumentation modernisiert
- ✅ Struktur für professionellen Open-Source-Betrieb vorbereitet
- 🔄 Ziel-Migration: `https://github.com/IrsanAI/LRP-v1.3`

## Start in 30 Sekunden
1. Repository klonen.
2. `index.html` direkt im Browser öffnen **oder** lokal per Webserver starten:
   ```bash
   python3 -m http.server 4173
   ```
3. Im Browser aufrufen: `http://127.0.0.1:4173/index.html`
4. Anfrage eingeben → analysieren → LRP generieren → in dein LLM einsetzen.

## Dokumentation
- [Projektüberblick](docs/overview.md)
- [Features](docs/features.md)
- [Nutzungsleitfaden](docs/usage.md)
- [Änderungsprotokoll](docs/changelog.md)
- [LRP-HTML Audit & Optimierungsvorschläge](docs/lrp-html-audit.md)
- [Erste Live-Erfahrung mit dem Protokoll](docs/first-experience.md)
- [Professional GitHub Pages Landing](website/index.html)
- [Professionalization Roadmap](docs/professionalization-roadmap.md)
- [Migration Guide](MIGRATION.md)
- [Progress-to-Target (Ist/Soll Gap-Analyse)](docs/progress-to-fazit.md)
- [WEG 1/WEG 2 + Probability-Modell für nächste Schritte](docs/weg1-weg2-probability-next-steps.md)
- [Repo Validation Report (Konsistenzcheck)](docs/repo-validation-report.md)

## Repositories & Links
- **Legacy Demo / Legacy Account:**
  - https://pythonlover2023.github.io/IrsanAI-LRP/
  - https://pythonlover2023.github.io/IrsanAI-Landingpage-Logic-Factory/
- **Aktuelles Ziel-Repository:**
  - https://github.com/IrsanAI/LRP-v1.3

## Mitwirken
Beiträge sind willkommen – von UX-Verbesserungen bis zu Protokoll-Forschung.
Siehe: [CONTRIBUTING.md](CONTRIBUTING.md)

## Lizenz
Dieses Projekt steht unter der [MIT License](LICENSE).

## Hinweis für Entwickler (LOP – Liste offener Punkte)

Was aus meiner Sicht noch offen ist (fachlich, nicht technisch blockiert):

_Stand der Prüfung: aktuell gegen den Inhalt dieses Repos validiert._

1. **Messbare Qualitätssicherung (Status: offen)**
   Eine dedizierte Regression-/Snapshot-Test-Suite für Referenz-Prompts ist weiterhin nicht im Repo enthalten (es existieren aktuell keine entsprechenden Testartefakte oder Test-Runner).
   **Weiterführung:** Referenzkorpus (z. B. 20+ repräsentative Prompts) definieren, erwartete LRP-Outputs als Snapshots versionieren und in CI automatisch gegen neue Änderungen prüfen.

2. **Explainability der Analyse im LRP-Core (Status: offen)**
   Die Analyse läuft regelbasiert, aber ein sichtbarer Explainability-/Decision-Trace für Nutzer ist im UI weiterhin nicht vorhanden.
   **Weiterführung:** In `index.html` einen „Warum dieses Ergebnis?“-Block ergänzen (Top-Signale + Gewichtung) und die Darstellung anhand der Referenz-Prompts gegenprüfen.

3. **Architektur-Entkopplung des monolithischen Core (Status: offen)**
   Der Kern ist weiterhin in einer zentralen Datei (`index.html`) gebündelt; die in der Roadmap beschriebene Modultrennung wurde noch nicht begonnen.
   **Weiterführung:** In kleinen Schritten trennen: zuerst Analyse-Logik, dann Protokoll-Template-Generator, danach UI/Styles. Pro Schritt Snapshot-Vergleich, um Verhalten stabil zu halten.

4. **Governance-Paket für professionellen Betrieb (Status: offen)**
   `SECURITY.md`, `CODEOWNERS` und standardisierte Issue-/PR-Templates fehlen weiterhin.
   **Weiterführung:** Governance-Minimum als separaten PR einführen (Security-Policy + Verantwortlichkeiten + Vorlagen), damit externe Beiträge klarer und skalierbarer bearbeitet werden können.

5. **Migration auf Ziel-Repository finalisieren (Status: teilweise offen)**
   Positiv: Das Zielrepo `IrsanAI/LRP-v1.3` ist in README/Migration bereits verankert. Offen: Im Core (`index.html`) sind noch Legacy-Links auf `pythonlover2023/IrsanAI-LRP` enthalten.
   **Weiterführung:** Legacy-Links im Core auf das Zielrepo aktualisieren, Ziel-Pages final verifizieren und das alte Repo anschließend klar als Legacy/Archiv markieren.

### Bereits erledigt (aktuell bestätigt)
- ✅ Dokumentationsfundament inkl. Überblick, Features, Usage, Changelog und Gap-Analyse ist vorhanden.
- ✅ Professionalisierungs-Roadmap und Migrationsleitfaden sind dokumentiert.
- ✅ Mehrsprachige Landingpage (8 Sprachen) ist vorhanden.
- ✅ GitHub-Pages-Workflow für statische Auslieferung ist eingerichtet.

### Kurzfazit
Der aktuelle Fokus sollte auf **P1 Qualitätssicherung** (Regression/Snapshots) liegen, weil damit die Basis für die nächsten Punkte (Explainability, Modularisierung, sichere Migration) belastbar abgesichert wird.
