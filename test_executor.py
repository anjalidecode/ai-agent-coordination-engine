from workflows.tool_executor import execute_tool

print(execute_tool("calculator", "25 * 67"))
print(execute_tool("calculator", "150 / 3"))
print(execute_tool("unknown", "123"))