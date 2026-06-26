print("TEST STARTED")

from app.multihop.multihop_retriever import (
    MultiHopRetriever
)

print("IMPORT SUCCESS")

retriever = MultiHopRetriever()

print("RETRIEVER CREATED")

results = retriever.retrieve(
    "What is Cooking?"
)

print("RETRIEVE FINISHED")

print()
print("=" * 80)
print("FINAL RESULTS")
print("=" * 80)

for result in results[:5]:
    print()
    print(f"ID: {result['id']}")
    print(f"Score: {result['multihop_score']:.4f}")
    print(result["text"][:200])