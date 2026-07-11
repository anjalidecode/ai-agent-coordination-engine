from agents.planner import create_plan
from agents.researcher import research_plan

print("=" * 60)
print("      AI Agent Coordination Engine")
print("=" * 60)

task = input("\nEnter your task: ")

print("\nGenerating project plan...\n")

plan = create_plan(task)

print(plan)

print("\n" + "=" * 60)
print("Research Agent")
print("=" * 60)

research = research_plan(plan)

print(research)