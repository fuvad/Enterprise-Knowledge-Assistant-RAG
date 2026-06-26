#Not Production ready. For production we should use LLM extractor

from collections import Counter
import spacy

class EntityExtractor:
    def __init__(self):
        print("Loading spaCy model...")
        self.nlp = spacy.load("en_core_web_sm")
        print("spaCy loaded")
        
        self.technical_entities = {
            "jwt",
            "oauth",
            "authentication",
            "authorization",

            "postgresql",
            "mysql",
            "mongodb",
            "redis",

            "docker",
            "kubernetes",
            "configmap",
            "secrets",

            "fastapi",
            "qdrant",

            "langchain",
            "llamaindex",

            "rag",
            "embedding",
            "embeddings",
            "reranker",

            "vector database",
            "vector store",

            "api",
            "microservice"
        }

    def extract(self, results, max_entities=5):
        candidates = []
        entity_map = {}

        for result in results:
            text = result["text"]
            doc = self.nlp(text)
            doc_candidates = set()

            # Named Entities
            for ent in doc.ents:
                entity = ent.text.strip()
                if len(entity) > 2:
                    normalized = (entity.lower())
                    doc_candidates.add(normalized)
                    if normalized not in entity_map:
                        entity_map[normalized] = entity

            # Noun Phrases
            for chunk in doc.noun_chunks:
                phrase = chunk.text.strip()
                words = phrase.split()
                if len(words) >= 2:
                    normalized = phrase.lower()
                    doc_candidates.add(normalized)
                    if normalized not in entity_map:
                        entity_map[normalized] = phrase

            # Technical Entity Rules
            lower_text = text.lower()
            for tech_entity in self.technical_entities:
                if tech_entity in lower_text:
                    doc_candidates.add(tech_entity)
                    if tech_entity not in entity_map:
                        entity_map[tech_entity] = tech_entity

            candidates.extend(doc_candidates)

        frequencies = Counter(candidates)

        entities = [entity_map[entity] for entity, _ in frequencies.most_common(max_entities)]

        return entities