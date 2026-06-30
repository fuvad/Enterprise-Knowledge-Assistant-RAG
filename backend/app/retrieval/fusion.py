from collections import defaultdict

class ReciprocalRankFusion:
    def fuse(self, dense_results, bm25_results, k=60):
        scores = defaultdict(float)

        for rank, point in enumerate(dense_results, start=1):
            scores[point.id] += 1 / (k + rank)      #Gives Dense score for each chunk

        for rank, result in enumerate(bm25_results,start=1):
            scores[result[0]] += 1 / (k + rank)     #Add/Create BM25 score

        return sorted(
            scores.items(),
            key=lambda x: x[1],     #Sort by score
            reverse=True        #Desc
        )
        
class WeightedFusion:
    def fuse(self, dense_results, bm25_results, dense_weight=0.7, bm25_weight=0.3):
        scores = defaultdict(float)

        for point in dense_results:
            scores[point.id] += (point.score * dense_weight)    #Gives Dense score for each chunk

        max_bm25 = max(r[2] for r in bm25_results)      #Max score of BM25 result

        for result in bm25_results:
            normalized = (result[2] / max_bm25)     #Normalize each score

            scores[result[0]] += (normalized * bm25_weight)     #Add/Create BM25 score

        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )