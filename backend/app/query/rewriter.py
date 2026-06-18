from transformers import pipeline
from app.query.prompts import REWRITE_PROMPT

class QueryRewriter:
    def __init__(self):
        self.model = pipeline(
            task="text2text-generation",
            model="google/flan-t5-base"
        )

    def rewrite(self, query: str) -> str:
        prompt = REWRITE_PROMPT.format(query=query)

        result = self.model(
            prompt,
            max_new_tokens=50,
            do_sample=False
        )

        return result[0]["generated_text"].strip()