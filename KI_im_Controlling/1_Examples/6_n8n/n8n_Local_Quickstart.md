# n8n lokal starten – Quick-Start-Anleitung

*Für Controlling-Kollegen ohne IT-Vorkenntnisse | Stand: März 2026*

---

## Was ist n8n?

n8n ist ein Open-Source-Automatisierungstool mit visueller Oberfläche.
Workflows werden als Nodes (Bausteine) verbunden – ohne tiefe Programmierkenntnisse.

**Controlling-Use-Cases:**
- Automatischer KPI-Report bei Schwellwert-Überschreitung
- Excel-Datei landet im Ordner → Claude analysiert → E-Mail geht raus
- FX-Rate täglich automatisch in Planungsmodell einspeisen
- Wöchentlicher Wettbewerbs-Digest per Perplexity → automatisch als PDF

**n8n läuft komplett lokal – keine Daten verlassen deinen Rechner.**

---

## Systemvoraussetzungen

| Prüfpunkt | Erwartetes Ergebnis |
|---|---|
| `node --version` | v18.0.0 oder höher |
| `npm --version` | v8.0.0 oder höher |

**Terminal öffnen (Windows):** Windows-Taste → "cmd" → Enter (oder PowerShell)

---

## Installation (einmalig, ca. 2 Minuten)

```bash
npm install -g n8n
```

Abschluss: Keine Fehlermeldung, Terminal zeigt Prompt.

> **Hinweis:** Fehlermeldung wegen Berechtigungen? Terminal als Administrator starten
> (Rechtsklick → "Als Administrator ausführen")

---

## n8n starten

```bash
n8n
```

Ausgabe:
```
Editor is now accessible via:
http://localhost:5678
```

> **Wichtig:** Terminal-Fenster offen lassen – wird es geschlossen, stoppt n8n.

---

## Browser öffnen

→ `http://localhost:5678`

Beim ersten Start: E-Mail + Passwort vergeben (nur für lokalen Login) → "Get started"

---

## n8n stoppen

Im Terminal: **Strg + C**

Alle Workflows bleiben gespeichert.

---

## Häufige Fehler

| Fehler | Lösung |
|---|---|
| "n8n" wird nicht erkannt | `npm install -g n8n` erneut, Terminal neu starten |
| Port 5678 belegt | `n8n --port 5679` |
| Seite lädt nicht | `http://` nicht `https://` prüfen |
| npm: Berechtigung verweigert | Terminal als Administrator starten |

---

## Datenspeicherung

Alle Workflows liegen lokal:
```
Windows: C:\Users\<DeinName>\.n8n\
```
**Diesen Ordner regelmäßig sichern, besonders vor n8n-Updates.**

---

## Kurzreferenz

| Befehl | Funktion |
|---|---|
| `npm install -g n8n` | Einmalig installieren |
| `n8n` | Starten (Port 5678) |
| `n8n --port 5679` | Alternativer Port |
| `n8n update` | Auf neueste Version updaten |
| `Strg + C` | Stoppen |

---

*Internes Schulungsdokument – Controlling-Team | März 2026*
