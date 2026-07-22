from workflows.tool_executor import execute_tool

print("Calculator")
print(execute_tool("calculator", "25 * 67"))

print()

print("Weather")
print(execute_tool("weather", "Weather in Bangalore"))

print()

print("Invalid Tool")
print(execute_tool("xyz", "Hello"))