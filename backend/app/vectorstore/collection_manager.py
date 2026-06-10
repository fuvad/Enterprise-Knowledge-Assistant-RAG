from qdrant_client.models import Distance, VectorParams
#Distance for how similarity will be calculated, VectorParams for configuration for vector storage

from app.vectorstore.qdrant_client import get_qdrant_client

class CollectionManager:
    COLLECTION_NAME = "enterprise_documents"        #Collection will always be named this for now

    def create_collection(self, vector_size):
        client = get_qdrant_client()
        collections = client.get_collections()      #Get existing collections
        existing = [c.name for c in collections.collections]    #Extract collection names

        if self.COLLECTION_NAME in existing:
            print("Collection already exists")
            return

        client.create_collection(       #Creates new collection
            collection_name=self.COLLECTION_NAME,
            vectors_config=VectorParams(        #Defines how vectors are stored
                size=vector_size,
                distance=Distance.COSINE
            )
        )

        print("Collection created")
        
#Equivalent to SQL table
#Done coz configuration for vector storage Vector Size, Distance Metric before storing anything