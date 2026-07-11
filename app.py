from agents.planner import create_plan
from agents.researcher import research_plan
from agents.decision import make_decision

print("=" * 60)
print("      AI Agent Coordination Engine")
print("=" * 60)

task = input("\nEnter your task: ")

print("\nPlanner Agent Working...\n")
plan = create_plan(task)
print(plan)

print("\n" + "=" * 60)
print("Research Agent Working...\n")
research = research_plan(plan)
print(research)

print("\n" + "=" * 60)
print("Decision Agent Working...\n")
decision = make_decision(research)
print(decision)