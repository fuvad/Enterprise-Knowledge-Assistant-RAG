import fitz
import os

from app.schemas.document import Document


class PDFLoader:

    def load(self, path: str) -> Document:

        pdf = fitz.open(path)

        text = ""

        for page in pdf:
            text += page.get_text()

        return Document(
            source="pdf",
            filename=os.path.basename(path),
            text=text
        )