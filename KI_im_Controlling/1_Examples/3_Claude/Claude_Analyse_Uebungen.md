# Übungen: Claude als Controlling-Assistent

## Setup
1. claude.ai im Browser öffnen (oder Claude Desktop / Cowork)
2. Kostenloses Konto reicht für diese Übungen
3. Claude Pro empfohlen für längere Analysen und Datei-Upload

---

## Übung 1 – Variance Commentary (5 Minuten)

**Kontext direkt eingeben:**

```
Du bist ein erfahrener Controller in der Maschinenvision-Branche.
Monatsbericht Oktober:
- Umsatz: Plan 18 Mio. €, Ist 16,8 Mio. € (-6,7%)
- Materialkosten: Plan 7,2 Mio. €, Ist 8,1 Mio. € (+12,5%)
- PerEx: Plan 4,5 Mio. €, Ist 4,5 Mio. € (on plan)
- EBITDA: Plan 2,8 Mio. €, Ist 1,3 Mio. € (-53,6%)
Hintergründe: Umsatz: Projektverschiebung Kunde A (1,2 Mio. €).
Materialkosten: Kupferpreisanstieg +18% + Lieferantenausfall.
Erstelle:
1. Executive Summary (3 Sätze, CFO-ready)
2. Kommentierungstabelle je KPI (Abweichung | Ursache | Maßnahme)
3. Risikobewertung für den Rest des Quartals (Ampel: Rot/Gelb/Grün)
```

**Bewertung:** Rechnerisch prüfen! EBITDA-Berechnung manuell gegenchecken.

---

## Übung 2 – CSV-Daten analysieren (mit Datei-Upload)

**Voraussetzung:** Claude Pro (Datei-Upload)

**Schritt 1:** Beispieldaten_AB_Test.csv in Claude hochladen

**Schritt 2:** Prompts ausprobieren:
```
Analysiere diese Daten. Was fällt dir auf?
```
```
Vergleiche die Conversion Rate zwischen Gruppe A und Gruppe B
für das Marketing-Szenario. Gibt es einen signifikanten Unterschied?
```
```
Welches der drei Szenarien (Marketing, Pricing, Prozess) zeigt
die beste Performance? Definiere "beste Performance" selbst
und begründe deine Wahl.
```
```
Erstelle eine Python-Funktion, die aus diesem Datensatz
einen One-Page-Bericht als HTML generiert.
```

**Erwartete Erkenntnisse:**
- Marketing: Gruppe B hat höhere Revenue, aber auch höhere Costs
- Pricing: Gruppe B zeigt höhere Conversion Rates
- Prozess: Gruppe A hat längere Cycle Times aber weniger Errors

---

## Übung 3 – Python-Code generieren (15 Minuten)

**Prompt für Python-Analyse:**

```
Erstelle einen Python-Code (Jupyter Notebook-Stil) für folgende Aufgabe:

Ich habe eine CSV-Datei mit folgenden Spalten:
scenario, group, units, conversions, revenue, costs,
cycle_time_days, errors, conversion_rate, cost_per_unit

Aufgabe:
1. Daten laden und bereinigen (fehlende Werte behandeln)
2. Für jedes Szenario (Marketing, Pricing, Prozess):
   - Durchschnittswerte je Gruppe A vs. B berechnen
   - Statistischen Signifikanztest (t-Test) durchführen
3. Visualisierung: Grouped Bar Chart (Matplotlib oder Plotly)
4. Executive Summary: Welche Gruppe "gewinnt" je Szenario?

Anforderungen:
- Kommentierter Code auf Englisch
- Error Handling für fehlende Spalten
- Output als druckbares HTML speichern
```

**Hinweis:** Code immer in einer Testumgebung ausführen, nie direkt auf Produktivdaten.

---

## Übung 4 – Claude als Sparring-Partner

**Scenario:** Du planst eine Preiserhöhung von 5% für das nächste Jahr.

**Prompt:**
```
Ich bin Controller in der Maschinenvision-Branche und plane
eine Preiserhöhung von 5% für 2026. Spiele den advocatus diaboli:
Welche 5 Gegenargumente wird mein CFO bringen?
Und welche 3 datenbasierten Argumente sollte ich vorbereiten?
Format: Pro/Contra-Tabelle + Empfehlung für die Präsentation.
```

---

## Übung 5 – KI scheitert bewusst testen

**Prompt mit Absicht fehlerhaft:**
```
Wenn Umsatz 50 Mio. € ist und Kosten 55 Mio. €,
berechne den EBITDA-Prozentsatz vom Umsatz
unter Berücksichtigung von 3% Abschreibungen
und 12% Steuern auf den Vorsteuergewinn.
```

→ Ergebnis kritisch prüfen: Hat Claude den Rechenschritt korrekt ausgeführt?
→ Lesson: Bei komplexen abhängigen Berechnungen immer manuell gegenchecken.

---

*Schulungsunterlage | KI im Controlling | März 2026*
