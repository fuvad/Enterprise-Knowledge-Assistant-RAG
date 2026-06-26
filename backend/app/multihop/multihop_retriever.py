from collections import defaultdict

from app.retrieval.hybrid_retriever import HybridRetriever
from app.hyde.hyde_retriever import HyDERetriever
from app.multihop.entity_extractor import EntityExtractor


class MultiHopRetriever:

    FIRST_HOP_WEIGHT = 1.0
    SECOND_HOP_WEIGHT = 0.7

    def __init__(self, use_hyde=False):
        print("ENTERED MULTIHOP INIT")

        if use_hyde:
            print("Creating HyDE")
            self.retriever = HyDERetriever()
        else:
            print("Creating Hybrid")
            self.retriever = HybridRetriever()
            
        print("Retriever created")

        self.extractor = EntityExtractor()
        print("Extractor created")

    def retrieve(self, query, k=10):

        print()
        print("=" * 80)
        print("MULTI-HOP RETRIEVAL")
        print("=" * 80)

        print(f"Query: {query}")

        # First hop

        first_results = self.retriever.retrieve(
            query,
            k=k
        )

        print()
        print("=" * 80)
        print("FIRST HOP")
        print("=" * 80)

        print(
            f"Retrieved {len(first_results)} documents"
        )

        for result in first_results:

            print()
            print(
                f"ID: {result['id']}"
            )

            print(
                f"Score: {result['score']:.4f}"
            )

            print(
                result["text"][:150]
            )

        # Entity extraction

        entities = self.extractor.extract(
            first_results[:3],
            max_entities=5
        )

        print()
        print("=" * 80)
        print("EXTRACTED ENTITIES")
        print("=" * 80)

        for entity in entities:
            print(entity)

        # Second hop

        second_results = []

        print()
        print("=" * 80)
        print("SECOND HOP")
        print("=" * 80)

        for entity in entities:

            print()
            print(
                f"Searching entity: {entity}"
            )

            entity_results = (
                self.retriever.retrieve(
                    entity,
                    k=2
                )
            )

            print(
                f"Retrieved {len(entity_results)} docs"
            )

            for result in entity_results:

                print(
                    f"  ID={result['id']} "
                    f"Score={result['score']:.4f}"
                )

            second_results.extend(
                entity_results
            )

        # Merge

        scores = defaultdict(float)

        documents = {}

        print()
        print("=" * 80)
        print("MERGING")
        print("=" * 80)

        for result in first_results:

            doc_id = result["id"]

            contribution = (
                result["score"]
                * self.FIRST_HOP_WEIGHT
            )

            scores[doc_id] += contribution

            documents[doc_id] = result

        for result in second_results:

            doc_id = result["id"]

            contribution = (
                result["score"]
                * self.SECOND_HOP_WEIGHT
            )

            scores[doc_id] += contribution

            documents[doc_id] = result

        ranked = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        print()
        print("=" * 80)
        print("FINAL RANKING")
        print("=" * 80)

        for doc_id, score in ranked:

            print(
                f"ID={doc_id} "
                f"MultiHopScore={score:.4f}"
            )

        final_results = []

        for doc_id, score in ranked:

            item = documents[doc_id].copy()

            item["multihop_score"] = score

            final_results.append(
                item
            )

        return final_results