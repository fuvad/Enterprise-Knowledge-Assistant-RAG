import re

class TextCleaner:
    def clean(self, text: str) -> str:
        # collapse multiple spaces/tabs
        text = re.sub(r"[ \t]+", " ", text)

        # collapse excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()