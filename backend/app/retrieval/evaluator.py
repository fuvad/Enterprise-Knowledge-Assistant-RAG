from app.retrieval.metrics import recall_at_k, precision_at_k, mrr, ndcg

class RetrievalEvaluator:
    def evaluate(self, retrieved_ids, relevant_ids):
        return {
            "recall":
            recall_at_k(retrieved_ids, relevant_ids),

            "precision":
            precision_at_k(retrieved_ids, relevant_ids),

            "mrr":
            mrr(retrieved_ids, relevant_ids),

            "ndcg":
            ndcg(retrieved_ids, relevant_ids)
        }