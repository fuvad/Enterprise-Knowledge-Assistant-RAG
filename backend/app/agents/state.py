from typing import TypedDict

class AgentState(TypedDict):
    query: str
    documents: list
    entities: list
    answer: str
    
#Needed so that every agent sees what previous agents did