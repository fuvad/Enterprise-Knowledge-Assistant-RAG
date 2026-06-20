def recall_at_k(retrieved_ids, relevant_ids):       #Did we find the correct chunk?
    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    hits = len(retrieved & relevant)

    return (hits / len(relevant))

def precision_at_k(retrieved_ids, relevant_ids):        #How many retrieved chunks were relevant?
    retrieved = set(retrieved_ids)
    relevant = set(relevant_ids)

    hits = len(retrieved & relevant)

    return (hits / len(retrieved))

def mrr(retrieved_ids, relevant_ids):       #How early does the first relevant document appear? (Reranking)
    for rank, doc_id in enumerate(retrieved_ids, start=1):
        if doc_id in relevant_ids:
            return 1 / rank

    return 0

import math

def ndcg(retrieved_ids, relevant_ids):      #How good is the entire ranking?
    dcg = 0
    
    for rank, doc_id in enumerate(retrieved_ids, start=1):
        if doc_id in relevant_ids:
            dcg += (1 / math.log2(rank + 1))        #gives higher reward to documents appearing earlier

    ideal = 0

    for rank in range(1, min(len(relevant_ids), len(retrieved_ids)) + 1):
        ideal += (1 / math.log2(rank + 1))

    if ideal == 0:
        return 0

    return dcg / ideal