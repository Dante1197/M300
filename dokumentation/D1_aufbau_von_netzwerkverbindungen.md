# Kompetenz D1 – Aufbau von Netzwerkverbindungen

### Beschreibung der Kompetenz

Diese Kompetenz umfasst das Einrichten, Überprüfen und Dokumentieren von Netzwerken und Netzwerkdiensten. Ziel ist es, Systeme sicher und erreichbar über das Netzwerk bereitzustellen und dafür grundlegende Netzwerkkenntnisse praktisch anzuwenden.

### Umsetzung in meinem Projekt

### Zielsetzung
	•	Die Anwendung (n8n) soll öffentlich über das Internet erreichbar sein.
	•	Es muss ein sicherer Zugang über HTTPS gewährleistet werden.
	•	Die Netzwerkverbindung soll performant und stabil laufen, trotz Containerisierung.

### Umsetzungskonzept
	•	EC2-Instanz in AWS wird mit einer statischen Elastic IP ausgestattet.
	•	Ein NGINX-Reverse-Proxy wird eingerichtet, der:
	•	den Port 443 (HTTPS) entgegennimmt
	•	Anfragen intern an den Docker-Container (Port 5678 für n8n) weiterleitet
	•	Konfiguration der Sicherheitsgruppen (Firewall in AWS):
	•	Nur Ports 22 (SSH), 80 (HTTP) und 443 (HTTPS) sind offen
	•	Intern kommunizieren die Container über ein Docker-Netzwerk

## DNS & SSL
	•	In Zukunft geplant: eigene Domain via Route53 (AWS)
	•	Let’s Encrypt SSL-Zertifikat wird automatisch über NGINX-Plugin (z. B. certbot) beantragt und verlängert

## Sicherheitstechnisches Vorgehen
	•	Root-Zugänge per SSH werden auf Schlüsselpaare beschränkt
	•	Netzwerkkommunikation erfolgt ausschließlich verschlüsselt über HTTPS
	•	Fail2Ban und grundlegende Firewallregeln sind vorgesehen

## Eingesetzte Technologien
	•	AWS EC2 mit Elastic IP
	•	NGINX als Reverse Proxy
	•	Docker Netzwerke
	•	AWS Security Groups

## Nachweise
	•	Netzwerksetup geplant in /dokumentation/installations-doku.md
