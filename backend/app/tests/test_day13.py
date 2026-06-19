from app.hyde.hyde_retriever import HyDERetriever

results = HyDERetriever().retrieve("How are passwords stored?")

for result in results:
    print()
    print("=" * 80)

    print(f"Score: {result['score']:.4f}")
    print(result["text"])