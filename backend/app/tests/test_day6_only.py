from app.embeddings.service import EmbeddingService

text = ["JWT tokens expire after 24 hours."]

service = EmbeddingService("e5")

embedding = service.embed(text)

print(embedding.shape)