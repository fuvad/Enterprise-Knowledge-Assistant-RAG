from app.retrieval.bm25_retriever import BM25Retriever

results = BM25Retriever().retrieve("astronomy", k=5)

for result in results:
    print()
    print("=" * 80)
    print(f"ID: {result[0]}")
    print(f"Score: {result[2]}")
    print(result[1])