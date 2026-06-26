from app.multihop.multihop_retriever import MultiHopRetriever
from app.reranking.reranker import BGEReranker

class RetrievalService:
    def __init__(self):
        self.retriever = MultiHopRetriever(use_hyde=False)
        self.reranker = BGEReranker()

    def search(self, query, k=5):
        results = self.retriever.retrieve(query, k=20)
        reranked = self.reranker.rerank(query, results)

        return reranked[:k]