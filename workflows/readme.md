# 🧠 Projekt: **Netspark – Intelligentes Lead Qualification System mit n8n & AI**

## Projektziel
Ziel dieses Systems ist es, Instagram-Influencer (in diesem Fall Mütter in der Schweiz) automatisiert zu identifizieren, deren Follower zu extrahieren, diese Leads mit Hilfe eines KI-gestützten Qualifizierungsprozesses zu analysieren und in zwei Kategorien aufzuteilen: **Unqualifizierte** und **Qualifizierte Leads**. Dies ermöglicht eine zielgerichtete Ansprache potenzieller Kunden im Influencer- und Marketingbereich.  

---

## Technologischer Stack
- **n8n** (No-Code/Low-Code Automation)
- **Google Sheets** (Datenhaltung)
- **SerpAPI** (Google Search API)
- **OpenAI GPT-4o** (für Lead-Qualifizierung)
- **Growman Extract** (Follower Extraction Tool)
- **Docker & HTTPS Deployment auf AWS EC2**

---

## Teil 1: Instagram-Mütter in der Schweiz identifizieren

### Workflow-Übersicht (Screenshot 1)

1. **Trigger Action**  
   Startpunkt des automatisierten Ablaufs, kann z. B. manuell oder zeitgesteuert ausgelöst werden.

2. **SerpAPI Request (HTTP Node)**  
   Führt eine Google-Suche aus mit dem Query:  
   `10 Instagram moms Switzerland site:instagram.com`  
   Dadurch werden reale Instagram-Profile von Schweizer Müttern gefunden, ohne manuelle Recherche.

3. **Parse to JSON**  
   Wandelt die SerpAPI-Antwort in ein sauberes JSON-Format um, sodass die Daten weiterverarbeitet werden können.

4. **Loop Over Items**  
   Iteriert über jedes der gefundenen Profile, um sie einzeln in Google Sheets zu schreiben.  
   Ohne diese Schleife würde nur ein Profil mehrfach eingetragen werden.

5. **Google Sheets (Append Sheet)**  
   Speichert alle Instagram-Profile in einem Google-Sheet.  
   Diese Tabelle dient als Ausgangspunkt für den nächsten Schritt: Follower-Extraktion mit **Growman Extract**.

   ![image](https://github.com/user-attachments/assets/9e8997a0-2ee8-4373-9791-9698ae3be881)


---

## Teil 2: Follower analysieren und mit GPT-4o qualifizieren

### Workflow-Übersicht (Screenshot 2)

1. **Trigger Action**  
   Startet den Qualifizierungsprozess, sobald neue Follower extrahiert wurden.

2. **Wait**  
   Kurze Pause, um sicherzustellen, dass Growman Extract genügend Zeit hat, alle Follower-Daten zu exportieren.

3. **Google Sheets (Unqualified Leads Read)**  
   Liest die extrahierten Follower (potenzielle Leads) aus einem Sheet, welches zuvor mit den Daten aus den Instagram-Profilen gefüllt wurde.

4. **Parse to JSON 1**  
   Wandelt die gelesenen Daten in JSON um, um sie im nächsten Schritt strukturiert verarbeiten zu können.

5. **Loop Over Items**  
   Führt eine Schleife über jeden Lead aus, um diese einzeln zu analysieren und um GPT-Ratenlimits zu umgehen.

6. **Wait 1 (0.5 Sekunden)**  
   Verzögert jede GPT-Anfrage leicht, um API-Rate-Limits nicht zu überschreiten.

7. **AI Agent Qualifier (OpenAI GPT-4o)**  
   Führt eine KI-gestützte Bewertung jedes Leads durch basierend auf einem individuell entwickelten Prompt.  
   Der Prompt filtert nur relevante Leads anhand vordefinierter Kriterien wie z. B. Aktivität, Beruf, Inhalt des Profils usw.  
   Modell: GPT-4o mit Memory Tool und Chat-Verlauf für bessere Kontextverarbeitung.

8. **Parse to JSON 2**  
   Wandelt die KI-Antwort wieder in strukturiertes JSON um, um die nötigen Felder extrahieren zu können.

9. **Edit Fields**  
   Extrahiert nur die benötigten Informationen aus der GPT-Antwort und bereitet diese für den Export auf.

10. **Google Sheets (Qualified Leads)**  
   Alle qualifizierten Leads werden final in ein dediziertes Google-Sheet geschrieben.  
   Diese Liste kann direkt für Marketing, Kontaktaufnahme oder CRM-Import genutzt werden.

![image](https://github.com/user-attachments/assets/0b0132a3-21af-497b-a759-5f7d87e2e9e1)


---

## Besonderheiten und Highlights

- **Automatisierte Lead-Recherche**: Keine manuelle Profilrecherche notwendig.
- **Datengestützte Entscheidungen**: KI filtert nach personalisierten, geschäftsrelevanten Kriterien.
- **Erweiterbar & Modular**: Das System kann einfach auf andere Zielgruppen oder Plattformen (z. B. TikTok, LinkedIn) angepasst werden.
- **Datenschutzfreundlich**: Speicherung erfolgt nur in Google Sheets ohne unnötige Cloud-Abhängigkeiten.

---

## Fazit

Mit viel Zeit und technischem Feingefühl wurde ein leistungsfähiges System zur Instagram Lead-Generierung gebaut. Es automatisiert den kompletten Workflow von der Recherche über die Extraktion bis hin zur Qualifizierung. Dank der Kombination aus n8n und GPT-4o bietet **Netspark** eine moderne, skalierbare und intelligente Lösung, die manuell kaum in dieser Qualität umsetzbar wäre.
