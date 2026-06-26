from app.reranking.service import RetrievalService

service = RetrievalService()

results = service.search("What is cooking?")

print()
print("=" * 80)
print("FINAL RESULTS")
print("=" * 80)

for result in results:
    print()
    print("-" * 80)

    print(
        f"Rerank Score: "
        f"{result['rerank_score']:.4f}"
    )

    print(
        result["text"][:300]
    )