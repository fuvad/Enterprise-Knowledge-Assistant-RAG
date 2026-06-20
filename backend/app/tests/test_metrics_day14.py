from app.hyde.hyde_retriever import HyDERetriever
from app.reranking.service import RetrievalService
from app.retrieval.evaluator import RetrievalEvaluator

query = "How do we add color and flavour in food?"
relevant_ids = [4]

evaluator = RetrievalEvaluator()

# Before reranking
hyde_results = HyDERetriever().retrieve(query)
hyde_ids = [r["id"] for r in hyde_results]

print(
    "Before Reranking:",
    evaluator.evaluate(hyde_ids, relevant_ids)
)

# After reranking
reranked_results = RetrievalService().search(query)
reranked_ids = [r["id"] for r in reranked_results]

print(
    "After Reranking:",
    evaluator.evaluate(reranked_ids, relevant_ids)
)