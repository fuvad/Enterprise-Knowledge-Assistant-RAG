from app.embeddings.factory import EmbeddingFactory

class EmbeddingService:
    def __init__(self, model_name):
        self.embedder = EmbeddingFactory.create(model_name)

    def embed(self, texts):
        return self.embedder.embed(texts)
    
#This is the file our project will use, others are hidden