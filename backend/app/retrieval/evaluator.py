from app.retrieval.metrics import recall_at_k, precision_at_k
from app.retrieval.dense_retriever import DenseRetriever

class RetrievalEvaluator:
    def evaluate(self, query, relevant_ids, k=5):
        results = DenseRetriever().retrieve(query, k)
        
        retrieved_ids = [point.id for point in results]
        
        print("\n=== DEBUG ===")
        print("Query:", query)
        print("Relevant IDs:", relevant_ids)
        print("Retrieved IDs:", retrieved_ids)
        print("=============\n")

        recall = recall_at_k(retrieved_ids, relevant_ids)
        precision = precision_at_k(retrieved_ids, relevant_ids)

        return {
            "recall":
            recall,

            "precision":
            precision
        }