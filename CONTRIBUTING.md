# Contributing to IrsanAI-LRP v1.3

Danke für dein Interesse am Projekt.

## Leitlinien
- Halte Änderungen klein, nachvollziehbar und thematisch klar.
- Schreibe sprechende Commit-Messages.
- Ergänze oder aktualisiere Dokumentation bei Funktionsänderungen.
- Verändere den LRP-Protokollkern in `index.html` nur mit klarer Begründung und Testfall.

## Setup
```bash
git clone <repo-url>
cd IrsanAI-LRP-v1.3
python3 -m http.server 4173
```

## Qualitätschecks (minimal)
- HTML-Datei auf Syntaxfehler prüfen (visuell im Browser)
- Links in Markdown dokumentieren und aktualisieren
- Änderungen gegen reale Nutzungsbeispiele testen

## Pull-Request-Empfehlung
- Kontext: Welches Problem wird gelöst?
- Änderung: Was wurde konkret umgesetzt?
- Wirkung: Warum ist es besser?
- Risiko: Was könnte brechen?
- Test: Welche Schritte wurden ausgeführt?
