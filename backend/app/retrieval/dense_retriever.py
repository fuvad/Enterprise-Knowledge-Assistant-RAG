from app.vectorstore.search import SearchService

class DenseRetriever:
    def __init__(self):
        self.search_service = SearchService()

    def retrieve(self, query, k=5):
        results = self.search_service.search(
            query=query,
            limit=k
        )

        return results.points
    
#Without this our system will be directly talking to Qdrant. This is ok for small projects, but when we scale, it'll;
    #Cause tight coupling: If every part of your application directly depends on Qdrant-specific code, you'll have to modify many files. With retriever layer the rest of the application doesn't care what database is underneath
    #Cause issues when using Multiple Retrieval Methods
    #Business Logic doesn't belong in SearchService. SearchService for Talking to Qdrant and Retriever for Retrieval Strategy

#With this application doesn't know anything about Qdrant, SearchService, Embeddings, Vector Search