from agents.tool_agent import agent_executor

response = agent_executor.invoke(
    {
        "input": "What is 125 * 56?"
    }
)

print(response["output"])