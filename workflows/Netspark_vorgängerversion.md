

# Netspark – Entwicklung der Vorgängerversionen

## Netspark V1

Wie man auf dem Screenshot sieht, habe ich in dieser ersten Version versucht, den gesamten Prozess in einem einzigen Workflow abzubilden: Potenzielle Leads wurden mithilfe eines KI-Agenten auf Basis von Gemini gefunden, ihre Follower extrahiert, anschließend durch einen Qualifizierungs-Agenten geschickt und schließlich in ein gefiltertes Leads-Sheet eingetragen.

**Probleme:**

- Die Lead-Qualität war unzureichend, da die Ergebnisse oft ungenau oder nicht relevant waren.
- Gemini eignete sich gut zum Testen, war jedoch für ein produktives System nicht konsistent genug und nicht intelligent genug.
- Der Qualifier-Prompt war zu allgemein formuliert, wodurch die Ergebnisse nicht ausreichend gefiltert wurden.

![image](https://github.com/user-attachments/assets/ad71934b-0ba5-4351-98f3-7ca97048df39)


## Netspark V2

In dieser Version habe ich einige entscheidende Änderungen vorgenommen. Anstelle eines All-in-One-Workflows entschied ich mich, das Lead-Scraping mithilfe von SerpAPI durchzuführen, um genauere Ergebnisse zu erzielen. Danach erfolgte wie zuvor die Qualifizierung der Leads.

**Verbesserungen:**
- SerpAPI als Tool zur Lead-Suche → deutlich bessere und gezieltere Ergebnisse.
- Einsatz von OpenAI als LLM zur Qualifizierung → deutlich intelligenter, allerdings mit höheren Kosten.

**Probleme:**
- OpenAI unterliegt Token- und Request-Limits, besonders bei den leistungsfähigeren Modellen. Dadurch konnten nur etwa 10 Leads pro Durchlauf qualifiziert werden – nicht ideal für größere Mengen.

![image](https://github.com/user-attachments/assets/57b3fecc-53d4-4d5d-995b-54a977e1ff4d)


## Netspark V3

Die aktuellste und zugleich beste Version von Netspark: schneller, stabiler und intelligenter. Ich habe den Prozess in einzelne Module aufgeteilt – Lead Scraping, Follower-Extraktion und Qualifizierung – um ihn effizienter und robuster zu gestalten.

**Verbesserungen:**

- Klare Trennung zwischen den Prozessen → bessere Übersicht und weniger Fehlerquellen.
- Die Qualifizierung ist nun in eine Loop-Funktion eingebettet, um Token-Limits zu umgehen.
- Eine zusätzliche „Wait“-Node verzögert jeden Durchlauf um 0.5 Sekunden, um API-Limits und parallele Überlastung zu vermeiden.

![image](https://github.com/user-attachments/assets/39e93d07-86cf-4768-9965-bfbc748e5dd3)
