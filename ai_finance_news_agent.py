"""
AI Finance & Controlling News Agent
====================================
Sucht wöchentlich im Internet nach Nachrichten zum Thema "KI in Finance und Controlling"
und erstellt daraus einen formatierten PDF-Report.

Verwendung:
    # Einmalig ausführen:
    python ai_finance_news_agent.py --run-now

    # Wöchentlichen Scheduler starten (läuft jeden Montag um 08:00 Uhr):
    python ai_finance_news_agent.py --schedule

    # Ausgabeverzeichnis festlegen:
    python ai_finance_news_agent.py --run-now --output-dir ./reports

Voraussetzungen:
    pip install anthropic reportlab schedule
    Umgebungsvariable ANTHROPIC_API_KEY muss gesetzt sein.
"""

import argparse
import json
import os
import smtplib
import sys
import time
from datetime import datetime, timedelta
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import anthropic
import schedule
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------
SEARCH_QUERIES = [
    "Künstliche Intelligenz Finance Controlling 2025 2026",
    "AI Finance Controlling Automatisierung aktuell",
    "Machine Learning CFO Finanzplanung Trends",
    "KI Buchhaltung Rechnungswesen Digitalisierung",
    "Generative AI Finance Reporting Forecasting",
    "Large Language Models Controlling Anwendungen",
]

DEFAULT_OUTPUT_DIR = Path("./ki_finance_reports")
MAX_TOKENS = 8192


# ---------------------------------------------------------------------------
# PDF-Hilfsfunktionen
# ---------------------------------------------------------------------------
def _build_styles():
    """Erstellt ein Stylesheet mit Corporate-Design."""
    base = getSampleStyleSheet()

    styles = {
        "title": ParagraphStyle(
            "ReportTitle",
            parent=base["Title"],
            fontSize=24,
            textColor=colors.HexColor("#1A3A5C"),
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName="Helvetica-Bold",
        ),
        "subtitle": ParagraphStyle(
            "ReportSubtitle",
            parent=base["Normal"],
            fontSize=12,
            textColor=colors.HexColor("#4A6FA5"),
            spaceAfter=4,
            alignment=TA_CENTER,
            fontName="Helvetica",
        ),
        "section": ParagraphStyle(
            "SectionHeading",
            parent=base["Heading1"],
            fontSize=14,
            textColor=colors.HexColor("#1A3A5C"),
            spaceBefore=16,
            spaceAfter=6,
            borderPad=4,
            fontName="Helvetica-Bold",
        ),
        "article_title": ParagraphStyle(
            "ArticleTitle",
            parent=base["Heading2"],
            fontSize=11,
            textColor=colors.HexColor("#2E5C8A"),
            spaceBefore=10,
            spaceAfter=3,
            fontName="Helvetica-Bold",
        ),
        "body": ParagraphStyle(
            "BodyText",
            parent=base["Normal"],
            fontSize=9,
            textColor=colors.HexColor("#333333"),
            spaceAfter=4,
            leading=14,
            alignment=TA_JUSTIFY,
            fontName="Helvetica",
        ),
        "meta": ParagraphStyle(
            "MetaInfo",
            parent=base["Normal"],
            fontSize=8,
            textColor=colors.HexColor("#777777"),
            spaceAfter=2,
            fontName="Helvetica-Oblique",
        ),
        "toc_item": ParagraphStyle(
            "TocItem",
            parent=base["Normal"],
            fontSize=10,
            textColor=colors.HexColor("#1A3A5C"),
            spaceAfter=4,
            leftIndent=10,
            fontName="Helvetica",
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontSize=8,
            textColor=colors.HexColor("#999999"),
            alignment=TA_CENTER,
            fontName="Helvetica",
        ),
        "summary_box": ParagraphStyle(
            "SummaryBox",
            parent=base["Normal"],
            fontSize=10,
            textColor=colors.HexColor("#1A3A5C"),
            spaceAfter=6,
            leading=16,
            alignment=TA_JUSTIFY,
            fontName="Helvetica",
            leftIndent=10,
            rightIndent=10,
        ),
    }
    return styles


