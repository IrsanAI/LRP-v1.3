# Professionalization Roadmap (Soll-Zustand)

## Zielbild
IrsanAI-LRP entwickelt sich von einer starken Single-File-App zu einem professionell wartbaren Produktstandard mit klaren Releases, reproduzierbarer Qualität und hochwertiger Außenwirkung.

## Phase 1 — Stabilität & Nachvollziehbarkeit (kurzfristig)
1. **Analyse-Trace einführen**
   - Bei der Intent-Analyse ein transparentes „Warum“ ausgeben (gewichtete Faktoren).
2. **Regressions-Samples aufbauen**
   - 20–50 Referenz-Prompts (SaaS, Data, Coding, Visual, Gaming, Mixed).
3. **Output-Snapshots versionieren**
   - Für jede Protokollversion stabile Vergleichsausgaben.
4. **Qualitäts-Gates per CI**
   - Markdown-Lint, Link-Checks, Basis-Validierung für statische Dateien.

## Phase 2 — Architektur & Wartbarkeit (mittelfristig)
1. **Code modularisieren**
   - Trennung in UI, Analyse, Protokoll-Template und Utilities.
2. **Template-Layer einziehen**
   - Prompt-/Protokollblöcke als klar versionierte Template-Dateien.
3. **i18n vorbereiten**
   - Zentraler Sprachkatalog für DE/EN.
4. **Konfigurierbare Heuristik-Profile**
   - Domain-Profile (Business, Engineering, Research, Creative).

## Phase 3 — Produktreife (strategisch)
1. **Release-Management**
   - SemVer, Release Notes, Migrationshinweise pro Version.
2. **Professional GitHub Pages Experience**
   - Landingpage mit klarer User Journey: Discover → Try → Deep Dive.
3. **Erweiterte Exporte**
   - JSON/Markdown/Prompt-Pack für Team-Workflows.
4. **Governance & Security**
   - Security Policy, Issue-/PR-Templates, Maintainer-Playbook.

## Erfolgskriterien (messbar)
- Reproduzierbare Analyse bei Referenz-Prompts (>= 90% konsistente Pfadentscheidung).
- Sinkende Änderungsrisiken durch modulare Architektur.
- Höhere Onboarding-Rate über professionellen Pages-Auftritt.
- Kürzere Time-to-Value für neue Nutzer:innen.
