from app.ingestion.ingestion_manager import IngestionManager
from app.cleaning.pipeline import CleaningPipeline
from app.metadata.pipeline import MetadataPipeline
from app.chunking.pipeline import ChunkingPipeline


document = IngestionManager().ingest("data/markdown/sample.md")

document = CleaningPipeline().process(document)
document = MetadataPipeline().process(document)

for method in ["fixed", "recursive", "semantic"]:
    print("\n")
    print("=" * 80)
    print(f"METHOD: {method.upper()}")
    print("=" * 80)

    chunks = ChunkingPipeline().process(document, method=method, chunk_size=512)

    print(f"Chunk Count: {len(chunks)}")

    for chunk in chunks:
        print("\n")
        print(f"Chunk ID: {chunk.chunk_id}")
        print("-" * 50)

        print(chunk.text[:250])