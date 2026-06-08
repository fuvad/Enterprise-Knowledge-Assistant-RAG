from sentence_transformers import SentenceTransformer
from app.embeddings.base import BaseEmbedder


class NomicEmbedder(BaseEmbedder):
    def __init__(self):
        self.model = SentenceTransformer("nomic-ai/nomic-embed-text-v1.5", trust_remote_code=True)

    def embed(self, texts):
        return self.model.encode(texts, normalize_embeddings=True)
    
#Everything done separately coz later we'll add Instructor, Jina, OpenAI, Voyage, Cohere