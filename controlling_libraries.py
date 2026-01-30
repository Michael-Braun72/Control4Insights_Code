"""
Control4Insights - Wichtige Python-Bibliotheken für Controlling
================================================================

Diese Datei gibt einen Überblick über die wichtigsten Python-Bibliotheken
für datengetriebenes Controlling und demonstriert deren Anwendungsbereiche.

Kategorien:
    1. Datenverarbeitung & Analyse
    2. Excel & Datei-Integration
    3. Visualisierung & Dashboards
    4. Forecasting & Zeitreihenanalyse
    5. Machine Learning für Controlling
    6. Datenbank-Anbindung
    7. Reporting & Automatisierung
"""

# =============================================================================
# 1. DATENVERARBEITUNG & ANALYSE
# =============================================================================

# pandas - Das Herzstück der Datenanalyse
# Anwendung: DataFrames, Pivot-Tabellen, Aggregationen, Zeitreihen
import pandas as pd

# numpy - Numerische Berechnungen
# Anwendung: Mathematische Operationen, Arrays, lineare Algebra
import numpy as np

# scipy - Wissenschaftliche Berechnungen
# Anwendung: Statistische Tests, Optimierung, Interpolation
from scipy import stats
from scipy.optimize import minimize

# =============================================================================
# 2. EXCEL & DATEI-INTEGRATION
# =============================================================================

# openpyxl - Excel-Dateien lesen und schreiben (.xlsx)
# Anwendung: Import/Export von Controlling-Reports, Formatierung
import openpyxl

# xlrd - Ältere Excel-Dateien lesen (.xls)
# Anwendung: Legacy-Dateien aus SAP/ERP-Systemen
try:
    import xlrd
except ImportError:
    xlrd = None  # Optional: pip install xlrd

# xlsxwriter - Excel-Dateien erstellen mit erweiterten Features
# Anwendung: Formatierte Reports, Charts in Excel
try:
    import xlsxwriter
except ImportError:
    xlsxwriter = None  # Optional: pip install xlsxwriter

# =============================================================================
# 3. VISUALISIERUNG & DASHBOARDS
# =============================================================================

# matplotlib - Grundlegende Visualisierung
# Anwendung: Liniendiagramme, Balkendiagramme, Zeitreihen
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# seaborn - Statistische Visualisierungen
# Anwendung: Heatmaps, Verteilungen, Korrelationsmatrizen
import seaborn as sns

# plotly - Interaktive Visualisierungen
# Anwendung: Web-Dashboards, Drill-Down-Analysen
try:
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
except ImportError:
    px, go, make_subplots = None, None, None  # pip install plotly

# =============================================================================
# 4. FORECASTING & ZEITREIHENANALYSE
# =============================================================================

# statsmodels - Statistische Modelle und Zeitreihen
# Anwendung: ARIMA, Saisonale Zerlegung, Regressionsanalyse
try:
    import statsmodels.api as sm
    from statsmodels.tsa.seasonal import seasonal_decompose
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    from statsmodels.tsa.arima.model import ARIMA
except ImportError:
    sm = None  # pip install statsmodels

# prophet - Facebook's Forecasting-Bibliothek
# Anwendung: Rolling Forecasts, Saisonalitäten, Feiertage
try:
    from prophet import Prophet
except ImportError:
    Prophet = None  # pip install prophet

# =============================================================================
# 5. MACHINE LEARNING FÜR CONTROLLING
# =============================================================================

# scikit-learn - Machine Learning Grundlagen
# Anwendung: Predictive Analytics, Anomalieerkennung, Clustering
try:
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.preprocessing import StandardScaler, MinMaxScaler
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.cluster import KMeans
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
except ImportError:
    pass  # pip install scikit-learn

# =============================================================================
# 6. DATENBANK-ANBINDUNG
# =============================================================================

# sqlalchemy - Datenbank-ORM
# Anwendung: SAP HANA, SQL Server, PostgreSQL, MySQL
try:
    from sqlalchemy import create_engine, text
except ImportError:
    create_engine = None  # pip install sqlalchemy

# pyodbc - ODBC-Verbindungen (z.B. zu SAP)
try:
    import pyodbc
except ImportError:
    pyodbc = None  # pip install pyodbc

# =============================================================================
# 7. REPORTING & AUTOMATISIERUNG
# =============================================================================

