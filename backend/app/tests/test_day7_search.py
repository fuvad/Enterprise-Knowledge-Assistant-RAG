from app.vectorstore.search import SearchService

results = SearchService().search("What are black holes?")

for point in results.points:
    print()
    print("=" * 80)
    print(f"Score: {point.score:.4f}")
    print(point.payload["text"])