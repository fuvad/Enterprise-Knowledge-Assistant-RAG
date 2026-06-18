from app.retrieval.dense_retriever import DenseRetriever
from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.fusion import ReciprocalRankFusion
from app.vectorstore.qdrant_client import get_qdrant_client
from app.vectorstore.collection_manager import CollectionManager
from app.query.query_pipeline import QueryPipeline

class HybridRetriever:
    def __init__(self):
        self.dense = DenseRetriever()
        self.bm25 = BM25Retriever()
        self.rrf = ReciprocalRankFusion()
        self.client = get_qdrant_client()
        self.collection = CollectionManager().COLLECTION_NAME
        self.query_pipeline = QueryPipeline()

    def retrieve(self, query, k=5):
        query = self.query_pipeline.process(query)
        dense_results = self.dense.retrieve(query, k)
        bm25_results = self.bm25.retrieve(query, k)

        fused_results = self.rrf.fuse(dense_results, bm25_results)

        results = []

        for point_id, score in fused_results[:k]:
            point = self.client.retrieve(
                collection_name=self.collection,
                ids=[point_id]
                )[0]

            results.append(
                {
                    "id": point_id,
                    "score": score,
                    "text": point.payload["text"],
                    "source": point.payload.get("source"),
                    "filename": point.payload.get("filename"),
                    "department": point.payload.get("department"),
                    "tags": point.payload.get("tags")
                }
            )

        return results