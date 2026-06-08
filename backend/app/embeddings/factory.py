from app.embeddings.e5_embedder import E5Embedder
from app.embeddings.bge_embedder import BGEEmbedder
from app.embeddings.nomic_embedder import NomicEmbedder


class EmbeddingFactory:
    @staticmethod
    def create(model_name):
        if model_name == "e5":
            return E5Embedder()
        elif model_name == "bge":
            return BGEEmbedder()
        elif model_name == "nomic":
            return NomicEmbedder()

        raise ValueError("Unknown model")