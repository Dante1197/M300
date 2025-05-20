# Kompetenz B1 – Entwicklung eines Integrationskonzepts

### Beschreibung der Kompetenz

Die Kompetenz umfasst die Planung und Erstellung eines Konzepts zur Integration von Services, Tools und Systemkomponenten. Ziel ist es, ein konsistentes, funktionierendes Gesamtsystem mit durchdachter Struktur zu entwerfen.

### Umsetzung in meinem Projekt

Anforderungsanalyse
	•	Ziel: n8n soll in der Cloud laufen und extern erreichbar sein.
	•	Der Dienst muss sicher und stabil laufen – auch bei längerer Uptime.
	•	Die Automatisierung soll auch AI-Funktionalität beinhalten (z. B. durch gebrauch von der Gemini-API)
	•	NGINX dient als Reverse Proxy zur externen Erreichbarkeit und SSL-Terminierung.

### Auswahl der Werkzeuge

Komponente =	Rolle im System
Docker = 	Containerisierung von n8n
NGINX =		Reverse Proxy + HTTPS
AWS EC2 =	Infrastrukturhost
n8n = 		Automatisierungsplattform

### Testplanung (geplant)
	•	Zugriff von extern auf n8n über HTTPS testen
	•	Testen der Workflows mit Beispiel-Automationen
	•	Neustart/Fehlertoleranz simulieren (Container-Resilienz)
	•	Später: Uptime-Monitoring über UptimeRobot

### Eingesetzte Technologien
	•	Docker
	•	NGINX
	•	AWS EC2
	•	n8n

### Nachweise
	•	Projektübersicht: IPERKA.md
	•	Architektur-Skizze geplant
