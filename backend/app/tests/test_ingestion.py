from app.ingestion.ingestion_manager import (
    IngestionManager
)


manager = IngestionManager()

document = manager.ingest(
    "data/markdown/sample.md"
)

print(document)