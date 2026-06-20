from sentence_transformers import CrossEncoder

class BGEReranker:
    def __init__(self):
        self.model = CrossEncoder("BAAI/bge-reranker-base")

    def rerank(self, query, documents):
        pairs = [(query, doc["text"]) for doc in documents]     #Builds Query-Doc pairs

        scores = self.model.predict(pairs)      #Predict scores

        ranked = []

        for doc, score in zip(documents, scores):       #Pairs Doc with Scores
            item = doc.copy()
            item["rerank_score"] = float(score)
            ranked.append(item)

        ranked.sort(
            key=lambda x:
            x["rerank_score"],
            reverse=True
        )

        return ranked
    
#Rerankers re-orders chunks more accurately