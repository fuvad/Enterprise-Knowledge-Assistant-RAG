from app.ingestion.ingestion_manager import IngestionManager
from app.cleaning.pipeline import CleaningPipeline
from app.metadata.pipeline import MetadataPipeline
from app.chunking.pipeline import ChunkingPipeline
from app.embeddings.benchmark import EmbeddingBenchmark

document = IngestionManager().ingest("data/markdown/sample.md")
document = CleaningPipeline().process(document)
document = MetadataPipeline().process(document)

chunks = ChunkingPipeline().process(document, method="semantic")

texts = [chunk.text for chunk in chunks]

print(f"Chunks Found: {len(texts)}")

EmbeddingBenchmark().run(texts)