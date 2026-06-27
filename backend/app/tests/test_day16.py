from app.agents.graph import agent

result = agent.invoke(
    {
        "query":
        "How are passwords stored?"
    }
)

print()
print("=" * 80)
print(result["answer"])