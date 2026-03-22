# n8n Schulungs-Workflow: Daten-Pipeline → E-Mail Report

## Uebersicht

Typische Controlling-Daten-Pipeline in n8n:

```
Manual Trigger → Demo-Daten → Transformation → HTML-Report → E-Mail
```

**Zielgruppe:** Controller, die n8n kennenlernen
**Dauer:** ca. 45-60 Minuten
**Vorkenntnisse:** Plan-Ist-Vergleich, keine Programmierkenntnisse noetig

---

## Import in n8n

1. n8n oeffnen: `http://localhost:5678`
2. Menu → **Import from File**
3. Datei: `Schulung_Daten_Pipeline_Workflow.json`

---

## Workflow-Nodes

| Node | Funktion | Lernpunkt |
|------|----------|-----------|
| 1. Manual Trigger | Startet Workflow per Klick | In Produktion: Schedule Trigger |
| 2. Demo-Daten | Simuliert D365-GuV-Export | Typische Fallstricke: Prozentzeilen, Kostenvorzeichen |
| 3. Transformation | Bereinigung + Abweichungsberechnung | Vorzeichenkonvention, Ampelbewertung |
| 4. HTML-Report | Management-tauglicher Report | Executive Summary, Formatierung, Farbcodierung |
| 5. E-Mail | Versand per SMTP | Credentials einrichten, Verteiler |

---

## Schulungsablauf

| Zeit | Thema |
|------|-------|
| 10 Min | n8n-Oberflaeche, Workflow importieren |
| 10 Min | Datenquelle und D365-Fallstricke |
| 15 Min | Transformationslogik live durchgehen |
| 10 Min | Report-Generierung und Formatierung |
| 5 Min | E-Mail-Versand konfigurieren |
| 10 Min | Workflow ausfuehren, Ergebnis pruefen, Q&A |

---

## Typische Fehlerquellen

| Fehler | Loesung |
|--------|---------|
| Prozentzeilen in Summen | Immer nach Typ filtern vor Aggregation |
| Kostenvorzeichen falsch | `cost_effect = -(actual - plan)` |
| Deutsche Zahlenformate | `Intl.NumberFormat('de-DE')` verwenden |
| E-Mail kommt nicht an | SMTP-Credentials pruefen |

---

## Erweiterungsideen

- Schedule Trigger (automatisch jeden Montag 8:00)
- Error Handling mit Slack-Alert
- KI-Kommentierung via OpenAI Node
- PDF-Anhang statt Inline-HTML
