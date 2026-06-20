from app.reranking.service import RetrievalService

results = RetrievalService().search("How do we add color and flavour in food?")

for result in results:
    print()
    print("=" * 80)

    print(
        f"Rerank Score: "
        f"{result['rerank_score']:.4f}"
    )

    print(result["text"])