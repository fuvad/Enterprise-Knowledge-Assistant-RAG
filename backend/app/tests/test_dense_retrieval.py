from app.retrieval.dense_retriever import DenseRetriever

results = DenseRetriever().retrieve("What is cooking?", k=3)        #Top k retrieval

for point in results:
    print()
    print("=" * 80)
    print(f"Score: {point.score:.4f}")
    print(point.payload["text"])