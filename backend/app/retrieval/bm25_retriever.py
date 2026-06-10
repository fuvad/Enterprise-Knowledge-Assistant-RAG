from rank_bm25 import BM25Okapi
from app.vectorstore.qdrant_client import get_qdrant_client
from app.vectorstore.collection_manager import CollectionManager

class BM25Retriever:
    def __init__(self):
        client = get_qdrant_client()
        collection = CollectionManager().COLLECTION_NAME

        points, _ = client.scroll(collection_name=collection, limit=1000)       #Read all chunks from Qdrant, retrieves up to 1000 stored chunks

        self.documents = []
        self.ids = []

        for point in points:
            text = point.payload["text"]
            self.documents.append(text)
            self.ids.append(point.id)

        tokenized_docs = [doc.lower().split() for doc in self.documents]      #Tokenize docs

        self.bm25 = BM25Okapi(tokenized_docs)     #Creates BM25 index. Builds the scoring structure. Like a keyworkd search engine

    def retrieve(self, query, k=5):
        tokenized_query = query.lower().split()     #Query tokenization
        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(self.ids, self.documents, scores),      #Combines IDs, docs, scores
            key=lambda x: x[2],     #Use 3rd element for sorting
            reverse=True        #Ascending order
        )
        
        ranked = [item for item in ranked if item[2] > 0]

        return ranked[:k]       #Top k