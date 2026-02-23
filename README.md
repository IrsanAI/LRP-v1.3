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

1. **Messbare Qualitätssicherung (Status: offen)**
   Es gibt bereits strategische Zielbilder für Regression, Snapshots und CI-Qualitätsgates, aber noch keine umgesetzte Test-Suite mit Referenz-Prompts im Repo.
   **Weiterführung:** Als nächsten Schritt einen Referenzkorpus (mind. 20 Prompts) anlegen, erwartete LRP-Outputs als Snapshots versionieren und diese Prüfungen per GitHub Actions automatisch laufen lassen.

2. **Explainability der Analyse im LRP-Core (Status: offen)**
   Die Dokumentation beschreibt klar den Bedarf für einen nachvollziehbaren „Decision Trace“, im UI selbst ist diese Transparenz aktuell jedoch noch nicht implementiert.
   **Weiterführung:** In `index.html` zunächst einen kompakten Explainability-Block ergänzen (gewichtete Trigger + Top-Faktoren), danach mit den Regression-Samples validieren.

3. **Architektur-Entkopplung des monolithischen Core (Status: offen)**
   Der LRP-Core liegt weiterhin als Single-File (`index.html`) vor; die Modularisierung ist als mittelfristige Roadmap definiert, aber noch nicht umgesetzt.
   **Weiterführung:** Schrittweise Split-Strategie ohne Verhaltensbruch: zuerst Analyse-Logik auslagern (`analysis.js`), dann Template-Layer (`protocol-template.js`), zuletzt UI/Styles trennen.

4. **Governance-Paket für professionellen Betrieb (Status: offen)**
   `SECURITY.md`, `CODEOWNERS` sowie Issue-/PR-Templates sind in den Strategie-Dokumenten vorgesehen, im aktuellen Repo aber noch nicht vorhanden.
   **Weiterführung:** Minimalpaket in einem eigenen Governance-PR einführen, damit externe Beiträge, Sicherheitsmeldungen und Verantwortlichkeiten klar standardisiert sind.

5. **Migration auf Ziel-Repository finalisieren (Status: teilweise offen)**
   Das Ziel-Repo `IrsanAI/LRP-v1.3` ist in README und Migrationsdoku bereits verankert; gleichzeitig existieren im Core noch Legacy-Links auf `pythonlover2023/IrsanAI-LRP`.
   **Weiterführung:** Nach dem Umzug alle verbleibenden Legacy-Links (insb. in `index.html`) auf `IrsanAI/LRP-v1.3` umstellen, GitHub Pages im Zielrepo final aktivieren und das alte Repo anschließend als „closed/archived“ kennzeichnen.

### Bereits erledigt (aktuell bestätigt)
- ✅ Dokumentationsfundament inkl. Überblick, Features, Usage, Changelog und Gap-Analyse ist vorhanden.
- ✅ Professionalisierungs-Roadmap und Migrationsleitfaden sind dokumentiert.
- ✅ Mehrsprachige Landingpage (8 Sprachen) ist vorhanden.
- ✅ GitHub-Pages-Workflow für statische Auslieferung ist eingerichtet.
