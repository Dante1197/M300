# Kompetenz E1 – Kontrolle und Test der Cloud-Lösung

### Beschreibung der Kompetenz

Die entwickelte Lösung wird systematisch kontrolliert, getestet und bei Bedarf verbessert. Dabei werden Funktionstests, Fehleranalysen und Leistungsüberprüfungen durchgeführt, um sicherzustellen, dass die Lösung den Anforderungen entspricht.

--- 

## Umsetzung in meinem Projekt

Funktionstests der Lösung
- Der entwickelte Workflow in n8n (Projekt: Netspark) wurde nach jedem Schritt getestet.
- Funktionen wie:
  - Formularinput via webhook
  - GPT-Auswertung des Leads
  - Conditional Logik (qualifiziert / nicht qualifiziert)
  - Logging in Google Sheets

wurden einzeln und im Gesamtkontext überprüft.

## Testszenarien

Ich habe die Lösung mit folgenden Testeingaben überprüft:

- Workflow mehrere male getestet verschiedene probleme behoben 
- Nicht-qualifizierter Lead überprüft ob es richtig ist
- Ungültige Eingabe leeres Feld / kein Text Fehler-Handling

## Monitoring

Um sicherzustellen, dass der Dienst dauerhaft erreichbar ist, habe ich:
- **UptimeRobot** eingerichtet zur Überwachung des n8n-Endpoints.
- Alerts konfiguriert, damit ich bei Ausfällen benachrichtigt werde.

--- 

### Eingesetzte Technologien

- n8n (on Docker) für das eigentliche Automations-Framework
- UptimeRobot für Überwachung der Erreichbarkeit (Monitoring)
- Google Sheets als Logging-Komponente
- Growman IG Extractor 

---

### Nachweis

- Screenshot UptimeRobot Dashboard – folgt
- Workflow-Diagramm in [here](/Workflows/readme.md)
