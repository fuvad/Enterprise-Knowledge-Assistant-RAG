import re


class TextCleaner:
    def clean(self, text: str) -> str:
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text