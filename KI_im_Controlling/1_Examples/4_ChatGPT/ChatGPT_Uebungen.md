# Übungen: ChatGPT – Custom GPTs & Deep Research

## Wann ChatGPT, wann Claude?

| Aufgabe | Empfehlung |
|---|---|
| Komplexe Analyse, langer Kontext | Claude |
| Persistenter Assistent mit fester Konfiguration | ChatGPT (Custom GPT) |
| Tiefenrecherche mit Synthese vieler Quellen | ChatGPT (Deep Research) |
| Eigene Wissensbasis abfragen | NotebookLM |

---

## Übung 1 – Custom GPT: Eigenen Controlling-Assistenten bauen

**Voraussetzung:** ChatGPT Plus (ca. 22 €/Monat)

**Schritt 1:** chatgpt.com → "Explore GPTs" → "Create"

**Schritt 2:** Im GPT Builder folgende Konfiguration eingeben:

**Name:** Controlling-Assistent [Firmenname]

**Instructions (kopieren und anpassen):**
```
Du bist ein erfahrener Controller in der [BRANCHE]-Industrie.

DEIN KONTEXT:
- Berichtsstruktur: Monatsbericht mit KPI-Cockpit + Variance Commentary
- Stil: Sachlich, direkt, CFO-ready – keine Weichspüler-Formulierungen
- Zahlenformat: Tausendertrennzeichen mit Punkt, Dezimal mit Komma (deutsches Format)
- Währung: Euro (Mio. €)

IMMER:
- Abweichungen in absolut und relativ angeben
- Ursache-Wirkung-Empfehlung-Struktur nutzen
- Rechenergebnisse explizit zeigen, damit ich prüfen kann

NIE:
- Echte Firmennamen oder Kundendaten in Beispielen verwenden
- Ungesicherte Annahmen als Fakten präsentieren
```

**Schritt 3:** Teste deinen Custom GPT mit dem Variance Commentary aus Übung 1_Prompting.

**Beobachtung:** Wie unterscheidet sich das Ergebnis vom gleichen Prompt in Standard-ChatGPT?

---

## Übung 2 – Custom GPT: Wissen hochladen

**Aufgabe:** Lade ein internes Dokument als Wissensquelle hoch.

**Beispieldokument (selbst erstellen, 1 Seite):**
- Interne Planungsprämissen für 2026 (anonymisiert)
- Beispiel: "FX-Kurs USD/EUR: 1,08 | Materialpreisindex: +3% | Volumenwachstum: +5%"

**Schritt 1:** Custom GPT Builder → "Knowledge" → Dokument hochladen

**Schritt 2:** Testen:
```
Welche FX-Annahmen gelten für unsere 2026-Planung?
```
```
Wie viel Umsatz würden wir bei 5% Volumenwachstum gegenüber
dem Vorjahreswert von 100 Mio. € erreichen?
```

**Datenschutz-Hinweis:** Nur anonymisierte oder nicht-vertrauliche Dokumente hochladen!

---

## Übung 3 – Deep Research

**Voraussetzung:** ChatGPT Plus → "Deep Research" aktivieren

**Szenario:** Vorbereitung auf ein Strategiemeeting zum Thema Maschinenvision-Markt 2026.

**Prompt für Deep Research:**
```
Erstelle eine strukturierte Marktanalyse für die Maschinenvision-Industrie 2025/2026.
Fokus:
1. Marktgröße und Wachstumsraten (global + DACH)
2. Top-3-Wachstumstreiber (mit konkreten Zahlen und Quellen)
3. Technologische Trends (KI-Integration, Edge Computing)
4. Regulatorische Entwicklungen relevant für europäische Hersteller
5. Competitive Landscape: 3-4 relevante Player
Format: Executive Summary (1 Seite) + Detailkapitel + Quellenverzeichnis
```

**Hinweis:** Deep Research dauert 5-10 Minuten. Ergebnis immer auf Quellenqualität prüfen!

**Vergleich mit Perplexity:**
- Deep Research: Tiefere Synthese, längere Antwort
- Perplexity: Schneller, jeder Satz mit Quellenlink

---

## Übung 4 – System Prompt vs. User Prompt

**Experiment:** Gleiche Frage, unterschiedliche Systemkonfiguration.

**Test A (Standard ChatGPT):**
```
Was sind die wichtigsten KPIs für einen Controller in der Maschinenvision?
```

**Test B (Custom GPT mit Kontext):**
Gleiche Frage – aber im konfigurierten Custom GPT.

**Beobachtung:** Qualität, Relevanz, Format vergleichen.

---

*Schulungsunterlage | KI im Controlling | März 2026*
