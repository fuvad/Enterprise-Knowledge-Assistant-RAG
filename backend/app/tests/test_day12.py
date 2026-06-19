from app.retrieval.multi_query_retriever import MultiQueryRetriever

results = MultiQueryRetriever().retrieve("What is cooking?")
for result in results:
    print()
    print("=" * 80)
    print(f"Score: {result['score']}")
    print(result["text"])