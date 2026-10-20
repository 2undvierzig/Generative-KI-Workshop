import logging
from pathlib import Path
from typing import List, Dict

from marker.converters.pdf import PdfConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered

from config import DATA_DIR, MARKER_OUTPUT_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PDFProcessor:
    __slots__ = ("converter", "output_dir")

    def __init__(self) -> None:
        self.converter = PdfConverter(
            artifact_dict=create_model_dict(),
            config={"output_format": "markdown", "languages": "de,en"},
        )
        self.output_dir = MARKER_OUTPUT_DIR

    def process_pdf(self, pdf_path: Path) -> Dict[str, str]:
        logger.info("Verarbeite PDF: %s", pdf_path)
        rendered = self.converter(str(pdf_path))
        full_text, images, metadata = text_from_rendered(rendered)

        output_file = self.output_dir / f"{pdf_path.stem}.md"
        output_file.write_text(full_text, encoding="utf-8")

        logger.info("PDF verarbeitet: %s", output_file)
        return {
            "text": full_text,
            "metadata": metadata,
            "source_file": str(pdf_path),
            "output_file": str(output_file),
        }

    def process_all_pdfs(self) -> List[Dict[str, str]]:
        pdf_files = list(DATA_DIR.glob("*.pdf"))
        if not pdf_files:
            logger.warning("Keine PDFs in %s", DATA_DIR)
            return []

        logger.info("Gefunden %d PDFs", len(pdf_files))
        docs: List[Dict[str, str]] = []
        for pdf in pdf_files:
            try:
                docs.append(self.process_pdf(pdf))
            except Exception as e:
                logger.error("Überspringe %s: %s", pdf, e)
        logger.info("Verarbeitet: %d Dokumente", len(docs))
        return docs

    def get_processed_texts(self) -> List[str]:
        texts: List[str] = []
        for md in self.output_dir.glob("*.md"):
            try:
                texts.append(md.read_text(encoding="utf-8"))
            except Exception as e:
                logger.error("Fehler beim Lesen %s: %s", md, e)
        return texts
