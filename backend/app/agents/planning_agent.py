class PlanningAgent:
    def run(self, state):
        query = state["query"].lower()

        if "why" in query:
            state["needs_multihop"] = True
        else:
            state["needs_multihop"] = False

        return state
    
#Rules or placeholder for now, later becomes LLM planner