from transformers import pipeline

class HyDEGenerator:
    def __init__(self):
        self.model = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )

    def generate(self, query: str) -> str:
        prompt = f"""
        Write a short answer to the question.

        Question:
        {query}
        """

        result = self.model(
            prompt,
            max_new_tokens=100,
            do_sample=False
        )

        return result[0]["generated_text"]