def recall_at_k(retrieved_ids, relevant_ids):
    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    hits = len(retrieved & relevant)

    return (hits / len(relevant))

def precision_at_k(retrieved_ids, relevant_ids):
    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    hits = len(retrieved & relevant)

    return (hits / len(retrieved))