def _add_header_footer(canvas, doc):
    """Fügt Kopf- und Fußzeile auf jeder Seite ein."""
    canvas.saveState()
    page_width, page_height = A4

    # Header-Linie
    canvas.setStrokeColor(colors.HexColor("#1A3A5C"))
    canvas.setLineWidth(2)
    canvas.line(2 * cm, page_height - 1.8 * cm, page_width - 2 * cm, page_height - 1.8 * cm)

    # Header-Text
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#4A6FA5"))
    canvas.drawString(2 * cm, page_height - 1.5 * cm, "Control4Insights | KI in Finance & Controlling")
    canvas.drawRightString(
        page_width - 2 * cm,
        page_height - 1.5 * cm,
        datetime.now().strftime("Ausgabe: %d.%m.%Y"),
    )

    # Footer
    canvas.setLineWidth(0.5)
    canvas.line(2 * cm, 1.8 * cm, page_width - 2 * cm, 1.8 * cm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#999999"))
    canvas.drawCentredString(
        page_width / 2,
        1.3 * cm,
        f"Seite {doc.page} | Automatisch generiert von KI Finance News Agent",
    )
    canvas.restoreState()


def create_pdf_report(articles: list[dict], output_path: Path, executive_summary: str) -> Path:
    """
    Erstellt einen formatierten PDF-Report aus den Artikeln.

    Args:
        articles: Liste von Artikeln mit Feldern: title, source, date, summary, url, category
        output_path: Pfad zum Speichern der PDF-Datei
        executive_summary: KI-generierte Zusammenfassung der Woche

    Returns:
        Pfad zur erstellten PDF-Datei
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
        title="KI in Finance & Controlling – Wochenreport",
        author="Control4Insights AI News Agent",
    )

    styles = _build_styles()
    elements = []

    # --- Titelseite ---
    elements.append(Spacer(1, 2 * cm))
    elements.append(Paragraph("KI in Finance &amp; Controlling", styles["title"]))
    week_num = datetime.now().isocalendar()[1]
    year = datetime.now().year
    elements.append(
        Paragraph(
            f"Wöchentlicher News-Report | KW {week_num}/{year}",
            styles["subtitle"],
        )
    )
    elements.append(
        Paragraph(
            f"Berichtszeitraum: {(datetime.now() - timedelta(days=7)).strftime('%d.%m.%Y')} – "
            f"{datetime.now().strftime('%d.%m.%Y')}",
            styles["subtitle"],
        )
    )
    elements.append(Spacer(1, 0.5 * cm))
    elements.append(HRFlowable(width="100%", thickness=2, color=colors.HexColor("#1A3A5C")))
    elements.append(Spacer(1, 0.5 * cm))

    # --- Executive Summary Box ---
    elements.append(Paragraph("Executive Summary", styles["section"]))
    summary_data = [[Paragraph(executive_summary, styles["summary_box"])]]
    summary_table = Table(summary_data, colWidths=[doc.width])
    summary_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EEF4FB")),
                ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#4A6FA5")),
                ("ROWPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 12),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
            ]
        )
    )
    elements.append(summary_table)
    elements.append(Spacer(1, 0.5 * cm))

    # --- Statistik-Kacheln ---
    categories = {}
    for art in articles:
        cat = art.get("category", "Sonstiges")
        categories[cat] = categories.get(cat, 0) + 1

    stat_header = [
        Paragraph("Artikel gesamt", styles["meta"]),
        Paragraph("Kategorien", styles["meta"]),
        Paragraph("Quellen", styles["meta"]),
    ]
    unique_sources = len({a.get("source", "") for a in articles})
    stat_values = [
        Paragraph(f"<b>{len(articles)}</b>", styles["section"]),
        Paragraph(f"<b>{len(categories)}</b>", styles["section"]),
        Paragraph(f"<b>{unique_sources}</b>", styles["section"]),
    ]
    stat_table = Table(
        [stat_header, stat_values],
        colWidths=[doc.width / 3] * 3,
    )
    stat_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F5F8FC")),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCDDEE")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCDDEE")),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    elements.append(stat_table)
    elements.append(PageBreak())

    # --- Inhaltsverzeichnis ---
    elements.append(Paragraph("Inhaltsverzeichnis", styles["section"]))
    elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CCDDEE")))
    elements.append(Spacer(1, 0.2 * cm))

    toc_data = []
    for i, art in enumerate(articles, 1):
        toc_data.append(
            [
                Paragraph(f"{i}.", styles["toc_item"]),
                Paragraph(art.get("title", "Ohne Titel"), styles["toc_item"]),
                Paragraph(art.get("category", ""), styles["meta"]),
            ]
        )

    if toc_data:
        toc_table = Table(toc_data, colWidths=[0.8 * cm, doc.width - 3 * cm, 2.2 * cm])
        toc_table.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LINEBELOW", (0, 0), (-1, -1), 0.25, colors.HexColor("#EEEEEE")),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )
        elements.append(toc_table)

    elements.append(PageBreak())

    # --- Artikel-Abschnitte ---
    elements.append(Paragraph("Artikel-Zusammenfassungen", styles["section"]))
    elements.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#1A3A5C")))

    for i, art in enumerate(articles, 1):
        elements.append(Spacer(1, 0.4 * cm))

        # Kategorien-Badge
        cat_label = art.get("category", "Sonstiges")
        cat_data = [[Paragraph(f"  {cat_label}  ", styles["meta"])]]
        cat_table = Table(cat_data, colWidths=[None])
        cat_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E8F0FA")),
                    ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#4A6FA5")),
                    ("TOPPADDING", (0, 0), (-1, -1), 2),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ]
            )
        )
        elements.append(cat_table)

        # Artikel-Titel
        elements.append(
            Paragraph(f"{i}. {art.get('title', 'Ohne Titel')}", styles["article_title"])
        )

        # Metadaten
        source = art.get("source", "Unbekannt")
        date = art.get("date", "")
        url = art.get("url", "")
        meta_text = f"Quelle: <b>{source}</b>"
        if date:
            meta_text += f" | Datum: {date}"
        if url:
            meta_text += f" | <a href='{url}' color='#4A6FA5'>{url[:60]}{'…' if len(url) > 60 else ''}</a>"
        elements.append(Paragraph(meta_text, styles["meta"]))

        # Zusammenfassung
        summary = art.get("summary", "")
        if summary:
            elements.append(Spacer(1, 0.15 * cm))
            elements.append(Paragraph(summary, styles["body"]))

        # Trennlinie zwischen Artikeln
        if i < len(articles):
            elements.append(Spacer(1, 0.2 * cm))
            elements.append(
                HRFlowable(width="100%", thickness=0.25, color=colors.HexColor("#DDDDDD"))
            )

    # --- PDF bauen ---
    doc.build(elements, onFirstPage=_add_header_footer, onLaterPages=_add_header_footer)
    return output_path


# ---------------------------------------------------------------------------
# KI-Recherche mit Claude + Web Search
# ---------------------------------------------------------------------------
def run_news_research(client: anthropic.Anthropic) -> tuple[list[dict], str]:
    """
    Führt eine KI-gestützte Web-Suche nach Finance/Controlling-KI-Nachrichten durch.

    Returns:
        (articles, executive_summary)
    """
    today = datetime.now().strftime("%d.%m.%Y")
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%d.%m.%Y")

    system_prompt = f"""Du bist ein spezialisierter Research-Assistent für den Bereich
Finance und Controlling. Deine Aufgabe ist es, die neuesten Nachrichten, Trends und
Entwicklungen zum Thema "Künstliche Intelligenz in Finance und Controlling" zu recherchieren.

Berichtszeitraum: {week_ago} bis {today}

Fokusthemen:
- KI-Automatisierung in der Buchhaltung und im Rechnungswesen
- Machine Learning für Forecasting und Finanzplanung
- Generative KI im CFO-Bereich und Reporting
- Automatisierte Variance Analysis und KPI-Überwachung
- LLM-Anwendungen im Controlling
- KI-Tools für Wirtschaftsprüfung und Compliance
- Digitalisierung des Finance-Bereichs durch KI
- Praxisberichte und Case Studies aus Unternehmen

Gib deine Antwort ausschließlich als gültiges JSON zurück (kein Markdown, keine Erklärungen):
{{
  "executive_summary": "Übergreifende Zusammenfassung der wichtigsten Entwicklungen dieser Woche in 3-5 Sätzen auf Deutsch",
  "articles": [
    {{
      "title": "Artikeltitel auf Deutsch (ggf. übersetzt)",
      "source": "Name der Quelle / Webseite",
      "date": "Datum (TT.MM.JJJJ oder 'Aktuell')",
      "url": "URL falls verfügbar, sonst leerer String",
      "category": "Eine von: KI-Automatisierung | Forecasting & Planung | Reporting & Analyse | Compliance & Audit | Praxisbericht | Technologie-Trend",
      "summary": "Sachliche Zusammenfassung des Artikels auf Deutsch, 3-5 Sätze, mit konkreten Details zum Finance/Controlling-Bezug"
    }}
  ]
}}

Suche nach mindestens 8-12 relevanten Artikeln. Priorisiere aktuelle Inhalte aus den letzten 7 Tagen."""

    user_message = f"""Bitte recherchiere aktuelle Nachrichten (Stand: {today}) zu folgenden Suchanfragen
und erstelle einen strukturierten JSON-Report:

Suchanfragen:
{chr(10).join(f'- {q}' for q in SEARCH_QUERIES)}

Liefere ausschließlich valides JSON ohne Markdown-Blöcke oder sonstige Erklärungen."""

    print("🔍 Starte KI-gestützte Web-Recherche...")

    with client.messages.stream(
        model="claude-opus-4-6",
        max_tokens=MAX_TOKENS,
        thinking={"type": "adaptive"},
        system=system_prompt,
        tools=[
            {"type": "web_search_20260209", "name": "web_search"},
            {"type": "web_fetch_20260209", "name": "web_fetch"},
        ],
        messages=[{"role": "user", "content": user_message}],
    ) as stream:
        for event in stream:
            if hasattr(event, "type"):
                if event.type == "content_block_start":
                    block = getattr(event, "content_block", None)
                    if block and getattr(block, "type", "") == "server_tool_use":
                        tool = getattr(block, "name", "")
                        print(f"   → Websuche läuft: {tool}")
        final = stream.get_final_message()

    # JSON aus der Antwort extrahieren
    raw_text = ""
    for block in final.content:
        if getattr(block, "type", "") == "text":
            raw_text = block.text
            break

    # JSON-Block bereinigen (falls Claude trotzdem Markdown zurückgibt)
    raw_text = raw_text.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
    raw_text = raw_text.strip().rstrip("```").strip()

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        print(f"⚠️  JSON-Parsing fehlgeschlagen: {exc}")
        print("   Versuche Fallback-Extraktion...")
        # Fallback: versuche JSON-Objekt aus dem Text zu extrahieren
        start = raw_text.find("{")
        end = raw_text.rfind("}") + 1
        if start >= 0 and end > start:
            data = json.loads(raw_text[start:end])
        else:
            raise ValueError("Kein gültiges JSON in der Antwort gefunden.") from exc

    articles = data.get("articles", [])
    executive_summary = data.get(
        "executive_summary",
        "Diese Woche wurden zahlreiche Entwicklungen im Bereich KI und Finance recherchiert.",
    )

    print(f"✅ {len(articles)} Artikel gefunden.")
    return articles, executive_summary


# ---------------------------------------------------------------------------
# E-Mail-Versand
# ---------------------------------------------------------------------------
def send_pdf_email(
    pdf_path: Path,
    recipient: str,
    sender: str | None = None,
    password: str | None = None,
    smtp_host: str = "mail.gmx.net",
    smtp_port: int = 587,
) -> None:
    """
    Sendet den erstellten PDF-Report per E-Mail.

    Zugangsdaten können als Parameter übergeben oder über Umgebungsvariablen
    bereitgestellt werden:
        EMAIL_FROM      – Absender-Adresse (z. B. deine GMX-Adresse)
        EMAIL_PASSWORD  – Passwort / App-Passwort des Absender-Kontos

    Args:
        pdf_path:   Pfad zur PDF-Datei
        recipient:  Empfänger-E-Mail-Adresse
        sender:     Absender-Adresse (überschreibt EMAIL_FROM)
        password:   Passwort (überschreibt EMAIL_PASSWORD)
        smtp_host:  SMTP-Server (Standard: mail.gmx.net)
        smtp_port:  SMTP-Port mit STARTTLS (Standard: 587)
    """
    sender = sender or os.environ.get("EMAIL_FROM", "")
    password = password or os.environ.get("EMAIL_PASSWORD", "")

    if not sender or not password:
        print("⚠️  E-Mail nicht gesendet: EMAIL_FROM und EMAIL_PASSWORD müssen gesetzt sein.")
        print("   Setze sie mit:")
        print("     export EMAIL_FROM='deine@adresse.de'")
        print("     export EMAIL_PASSWORD='dein-passwort'")
        return

    week_num = datetime.now().isocalendar()[1]
    year = datetime.now().year

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = f"KI Finance & Controlling News – KW {week_num:02d}/{year}"

    body = (
        f"Hallo,\n\n"
        f"anbei findest du den automatisch erstellten KI Finance & Controlling "
        f"News-Report für KW {week_num:02d}/{year}.\n\n"
        f"Der Report enthält die wichtigsten Nachrichten und Trends der letzten Woche "
        f"rund um Künstliche Intelligenz in Finance und Controlling.\n\n"
        f"Viele Grüße\n"
        f"Control4Insights KI News Agent"
    )
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with open(pdf_path, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="pdf")
        attachment.add_header(
            "Content-Disposition", "attachment", filename=pdf_path.name
        )
        msg.attach(attachment)

    print(f"\n📧 Sende E-Mail an {recipient} ...")
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipient, msg.as_string())

    print(f"✅ E-Mail erfolgreich gesendet an: {recipient}")


# ---------------------------------------------------------------------------
# Haupt-Job
# ---------------------------------------------------------------------------
def run_agent(output_dir: Path = DEFAULT_OUTPUT_DIR, email_recipient: str | None = None) -> Path:
    """
    Führt den vollständigen News-Agent-Zyklus aus:
    1. Web-Recherche via Claude + Web Search
    2. PDF-Report-Erstellung

    Returns:
        Pfad zum erstellten PDF
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Fehler: Umgebungsvariable ANTHROPIC_API_KEY ist nicht gesetzt.")
        print("   Setze sie mit: export ANTHROPIC_API_KEY='dein-api-key'")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    print("\n" + "=" * 60)
    print("  Control4Insights | KI Finance & Controlling News Agent")
    print("=" * 60)
    print(f"  Startzeit: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print("=" * 60 + "\n")

    # 1. Recherche
    articles, executive_summary = run_news_research(client)

    # 2. PDF erstellen
    week_num = datetime.now().isocalendar()[1]
    year = datetime.now().year
    filename = f"KI_Finance_News_KW{week_num:02d}_{year}.pdf"
    output_path = output_dir / filename

    print(f"\n📄 Erstelle PDF-Report: {output_path}")
    create_pdf_report(articles, output_path, executive_summary)

    print(f"\n✅ Report erfolgreich erstellt: {output_path}")
    print(f"   Artikel: {len(articles)}")
    print(f"   Dateigröße: {output_path.stat().st_size / 1024:.1f} KB")

    # 3. Optional: PDF per E-Mail versenden
    if email_recipient:
        send_pdf_email(output_path, email_recipient)

    print("\n" + "=" * 60 + "\n")

    return output_path


# ---------------------------------------------------------------------------
# Scheduler
# ---------------------------------------------------------------------------
def start_weekly_scheduler(
    output_dir: Path,
    weekday: str = "monday",
    time_str: str = "08:00",
    email_recipient: str | None = None,
):
    """
    Startet den wöchentlichen Scheduler.

    Args:
        output_dir: Ausgabeverzeichnis für PDFs
        weekday: Wochentag (monday, tuesday, ..., sunday)
        time_str: Uhrzeit im Format HH:MM
    """
    print(f"\n⏰ Scheduler gestartet – Ausführung jeden {weekday.capitalize()} um {time_str} Uhr")
    print("   Drücke Ctrl+C zum Beenden.\n")

    def job():
        try:
            run_agent(output_dir, email_recipient=email_recipient)
        except Exception as exc:
            print(f"❌ Fehler bei der Ausführung: {exc}")

    # Wochentag dynamisch setzen
    getattr(schedule.every(), weekday).at(time_str).do(job)

    while True:
        schedule.run_pending()
        time.sleep(60)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="KI Finance & Controlling News Agent – erstellt wöchentliche PDF-Reports",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  # Einmalig sofort ausführen
  python ai_finance_news_agent.py --run-now

  # Report erstellen und per E-Mail versenden
  python ai_finance_news_agent.py --run-now --email empfaenger@beispiel.de

  # Wöchentlichen Scheduler starten (Montag 08:00) mit E-Mail-Versand
  python ai_finance_news_agent.py --schedule --email empfaenger@beispiel.de

  # Anderen Wochentag und Uhrzeit festlegen
  python ai_finance_news_agent.py --schedule --weekday friday --time 07:30

  # Ausgabeverzeichnis anpassen
  python ai_finance_news_agent.py --run-now --output-dir /pfad/zu/reports

E-Mail-Konfiguration (Umgebungsvariablen):
  export EMAIL_FROM='absender@gmx.de'      # Absender-Adresse
  export EMAIL_PASSWORD='dein-passwort'    # Passwort des Absenders
        """,
    )
    parser.add_argument(
        "--run-now",
        action="store_true",
        help="Recherche sofort einmalig ausführen",
    )
    parser.add_argument(
        "--schedule",
        action="store_true",
        help="Wöchentlichen Scheduler starten",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Ausgabeverzeichnis für PDF-Reports (Standard: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--email",
        metavar="ADRESSE",
        default=None,
        help="E-Mail-Adresse, an die der PDF-Report gesendet wird (benötigt EMAIL_FROM und EMAIL_PASSWORD)",
    )
    parser.add_argument(
        "--weekday",
        default="monday",
        choices=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
        help="Wochentag für den Scheduler (Standard: monday)",
    )
    parser.add_argument(
        "--time",
        default="08:00",
        help="Uhrzeit für den Scheduler im Format HH:MM (Standard: 08:00)",
    )

    args = parser.parse_args()

    if not args.run_now and not args.schedule:
        parser.print_help()
        print("\nHinweis: Bitte --run-now oder --schedule angeben.")
        sys.exit(1)

    if args.run_now:
        run_agent(args.output_dir, email_recipient=args.email)

    if args.schedule:
        start_weekly_scheduler(args.output_dir, args.weekday, args.time, email_recipient=args.email)


if __name__ == "__main__":
    main()
