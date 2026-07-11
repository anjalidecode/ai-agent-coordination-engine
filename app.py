from agents.planner import create_plan

print("=" * 50)
print(" AI Agent Coordination Engine ")
print("=" * 50)

task = input("\nEnter your task: ")

plan = create_plan(task)

print("\nGenerated Plan:\n")
print(plan)