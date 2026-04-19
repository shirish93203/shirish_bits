from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def _clean_markdown_line(line: str) -> str:
    text = line.strip()
    if text.startswith("- "):
        text = f"• {text[2:]}"
    return text.replace("&", "&amp;")


def build_pdf(md_path: Path, pdf_path: Path) -> None:
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "ResumeTitle",
        parent=styles["Heading1"],
        fontSize=17,
        leading=20,
        spaceAfter=6,
        textColor=colors.HexColor("#0f172a"),
    )
    h2_style = ParagraphStyle(
        "ResumeH2",
        parent=styles["Heading2"],
        fontSize=12,
        leading=15,
        spaceBefore=8,
        spaceAfter=3,
        textColor=colors.HexColor("#0f172a"),
    )
    h3_style = ParagraphStyle(
        "ResumeH3",
        parent=styles["Heading3"],
        fontSize=10.5,
        leading=13,
        spaceBefore=6,
        spaceAfter=2,
        textColor=colors.HexColor("#1f2937"),
    )
    body_style = ParagraphStyle(
        "ResumeBody",
        parent=styles["BodyText"],
        fontSize=9.5,
        leading=12.5,
        spaceAfter=2.5,
        textColor=colors.HexColor("#111827"),
    )

    story = []
    for raw_line in md_path.read_text(encoding="utf-8").splitlines():
        line = _clean_markdown_line(raw_line)
        if not line:
            story.append(Spacer(1, 3))
            continue

        if line.startswith("# "):
            story.append(Paragraph(line[2:].strip(), title_style))
            continue
        if line.startswith("## "):
            story.append(Paragraph(line[3:].strip(), h2_style))
            continue
        if line.startswith("### "):
            story.append(Paragraph(line[4:].strip(), h3_style))
            continue

        # Preserve manual line-break hints from markdown (double spaces at line end).
        text = line.rstrip()
        if text.endswith("  "):
            text = text[:-2] + "<br/>"

        story.append(Paragraph(text, body_style))

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=14 * mm,
        bottomMargin=14 * mm,
        title="Shirish Meduri Resume",
        author="Shirish Meduri",
    )
    doc.build(story)


if __name__ == "__main__":
    workspace = Path(__file__).resolve().parents[1]
    md_file = workspace / "Shirish_Resume_Updated.md"
    pdf_file = workspace / "Shirish_Resume_Updated.pdf"
    build_pdf(md_file, pdf_file)
