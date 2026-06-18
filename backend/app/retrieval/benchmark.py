from app.retrieval.dense_retriever import DenseRetriever
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.hybrid_retriever import HybridRetriever

class RetrievalBenchmark:
    def compare(self, query):
        dense = DenseRetriever().retrieve(query, k=5)
        bm25 = BM25Retriever().retrieve(query, k=5)
        hybrid = HybridRetriever().retrieve(query, k=5)

        return {
            "dense": dense,
            "bm25": bm25,
            "hybrid": hybrid
        }