# 🧠 Lernjournal – Woche 20 (13.05.2025)

### Tagesziele
- Überblick über Modul 300 und Bewertungskriterien verschaffen
- Brainstorming für ein geeignetes Projekt
- Entscheidung treffen für ein Projekt, das V2-Kriterien erfüllt
- Projektziel und Technologie-Stack definieren

### Tagesresultate
- Entscheidung: Aufbau einer Cloud-basierten Automatisierungsplattform mit n8n
- Ziel: Plannung & Definition abzuschliessen 
- Technologie-Stack: Docker, NGINX, GitHub, evtl. Let's Encrypt, UptimeRobot/Prometheus
- Projektziel: Automationen (z. B. KI-gesteuerte Workflows) umsetzen und über Git versionieren
- Erste Strukturidee für IPERKA mit Clickup erarbeitet und Projektziele formuliert

### Aufgetretene Probleme & Reflexion
- Schwierigkeit bei der Einschätzung, ob n8n als "Cloud-Technologie" gilt
- Erkenntnis: Fokus auf *saubere technische Umsetzung*, *GitHub-Kompetenz* und *Dokumentation* bringt mehr Punkte als übertriebene Komplexität

### Eingesetzte Ressourcen
- Unterrichtsunterlagen zu Modul 300 (V1 vs. V2)
- Eigene Recherche zu n8n:
  - [n8n.io](https://n8n.io/)
  - [n8n Docker Docs](https://hub.docker.com/r/n8nio/n8n)
- ChatGPT zur Strukturplanung

### Praktische Übung
- der Fokus lag auf Planung & Definition des Projektes
- Clickup Task wurden erstellt -> Besser Task übersicht (meiner meinung) 
- Lokale Dev umgebung mit Docker wurde aufgesetzt

Natürlich! Hier ist dein Lernjournal-Eintrag für heute (20. Mai 2025) im sauberen Markdown-Format für GitHub:

--- 

# 🧠 Lernjournal – Woche 21 (20.05.2025)

### Tagesziele
- Formatierung und Strukturierung der Dokumentation für GitHub
- Erstellung der Kompetenznachweise ab Buchstabe B (Kompetenzmatrix)
- Detaillierte Ausarbeitung der Kompetenzen B1, C1, D1 nach dem A1-Beispiel
- Theoretische Fertigstellung des Dokumentationskonzepts vor praktischer Umsetzung

### Erreichte Tagesresultate
- Kompetenznachweise erstellt für:
- [A1 – Service Erhebung](dokumentation/A1_service_erhebung.md)
- [B1 – Planung der Umgebung](dokumentation/B1_entwicklung_eines_integrationskonzepts.md)
- [C1 – Monitoring und Logging](dokumentation/C1_konfiguration_und_monitoring.md) (UptimeRobot)
- [D1 – Netzwerkverbindungen](dokumentation/D1_aufbau_von_netzwerkverbindungen.md) (NGINX Reverse Proxy, Docker-Netzwerk, Elastic IP)
- Sicherheitskonzept konkretisiert (Zugriffsmanagement, Firewall, HTTPS)
- Projektumsetzung weiter vorbereitet (IPERKA finalisiert, klare Zielsetzung)

### Aufgetretene Probleme
- Schwierigkeit, CI/CD sinnvoll in das Projekt zu integrieren → bewusste Entscheidung, es nicht einzubauen
- Herausforderung, Monitoring-Lösung sinnvoll umzusetzen → Entscheidung für UptimeRobot als einfaches, externes Tool mit klarem Nutzen

### Eingesetzte Ressourcen
- Austausch mit ChatGPT zur Kompetenzstrukturierung und Formatierung
- Recherche auf:
- [UptimeRobot.com](Uptimerobot.com)  
- [NGINX Reverse Proxy Guide](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)

### Praktisch angewandtes Wissen
- Strukturierung von Projekt-Kompetenznachweisen für GitHub
- Sicherheitstechnisches Denken im Netzwerkbereich (Firewall, Zugriff, Reverse Proxy)

---

# 🧠Lernjournal – Woche 22 (27.05.2025)

### Tagesziele
- Zugang zum AWS Learner Lab erhalten und aktivieren
- n8n AI-Workflow finalisieren und funktional zum Laufen bringen

### Erreichte Tagesresultate
- Zugang zum AWS Learner Lab erfolgreich eingerichtet
- AI-basierter Workflow mit n8n ist voll funktionsfähig:
- KI-Entscheidungslogik zur Qualifikation von Leads funktioniert

### Aufgetretene Probleme
- Initiale Schwierigkeiten beim Zugang zum AWS Learner Lab (keine TBZ mail) → mehrmals probiert, schlussendlich mit Erfolg
- n8n hatte kleinere Probleme bei der Anbindung von Google Sheet API integration → gelöst durch richitge Konfiguration

### Eingesetzte Ressourcen
- AWS Learner Lab Zugang
- n8n Dokumentation: https://docs.n8n.io
- Diese [Youtube Video](https://www.youtube.com/watch?v=pWGXlZBGu4k&ab_channel=AustinReed%7CHorizonDev)
- Austausch mit ChatGPT zur Fehlerbehebung

### Praktisch angewandtes Wissen
- Konfiguration von Cloud-Workflows mit n8n
- Nutzung des AWS Learner Lab zur Entwicklung einer produktionsähnlichen Umgebung
- Verständnis über funktionale Workflow-Ketten und Triggerlogik vertieft

---

Natürlich! Hier ist dein Lernjournal-Eintrag für heute (02.06.2025) im richtigen Format für deine lernjournal.md:

---

# 🧠 Lernjournal – Woche 23 (03.06.2025)

### Geplante Tagesziele
- An der praktischen Umsetzung des Projekts beginnen
- Weitere Entwicklung und Tests des Tools Netspark auf einer lokalen Testumgebung
- Vorbereitung auf die Migration zur AWS EC2-Instanz

---

### Erreichte Tagesresultate
- Netspark lokal erfolgreich weiterentwickelt und getestet
- Grundfunktionen wie Form-Eingabe, KI-Verarbeitung und E-Mail-Benachrichtigung sind funktional
- Vorbereitung auf die Übertragung der lokalen Umgebung zur AWS-Cloud wurde begonnen (Installationstests, Reverse Proxy, etc.)

---

### Aufgetretene Probleme und Reflexion
- Teilweise Probleme mit lokalen Ports und Umgebungsvariablen beim Starten des lokalen Servers
- Fehlerhafte Rückgabe vom KI-Modul bei ungültiger Formateingabe → durch Validierungs-Node gelöst
- Es war hilfreich, die lokale Umgebung vollständig durchzutesten, bevor die AWS-Migration erfolgt

**Reflexion:**
Der heutige Tag hat gezeigt, wie wichtig eine solide lokale Testumgebung ist. Probleme lassen sich so isolieren und schneller lösen, ohne ständig auf die Cloud-Infrastruktur angewiesen zu sein. Für die Migration ist das Setup nun gut vorbereitet.

---

### Eingesetzte Ressourcen
- Eigene lokale Docker-Testumgebung mit n8n
- OpenAI API-Dokumentation
- Eigene Notizen zu Netspark

---

### Praktische Anwendung
- Netspark-Workflow lokal weiterentwickelt, Workflow auteilung hat stattgefunden
- Erfolgreiches Testen mehrerer Szenarien für Lead-Qualifikation
- Vorbereitung der Struktur und Docker-Konfiguration für den kommenden EC2-Transfer
