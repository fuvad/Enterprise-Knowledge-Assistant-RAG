class AnswerAgent:
    def run(self, state):
        context = "\n\n".join(doc["text"] for doc in state["documents"])
        state["answer"] = context

        return state
    
#For now we're just returning context, later it becomes an LLM call