# jinja2 - Template-Engine für automatisierte Reports
# Anwendung: HTML-Reports, E-Mail-Templates
try:
    from jinja2 import Template, Environment, FileSystemLoader
except ImportError:
    Template = None  # pip install jinja2

# python-pptx - PowerPoint-Automatisierung
# Anwendung: Management-Präsentationen automatisch erstellen
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
except ImportError:
    Presentation = None  # pip install python-pptx

# python-docx - Word-Dokumente erstellen
# Anwendung: Automatisierte Berichte, Dokumentation
try:
    from docx import Document
except ImportError:
    Document = None  # pip install python-docx

# =============================================================================
# CONTROLLING-SPEZIFISCHE HILFSFUNKTIONEN
# =============================================================================


def berechne_abweichung(ist: float, plan: float) -> dict:
    """
    Berechnet absolute und prozentuale Abweichung (Varianzanalyse).

    Args:
        ist: Ist-Wert
        plan: Plan-Wert

    Returns:
        dict mit absoluter und prozentualer Abweichung
    """
    abw_abs = ist - plan
    abw_pct = (abw_abs / abs(plan) * 100) if plan != 0 else 0
    return {
        'ist': ist,
        'plan': plan,
        'abweichung_absolut': abw_abs,
        'abweichung_prozent': abw_pct
    }


def berechne_deckungsbeitrag(umsatz: float, variable_kosten: float) -> dict:
    """
    Berechnet den Deckungsbeitrag und die DB-Quote.

    Args:
        umsatz: Umsatzerlöse
        variable_kosten: Variable Kosten (als positiver Wert)

    Returns:
        dict mit Deckungsbeitrag und Quote
    """
    db = umsatz - variable_kosten
    db_quote = (db / umsatz * 100) if umsatz != 0 else 0
    return {
        'deckungsbeitrag': db,
        'db_quote_prozent': db_quote
    }


def berechne_break_even(fixkosten: float, db_quote: float) -> float:
    """
    Berechnet den Break-Even-Umsatz.

    Args:
        fixkosten: Fixe Kosten (Gesamtbetrag)
        db_quote: Deckungsbeitragsquote in Prozent

    Returns:
        Break-Even-Umsatz
    """
    if db_quote <= 0:
        return float('inf')
    return fixkosten / (db_quote / 100)


def berechne_rentabilitaet(gewinn: float, bezugsgroesse: float,
                           kennzahl: str = 'umsatz') -> dict:
    """
    Berechnet verschiedene Rentabilitätskennzahlen.

    Args:
        gewinn: Gewinn (z.B. EBIT, Jahresüberschuss)
        bezugsgroesse: Bezugsgröße (Umsatz, Eigenkapital, Gesamtkapital)
        kennzahl: Art der Rentabilität ('umsatz', 'eigenkapital', 'gesamtkapital')

    Returns:
        dict mit Rentabilitätskennzahl
    """
    if bezugsgroesse == 0:
        return {f'{kennzahl}rentabilitaet_prozent': 0}
    return {f'{kennzahl}rentabilitaet_prozent': (gewinn / bezugsgroesse) * 100}


def berechne_cashflow_indirekt(jahresueberschuss: float,
                                abschreibungen: float,
                                rueckstellungen_veraenderung: float = 0) -> dict:
    """
    Berechnet den operativen Cashflow (indirekte Methode).

    Args:
        jahresueberschuss: Jahresüberschuss/-fehlbetrag
        abschreibungen: Abschreibungen auf Anlagevermögen
        rueckstellungen_veraenderung: Veränderung der Rückstellungen

    Returns:
        dict mit Cashflow-Komponenten
    """
    cashflow = jahresueberschuss + abschreibungen + rueckstellungen_veraenderung
    return {
        'jahresueberschuss': jahresueberschuss,
        'abschreibungen': abschreibungen,
        'rueckstellungen_delta': rueckstellungen_veraenderung,
        'operativer_cashflow': cashflow
    }


def berechne_working_capital(umlaufvermoegen: float,
                              kurzfristige_verbindlichkeiten: float) -> dict:
    """
    Berechnet das Working Capital und die Quote.

    Args:
        umlaufvermoegen: Summe Umlaufvermögen
        kurzfristige_verbindlichkeiten: Kurzfristige Verbindlichkeiten

    Returns:
        dict mit Working Capital Kennzahlen
    """
    wc = umlaufvermoegen - kurzfristige_verbindlichkeiten
    wc_ratio = umlaufvermoegen / kurzfristige_verbindlichkeiten if kurzfristige_verbindlichkeiten != 0 else 0
    return {
        'working_capital': wc,
        'current_ratio': wc_ratio
    }


