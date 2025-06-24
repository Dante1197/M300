# Installation & Konfiguration: n8n auf AWS EC2

Projekt: Deployment von NetSpark = n8n mit Docker, HTTPS (Let’s Encrypt), DuckDNS & Google OAuth

Datum: 17. Juni 2025

System: Ubuntu 20.04 (auf AWS EC2)

---

### 1. AWS EC2 Instanz vorbereiten

#### 1.1 EC2 Instanz erstellen
	•	Öffne die AWS Management Console
	•	Wähle EC2 → Instanzen → Launch Instance
	•	AMI: Ubuntu Server 20.04 LTS (HVM), SSD
	•	Instance Type: t2.micro
	•	Key Pair: Neues oder bestehendes Key-Pair (z. B. netspark-ec2.pem)
	•	Sicherheitsgruppen:
	•	TCP 22 (SSH)
	•	TCP 80 (HTTP)
	•	TCP 443 (HTTPS)
	•	Optional: TCP 5679 (nur für Debug-Zugriff auf n8n)

--- 

### 1.2 Elastic IP zuweisen 
	1.	In AWS EC2 → Elastic IPs → Allocate Elastic IP
	2.	Neue IP-Adresse zuweisen
	3.	Unter „Actions“ → Associate Elastic IP
	•	Wähle deine EC2-Instanz aus
	•	Beispiel-IP: 34.192.222.54
	4.	Hinweis: Diese IP ist jetzt dauerhaft mit deiner Instanz verknüpft, auch nach Neustarts.

---

### 1.3 SSH-Zugriff auf die EC2-Instanz

```
chmod 400 ~/Downloads/netspark-ec2.pem
ssh -i "~/Downloads/netspark-ec2.pem" ubuntu@34.192.222.54
```

---

### 2. 🐳 Docker & n8n Installation

#### 2.1 Docker installieren

```
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker
```

---

### 2.2 n8n mit Docker starten

```
docker run -d \
  --name n8n \
  -p 5679:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -e N8N_SECURE_COOKIE=false \
  -e N8N_BASIC_AUTH_ACTIVE=true \
  -e N8N_BASIC_AUTH_USER=admin \
  -e N8N_BASIC_AUTH_PASSWORD=mypassword \
  -e N8N_HOST=netspark.duckdns.org \
  -e N8N_PORT=5678 \
  -e WEBHOOK_URL=https://netspark.duckdns.org \
  -e VUE_APP_URL_BASE_API=https://netspark.duckdns.org \
  n8nio/n8n
```

--- 

### 3. 🌍 DuckDNS Domain einrichten
	1.	Gehe zu https://duckdns.org
	2.	Melde dich an (GitHub o. Ä.)
	3.	Registriere Subdomain z. B. netspark.duckdns.org
	4.	Trage deine Elastic IP (34.192.222.54) im DuckDNS-Dashboard ein

--- 

### 4. NGINX & HTTPS (Let’s Encrypt)

#### 4.1 NGINX installieren

```
sudo apt install nginx -y
```

#### 4.2 NGINX konfigurieren

**Datei: /etc/nginx/sites-available/netspark**

```
server {
    listen 80;
    server_name netspark.duckdns.org;

    location / {
        proxy_pass http://localhost:5679;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

```
sudo ln -s /etc/nginx/sites-available/netspark /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

--- 

### 4.3 TLS mit Let’s Encrypt (Certbot)

```
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d netspark.duckdns.org
```

**Automatische Erneuerung testen:**

```
sudo certbot renew --dry-run
```

--- 

### 5. Google OAuth2 Integration

#### 5.1 OAuth2 in Google Console
	•	Gehe zu: Google Cloud Console
	•	OAuth-Projekt erstellen
	•	OAuth-Client-Typ: „Webanwendung“
	•	Redirect URI:

**https://netspark.duckdns.org/rest/oauth2-credential/callback**

	•	In n8n unter Credentials eintragen:
	•	Client ID
	•	Client Secret
	•	Redirect URI: exakt wie oben

--- 

### 6. UptimeRobot Monitoring
	•	Account erstellen: https://uptimerobot.com
	•	Monitor-Typ: HTTPS
	•	URL: https://netspark.duckdns.org
	•	Checkintervall: z. B. alle 5 Minuten
	•	Optional: Telegram/E-Mail Benachrichtigung

--- 

### 7. Neustart, Fehlerbehandlung & Wiederanlauf

#### 7.1 Container neu starten

```
docker stop n8n
docker start n8n
```

#### 7.2 Bei Container-Konflikten:

```
docker rm n8n
# dann wieder: docker run ...
```



**✅ Abschluss**

Bereich	Status
- EC2 + Docker bereit	✅
- n8n läuft mit HTTPS	✅ https://netspark.duckdns.org
- DuckDNS & Domain	✅
- Google OAuth aktiv	✅
- UptimeRobot aktiv	✅

