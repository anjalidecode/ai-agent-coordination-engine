from workflows.main_workflow import run_workflow

print("=" * 60)
print("        AI Agent Coordination Engine")
print("=" * 60)

task = input("Enter your task: ")

result = run_workflow(task)

if result["type"] == "tool":

    print(f"\nTool Selected: {result['tool']}")
    print(f"\nResult:\n{result['result']}")

else:

    print("\n" + "=" * 60)
    print("Planner Agent")
    print("=" * 60)
    print(result["plan"])

    print("\n" + "=" * 60)
    print("Research Agent")
    print("=" * 60)
    print(result["research"])

    print("\n" + "=" * 60)
    print("Decision Agent")
    print("=" * 60)
    print(result["decision"])