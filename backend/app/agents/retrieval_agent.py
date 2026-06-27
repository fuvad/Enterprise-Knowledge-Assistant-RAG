from app.multihop.multihop_retriever import MultiHopRetriever

class RetrievalAgent:
    def __init__(self):
        self.retriever = MultiHopRetriever()

    def run(self, state):
        results = self.retriever.retrieve(state["query"])
        state["documents"] = results

        return state
    
#Again these are just placeholders for now