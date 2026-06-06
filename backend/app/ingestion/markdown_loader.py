import os

from app.schemas.document import Document


class MarkdownLoader:

    def load(self, path: str) -> Document:

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        return Document(
            source="markdown",
            filename=os.path.basename(path),
            text=text
        )