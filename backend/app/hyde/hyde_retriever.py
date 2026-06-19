from collections import defaultdict
from app.hyde.generator import HyDEGenerator
from app.retrieval.hybrid_retriever import HybridRetriever

class HyDERetriever:
    def __init__(self):
        self.generator = HyDEGenerator()
        self.retriever = HybridRetriever()

    def retrieve(self, query, k=5):
        hypothetical_answer = self.generator.generate(query)
        
        print()
        print("=" * 80)
        print("ORIGINAL QUERY")
        print("=" * 80)
        print(query)

        print()
        print("=" * 80)
        print("HYPOTHETICAL ANSWER")
        print("=" * 80)
        print(hypothetical_answer)

        original_results = self.retriever.retrieve(query, k)
        hyde_results = self.retriever.retrieve(hypothetical_answer, k)

        scores = defaultdict(float)
        documents = {}

        for result in original_results:
            doc_id = result["id"]
            scores[doc_id] += result["score"]
            documents[doc_id] = result

        for result in hyde_results:
            doc_id = result["id"]
            scores[doc_id] += result["score"]
            documents[doc_id] = result

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        final_results = []
        for doc_id, total_score in ranked:
            item = documents[doc_id].copy()
            item["score"] = total_score
            final_results.append(item)

        return final_results[:k]