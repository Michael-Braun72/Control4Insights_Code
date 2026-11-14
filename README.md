# Control4insights

**Python-Toolbox fuer modernes, datengetriebenes Controlling**

---

## Inhaltsverzeichnis

- [Ueber dieses Projekt](#ueber-dieses-projekt)
- [Praxisrelevanz fuer Controller](#praxisrelevanz-fuer-controller)
- [Repository-Struktur](#repository-struktur)
  - [Python-Anwendungen](#python-anwendungen)
  - [Jupyter Notebooks](#jupyter-notebooks)
  - [Process Analyzer](#process-analyzer)
  - [KI im Controlling - Schulung](#ki-im-controlling---schulung)
  - [Output / Workflows](#output--workflows)
  - [Claude Skills](#claude-skills)

---

## Ueber dieses Projekt

Control4insights ist eine Sammlung professioneller Python-Anwendungen fuer das moderne Controlling. Als Business Partner Controller mit Fokus auf Datenanalyse und Automatisierung entwickle ich hier Loesungen, die zeigen, wie klassische Controlling-Aufgaben durch Python-basierte Workflows effizienter und skalierbarer werden.

**Kernkompetenzen, die dieses Repository demonstriert:**
- Advanced Analytics fuer Forecasting und Variance Analysis
- Automatisierung von Reporting-Prozessen und Datenintegration
- Visualisierung komplexer Finanzdaten fuer Self-Service Analytics
- Clean Code und Software Engineering Best Practices im Finance-Kontext
- Bruecke zwischen Controlling-Expertise und technischer Umsetzung

---

## Praxisrelevanz fuer Controller

Alle Tools und Scripts basieren auf realen Controlling-Herausforderungen:

| Use Case | Business Problem | Technische Loesung |
|----------|-----------------|-------------------|
| **Explorative Datenanalyse - EDA** | EDA ueber Excel zeitintensiv und nicht automatisiert | Automatisierte EDA von Controllingdaten in xls oder csv Format |
| **Variance Analysis** | Manuelle Plan-Ist-Vergleiche zeitintensiv | Automatisierte Abweichungsanalyse mit Root-Cause-Drilling |
| **Rolling Forecast** | Excel-basierte Forecasts fehleranfaellig | ML-gestuetzte Zeitreihenprognosen mit Konfidenzintervallen |
| **KPI-Reporting** | Statische Reports ohne Interaktivitaet | Self-Service Dashboards mit Drill-Down-Funktionalitaet |
| **Datenintegration** | Manuelle Datenextraktion aus SAP/Excel | ETL-Pipelines mit Validierung und Fehlerbehandlung |
| **Ad-hoc Analysen** | Wiederholte manuelle Auswertungen | Wiederverwendbare Analyse-Templates und Notebooks |

---

## Repository-Struktur

### Python-Anwendungen

| Datei | Beschreibung |
|-------|-------------|
| [`ai_finance_news_agent.py`](ai_finance_news_agent.py) | KI-gestuetzter Finance-News-Agent - automatisierte Aggregation und Analyse von Finanznachrichten |
| [`controlling_libraries.py`](controlling_libraries.py) | Sammlung wiederverwendbarer Controlling-Bibliotheken und Hilfsfunktionen |
| [`prime_numbers_visualization.py`](prime_numbers_visualization.py) | Visualisierung von Primzahlen - Demonstration mathematischer Datenvisualisierung |

### Jupyter Notebooks

| Notebook | Beschreibung |
|----------|-------------|
| [`eda_notebook_creator.ipynb`](eda_notebook_creator.ipynb) | Automatisierter EDA-Notebook-Generator fuer Controllingdaten (Excel/CSV) |
| [`guv_analyse.ipynb`](guv_analyse.ipynb) | GuV-Analyse (Gewinn- und Verlustrechnung) - strukturierte Ergebnisanalyse |

### Process Analyzer

Modulare Python-Anwendung zur Analyse von Geschaeftsprozessen auf Basis von Event-Logs.

| Datei | Beschreibung |
|-------|-------------|
| [`process_analyzer/main.py`](process_analyzer/main.py) | Hauptmodul und Einstiegspunkt |
| [`process_analyzer/config.py`](process_analyzer/config.py) | Konfiguration und Parameter |
| [`process_analyzer/loader.py`](process_analyzer/loader.py) | Datenlade-Modul fuer Event-Logs |
| [`process_analyzer/analysis.py`](process_analyzer/analysis.py) | Analyse-Logik fuer Prozess-Mining |
| [`process_analyzer/visualization.py`](process_analyzer/visualization.py) | Visualisierung der Prozessanalyse-Ergebnisse |
| [`process_analyzer/generate_sample_data.py`](process_analyzer/generate_sample_data.py) | Generator fuer Beispiel-Event-Log-Daten |
| [`process_analyzer/data/sample_event_log.csv`](process_analyzer/data/sample_event_log.csv) | Beispiel-Event-Log (CSV) |
| [`process_analyzer/requirements.txt`](process_analyzer/requirements.txt) | Python-Abhaengigkeiten |

### KI im Controlling - Schulung

Strukturierte Schulungsunterlagen zum Einsatz von KI-Tools im Controlling.
Siehe [`KI_im_Controlling/README.md`](KI_im_Controlling/README.md) fuer die vollstaendige Moduluebersicht.

#### Praesentationen

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/0_Presentation/KI_im_Controlling_Praesentation_v2.html`](KI_im_Controlling/0_Presentation/KI_im_Controlling_Praesentation_v2.html) | Gesamtpraesentation V2 (HTML) |
| [`KI_im_Controlling/0_Presentation/KI_im_Controlling_Praesentation_v3.html`](KI_im_Controlling/0_Presentation/KI_im_Controlling_Praesentation_v3.html) | Gesamtpraesentation V3 (HTML) |

#### Uebungen & Beispiele

| Datei | Thema |
|-------|-------|
| [`KI_im_Controlling/1_Examples/Schulungsübersicht.html`](KI_im_Controlling/1_Examples/Schulungsübersicht.html) | Schulungsuebersicht (HTML) |
| [`KI_im_Controlling/1_Examples/README.md`](KI_im_Controlling/1_Examples/README.md) | Beispiele-Uebersicht |

**Prompting**

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/1_Examples/1_Prompting/Prompt_Uebungen.md`](KI_im_Controlling/1_Examples/1_Prompting/Prompt_Uebungen.md) | Prompt-Engineering-Uebungen fuer Controller |
| [`KI_im_Controlling/1_Examples/1_Prompting/Prompt_Vorlagen_Controlling.md`](KI_im_Controlling/1_Examples/1_Prompting/Prompt_Vorlagen_Controlling.md) | Prompt-Vorlagen fuer Controlling-Aufgaben |

**Copilot**

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/1_Examples/2_Copilot/Copilot_Uebungen.md`](KI_im_Controlling/1_Examples/2_Copilot/Copilot_Uebungen.md) | Microsoft Copilot Uebungen |
| [`KI_im_Controlling/1_Examples/2_Copilot/Beispieldaten_AB_Test.csv`](KI_im_Controlling/1_Examples/2_Copilot/Beispieldaten_AB_Test.csv) | A/B-Test Beispieldaten (CSV) |
| [`KI_im_Controlling/1_Examples/2_Copilot/Copilot_Excel/KI_im_Controlling_Demo_Daten.xlsx`](KI_im_Controlling/1_Examples/2_Copilot/Copilot_Excel/KI_im_Controlling_Demo_Daten.xlsx) | Demo-Daten fuer Copilot Excel-Uebungen |
| [`KI_im_Controlling/1_Examples/2_Copilot/Copilot_Excel/DB_Rechnung_5J_Simulation_break_even.xlsx`](KI_im_Controlling/1_Examples/2_Copilot/Copilot_Excel/DB_Rechnung_5J_Simulation_break_even.xlsx) | DB-Rechnung 5-Jahres-Simulation mit Break-Even |

**Claude**

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/1_Examples/3_Claude/Claude_Analyse_Uebungen.md`](KI_im_Controlling/1_Examples/3_Claude/Claude_Analyse_Uebungen.md) | Claude Analyse-Uebungen |
| [`KI_im_Controlling/1_Examples/3_Claude/AB_Test_Analyse.ipynb`](KI_im_Controlling/1_Examples/3_Claude/AB_Test_Analyse.ipynb) | A/B-Test Analyse Notebook |
| [`KI_im_Controlling/1_Examples/3_Claude/Beispieldaten_AB_Test.csv`](KI_im_Controlling/1_Examples/3_Claude/Beispieldaten_AB_Test.csv) | A/B-Test Beispieldaten (CSV) |
| [`KI_im_Controlling/1_Examples/3_Claude/Claude_Excel/KI_im_Controlling_Demo_Daten.xlsx`](KI_im_Controlling/1_Examples/3_Claude/Claude_Excel/KI_im_Controlling_Demo_Daten.xlsx) | Demo-Daten fuer Claude Excel-Uebungen |
| [`KI_im_Controlling/1_Examples/3_Claude/Claude_Excel/DB_Rechnung_5J_Simulation_break_even.xlsx`](KI_im_Controlling/1_Examples/3_Claude/Claude_Excel/DB_Rechnung_5J_Simulation_break_even.xlsx) | DB-Rechnung 5-Jahres-Simulation mit Break-Even |
| [`KI_im_Controlling/1_Examples/3_Claude/Claude_Excel/DB_Rechnung_Break_Even_Analyse.ipynb`](KI_im_Controlling/1_Examples/3_Claude/Claude_Excel/DB_Rechnung_Break_Even_Analyse.ipynb) | Break-Even-Analyse Notebook |

**ChatGPT**

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/1_Examples/4_ChatGPT/ChatGPT_Uebungen.md`](KI_im_Controlling/1_Examples/4_ChatGPT/ChatGPT_Uebungen.md) | ChatGPT Uebungen |

**Perplexity**

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/1_Examples/5_Perplexity/Perplexity_Uebungen.md`](KI_im_Controlling/1_Examples/5_Perplexity/Perplexity_Uebungen.md) | Perplexity Uebungen |

**n8n Workflow-Automatisierung**

| Datei | Beschreibung |
|-------|-------------|
| [`KI_im_Controlling/1_Examples/6_n8n/n8n_Workflow_Uebungen.md`](KI_im_Controlling/1_Examples/6_n8n/n8n_Workflow_Uebungen.md) | n8n Workflow-Uebungen |
| [`KI_im_Controlling/1_Examples/6_n8n/n8n_Local_Quickstart.md`](KI_im_Controlling/1_Examples/6_n8n/n8n_Local_Quickstart.md) | n8n Lokaler Schnellstart-Guide |
| [`KI_im_Controlling/1_Examples/6_n8n/N8n mein eigenes Beispiel für Workflow.docx`](KI_im_Controlling/1_Examples/6_n8n/N8n%20mein%20eigenes%20Beispiel%20für%20Workflow.docx) | Eigenes n8n Workflow-Beispiel (Word) |

### Output / Workflows

| Datei | Beschreibung |
|-------|-------------|
| [`output/n8n_workflows/Schulung_Daten_Pipeline_Workflow.json`](output/n8n_workflows/Schulung_Daten_Pipeline_Workflow.json) | n8n Workflow: Schulungs-Daten-Pipeline (JSON-Export) |
| [`output/n8n_workflows/README_Schulung_Daten_Pipeline.md`](output/n8n_workflows/README_Schulung_Daten_Pipeline.md) | Dokumentation zur Schulungs-Daten-Pipeline |

### Claude Skills

85 kuratierte Claude Skills fuer Business Partner Controlling in der Maschinenvision-Industrie.
Siehe [`claude_skills.md`](claude_skills.md) fuer die vollstaendige Uebersicht mit Beschreibungen und Routing-Regeln.

**Kategorien:** Analyse & Abweichungen | Reporting & Abschluss | Planung & Forecast | Kosten & Steuerung | Spezialanalysen | Business Partnering & Strategie | Daten & Analytics | Python & Code | ERP & Automatisierung | KI & Digitalisierung | LinkedIn & Content | Prozesse & Dokumentation | Wissensmanagement | Qualitaetssicherung | Standard-Tools

---

## Konfiguration

| Datei | Beschreibung |
|-------|-------------|
| [`.gitignore`](.gitignore) | Git-Ausschlussliste |

---

*Business Partner Controlling - Maschinenvision / Bildverarbeitung*
