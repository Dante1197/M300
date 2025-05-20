# Kompetenz C1 – Konfiguration und Monitoring

### Beschreibung der Kompetenz

Die Kompetenz beinhaltet die Einrichtung und Anpassung von Systemdiensten sowie das Einrichten von Monitoringlösungen. Ziel ist es, Systeme stabil zu betreiben, Zustände sichtbar zu machen und nötige Änderungen kontrolliert vorzunehmen.

### Umsetzung in meinem Projekt

### Konfiguration
	•	Die Containerisierung mit Docker erlaubt es, n8n einfach und reproduzierbar zu starten.
	•	Der NGINX-Container wird so konfiguriert, dass er Anfragen per HTTPS (SSL-Zertifikat via Let’s Encrypt) an n8n weiterleitet.
	•	Es wird ein Docker-Compose-Setup erstellt, das sowohl n8n als auch NGINX orchestrationstechnisch verbindet.
	•	Planung: Konfiguration wird versioniert über GitHub gepflegt.

### Monitoring
	•	Für die erste Ausbaustufe wurde UptimeRobot gewählt:
	•	Externes Monitoring über HTTP/HTTPS
	•	Kostenlos, einfach einzurichten
	•	Zeigt direkt die Erreichbarkeit des n8n-Endpoints
	•	Weitere mögliche Monitoring-Tools (z. B. Prometheus, Grafana) wurden geprüft, aber vorerst zurückgestellt.

### Änderungsmanagement (geplant)
	•	Änderungen an der docker-compose.yml, NGINX-Konfiguration oder n8n-Einstellungen werden dokumentiert.
	•	Ziel: Nachvollziehbare Konfigurationshistorie im GitHub-Repo.
	•	Notwendige Anpassungen (z. B. an API-Keys, Ports, Ressourcen) werden über .env-Dateien verwaltet.

### Eingesetzte Technologien
	•	Docker + Docker Compose
	•	NGINX (für Routing & SSL)
	•	UptimeRobot (Monitoring)

