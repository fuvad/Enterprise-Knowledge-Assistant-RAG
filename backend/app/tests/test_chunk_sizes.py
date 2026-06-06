from app.ingestion.ingestion_manager import IngestionManager
from app.cleaning.pipeline import CleaningPipeline
from app.metadata.pipeline import MetadataPipeline
from app.chunking.pipeline import ChunkingPipeline


document = IngestionManager().ingest("data/markdown/sample.md")
document = CleaningPipeline().process(document)
document = MetadataPipeline().process(document)

for size in [256, 512, 1024]:
    chunks = ChunkingPipeline().process(
        document,
        method="recursive",
        chunk_size=size
    )

    print(f"\nChunk Size: {size}")
    print(f"Chunk Count: {len(chunks)}")

    for chunk in chunks:
        print(
            f"Chunk {chunk.chunk_id}: "
            f"{len(chunk.text)} characters"
        )