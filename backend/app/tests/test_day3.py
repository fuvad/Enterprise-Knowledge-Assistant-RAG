from app.ingestion.ingestion_manager import IngestionManager
from app.cleaning.pipeline import CleaningPipeline
from app.metadata.pipeline import MetadataPipeline

manager = IngestionManager()

document = manager.ingest("data/markdown/sample.md")
document = CleaningPipeline().process(document)
document = MetadataPipeline().process(document)

print(document.model_dump())