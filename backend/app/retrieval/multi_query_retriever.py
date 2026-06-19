from collections import defaultdict
from app.query.multi_query import MultiQueryGenerator
from app.retrieval.hybrid_retriever import HybridRetriever

class MultiQueryRetriever:
    def __init__(self):
        self.generator = MultiQueryGenerator()
        self.retriever = HybridRetriever()

    def retrieve(self, query, k=5):
        queries = self.generator.generate(query)
        
        scores = defaultdict(int)
        documents = {}

        for q in queries:
            results = self.retriever.retrieve(q, k)
            
            for result in results:
                doc_id = result['id']
                scores[doc_id] += result['score']
                if doc_id not in documents:
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

        return final_results