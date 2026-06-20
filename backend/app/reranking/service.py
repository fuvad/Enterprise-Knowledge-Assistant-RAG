from app.retrieval.hybrid_retriever import HybridRetriever
from app.hyde.hyde_retriever import HyDERetriever
from app.reranking.reranker import BGEReranker

class RetrievalService:
    def __init__(self):
        self.hybrid = HybridRetriever()
        self.hyde = HyDERetriever()
        self.reranker = BGEReranker()

    def search(self, query, k=5, use_hyde=False):
        if use_hyde:
            results = self.hyde.retrieve(query, k=20)       #k=20, coz lets the reranker inspect 20 chunks
        else:
            results = self.hybrid.retrieve(query, k=20)

        reranked = self.reranker.rerank(query, results)

        return reranked[:k]