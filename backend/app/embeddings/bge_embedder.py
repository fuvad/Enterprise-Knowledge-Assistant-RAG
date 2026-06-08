from sentence_transformers import SentenceTransformer
from app.embeddings.base import BaseEmbedder


class BGEEmbedder(BaseEmbedder):
    def __init__(self):
        self.model = SentenceTransformer("BAAI/bge-m3")

    def embed(self, texts):
        return self.model.encode(texts, normalize_embeddings=True)
        
#Later if BGE requires instruction prefixes or special preprocessing, we put it here