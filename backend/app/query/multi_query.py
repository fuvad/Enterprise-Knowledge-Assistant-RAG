from transformers import pipeline
from app.query.prompts import MULTI_QUERY_PROMPT

class MultiQueryGenerator:
    def __init__(self):
        self.model = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

    def generate(self, query: str):
        prompt = MULTI_QUERY_PROMPT.format(query=query)

        result = self.model(
            prompt,
            max_new_tokens=100,
            do_sample=False
        )

        output = result[0]["generated_text"]

        queries = [q.strip() for q in output.split("\n") if q.strip()]
        
        if len(queries) < 2:
            queries = [
                query,
                f"Explain {query}",
                f"Information about {query}",
                f"Details regarding {query}",
                f"Documentation for {query}"
            ]

        if query not in queries:
            queries.insert(0, query)

        return queries[:5]