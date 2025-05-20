# Kompetenz A1 – Ermittlung erforderlicher Services

## Beschreibung der Kompetenz
> Die benötigten Cloud-Services und Tools werden auf Grundlage einer Anforderungsanalyse ausgewählt und sinnvoll geplant. Ziel ist es, passende Technologien zu evaluieren und ein Konzept für deren Einsatz zu erstellen.

## Umsetzung in meinem Projekt

### Bedarfserhebung
- Ziel war es, ein Automatisierungsprojekt zu realisieren, das cloudfähig ist, innovativ ist und gleichzeitig bisschen drüber von dem Rahmen meiner Fähigkeiten liegt. (Damit ich mich fordere soll ja nicht easy sein) 
- Ich habe mich für **n8n** entschieden, da es:
  - neu für mich war (→ neue Technologie laut V2)
  - sich gut in Container-Umgebungen integrieren lässt
  - skalierbar in der Cloud betrieben werden kann
  - produktiv zur Automatisierung von Geschäftsprozessen eingesetzt wird

### Technische Anforderungen
- Zugriff über das Internet (Reverse Proxy mit SSL)
- Stabiler Betrieb über Docker Container
- Verwaltung über eine EC2-Instanz (AWS)
- Zukunftsfähig erweiterbar (APIs, Webhooks, AI-Plug-ins)

### Entscheidungsgrundlage
Ich habe folgende Optionen verglichen:
| Tool       | Eignung | Cloud-fähig | Aufwand | Community |
|------------|---------|-------------|---------|-----------|
| Zapier     | ❌      | ✅          | gering  | hoch      |
| Node-RED   | ✅      | ⚠️ begrenzt | mittel  | hoch      |
| **n8n**    | ✅✅     | ✅✅         | mittel  | aktiv     |

**→ Entscheidung für n8n als Basis meiner Automationsplattform.**

## Eingesetzte Technologien
- AWS EC2 (Cloud-Infrastruktur)
- Docker (Containerisierung)
- NGINX (Reverse Proxy)
- n8n (Workflow-Automation)

## Nachweise
- Projektplanung in `IPERKA.md` coming soon
- Lernjournal Woche 20
- n8n Architektur: siehe "coming soon" 
