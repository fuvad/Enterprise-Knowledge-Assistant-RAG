REWRITE_PROMPT = """
Rewrite the following enterprise search query.

Rules:
1. Expand abbreviations.
2. Replace vague words with specific technical terms.
3. Keep the meaning unchanged.
4. Return only the rewritten query.

Query:
{query}
"""