from sentence_transformers import SentenceTransformer
from app.embeddings.base import BaseEmbedder


class E5Embedder(BaseEmbedder):
    def __init__(self):
        self.model = SentenceTransformer("intfloat/e5-base-v2")     #Loads E5

    def embed(self, texts):
        texts = [f"passage: {t}" for t in texts]

        return self.model.encode(texts, normalize_embeddings=True)
    
    #E5 expects passage: for documents and query: for user questions or queries