def erstelle_plan_ist_vergleich(df: pd.DataFrame,
                                 ist_spalte: str = 'Ist',
                                 plan_spalte: str = 'Plan') -> pd.DataFrame:
    """
    Erstellt einen Plan-Ist-Vergleich mit Abweichungsanalyse.

    Args:
        df: DataFrame mit mindestens Ist- und Plan-Spalten
        ist_spalte: Name der Ist-Spalte
        plan_spalte: Name der Plan-Spalte

    Returns:
        DataFrame mit zusätzlichen Abweichungsspalten
    """
    result = df.copy()
    result['Abweichung_absolut'] = result[ist_spalte] - result[plan_spalte]
    result['Abweichung_prozent'] = np.where(
        result[plan_spalte] != 0,
        (result[ist_spalte] - result[plan_spalte]) / result[plan_spalte].abs() * 100,
        0
    )
    return result


def berechne_rollierende_prognose(zeitreihe: pd.Series,
                                   perioden: int = 3) -> pd.Series:
    """
    Berechnet eine einfache rollierende Durchschnittsprognose.

    Args:
        zeitreihe: Zeitreihe mit historischen Werten
        perioden: Anzahl Perioden für gleitenden Durchschnitt

    Returns:
        Serie mit Prognosewerten
    """
    return zeitreihe.rolling(window=perioden).mean()


# =============================================================================
# BEISPIEL: CONTROLLING-DASHBOARD DATENSTRUKTUR
# =============================================================================

BEISPIEL_KENNZAHLEN = {
    'GuV-Struktur': {
        'Umsatzerlöse': 'Erlöse aus dem Verkauf von Produkten/Dienstleistungen',
        'Materialaufwand': 'Kosten für Roh-, Hilfs- und Betriebsstoffe',
        'Personalaufwand': 'Löhne, Gehälter, Sozialabgaben',
        'Abschreibungen': 'Wertminderung von Vermögensgegenständen',
        'EBITDA': 'Earnings Before Interest, Taxes, Depreciation & Amortization',
        'EBIT': 'Earnings Before Interest and Taxes (operatives Ergebnis)',
        'EBT': 'Earnings Before Taxes (Ergebnis vor Steuern)',
        'Jahresüberschuss': 'Nettoergebnis nach Steuern',
    },
    'Margen': {
        'Bruttomarge': '(Umsatz - Materialaufwand) / Umsatz',
        'EBITDA-Marge': 'EBITDA / Umsatz',
        'EBIT-Marge': 'EBIT / Umsatz',
        'Umsatzrentabilität': 'Jahresüberschuss / Umsatz',
    },
    'Liquidität': {
        'Current Ratio': 'Umlaufvermögen / kurzfristige Verbindlichkeiten',
        'Quick Ratio': '(Umlaufvermögen - Vorräte) / kurzfristige Verbindlichkeiten',
        'Cash Ratio': 'Liquide Mittel / kurzfristige Verbindlichkeiten',
    },
    'Kapitalstruktur': {
        'Eigenkapitalquote': 'Eigenkapital / Gesamtkapital',
        'Verschuldungsgrad': 'Fremdkapital / Eigenkapital',
        'Anlagendeckung I': 'Eigenkapital / Anlagevermögen',
    }
}


# =============================================================================
# HAUPTFUNKTION: BIBLIOTHEKEN-CHECK
# =============================================================================

def pruefe_installierte_bibliotheken() -> dict:
    """
    Prüft, welche Controlling-relevanten Bibliotheken installiert sind.

    Returns:
        dict mit Bibliotheksnamen und Installationsstatus
    """
    bibliotheken = {
        # Kern-Bibliotheken
        'pandas': pd is not None,
        'numpy': np is not None,
        'scipy': stats is not None,

        # Excel/Dateien
        'openpyxl': openpyxl is not None,
        'xlrd': xlrd is not None,
        'xlsxwriter': xlsxwriter is not None,

        # Visualisierung
        'matplotlib': plt is not None,
        'seaborn': sns is not None,
        'plotly': px is not None,

        # Forecasting/ML
        'statsmodels': sm is not None,
        'prophet': Prophet is not None,

        # Datenbank
        'sqlalchemy': create_engine is not None,
        'pyodbc': pyodbc is not None,

        # Reporting
        'jinja2': Template is not None,
        'python-pptx': Presentation is not None,
        'python-docx': Document is not None,
    }
    return bibliotheken


