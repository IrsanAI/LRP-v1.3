# Projektüberblick

## Kurzbeschreibung
IrsanAI-LRP v1.3 ist eine browserbasierte Single-File-Anwendung (`index.html`) zur Erzeugung strukturierter LRP-Protokolle für große Sprachmodelle (LLMs).

## Kernidee
Statt nur einen Prompt zusammenzuklicken, führt das Tool einen Meta-Prozess aus:
1. Analyse des Nutzer-Intents
2. Ableitung eines geeigneten Ausführungswegs
3. Generierung eines formal strukturierten Protokolls
4. Ausgabe mit Fallback- und Kompatibilitäts-Hinweisen

## Zielgruppen
- Prompt Engineers
- Produktteams in Discovery-/MVP-Phasen
- Entwickler:innen für AI-gestützte Anwendungen
- Solo-Founder mit hohem Iterationsdruck

## Architektur (Ist-Stand)
- **Frontend/UI:** HTML + CSS + Vanilla JavaScript
- **Runtime:** vollständig client-seitig
- **Deployment:** statisch (GitHub Pages, lokaler Browser)
- **Persistenz:** keine serverseitige Speicherung

## Zukunftsbild
- Dokumentierte Release-Pipeline
- Versionierte Prompt-Schemas
- Bessere Internationalisierung
- Striktere Trennung von UI, Logik und Protokoll-Templates
