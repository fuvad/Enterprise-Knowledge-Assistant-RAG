from app.retrieval.evaluator import RetrievalEvaluator

metrics = RetrievalEvaluator().evaluate(
    query="What is cooking?",
    relevant_ids=[3, 4],
    k=5
    )

print(metrics) 