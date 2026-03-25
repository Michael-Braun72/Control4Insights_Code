# Examples – Übungsmaterialien | KI im Controlling

Praxisübungen und Beispieldaten für die Schulung.
Jeder Ordner entspricht einem Tool-Block aus der Schulung.

---

## Übersicht

| Ordner | Tool | Dateien | Dauer |
|---|---|---|---|
| 1_Prompting | Prompt-Kompetenz | Prompt_Uebungen.md, Prompt_Vorlagen_Controlling.md | 20 min |
| 2_Copilot | Microsoft 365 Copilot | Copilot_Uebungen.md, Beispieldaten_AB_Test.csv | 20 min |
| 3_Claude | Claude (claude.ai) | Claude_Analyse_Uebungen.md, Beispieldaten_AB_Test.csv | 25 min |
| 4_ChatGPT | ChatGPT Plus | ChatGPT_Uebungen.md | 20 min |
| 5_Perplexity | Perplexity Pro | Perplexity_Uebungen.md | 15 min |
| 6_n8n | n8n (lokal oder Cloud) | n8n_Local_Quickstart.md, n8n_Workflow_Uebungen.md | 30 min |

---

## Beispieldaten: Beispieldaten_AB_Test.csv

500 synthetische Datensätze aus einem A/B-Test-Szenario.
Drei Szenarien: Marketing, Pricing, Prozessoptimierung.
Zwei Gruppen: A (Kontrollgruppe) und B (Testgruppe).

**Spalten:**
- `scenario` – Marketing / Pricing / Prozess
- `group` – A / B
- `units` – Einheiten / Besucher
- `conversions` – Konversionen
- `revenue` – Umsatz in €
- `costs` – Kosten in €
- `cycle_time_days` – Durchlaufzeit (nur Prozess)
- `errors` – Fehler (nur Prozess)
- `conversion_rate` – Konversionsrate
- `cost_per_unit` – Kosten pro Einheit

**Verwendung:** In Claude (Upload), Excel/Copilot, Python/Jupyter.

---

## Empfohlene Reihenfolge

1. **1_Prompting** – Basis für alle anderen Tools
2. **3_Claude** – Kernwerkzeug für Analyse
3. **2_Copilot** – Wenn M365-Lizenz vorhanden
4. **4_ChatGPT** – Für Custom GPTs & Deep Research
5. **5_Perplexity** – Für Marktrecherche
6. **6_n8n** – Für Automatisierungs-Interessierte

---

*Version 1.0 | KI im Controlling | März 2026*
