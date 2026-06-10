#Retriever

from qdrant_client.models import Filter, FieldCondition, MatchValue
from app.embeddings.service import EmbeddingService
from app.vectorstore.qdrant_client import get_qdrant_client
from app.vectorstore.collection_manager import CollectionManager

class SearchService:
    def __init__(self):     #Runs when, search_service = SearchService()
        self.client = get_qdrant_client()
        self.collection = CollectionManager().COLLECTION_NAME
        self.embedder = EmbeddingService("e5")      #Load Embedding Model, same embedding model used during indexing

    def search(self, query, department=None, tag=None, limit=5):
        query_vector = self.embedder.embed([f"query: {query}"])[0]      #prefixes help the model understand whether it's embedding a search query or a document

        conditions = []
        
        if department:
            conditions.append(
                FieldCondition(
                    key="department",
                    match=MatchValue(value=department)
                )
            )
            
        if tag:
            conditions.append(
                FieldCondition(
                    key="tags",
                    match=MatchValue(value=tag)
                )
            )
            
        query_filter = None
        
        if conditions:
            query_filter = Filter(must=conditions)      #must -> ALL conditions must be true
        
        #Dense Retrieval    
        results = self.client.query_points(
            collection_name=self.collection,
            query=query_vector.tolist(),
            query_filter=query_filter,      #Restricts which vectors are eligible
            limit=limit     #Return the top 5 most similar chunks, Qdrant ranks them based on cosine similarity
        )

        return results
    
#Added metadata filtering as well. Useful when Qdrant contains Department or Tags
#Right now users have to provide department or tag for it to work.
#But in real case we could do;
    #User explicitly specifies them in the text and then extract them
    #Retrieve from the user's profile
    #Admin dashboard filters (Show options in the UI)