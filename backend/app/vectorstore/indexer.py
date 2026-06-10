#Chunks + Vectors -> Store in Qdrant

from qdrant_client.models import PointStruct    #PointStruct -> a single vector record inside Qdrant, like a row in SQL
from app.vectorstore.qdrant_client import get_qdrant_client
from app.vectorstore.collection_manager import CollectionManager

class Indexer:
    def __init__(self):
        self.client = get_qdrant_client()
        self.collection = CollectionManager().COLLECTION_NAME

    def index(self, chunks, vectors):
        points = []     #Will store all records before sending them to Qdrant

        for idx, (chunk,vector) in enumerate(zip(chunks, vectors)):     #Loop Through Chunks and Vectors
            payload = {     #Payload -> metadata stored alongside the vector
                "text":
                chunk.text,

                "source":
                chunk.source,

                "filename":
                chunk.filename,

                **chunk.metadata.model_dump()       #Automatically converts whole metadata to dict format
            }

            points.append(
                PointStruct(        #Represents one point inside Qdrant
                    id=idx,
                    vector=vector.tolist(),     #Embeddings are often NumPy arrays. converts NumPy → Python list
                    payload=payload
                )
            )

        self.client.upsert(     #actual database write (insert) for vectors
            collection_name=self.collection,
            points=points
        )

        print(f"Indexed {len(points)} chunks")
        
#Inserts vectors into Qdrant
#Vector is used for searching, Payload is what gets returned to your RAG system and eventually shown to the LLM