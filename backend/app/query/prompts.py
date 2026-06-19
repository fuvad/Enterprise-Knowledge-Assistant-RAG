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

MULTI_QUERY_PROMPT = """
Generate 5 different search queries.

Requirements:
- Preserve meaning.
- Use different wording.
- Return one query per line.

Return exactly 5 queries.
Each query must be on a new line.

Query:
{query}
"""