# Primzahlen-Visualisierung

Dieses Python-Skript findet alle Primzahlen bis 100.000 und erstellt verschiedene Visualisierungen.

## Features

- **Effiziente Berechnung**: Verwendet den Sieve of Eratosthenes Algorithmus
- **Multiple Visualisierungen**:
  - Verteilung der Primzahlen
  - Primzahldichte in Intervallen
  - Abstände zwischen aufeinanderfolgenden Primzahlen
  - Ulam-Spirale (bis 10.000)
  - Kumulative Anzahl der Primzahlen
  - Detaillierte Statistiken

## Installation

1. Installieren Sie die erforderlichen Pakete:
```bash
pip install -r requirements.txt
```

## Verwendung

Führen Sie das Skript aus:
```bash
python prime_numbers_visualization.py
```

Das Skript wird:
1. Alle Primzahlen bis 100.000 berechnen
2. Statistiken in der Konsole anzeigen
3. Eine Visualisierung erstellen und als `prime_numbers_visualization.png` speichern
4. Die Visualisierung in einem Fenster anzeigen

## Ausgabe

Das Skript generiert eine hochauflösende PNG-Datei mit 6 verschiedenen Visualisierungen der Primzahlen.
