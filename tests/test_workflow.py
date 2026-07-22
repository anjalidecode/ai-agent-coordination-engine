from workflows.main_workflow import run_workflow

print("=" * 50)
print("Calculator Test")
print("=" * 50)

print(run_workflow("25 * 67"))

print()

print("=" * 50)
print("Weather Test")
print("=" * 50)

print(run_workflow("Weather in Bangalore"))