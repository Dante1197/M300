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

---

# 🧠 Lernjournal – Dienstag, 10.06.2025

### Geplante Tagesziele
- Entwicklung einer verbesserten, intelligenteren Version von Netspark v2
- Implementierung eines Item-Loops zur Verarbeitung mehrerer Leads
- Integration eines leistungsfähigeren LLM (openai-o4-latest)
- Fehlerfreie Strukturierung und Optimierung des bestehenden n8n-Workflows

--- 

### Erreichte Tagesresultate

Loop-Funktion zur Verarbeitung von Leads
- Die neue Version verwendet eine Loop Over Items Node, um automatisch über mehrere Zeilen aus dem Google Sheet zu iterieren (Unqualified Leads).
- Jeder Datensatz wird einzeln verarbeitet, wodurch Skalierbarkeit und Fehlertoleranz massiv verbessert wurden.

### Technische Optimierungen
- Die Architektur erlaubt zukünftig:
- Den Austausch des LLMs (z. B. GPT-4o, Claude 3 etc.)
- Integration externer API-Checks (z. B. Scoring, Standortvalidierung)
- Live-Monitoring des Flows via Trigger und Webhooks

---

### Reflexion & Learnings
- Durch das Einfügen der Loop-Logik konnte die LLM-Nutzung deutlich effizienter gestaltet werden – keine Massenauswertung, sondern intelligente Einzelverarbeitung.
- Die Modularisierung erleichtert die Wartung und spätere Migration auf Cloud-Umgebungen wie AWS.
- Der KI-Agent agiert nicht mehr als Filter auf ein gesamtes Dataset, sondern reagiert kontextuell auf jeden einzelnen Eintrag – das erhöht die Genauigkeit der Qualifikation drastisch.

--- 

### Tools & Technologien
- n8n.io (Workflow-Automatisierung)
- OpenAI Chat Model
- Google Sheets & Drive API
- Custom Code Nodes (JavaScript) für Parsing, Formatierung und Evaluation
- Lokale n8n-Testumgebung, vorbereitet auf spätere AWS-Migration



# 🧠 Lernjournal – Dienstag, 17.06.2025

### Geplante Tagesziele
- Praktische Umsetzung: Vollständige Bereitstellung von n8n mit Netspark draufgespitzt auf einer AWS EC2 Instanz
- Konfiguration von HTTPS-Zugriff mit DuckDNS und Let’s Encrypt
- Fehlerbehebung bei Google OAuth Redirect URI
- Integration eines Monitoringsystems (UptimeRobot)

---

### Erreichte Tagesresultate

**EC2 Setup & n8n Deployment**
- Ubuntu 20.04 Instanz via AWS EC2 gestartet
- Sicherheitsgruppen für Ports 22, 80, 443 korrekt eingerichtet
- Verbindung über SSH (Schlüsselberechtigung mittels chmod 400 korrigiert)
- Docker installiert und n8n mit Umgebungsvariablen (inkl. Basic Auth) im Container gestartet

**Docker-Konfiguration**
- n8n Container mit persistentem Volume (~/.n8n) eingerichtet
- Secure Cookies deaktiviert zur Fehlerbehebung in Safari
- Portkonflikt gelöst durch Stoppen und Entfernen des alten Containers

**HTTPS via DuckDNS & NGINX**
- DuckDNS-Domain https://netspark.duckdns.org registriert und konfiguriert
- Reverse Proxy mit NGINX eingerichtet
- Zertifikat von Let’s Encrypt erfolgreich via Certbot eingerichtet
- HTTPS-Zugriff funktionierte danach stabil

**Google OAuth Problem gelöst**
- Fehler redirect_uri_mismatch bei Google Sheets OAuth
- Lösung: Redirect URI in Google OAuth Console angepasst auf:
https://netspark.duckdns.org/rest/oauth2-credential/callback
- Docker-Container neu gestartet mit korrekten Umgebungsvariablen:
WEBHOOK_URL und VUE_APP_URL_BASE_API → öffentliche Domain statt localhost

**Monitoring mit UptimeRobot**
- Öffentliche URL (https://netspark.duckdns.org) bei UptimeRobot hinzugefügt
- Funktionierende Verfügbarkeitserkennung bestätigt

--- 

### Reflexion & Probleme
- Die HTTPS-Einrichtung und das OAuth Redirect URI Debugging erforderten präzises Arbeiten und gutes Verständnis von Cloud, Reverse Proxy und Auth-Mechanismen
- Trotz Komplexität der Konfiguration konnte der gesamte Stack erfolgreich produktionsreif aufgebaut werden
- Erkenntnis: Verständnis für Domains, Proxies und OAuth ist kritisch für skalierbare Webanwendungen

--- 

### Eingesetzte Ressourcen
- n8n Documentation
- DuckDNS
- Certbot Anleitung Ubuntu + NGINX
- Google Cloud OAuth Credentials Portal
- Eigene EC2-Instanz (AWS)
- UptimeRobot

--- 

### Praktische Anwendung
- Erfolgreiche Implementierung eines vollständigen Cloud-Deployments von Netspark:
- Zugriff über HTTPS
- Reverse Proxy mit NGINX
- Authentifizierung via Google OAuth 2.0
- Monitoring über externen Service


---

# 🧠 Lernjournal – Dienstag, 24.06.2025

### Geplante Tagesziele
- Ausführliche Dokumentation des gesamten Systems rund um Netspark
- Erstellung einer technischen Readme für den Workflow
- Analyse und Ablage des eingesetzten Prompts
- Strukturierung und Optimierung des GitHub-Repositories

---

###Erreichte Tagesresultate

#### Installationsdokumentation
- Vollständige Markdown-Dokumentation erstellt mit allen Konfigurationsschritten:
- AWS EC2 Deployment
- Docker Setup
- NGINX Reverse Proxy
- HTTPS via DuckDNS & Let’s Encrypt
- Google OAuth Redirect URI Fix


#### README.md für Netspark-Workflow
- Strukturierte Readme im Verzeichnis /workflows erstellt
- Aufbau, Zweck und Ablauf jedes Workflow-Elements detailliert erklärt
- Besonderes Augenmerk auf:
- Loop-Mechanik
- KI-Analyse durch GPT
- Sheet-Integration für qualifizierte Leads

#### Prompt hochgeladen & analysiert
- Verwendeter Prompt als .md-Datei gespeichert und dokumentiert
- Analytische Reflexion geschrieben: Stärken, Schwächen, Wirkung
- Ziel: Transparenz über die Logik der KI-Entscheidung und Optimierungspotenzial

#### GitHub Repository verbessert
- Verzeichnisstruktur aufgeräumt und logisch gegliedert
- Irrelevante Dateien entfernt, Readmes hinzugefügt

---

### Reflexion & Probleme
- Strukturierung und Dokumentation haben viel Zeit gekostet, sind aber essenziell für die Wartbarkeit des Projekts
- Die Analyse des Prompts zeigte, wie sensibel GPT auf Formulierungen reagiert – kleine Anpassungen ändern die gesamte Entscheidungslogik
- Stolz auf das Resultat: ein durchdachtes, öffentlich verständliches Projekt-Repository mit klarer Dokumentation

--- 

### Eingesetzte Ressourcen
- Eigenes GitHub Repository (private)
- Vorwissen aus OAuth-, Docker- und NGINX-Konfiguration

--- 

### Praktische Anwendung
- nur mein Github und die nachkontrolle in AWS & n8n 



