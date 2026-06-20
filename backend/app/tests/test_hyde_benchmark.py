from app.retrieval.hybrid_retriever import HybridRetriever
from app.hyde.hyde_retriever import HyDERetriever

query = "How do we add color and flavour in food?"

print()
print("=" * 80)
print("WITHOUT HYDE")
print("=" * 80)

normal_results = HybridRetriever().retrieve(query)

for result in normal_results[:3]:
    print()
    print(result["text"])

print()
print("=" * 80)
print("WITH HYDE")
print("=" * 80)

hyde_results = HyDERetriever().retrieve(query)

for result in hyde_results[:3]:
    print()
    print(result["text"])