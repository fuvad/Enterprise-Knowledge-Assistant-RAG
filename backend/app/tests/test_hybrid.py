from app.retrieval.hybrid_retriever import HybridRetriever

results = HybridRetriever().retrieve("What is cooking?")

for result in results:

    print()
    print("=" * 80)
    print(f"ID: {result['id']}")
    print(f"Score: {result['score']:.4f}")
    print(f"Source: {result['source']}")
    print(f"File: {result['filename']}")
    print()
    print(result["text"])