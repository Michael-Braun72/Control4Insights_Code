# Übungen: n8n Workflow-Automatisierung für Controller

## Ziel dieser Übungen
Erste eigene Workflows bauen – ohne Code, rein visuell.
Zeitaufwand: je 15-30 Minuten.

---

## Vorbereitung

1. n8n lokal starten (siehe n8n_Local_Quickstart.md)
2. Browser: http://localhost:5678
3. "New Workflow" klicken

---

## Übung 1 – Erster Workflow: HTTP-Request → Daten anzeigen

**Lernziel:** Wie funktioniert ein Node? Wie verbinde ich zwei Nodes?

**Schritt 1:** "+ Add node" → "HTTP Request"
- Method: GET
- URL: `https://api.exchangerate-api.com/v4/latest/EUR`
- Ausführen: "Execute node"

**Schritt 2:** Output anschauen: JSON mit aktuellen FX-Kursen.

**Schritt 3:** "+ Add node" → "Set" (oder "Edit Fields")
- Extrahiere: `USD`, `GBP`, `CHF`, `JPY`

**Ergebnis:** Ein einfacher FX-Rate-Abruf in 5 Minuten.

**Anwendung:** Dieser Workflow kann täglich automatisch ausgeführt werden
und die Kurse in eine Excel/CSV schreiben.

---

## Übung 2 – Trigger: Workflow automatisch starten

**Lernziel:** Workflows zeitgesteuert ausführen.

**Schritt 1:** Ersten Node durch "Schedule Trigger" ersetzen
- Trigger: "Every Day" um 07:00 Uhr

**Schritt 2:** HTTP Request Node wie in Übung 1 verbinden.

**Schritt 3:** "+ Add node" → "Write Binary File" oder "Spreadsheet File"
- Werte in CSV speichern

**Ergebnis:** Täglich automatisch aktuelle FX-Kurse in einer CSV-Datei.

---

## Übung 3 – KI-Integration: Claude analysiert Daten

**Voraussetzung:** Claude API Key (über anthropic.com/api)

**Workflow-Idee:**
```
[Schedule: Jeden Montag 08:00]
     ↓
[Read File: Monatsbericht.csv]
     ↓
[Claude API: "Analysiere diese Daten, schreibe Kommentar"]
     ↓
[Gmail / Outlook: Kommentar per E-Mail senden]
```

**Schritt 1:** Schedule Trigger → Montag 08:00
**Schritt 2:** "Read Binary File" Node → Pfad zur CSV
**Schritt 3:** "HTTP Request" Node (Claude API)
- URL: `https://api.anthropic.com/v1/messages`
- Method: POST
- Authentication: Header Auth → `x-api-key: [DEIN_API_KEY]`
- Body: JSON mit `model: "claude-opus-4-6"`, Prompt, Daten

**Schritt 4:** Gmail/SMTP Node → E-Mail mit Ergebnis

---

## Übung 4 – Schwellwert-Alert

**Use Case:** Wenn KPI unter Schwellwert → Slack-Nachricht + Draft-Kommentar

**Workflow:**
```
[Schedule: Täglich 09:00]
     ↓
[HTTP Request: KPI aus BI-System oder CSV lesen]
     ↓
[IF Node: KPI < Schwellwert?]
     ↓ JA
[Claude: Kommentar-Entwurf generieren]
     ↓
[Slack / E-Mail: Alert senden]
```

**IF Node konfigurieren:**
- Value 1: `{{ $json.ebitda_margin }}`
- Operator: "smaller than"
- Value 2: `0.05` (= 5% EBITDA-Marge)

---

## Was n8n kann vs. was es nicht kann

| Kann n8n | Kann n8n NICHT |
|---|---|
| Zeitgesteuerte Ausführung | Eigene KI-Modelle trainieren |
| APIs verbinden (REST/JSON) | Komplexe Datenbanktransaktionen |
| Dateien lesen/schreiben | Echtzeitverarbeitung großer Datenmenge |
| E-Mails/Slack senden | SAP-direkt-Integration (ohne API) |
| Claude/ChatGPT API nutzen | Entscheidungen verantworten |

---

## Nächste Schritte

- n8n Cloud: https://n8n.io (kostenlose Testversion, dann ab ~20 €/Monat)
- Templates: https://n8n.io/workflows (fertige Workflow-Vorlagen)
- Community: https://community.n8n.io

---

*Schulungsunterlage | KI im Controlling | März 2026*
