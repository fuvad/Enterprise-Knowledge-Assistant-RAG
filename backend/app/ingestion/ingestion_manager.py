from app.ingestion.pdf_loader import PDFLoader
from app.ingestion.docx_loader import DOCXLoader
from app.ingestion.markdown_loader import MarkdownLoader


class IngestionManager:

    def ingest(self, path):

        if path.endswith(".pdf"):
            return PDFLoader().load(path)

        elif path.endswith(".docx"):
            return DOCXLoader().load(path)

        elif path.endswith(".md"):
            return MarkdownLoader().load(path)

        raise ValueError(
            f"Unsupported file type: {path}"
        )