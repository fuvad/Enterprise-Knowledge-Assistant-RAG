import time
from app.embeddings.service import EmbeddingService

MODELS = ["e5", "bge", "nomic"]

class EmbeddingBenchmark:
    def run(self, texts: list[str]):
        for model in MODELS:
            service = EmbeddingService(model)
            start = time.time()
            vectors = service.embed(texts)
            end = time.time()

            print()
            print(f"Model: {model}")
            print(f"Vectors: {vectors.shape}")
            print(f"Time: {end-start:.2f}s")