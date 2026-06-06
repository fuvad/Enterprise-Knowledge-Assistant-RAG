from app.ingestion.ingestion_manager import IngestionManager
from app.cleaning.pipeline import CleaningPipeline
from app.metadata.pipeline import MetadataPipeline
from app.chunking.pipeline import ChunkingPipeline

document = IngestionManager().ingest("data/markdown/sample.md")
document = CleaningPipeline().process(document)
document = MetadataPipeline().process(document)

chunks = ChunkingPipeline().process(document,method="recursive",chunk_size=512)

print(f"Chunks: {len(chunks)}")

for chunk in chunks:
    print()
    print(chunk.model_dump())