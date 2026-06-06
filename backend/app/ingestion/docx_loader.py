import os

from docx import Document as DocxDocument

from app.schemas.document import Document


class DOCXLoader:

    def load(self, path: str) -> Document:

        doc = DocxDocument(path)

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

        return Document(
            source="docx",
            filename=os.path.basename(path),
            text=text
        )