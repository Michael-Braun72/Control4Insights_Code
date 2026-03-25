# Übungen: Microsoft 365 Copilot im Controlling

## Voraussetzung
Microsoft 365 Copilot-Lizenz aktiv. Getestet in: Excel, Word, Outlook, Teams.

---

## Übung 1 – Copilot in Excel: Daten analysieren

**Datei:** Beispieldaten_AB_Test.csv (liegt im selben Ordner)

**Schritt 1:** CSV in Excel öffnen → Als Tabelle formatieren (Strg+T)

**Schritt 2:** Copilot öffnen (Home-Menü → Copilot-Symbol)

**Prompts ausprobieren:**
```
Zeige mir eine Zusammenfassung dieser Daten.
```
```
Welche Szenarien haben die höchste Conversion Rate?
```
```
Erstelle ein Balkendiagramm: Durchschnittliche Revenue nach Scenario und Group.
```
```
Welche Zeilen haben die höchsten Kosten pro Unit? Zeige Top 10.
```

**Ziel:** Erkenntnisse in 2 Minuten – ohne eine Formel selbst zu schreiben.

---

## Übung 2 – Copilot in Excel: Formeln generieren

**Aufgabe:** Berechne neue Kennzahlen direkt per Spracheingabe.

**Prompts:**
```
Füge eine neue Spalte "Profit" hinzu: revenue minus costs.
```
```
Berechne den Profit-Margin in Prozent und füge ihn als Spalte hinzu.
```
```
Markiere alle Zeilen rot, bei denen cost_per_unit über 20 liegt.
```

**Diskussion:** Welche Formeln hat Copilot generiert? Stimmen sie rechnerisch?

---

## Übung 3 – Copilot in Word: Bericht überarbeiten

**Aufgabe:** Einen bestehenden Controlling-Text per Copilot überarbeiten.

**Schritt 1:** Word öffnen → Neues Dokument → folgenden Text einfügen:

> *"Im dritten Quartal lag der Umsatz bei 47 Millionen Euro, was unter dem geplanten Wert von 50 Millionen Euro lag. Die Differenz von 3 Millionen Euro ist auf verschiedene Faktoren zurückzuführen, unter anderem auf Verschiebungen bei einigen größeren Projekten. Die Situation wird im vierten Quartal beobachtet."*

**Schritt 2:** Copilot → Prompt:
```
Überarbeite diesen Text für ein CFO-Reporting. Sachlich, präzise, max. 3 Sätze,
keine Passivkonstruktionen, mit konkreter Handlungsempfehlung.
```

**Diskussion:** Vergleich Original vs. Copilot-Version. Was ist besser, was fehlt?

---

## Übung 4 – Copilot in Outlook: E-Mail-Entwurf

**Situation:** Du musst dem BU-Leiter erklären, warum der Umsatz 6% unter Plan liegt.

**Schritt 1:** Neue E-Mail in Outlook → Copilot → "E-Mail verfassen"

**Prompt:**
```
Schreibe eine E-Mail an den BU-Leiter.
Thema: Umsatzabweichung Q3 (-6% vs. Plan, -3 Mio. €)
Ursache: 2 Projektverschiebungen (je 1,5 Mio. €)
Ton: Sachlich, lösungsorientiert, Handlungsempfehlung für Q4 enthalten.
```

**Bewertung:** Würdest du die E-Mail so abschicken? Was würdest du ändern?

---

## Copilot vs. Claude – Schnellvergleich

| Aspekt | Copilot | Claude |
|---|---|---|
| Integration | Direkt in M365 | Browser / Cowork |
| Excel-Formeln | Sehr stark (nativ) | Gut (als Code) |
| Textqualität | Gut | Sehr gut |
| Datenanalyse | Mittel | Sehr gut (mit Python) |
| Datenschutz | Enterprise-Tier | Enterprise-Tier |

---

*Schulungsunterlage | KI im Controlling | März 2026*