def zeige_bibliotheks_status():
    """Zeigt den Installationsstatus aller Bibliotheken an."""
    status = pruefe_installierte_bibliotheken()

    print("\n" + "=" * 60)
    print(" CONTROLLING-BIBLIOTHEKEN STATUS")
    print("=" * 60)

    kategorien = {
        'Kern-Analyse': ['pandas', 'numpy', 'scipy'],
        'Excel/Dateien': ['openpyxl', 'xlrd', 'xlsxwriter'],
        'Visualisierung': ['matplotlib', 'seaborn', 'plotly'],
        'Forecasting/ML': ['statsmodels', 'prophet'],
        'Datenbank': ['sqlalchemy', 'pyodbc'],
        'Reporting': ['jinja2', 'python-pptx', 'python-docx'],
    }

    for kategorie, libs in kategorien.items():
        print(f"\n{kategorie}:")
        for lib in libs:
            symbol = "[OK]" if status.get(lib, False) else "[X] "
            print(f"  {symbol} {lib}")

    print("\n" + "=" * 60)
    installiert = sum(1 for v in status.values() if v)
    print(f" {installiert}/{len(status)} Bibliotheken installiert")
    print("=" * 60 + "\n")


# =============================================================================
# REQUIREMENTS FÜR CONTROLLING-PROJEKTE
# =============================================================================

REQUIREMENTS = """
# Control4Insights - Python Controlling Libraries
# Installation: pip install -r requirements_controlling.txt

# === KERN-BIBLIOTHEKEN (Pflicht) ===
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0

# === EXCEL & DATEI-INTEGRATION ===
openpyxl>=3.1.0
xlrd>=2.0.0
xlsxwriter>=3.1.0

# === VISUALISIERUNG ===
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0

# === FORECASTING & ZEITREIHEN ===
statsmodels>=0.14.0
prophet>=1.1.0

# === MACHINE LEARNING ===
scikit-learn>=1.2.0

# === DATENBANK-ANBINDUNG ===
sqlalchemy>=2.0.0
pyodbc>=4.0.0

# === REPORTING & AUTOMATISIERUNG ===
jinja2>=3.1.0
python-pptx>=0.6.21
python-docx>=0.8.11

# === ZUSÄTZLICHE TOOLS ===
tqdm>=4.65.0           # Fortschrittsbalken
python-dateutil>=2.8.0 # Datumsverarbeitung
fuzzywuzzy>=0.18.0     # Text-Matching (Kontenpläne)
python-Levenshtein>=0.21.0  # Schnelleres fuzzy matching
"""


def erstelle_requirements_datei(pfad: str = 'requirements_controlling.txt'):
    """Erstellt eine requirements.txt Datei für Controlling-Projekte."""
    with open(pfad, 'w', encoding='utf-8') as f:
        f.write(REQUIREMENTS)
    print(f"Requirements-Datei erstellt: {pfad}")


# =============================================================================
# AUSFÜHRUNG BEI DIREKTEM AUFRUF
# =============================================================================

if __name__ == '__main__':
    print(__doc__)
    zeige_bibliotheks_status()

    # Beispiel: Abweichungsberechnung
    print("\nBeispiel - Plan-Ist-Abweichung:")
    ergebnis = berechne_abweichung(ist=1_250_000, plan=1_200_000)
    for key, value in ergebnis.items():
        if 'prozent' in key:
            print(f"  {key}: {value:+.2f}%")
        else:
            print(f"  {key}: {value:,.0f} EUR")

    # Beispiel: Deckungsbeitrag
    print("\nBeispiel - Deckungsbeitragsrechnung:")
    db = berechne_deckungsbeitrag(umsatz=5_000_000, variable_kosten=3_000_000)
    print(f"  Deckungsbeitrag: {db['deckungsbeitrag']:,.0f} EUR")
    print(f"  DB-Quote: {db['db_quote_prozent']:.1f}%")

    # Beispiel: Break-Even
    print("\nBeispiel - Break-Even-Analyse:")
    be_umsatz = berechne_break_even(fixkosten=800_000, db_quote=40)
    print(f"  Break-Even-Umsatz: {be_umsatz:,.0f} EUR")
