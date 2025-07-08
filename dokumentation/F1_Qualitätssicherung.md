# F1 – Qualitätssicherung durchführen

### 🧩 Kompetenzbeschreibung

Ich kann die Qualität meiner Arbeit sicherstellen, indem ich systematisch überprüfe, ob das Ergebnis den Anforderungen entspricht. Dazu nutze ich geeignete Werkzeuge zur Kontrolle, Dokumentation und Korrektur.

--- 

### Umsetzung im Projekt

Im Verlauf meines Projekts „Netspark“ habe ich mehrfach Qualitätssicherungsmaßnahmen durchgeführt, um sicherzustellen, dass mein Workflow stabil, sicher und nachvollziehbar funktioniert. Dazu gehörten:

- Testläufe in lokaler Entwicklungsumgebung: Der n8n-Workflow wurde auf einer lokalen Instanz ausgeführt und mit verschiedenen Testfällen validiert.
- Kontrollausgaben: Alle Zwischenschritte wie KI-Entscheidungslogik, Fehlerbehandlung und Dateiausgabe in Excel wurden getestet.
- Fehlerbehebung: Entdeckte Fehler (z. B. fehlende Einträge, falsche E-Mail-Adressen, KI-Filterung zu streng/zu lasch) wurden systematisch behoben.
- Funktionstest nach Deployment: Auch nach dem Deployment auf AWS mit HTTPS und OAuth wurden nochmals alle Funktionen getestet.
- Promptanalyse: Ich habe eine eigene Markdown-Datei erstellt, in der ich die verwendeten KI-Prompts dokumentiert, evaluiert und optimiert habe.

--- 

### Eingesetzte Technologien & Werkzeuge
- n8n (zur Prozessautomatisierung & Testausführung)
- VS Code / GitHub (für Codequalität, Versionskontrolle, Readme-Review)
- Markdown (zur Dokumentation und Promptanalyse)
- Excel (zur Prüfung der automatisch generierten Bewerberlisten)
- Posteingangstest & Mail-Debugging (zur Validierung der E-Mail-Vorlagen)

--- 

### Nachweise
- prompt-analyse.md (Dokumentation und Evaluation der LLM-Eingaben)
- Screenshot der Excel-Ausgabe
- Funktionierender Workflow auf https://netspark.duckdns.org
