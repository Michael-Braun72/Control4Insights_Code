# Übungen: Prompt-Kompetenz für Controller

## Lernziel
Prompts systematisch von vage → professionell entwickeln. Jede Übung dauert ca. 5 Minuten.

---

## Übung 1 – Variance Commentary

**Ausgangssituation:**
> Umsatz Q3: Plan 50 Mio. €, Ist 47 Mio. €, Abweichung -3 Mio. € (-6%)
> Hauptursache: Zwei Großprojekte wurden auf Q4 verschoben.

**Schritt 1 – Vager Prompt (ausprobieren):**
```
Schreibe einen Kommentar zur Umsatzabweichung.
```
→ Ergebnis bewerten: Verwendbar? Was fehlt?

**Schritt 2 – Mit Kontext:**
```
Du bist Controller. Umsatz Q3: Plan 50 Mio. €, Ist 47 Mio. €.
Schreibe einen Kommentar für den CFO.
```
→ Ergebnis bewerten: Besser? Was fehlt noch?

**Schritt 3 – Vollständiger Prompt:**
```
Du bist ein erfahrener Controller in der Maschinenvision-Branche.
Umsatz Q3: Plan 50 Mio. €, Ist 47 Mio. €, Abweichung -3 Mio. € (-6%).
Hauptursachen: Projektverschiebungen bei 2 Großkunden (je ca. 1,5 Mio. €).
Schreibe einen Management-Kommentar: max. 4 Sätze, sachlich, mit Ausblick Q4.
```
→ Ergebnis verwenden.

**Diskussion:** Welcher Schritt hat die größte Verbesserung gebracht? Warum?

---

## Übung 2 – Kostentreiber erklären

**Ausgangssituation:**
> Materialkosten im Oktober: Plan 8 Mio. €, Ist 9,2 Mio. € (+15%)
> Hintergrund: Rohstoffpreise gestiegen, ein Lieferant ausgefallen.

**Ihr Prompt (selbst formulieren):**
- Rolle definieren
- Zahlen mit Kontext eingeben
- Format vorgeben (Länge, Stil, Empfänger)

Ziel: Einen Kommentar erzeugen, den ihr direkt in den Monatsbericht übernehmen könntet.

---

## Übung 3 – Sensitivitätsanalyse

**Fragestellung:**
> Was passiert mit dem EBITDA wenn:
> - Materialkosten +5%
> - Volumen -3%
> - Personalkosten +2% (Tarifanpassung)

**Ausgangsdaten (fiktiv):**
- Umsatz: 100 Mio. €
- Materialquote: 40%
- Personalkosten: 25 Mio. €
- EBITDA: 12 Mio. €

**Prompt formulieren:** Claude soll eine strukturierte Sensitivitätstabelle erstellen.

Hinweis: Ergebnis immer rechnerisch prüfen – KI macht Rechenfehler!

---

## Übung 4 – Prompt-Bibliothek aufbauen

**Aufgabe:** Notiert euren besten Prompt aus Übung 1–3.
Struktur für die Bibliothek:

| Prompt-Name | Einsatzbereich | Prompt-Text (Vorlage) |
|---|---|---|
| Variance Commentary | Monatsbericht | Du bist... |
| Kostentreiber-Kommentar | Monatsbericht | ... |
| Sensitivitätsanalyse | Ad-hoc-Anfragen | ... |

---

## Drei Grundregeln

1. **Rolle zuweisen** – "Du bist ein erfahrener Controller in der Maschinenvision-Branche..."
2. **Format definieren** – "Antworte in max. 5 Sätzen. Stil: Management-Reporting."
3. **Kontext liefern** – Zahlen, Branche, Zweck des Dokuments mitgeben

---

*Schulungsunterlage | KI im Controlling | März 2026*
