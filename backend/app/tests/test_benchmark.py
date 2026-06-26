from app.retrieval.benchmark import RetrievalBenchmark

results = RetrievalBenchmark().compare("cooking")

print()
print("=" * 80)
print("DENSE")
print("=" * 80)

for point in results["dense"]:
    print()
    print(point.payload["text"])

print()
print("=" * 80)
print("BM25")
print("=" * 80)

for point in results["bm25"]:
    print()
    print(point[1])
    
print()
print("=" * 80)
print("Hybrid")
print("=" * 80)

for point in results["hybrid"]:
    print(print(point["text"]))