# Claude Skills - Meine Skill-Bibliothek

**Kuratierte Sammlung von Claude Skills fuer Business Partner Controlling in der Maschinenvision-Industrie**

Stand: 14.11.2026 | Anzahl Skills: 85

---

## Inhaltsverzeichnis

- [Controlling & Finance - Analyse & Abweichungen](#controlling--finance---analyse--abweichungen)
- [Controlling & Finance - Reporting & Abschluss](#controlling--finance---reporting--abschluss)
- [Controlling & Finance - Planung & Forecast](#controlling--finance---planung--forecast)
- [Controlling & Finance - Kosten & Steuerung](#controlling--finance---kosten--steuerung)
- [Controlling & Finance - Spezialanalysen](#controlling--finance---spezialanalysen)
- [Business Partnering & Strategie](#business-partnering--strategie)
- [Daten & Analytics](#daten--analytics)
- [Python & Code-Generierung](#python--code-generierung)
- [ERP & Automatisierung](#erp--automatisierung)
- [KI & Digitalisierung](#ki--digitalisierung)
- [LinkedIn & Content](#linkedin--content)
- [Prozesse & Dokumentation](#prozesse--dokumentation)
- [Wissensmanagement & Session](#wissensmanagement--session)
- [Qualitaetssicherung & Methodik](#qualitaetssicherung--methodik)
- [Tools & System (Anthropic Standard-Skills)](#tools--system-anthropic-standard-skills)

---

## Controlling & Finance - Analyse & Abweichungen

### variance-master
**Abweichungsanalyse & Bridge-Analyse fuer BP Controlling**

Modi: (A) Variance Commentary nach Zielgruppe (BU-Leiter/CFO/Board), (B) Bridge-Analyse (EBIT-Bridge, Umsatz-Bridge, Kosten-Bridge), (C) PVM Python-Notebook (Preis-/Mengen-/Mix-Zerlegung, Plotly-Wasserfall). Aktivierung bei: Abweichungsanalyse, Variance, Plan-Ist-Vergleich, Bridge, Waterfall, EBIT-Bridge, Umsatzabweichung, Kostenabweichung, PVM, Preis-Mengen-Mix, Revenue Bridge, Variance Commentary, Forecast-Anpassung.

### variance-bp
**Strukturierte Abweichungsanalyse fuer Business Partner Controlling**

Spezialisiert auf Maschinenvision-Industrie. Aktivierung bei: Variance, Plan-Ist-Vergleich, Bridge-Analyse, Waterfall, Kommentierung, Monatsbericht, EBIT-Bridge, BU-Review. Auch wenn Zahlen mit Plan/Budget/Forecast verglichen oder CFO-Berichte/BU-Praesentationen mit Abweichungsdaten erstellt werden sollen.

### abweichungsanalyse-bridge
**Strukturierte Abweichungsanalysen mit Preis-Mengen-Mix-Zerlegung**

Fuehrt Preis-Mengen-Mix-Zerlegung, FX-Effekte, Kostenarten-Bridges und Wasserfall-Visualisierungen durch. Fuer Umsatz-, Kosten- und Ergebnisanalysen im Industrie-Controlling.

### pvm-controlling
**Price-Volume-Mix (PVM) Analyse**

Zerlegung von Umsatz- oder Margenaenderungen in Preis-, Volumen- und Mixeffekte. Erstellt Python-Notebooks fuer PVM-Reporting mit Waterfall-Charts. Aktivierung bei: PVM, Preiseffekt, Volumeneffekt, Mixeffekt, Abweichungsanalyse Umsatz, Revenue Bridge.

### break-even-controlling
**Strukturierte Break-Even-Analyse fuer Industrie-Controlling**

Berechnet Gewinnschwelle (Menge und Umsatz), Sicherheitsmarge, Fixkostendegression und Preissensitivitaet. Liefert CFO/COO-taugliche Entscheidungsvorlage inkl. Sensitivitaetstabelle und Szenario-Vergleich. Aktivierung bei: Break-Even, Gewinnschwelle, Deckungspunkt, Mindestauslastung, Mindestpreis, Make-or-Buy Break-Even.

### sensitivitaetsanalyse-controlling
**Strukturierte Sensitivitaetsanalyse fuer Controlling**

One-Way-/Two-Way-Sensitivitaeten, Tornado-Diagramme, Spider-Charts, Break-Even-Sensitivitaet via Excel Data Tables oder Python. Aktivierung bei: Sensitivitaetsanalyse, Tornado-Diagramm, What-If-Analyse, Treiberanalyse, Stresstest Annahmen, Werttreiberanalyse NPV/EBITDA/Marge.

### db-szenario-skill-eval-v3
**Treiberbasierte Contribution-Margin-Szenarien**

Vollstaendige P&L-Kaskade: Revenue -> CM1 -> CM2 -> EBITDA inkl. aller Kostenbloecke. Erstellt Management-ready One-Pager mit Waterfall-Chart und Szenario-Vergleich (Base/Best/Worst) inkl. EBITDA-Delta und Margin-Ausweis. Auch fuer Excel-Export und iterative Verbesserung bestehender DB-Rechnungen geeignet.

### cash-conversion-analyse
**Working-Capital-Analyse auf Basis des Cash Conversion Cycle (CCC)**

Berechnet gebundenes Kapital in Forderungen, Lager und Verbindlichkeiten, identifiziert den wirkungsstaerksten Hebel zur Liquiditaetsverbesserung und liefert eine priorisierte Massnahmenempfehlung mit konkretem Cash-Release-Potenzial in Euro.

---

## Controlling & Finance - Reporting & Abschluss

### management-reporting-output
**Management Reporting fuer BU Controlling**

Erstellt CFO/COO-taugliche Outputs: Management Summary, KPI-Dashboards, Kommentierungsvorlagen, One-Pager und Praesentationsfolien. Aktivierung bei: Management Report, Monatsbericht, Monthly Report, Executive Summary, Flash Report, Vorstandsbericht, Reporting-Paket.

### monatsbericht-controlling
**Standardisierte Monatsberichte fuer Industrie-Controlling**

KPI-Analyse, Abweichungskommentierung und Management Summary. Aktivierung bei: Monatsbericht, Monthly Report, Monatsreporting, Monatsclosing.

### monatsabschluss-checkliste
**Operativer Monatsabschluss-Begleiter**

Kombiniert strukturierte Checkliste (9 Bereiche + Projektgeschaeft) mit Gap-Analyse und Risikopriorisierung. Aktivierung bei: Monthly Close, Close-Prozess, Abschluss-Checkliste, Pre-Close, Rueckstellungen pruefen, Accruals, WIP-Bewertung, POC-Pruefung, Cutoff-Pruefung.

### bu-controlling-dashboard
**Interaktives HTML-Dashboard fuer BU Controlling**

Generiert ein interaktives HTML-Dashboard aus hochgeladenen Finanzdaten (Excel, CSV, PDF). Ausgabe: Selbst-enthaltene HTML-Datei mit Chart.js, Szenario-Toggles, KPI-Cards und Tabellen. Aktivierung bei: Dashboard erstellen, KPI-Uebersicht, Management Cockpit, Budget vs Ist, Rolling Forecast Dashboard.

### pre-close-data-quality
**Regelbasierte GL-Datenqualitaetspruefung vor dem Monatsabschluss**

Pre-Close Validation: Buchungsqualitaet pruefen, GL-Fehler identifizieren, Cutoff-Probleme erkennen, fehlerhafte Kontierungen aufdecken. Aktivierung bei: Pre-Close Check, GL-Validierung, Fehlbuchungen, Accrual-Validierung, Journal Entry Review, Kontierungsfehler.

### forderungsmanagement-aging
**Debitoren-Altersstrukturanalyse (Aging Report)**

Risikoklassifizierung, Wertberichtigungsbedarfsrechnung (EWB/PWB nach HGB) und Eskalationsmatrix. Liefert CFO-taugliche Entscheidungsvorlage zur Forderungssicherung und DSO-Steuerung. Aktivierung bei: Aging Report, ueberfaellige Forderungen, EWB, PWB, DSO-Steuerung, offene Posten Analyse.

---

## Controlling & Finance - Planung & Forecast

### rolling-forecast-budgetierung
**Operativer Planungs- und Forecast-Skill**

Vollstaendiger Planungszyklus: Bottom-up-Budgetierung, Treiberbaum-Logik, Rolling Forecast, Forecast-Qualitaet und Abweichungskommentierung. Aktivierung bei: Budget, Jahresplanung, Rolling Forecast, Forecast-Accuracy, Planungspraemissen, Treiberbaum, Gegenstromverfahren.

### revenue-driver-model
**Treiberbasierter Umsatzplan-Aufbau fuer bestehendes Geschaeft**

Zerlegt den Planumsatz in Bausteine: Bestandsgeschaeft/Run-Rate, Vertragsverlaengerung, Cross-/Upsell, Neugeschaeft aus Pipeline, Auftragsbestands-Abbau und Preis-/Mix-Effekt mit Konfidenzstufe (Committed/Pipeline-gewichtet/Greenfield). Liefert Revenue-Bridge (Wasserfall) von Vorjahr zu Plan.

### neugeschaefts-treiberbaum
**Treiberbasierte Bewertung neuer Geschaeftsideen**

Umsatz-Treiberbaum mit harten (kardinalen) und weichen (ordinalen) Einflussfaktoren. Base/Best/Worst-Szenarien, Monte-Carlo-Simulation und CFO-taugliche Entscheidungsvorlage. Aktivierung bei: Treiberbaum neue Geschaeftsidee, Business Case Umsatzsimulation, Marktpotenzial neues Angebot, Go/No-Go Umsatzseite.

### personalkosten-controlling
**Personalkosten-Controlling fuer BU Controlling**

HC-Planung, Vollkostenermittlung, PerEx-Steuerung, Stellenplan-Controlling und Gehaltsrunden-Modellierung. Aktivierung bei: Personalkosten, Headcount, FTE, Personalbudget, Gehaltsrunde, Merit Increase, Vollkostensatz, PerEx-Abweichung.

### liquiditaetsplanung
**Liquiditaetsplanung und Cashflow-Steuerung**

Cashflow-Planung, Working-Capital-Analyse, NWC-Optimierung und Liquiditaetsvorschau. Aktivierung bei: Liquiditaetsplanung, Cashflow-Forecast, Free Cashflow, Working Capital, DSO, DPO, DIO, Cash Conversion Cycle, 13-Wochen-Vorschau.

### investitionsrechnung
**Strukturierte Investitionsrechnung und Business-Case-Erstellung**

NPV, IRR, WACC, Annuitaet, Payback Period, DCF, ROI, Make-or-Buy-Rechnung. Aktivierung bei: Investitionsrechnung, Business Case, Kapitalwert, Wirtschaftlichkeitsrechnung, CAPEX, Investitionsfreigabe.

---

## Controlling & Finance - Kosten & Steuerung

### kostenstruktur-analyse
**Strukturierte Kostenstrukturanalyse und Kostentreiberidentifikation**

Fixkosten, variable Kosten, Kostentreiber, mehrstufige Deckungsbeitragsrechnung, Vollkosten-/Teilkostenrechnung, Operating Leverage. Aktivierung bei: Kostenstruktur, Kostentreiber, Deckungsbeitrag, Fixkostendegression, Kostenarten, Kostenstellen.

### kostenfresser-scan
**Scan nach den groessten Kostenfressern (Verlustquellen)**

Fuenf Typen: Prozesse, Fehler/Nacharbeit, Durchlaufzeiten, ungenutzte Kapazitaet, fehlende Transparenz. Bewertet in Euro mit Konfidenzstufe (Fakt/Hochrechnung/Hypothese), bereinigt Doppelzaehlungen, priorisiert nach Hebel und Umsetzbarkeit. Output: HTML-One-Pager fuer CFO/COO.

### kostenmassnahmen-controlling
**Kostenmasssnahmen-Controlling: Identifikation, Bewertung, Tracking und Validierung**

Savings-Tracking, Savings-Validierung, echte vs. buchhalterische Einsparung, Cost Avoidance vs. Cost Reduction. Aktivierung bei: Kostensenkung, Einsparpotenzial, Zero-Based Budgeting, Should-Cost, Gemeinkostenoptimierung.

### komplexitaets-controlling
**Komplexitaets-Controlling fuer BU Controlling**

Diagnostiziert, quantifiziert und priorisiert EBIT-relevante Komplexitaetstreiber in 3 Stufen: Scoring der 8 Typen, EBIT-Impact-Schaetzung, Massnahmenpriorisierung (Quick Win vs. Strukturmassnahme). Output: CFO-tauglicher HTML-One-Pager.

### projektcontrolling
**Projektcontrolling und Projektmargenverfolgung**

EAC, ETC, POC, Revenue Recognition, Fertigstellungsgrad, Auftragsbestand, Projektkalkulation, Cost-to-Complete, WIP. Besonders relevant fuer Maschinenvision, wo Projekte 6-18 Monate dauern und Hardware+Software+Services kombiniert werden.

### lean-controlling
**Lean-Management-Methoden auf Controlling-Prozesse**

Effizienz, Verschwendung, Optimierung von Controlling-Prozessen (Reporting, Budgetierung, Forecasting, Abschluesse). Kombiniert Lean-Methodik (Muda, Wertstrom, PDCA, 5S) mit Controlling-Praxis im industriellen B2B-Umfeld.

### intercompany-controlling
**Intercompany-Controlling fuer BU Controlling im Konzerngeschaeft**

IC-Abstimmung, Verrechnungspreise, Konsolidierungsvorbereitung, IC-Billing und Eliminierungslogik. Aktivierung bei: Intercompany, Transfer Pricing, Arm's Length, Konsolidierungspaket, IC-Eliminierung, Managementumlage, Shared Services.

---

## Controlling & Finance - Spezialanalysen

### 3-statement-integration
**Integriertes 3-Statement-Finanzmodell**

Verknuepft P&L -> Bilanz -> Cashflow konsistent. Schliesst die Cashflow-Bruecke (indirekte Methode), leitet Bilanzpositionen aus Planpraemissen ab (NWC/DSO/DPO/DIO, CAPEX, Debt-Schedule) und fuehrt Konsistenz-Checks durch (Assets=Liabilities, Cash-Reconciliation, Net Income->Equity).

### carve-out-divestiture
**Carve-out- und Divestiture-Modell fuer BU Controlling**

HGB, B2B-Projektgeschaeft: Perimeter, Stand-alone-Kosten, Dis-Synergien, Stranded Costs, TSA, One-off-Kosten, NWC-Split, Paragraph 613a BGB. Aktivierung bei: Carve-out, Divestiture, Ausgliederung, NewCo/RemainCo, Day-1-Readiness.

### unit-economics-analysis
**Unit-Economics-Analyse fuer industrielles B2B-Projektgeschaeft**

Deckungsbeitrag je Einheit (Projekt/System/Servicevertrag), Cost-to-Win als CAC-Aequivalent, Payback-Horizont ueber den Anlagen-Lifecycle. Explizit KEIN SaaS-Modell, sondern angepasst an Hardware+Software+Service-Projektgeschaeft mit langen Zyklen.

### cohort-analysis-saas-controlling
**Kohorten-Analyse fuer SaaS- und Recurring-Revenue-Geschaeftsmodelle**

Retention-Raten, Revenue-per-Cohort, Churn-Muster ueber Kohorten. Aktivierung bei: Kohortenanalyse, Retention Heatmap, NRR, GRR, Scan-as-a-Service, OpEx-Transformation, Recurring Revenue Controlling, ARR, CLV.

### kundenwert-scanner
**Strukturierte Kundensegmentierung nach Wert und Aufwand**

Klassifiziert Kunden in vier strategische Zonen (Stars, Cash Cows, Investitionsfaelle, Kostenbloecke) auf Basis von Umsatz, Marge, Betreuungsaufwand und Reklamationsquote. Liefert differenzierte Handlungsempfehlungen pro Segment.

### value-wedge-pricing
**Strukturierte Value-Gap-Analyse fuer Pricing-Entscheidungen**

Berechnet die Luecke zwischen geliefertem Kundenwert und aktuellem Preis. Identifiziert Preiserhoehungspotenziale pro Leistungssegment ohne Abwanderungsrisiko. Ausgabe als CFO/COO-taugliche Entscheidungsvorlage.

### spend-anomaly-detection
**Statistisch fundierte Ausgaben-Anomalieerkennung**

IQR-Analyse, Z-Score, Isolation Forest auf Transaktionsdaten. Aktivierung bei: Ausgaben-Outlier, Transaktionsmonitoring, auffaellige Buchungen, statistische Kostenkontrolle, Duplikaterkennung Rechnungen, Spend Analytics.

---

## Business Partnering & Strategie

### business-partner-controlling
**Umfassender Business Partner Controlling Skill**

Strategische Planung, Performance Management, Business Cases, Kostenmanagement, Datenanalyse-Automatisierung. Beruecksichtigt MS Dynamics AX/D365, Power BI, Python, Keboola und Branchenspezifika (Hardware/Software-Mix, Projektgeschaeft). Zielgruppe: BU Management und C-Level.

### strategic-planning-partner
**Business Partner Controlling fuer strategische Planung**

Erstellt Decision Packs, Finanzbruecken, Portfolio-Uebersichten. Begleitet den Strategieprozess, identifiziert Schwachstellen. Enthaelt Methoden-Module inkl. Balanced Scorecard (BSC): Strategy Map, KPI-Kaskadierung und Steuerungslogik.

### strategie-orchestrator
**5-Phasen-Strategieprozess (Scan, Diagnose, Choose, Execute, Track)**

Prueft vorab Datenbasis und Entscheidungsrahmen, routet auf vorhandene Controlling-Skills. Einsatz bei Entscheidungsvorlagen, Strategie- und Investitionsfragen im Maschinenvision-Umfeld.

### bu-wachstums-sparring
**Interner Beratungs-Sparringspartner fuer BU-Management**

Fragen zu Wachstum und Skalierung: Umsatzhebel, Win Rate, Retention, Installed Base, angrenzende Geschaeftsmodelle (Service-Abo, Pay-per-Use, Retrofit, Performance-Vertrag, Software-Lizenz). Liefert Hebel-Diagnose, Optionenmatrix und Entscheidungsvorlage.

### prompt-briefing
**Strukturiertes Briefing vor analytischen Controlling-Aufgaben**

Vor Abweichungsanalyse, Management-Kommentar, Forecast, Entscheidungsvorlage: Luecken abfragen, Success Criteria bestaetigen lassen, dann erst ausfuehren.

### controlling-reifegrad-assessment
**Selbstbewertung der Controlling-Reife**

Entlang des Prozessmodells (9 Kernprozesse, Enabling-Prozesse). Liefert HTML-One-Pager und Excel zur Fortschreibung.

### eisenhower-kanban-controlling
**Integriertes Prioritaets- und Workflow-Management**

Kombiniert Eisenhower-Matrix als Task-Filter mit Kanban-Board als Execution-Workflow. Fuer Business Partner Controlling Rollen: Task-Priorisierung, Weekly Planning, Workload Management, Ad-hoc-Requests vs. strategische Arbeit.

---

## Daten & Analytics

### citizen-data-science-co
**Data-Driven Analysis und Forecasting fuer Business Partner Controller**

Variance Analysis, Forecast Modeling, Margin Analytics, Project Profitability Tracking, KPI Driver Analysis, Executive-ready Reporting. Optimiert fuer projektbasiertes B2B-Geschaeft in der industriellen Fertigung.

### universal-data-cleaning
**Daten-Profiling, Bereinigung und Validierung**

Bei jedem rohen/unsauberen Datensatz (Excel, CSV, Export aus D365 etc.), der vor einer Analyse profiliert, bereinigt und validiert werden muss.

### zeitreihen-controlling
**Spezialisierter Analyst fuer Zeitreihenanalyse und -prognose**

Statistisches Methoden-Know-how kombiniert mit Controlling-Praxis. Fuer Auftragseingang, Umsatz, Kosten und KPIs im Zeitverlauf. ARIMA, Holt-Winters, Saisonalitaet, Trendanalyse, Anomalieerkennung.

### ml-forecasting-controlling
**ML-basiertes Forecasting (Prophet, XGBoost, LSTM)**

Fuer Controlling-Zeitreihen mit hoher Komplexitaet: externe Treiber, nichtlineare Muster, mehrere interagierende Einflussfaktoren. Ergaenzung zu zeitreihen-controlling fuer komplexere Faelle.

### crisp-dm-controlling
**Strukturierte CRISP-DM Projektmethodik fuer Controlling-Analytics**

Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment. Deliverables: Problem Statements, Data Inventories, Feature Engineering Plans, Evaluation Reports, Rollout Plans.

### datenreife-check
**Strukturierte Datenreife-Analyse fuer KI- und Digitalisierungsprojekte**

Bewertet Datenquellen, Datenqualitaetsrisiken und Datenluecken systematisch. Output: Datenreife-Score je Quelle, Risikobewertung, priorisierter Massnahmenplan.

### dashboard-mvp-designer
**Vom Entscheidungsbedarf zum MVP Dashboard Spec**

Fuehrt iterativ und gemeinsam mit Stakeholdern von der Entscheidung zum klickbaren HTML-Mockup. Fragt aktiv nach dem produktiven Zielwerkzeug (Excel, Power BI, Tableau, Qlik, Looker). NICHT fuer das reine Befuellen eines fertigen Dashboards.

---

## Python & Code-Generierung

### python-controlling-codegen
**Strukturierte Code-Generierung fuer Python-Analysen im Controlling**

Fuer Analysen auf Basis von Rohdaten (Excel, CSV, SQL). Aktivierung bei: Jupyter, Notebook, Plotly, Analyse generieren, CRM-Daten, Pipeline, Reporting-Automatisierung. Auch bei Uploads von Excel-/CSV-Dateien mit Analyseanfrage.

### python-controlling-finance
**Python Coding Skill fuer Controlling & Finance Use Cases**

Generiert production-ready Jupyter Notebooks (.ipynb) optimiert fuer VS Code. Aktivierung nur bei expliziter Code-Anforderung: Python-Loesung, Notebook erstellen, Analyse-Script, automatisieren.

### sql-query-generator-controlling
**SQL-Queries fuer Controlling-Analysen**

Generiert SQL-Queries basierend auf natuerlichsprachlichen Anfragen. Unterstuetzt SAP-Datenmodelle, Data Warehouses und gaengige ERP-Strukturen. Optimiert fuer analytische Abfragen.

---

## ERP & Automatisierung

### d365-controlling
**D365 Finance (F&O) Workflows fuer Business Partner Controlling**

Datenextraktion (OData, Excel-Export, Keboola-Integration), Kostenstellenberichte & Dimensionsnavigation, Periods Management/Close-Prozess, Projektmodul (Revenue Recognition, EAC, Zeiterfassung). Aktivierung bei: D365, Dynamics 365, F&O, OData, D365 nach Python/Power BI.

### power-automate-controlling
**Power Automate Flows fuer Controlling-Workflows**

Flow-Design, D365 F&O-Integration, SharePoint/Teams-Anbindung, Genehmigungsworkflows, Fehlerbehandlung und Monitoring. Aktivierung bei: Power Automate, Approval Flow, D365 Connector, automatisches Reporting, Budget-Ueberschreitung melden.

---

## KI & Digitalisierung

### ki-usecase-finder
**Internes KI-Beratungstool fuer Business Partner Controlling**

Strukturiert Discovery, Bewertung und Roadmap fuer KI-Use-Cases in Finance, Verwaltung und Vertrieb. Erweitertes 6-Kriterien-Scoring (inkl. Datenreife) und Governance-Kurzcheck (EU AI Act, Bias, Human-in-the-Loop). Output: HTML One-Pager.

### ki-pilot-blueprint
**Vollstaendiges KI-Pilot-Blueprint-Dokument**

Operative Entscheidungsvorlage fuer CFO/COO/Steuerkreis: Zielbild, Scope, KPIs, Rollen, Risiken und Next Steps. Das fehlende Bindeglied zwischen Use-Case-Auswahl und Umsetzung. Output: Professioneller HTML One-Pager.

### stakeholder-impact-analyse
**Strukturierte Stakeholder-Map und Impact-Analyse**

Fuer KI-Rollouts und Controlling-Digitalisierungsprojekte. Klassifiziert Stakeholder nach Einfluss, Interesse und Widerstandspotenzial. Leitet differenzierte Einbindungsstrategien ab. Output: Stakeholder-Matrix + Engagement-Plan.

---

## LinkedIn & Content

### linkedin-content-planner
**LinkedIn Post-Ideen und Content-Planung**

Generiert Post-Ideen und vollstaendige Post-Entwuerfe. Themen: Operatives Controlling, Business Partner Controlling, Digitalisierung, Automatisierung, Prozessmanagement, Zeitreihenanalyse, KI/ML/LLMs.

### linkedin-post-writer
**Ghostwriter fuer LinkedIn-Posts (V1)**

Transformiert rohe Stichworte, Erfahrungen, Thesen in druckfertige LinkedIn-Posts. Persona: Senior Controller / Business Partner in der Maschinenvision-Industrie.

### linkedin-post-writer-v2
**Ghostwriter fuer LinkedIn-Posts (V2 - erweitert)**

Erweiterte Hook-Bibliothek, Verbotsliste und Zahlen-Guardrail. Bevorzugt gegenueber V1 wenn aus Rohmaterial ein Post entstehen soll.

### linkedin-post-checker
**LinkedIn-Post-Review mit 7 Qualitaetskriterien (V1)**

Ampel-Bewertung pro Kriterium, identifiziert kritischsten Schwachpunkt, gibt konkrete Ueberarbeitungsvorschlaege. Optimiert fuer sachliche, erfahrene Controller-Persona.

### linkedin-post-checker-v2
**LinkedIn-Post-Review (V2 - erweitert)**

Erweiterte Hook-Pruefung mit Zielgruppen-Ansprache, Verbotsliste, Zahlen-Guardrail. Bevorzugt gegenueber V1 wenn Hooks geprueft werden.

---

## Prozesse & Dokumentation

### prozess-dokumentation
**IST-Dokumentation und Visualisierung von Geschaeftsprozessen**

Aus beliebigen Eingabeformaten (Word, PDF, PowerPoint, Markdown, Freitext). Diagramm in Mermaid Flowchart, Swimlane, ePK oder BPMN-Notation. Erzeugt immer IST-Befund mit SOLL-Entwurf.

### workshop-dokumentation
**Dokumentation interner Workshops**

Fuehrt Handyfotos (Karteikarten, Wand, Flipchart), Teams-Transkript und Word-Notizen zu einer bereinigten, gegliederten Dokumentation zusammen. Liefert Protokoll, Kachel-Visualisierung und Massnahmenliste (Wer macht was bis wann).

### vier-c-arbeitsassistent
**Arbeitsassistent im 4-C-Framework**

Koordination (E-Mail/Kalender), Erstellung (CFO-Mails, Decks), Klarheit (Research, Vertragspruefung), Coaching (Gespraechssimulation).

---

## Wissensmanagement & Session

### obsidian-knowledge-bridge
**Bidirektionale Wissensbruecke zwischen Claude Code und Obsidian Vault**

Strukturiertes Lesen, Erstellen und Verknuepfen von Notizen. Fokus auf Controlling-Wissensmanagement, Skill-Dokumentation und Session-Wissen.

### screenshot-extractor
**Extraktion und Strukturierung von Screenshot-Inhalten**

Erkennt automatisch Screenshot-Typ (Newsletter, Dashboard/KPI, LinkedIn, Folie, ERP/BI-Tabelle). Liefert strukturierte Markdown-Zusammenfassung + Controlling-relevante Key Takeaways.

### screenshot-to-notion
**Screenshot-Extraktion mit automatischer Notion-Ablage**

Erweitert den screenshot-extractor um automatische Ablage als strukturierte Unterseite im Notion-Screenshot-Archiv.

### instinct-tracker
**Analyse von Claude-Sessions auf wiederkehrende Interaktionsmuster**

Schreibt strukturierte Obsidian-Notizen mit Praeferenzen und Arbeitsweisen. Erzeugt persistentes Session-Gedaechtnis fuer kuenftige Sessions.

### session-debrief
**Cowork-nativer Session-Debrief**

Analysiert abgeschlossene Arbeits-Sessions, extrahiert strukturierte Erkenntnisse, schreibt autonom in Obsidian Vault UND Notion. Dual: Obsidian fuer PKM und Muster-Tracking, Notion fuer operative Ablage.

### project-memory-management
**Pflege und Optimierung von CLAUDE.md-Dateien**

Audits (Veraltung, Redundanz, Widersprueche), Aktualisierung nach Arbeitssessions, kompaktes und relevantes Projekt-Gedaechtnis.

---

## Qualitaetssicherung & Methodik

### harness-check-skills
**Skill-Qualitaetspruefung gegen 24 Fragen der Harness-Logik**

Kontext, Pruefung, Leitplanken. Liefert Ampel plus Massnahmenplan. Bei Skill-Audit, Review oder Qualitaetscheck nutzen.

### fable-mode
**Gruendlicher Arbeitsmodus fuer komplexe mehrstufige Aufgaben**

Aktivierung bei: Features ueber mehrere Dateien, Architektur-Entscheidungen, Debugging, Refactorings, riskanten oder zustandsaendernden Operationen.

### kaizen-kaizen
**Iterative Verbesserungen und Anti-Over-Engineering**

Anwenden bei Code-Implementierung und Refactoring, System-Architektur und -Design, Prozess- und Workflow-Verbesserungen sowie Fehlerbehandlung und Validierung.

---

## Tools & System (Anthropic Standard-Skills)

Diese Skills sind von Anthropic bereitgestellte Standard-Tools, die mein Setup ergaenzen:

| Skill | Beschreibung |
|-------|-------------|
| **docs** | Living Docs erstellen und bearbeiten in Claude |
| **docx** | Microsoft Word Dokumente (.docx, .dotx) erstellen, lesen, bearbeiten |
| **xlsx** | Excel-Dateien (.xlsx, .xlsm, .csv, .tsv) erstellen und bearbeiten |
| **pptx** | PowerPoint-Praesentationen (.pptx, .potx) erstellen und bearbeiten |
| **pdf** | PDF-Dateien lesen, erstellen, zusammenfuegen, teilen, OCR |
| **deep-research** | Multi-Source-Research mit Synthese zu umfassendem Bericht |
| **google-workspace** | Google Drive, Docs, Sheets, Slides Integration |
| **morning** | Persoenliches Morning-Briefing als HTML-Artifact |
| **doc-coauthoring** | Strukturierter Workflow fuer Co-Authoring von Dokumentation |
| **web-artifacts-builder** | Komplexe HTML-Artifacts mit React, Tailwind, shadcn/ui |
| **skill-creator** | Skills erstellen, modifizieren, messen und optimieren |
| **theme-factory** | Styling von Artifacts mit 10 vordefinierten Themes |
| **mcp-builder** | MCP-Server erstellen fuer externe API-Integrationen |
| **internal-comms** | Interne Kommunikation (Status Reports, Leadership Updates) |
| **canvas-design** | Visuelle Designs und Poster als .png/.pdf |
| **brand-guidelines** | Anthropic Brand Colors und Typografie |
| **algorithmic-art** | Generative Kunst mit p5.js |
| **slack-gif-creator** | Animierte GIFs fuer Slack |
| **chrome-browser** | Chrome Browser Extension (Claude in Chrome) |
| **built-in-browser** | Built-in Browser Pane in der Claude Desktop App |
| **computer-use** | Desktop-Steuerung ueber Claude Desktop App |
| **import-memory** | Memory-Import aus anderen KI-Assistenten |

---

## Skill-Architektur: Routing und Abgrenzung

Viele Skills haben explizite Routing-Regeln, um Ueberlappungen zu vermeiden:

| Thema | Richtiger Skill | NICHT verwenden |
|-------|----------------|-----------------|
| Bestehendes Geschaeft - Umsatzplan | revenue-driver-model | neugeschaefts-treiberbaum |
| Neue Geschaeftsidee - Umsatz | neugeschaefts-treiberbaum | revenue-driver-model |
| P&L-Kaskade CM1->EBITDA | db-szenario-skill-eval-v3 | kostenstruktur-analyse |
| Ist vs. Plan Abweichung | variance-master, pvm-controlling | sensitivitaetsanalyse-controlling |
| Sensitivitaet / What-If | sensitivitaetsanalyse-controlling | variance-master |
| Monte-Carlo / Szenarien | db-szenario-skill-eval-v3 | sensitivitaetsanalyse-controlling |
| Kostenstruktur / DB-Stufen | kostenstruktur-analyse | kostenfresser-scan |
| Verlustquellen / Waste | kostenfresser-scan | kostenstruktur-analyse |
| Massnahmen-Tracking | kostenmassnahmen-controlling | kostenfresser-scan |
| Working Capital / CCC | cash-conversion-analyse | liquiditaetsplanung |
| Cashflow-Planung | liquiditaetsplanung | cash-conversion-analyse |
| SaaS-Kohorten | cohort-analysis-saas-controlling | unit-economics-analysis |
| Unit Economics B2B | unit-economics-analysis | cohort-analysis-saas-controlling |
| Pricing / Value Gap | value-wedge-pricing | bu-wachstums-sparring |
| Kundenwert / Segmentierung | kundenwert-scanner | bu-wachstums-sparring |
| Dashboard konzipieren | dashboard-mvp-designer | bu-controlling-dashboard |
| Dashboard befuellen | bu-controlling-dashboard | dashboard-mvp-designer |
| Einfache Zeitreihen | zeitreihen-controlling | ml-forecasting-controlling |
| ML-basierte Prognose | ml-forecasting-controlling | zeitreihen-controlling |
| LinkedIn Post schreiben | linkedin-post-writer-v2 | linkedin-post-checker-v2 |
| LinkedIn Post pruefen | linkedin-post-checker-v2 | linkedin-post-writer-v2 |

---

*Erstellt mit Claude Code | Business Partner Controlling - Maschinenvision / Bildverarbeitung*
