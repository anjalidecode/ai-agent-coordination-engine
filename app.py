from agents.planner import create_plan
from agents.researcher import research_plan
from agents.decision import make_decision
from workflows.tool_selector import select_tool
from workflows.tool_executor import execute_tool

print("=" * 60)
print("      AI Agent Coordination Engine")
print("=" * 60)

task = input("Enter your task: ")

# Check if a tool should handle the task
tool = select_tool(task)

if tool:
    print("\nTool Selected:", tool)
    result = execute_tool(tool, task)
    print(result)

else:
    print("\nPlanner Agent Working...\n")
    plan = create_plan(task)
    print(plan)

    print("\n" + "=" * 60)
    print("Research Agent Working...\n")
    research = research_plan(plan)
    print(research)

    print("\n" + "=" * 60)
    print("Decision Agent Working...\n")
    decision = make_decision(task, research)
    print(decision)