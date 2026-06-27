from langgraph.graph import StateGraph
from app.agents.state import AgentState
from app.agents.planning_agent import PlanningAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.answer_agent import AnswerAgent

planner = PlanningAgent()
retriever = RetrievalAgent()
answerer = AnswerAgent()

graph = StateGraph(AgentState)

graph.add_node("planner", planner.run)
graph.add_node("retriever", retriever.run)
graph.add_node("answerer", answerer.run)
graph.set_entry_point("planner")
graph.add_edge("planner", "retriever")
graph.add_edge("retriever", "answerer")
graph.set_finish_point("answerer")
agent = graph.compile()