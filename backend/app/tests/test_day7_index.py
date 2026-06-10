from app.ingestion.ingestion_manager import IngestionManager
from app.cleaning.pipeline import CleaningPipeline
from app.metadata.pipeline import MetadataPipeline
from app.chunking.pipeline import ChunkingPipeline
from app.embeddings.service import EmbeddingService
from app.vectorstore.collection_manager import CollectionManager
from app.vectorstore.indexer import Indexer

document = IngestionManager().ingest("data/markdown/sample.md")     #Read the doc
document = CleaningPipeline().process(document)     #Clean the doc
document = MetadataPipeline().process(document)     #Add Metadata

chunks = ChunkingPipeline().process(document, method="semantic")        #Chunk the document

texts = [chunk.text for chunk in chunks]        #Extract text from chunks

embedder = EmbeddingService("e5")       #Load embedding model

vectors = embedder.embed(texts)     #Generate embeddings

CollectionManager().create_collection(vector_size=vectors.shape[1])     #Create Qdrant collection

Indexer().index(chunks, vectors)        #Store everything

#This takes a document from disk and pushes it all the way into Qdrant