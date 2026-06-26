from app.multihop.entity_extractor import EntityExtractor

results = [
    {
        "text": """
        Authentication uses JWT tokens.
        JWT tokens expire after 24 hours.
        PostgreSQL stores user metadata.
        Docker containers run on Kubernetes.
        """
    }
]

extractor = EntityExtractor()
entities = extractor.extract(results, max_entities=10)

print()
print("=" * 80)
print("EXTRACTED ENTITIES")
print("=" * 80)

for entity in entities:
    print(entity)