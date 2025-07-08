# IPERKA – n8n Cloud Automatisierungsprojekt mit Docker und NGINX

## I – Informieren

### Ausgangslage:

Ich möchte ein Automatisierungsprojekt realisieren, bei dem ich n8n in einem Docker-Container auf einer EC2-Instanz deploye. Der Container wird über NGINX als Reverse Proxy öffentlich erreichbar gemacht. Ziel ist es, eine oder mehrere Automationen zu erstellen, die über eine Web-UI steuerbar sind. Dabei wird n8n als neue Technologie verwendet.

### Ziel:

	•	n8n verstehen und produktiv einsetzen
	•	Projekt mit Docker und NGINX realisieren
	•	GitHub als Versionskontrolle korrekt nutzen
	•	Monitoring/Logging über UptimeRobot planen

---

## P – Planen

	•	Projektidee festlegen
	•	AWS-Umgebung vorbereiten (EC2-Instanz mit Ubuntu)
	•	Docker-Setup vorbereiten
	•	NGINX Reverse Proxy konfigurieren
	•	n8n Docker-Container bereitstellen
	•	Beispielworkflow mit API-Aufruf oder KI-Anbindung umsetzen
	•	GitHub-Repository strukturieren
	•	Lernjournal wöchentlich führen
	•	Kompetenzen in separaten .md-Dateien dokumentieren
	•	UptimeRobot für Monitoring einbinden

⸻

## E – Entscheiden

	•	Cloud-Deployment auf AWS EC2 (statt lokal oder hybrid)
	•	Nutzung von Docker und NGINX zur Skalierbarkeit und Trennung der Dienste
	•	n8n als Automatisierungstool, da es Open Source und UI-basiert ist
	•	GitHub Actions als einfaches Einstiegsmittel für DevOps-Prozesse
	•	UptimeRobot als leichter Einstieg ins Monitoring 
 

⸻

## R – Realisieren

	•	EC2-Instanz erstellt und mit SSH verbunden
	•	Docker installiert und n8n Container eingerichtet
	•	NGINX konfiguriert mit SSL über Let’s Encrypt
	•	GitHub-Repo eingerichtet und Projekt versioniert
	•	Beispielworkflow in n8n erstellt (z. B. automatische Begrüßungs-E-Mail bei Formular-Submit)
	•	UptimeRobot eingerichtet, um Verfügbarkeit zu überwachen

⸻

 ## K – Kontrollieren
 
	•	Funktionstest des n8n Workflows erfolgreich
	•	Zugriff über NGINX mit HTTPS gewährleistet
	•	Logs überprüft (Docker Logs und UptimeRobot Reports)
	•	Monitoring funktioniert (Benachrichtigung bei Downtime)

⸻

## A – Auswerten

	•	Projektziele wurden vollständig erreicht
	•	Neue Technologien wie n8n, GitHub Actions und UptimeRobot wurden erfolgreich integriert
	•	Projekt sauber dokumentiert (IPERKA.md, lernjournal.md, Kompetenz-MDs)


