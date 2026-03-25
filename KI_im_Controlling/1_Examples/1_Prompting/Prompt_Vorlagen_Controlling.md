# Prompt-Vorlagenbibliothek für Controller

Direkt einsetzbare Prompts – einfach [WERTE EINFÜGEN] ersetzen und abschicken.

---

## KATEGORIE 1: Monatsberichts-Kommentare

### Variance Commentary (Standard)
```
Du bist ein erfahrener Controller in der [BRANCHE]-Branche.
Umsatz [PERIODE]: Plan [PLAN] Mio. €, Ist [IST] Mio. €, Abweichung [ABWEICHUNG] Mio. € ([PROZENT]%).
Hauptursachen: [URSACHE 1], [URSACHE 2].
Schreibe einen Management-Kommentar: max. 4 Sätze, sachlich, mit Ausblick [NÄCHSTE PERIODE].
Stil: CFO-Reporting, keine Weichspüler-Formulierungen.
```

### Kostenabweichung erklären
```
Du bist Business Partner Controlling.
Kostenposition: [KOSTENART]
Plan: [PLAN] Mio. €, Ist: [IST] Mio. €, Abweichung: [DELTA] Mio. € ([PROZENT]%)
Mögliche Ursachen: [URSACHEN]
Erstelle: 1) Kommentar für CFO (3 Sätze), 2) To-Do-Liste für Ursachenanalyse (5 Punkte)
```

---

## KATEGORIE 2: Analyse-Prompts

### Sensitivitätsanalyse
```
Du bist Controller. Analysiere folgende Szenario-Auswirkungen auf das EBITDA:
Ausgangsbasis: Umsatz [X] Mio. €, Materialquote [X]%, PerEx [X] Mio. €, EBITDA [X] Mio. €
Szenarien:
- Materialkosten +[X]%
- Volumen -[X]%
- Personalkosten +[X]%
Erstelle eine Tabelle: Szenario | EBITDA-Impact (€) | EBITDA-Impact (%) | Maßnahme
Hinweis: Alle Berechnungen zeigen, damit ich prüfen kann.
```

### Plan-Ist-Analyse strukturieren
```
Ich gebe dir folgende Daten aus dem Monatsabschluss [PERIODE]:
[DATEN EINFÜGEN – z.B. Tabelle kopieren]
Aufgabe:
1. Identifiziere die Top-3-Abweichungen nach absolutem Wert
2. Schlage je Abweichung eine Ursachenhypothese vor
3. Empfehle Gesprächspunkte für das nächste BU-Review
Format: Strukturierte Tabelle + kurze Executive Summary (3 Sätze)
```

---

## KATEGORIE 3: Dokumente & Kommunikation

### Management Summary erstellen
```
Du bist erfahrener Controller. Erstelle eine Management Summary für [THEMA/PERIODE].
Inhalt-Stichpunkte: [STICHPUNKTE EINFÜGEN]
Struktur: 1) Headline-Botschaft (1 Satz), 2) Lage (2-3 Sätze), 3) Risiken (1-2 Punkte), 4) Empfehlung (1 Satz)
Ton: Direkt, faktenbasiert, CFO-ready. Keine Passivkonstruktionen.
```

### E-Mail an Stakeholder
```
Schreibe eine professionelle E-Mail an [EMPFÄNGER – z.B. BU-Leiter].
Thema: [THEMA]
Kernaussage: [BOTSCHAFT]
Benötigte Reaktion: [ERWARTETE AKTION]
Ton: Sachlich, kollegial, lösungsorientiert. Max. 150 Wörter.
```

---

## KATEGORIE 4: Python & Excel

### Python-Code für Datenanalyse
```
Schreibe Python-Code (Jupyter Notebook-Style) für folgende Aufgabe:
Datei: [DATEINAME.csv / .xlsx]
Spalten: [SPALTENNAME 1], [SPALTENNAME 2], ...
Ziel: [BESCHREIBUNG – z.B. "Umsatz nach Region gruppieren, monatliche Trend-Visualisierung"]
Bibliotheken: pandas, matplotlib/plotly
Anforderungen: Kommentierter Code, Error Handling, Ergebnis als Chart speichern.
```

### Excel-Formel generieren
```
Ich arbeite in Excel. Erkläre mir folgende Formel und optimiere sie falls möglich:
[FORMEL EINFÜGEN]
Kontext: [WAS DIE FORMEL MACHEN SOLL]
Falls eine bessere Alternative existiert: zeige sie direkt.
```

---

*Prompt-Bibliothek | KI im Controlling | Version 1.0 | März 2026*
*Tipp: Diese Datei in Obsidian/OneNote ablegen und laufend erweitern.*
