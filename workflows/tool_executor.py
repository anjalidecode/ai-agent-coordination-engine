from workflows.tool_registry import TOOLS


def execute_tool(tool_name: str, tool_input: str):
    """
    Execute a tool based on its name.
    """

    if tool_name not in TOOLS:
        return f"Error: Tool '{tool_name}' not found."

    tool = TOOLS[tool_name]

    try:
        return tool.invoke({"expression": tool_input})

    except Exception as e:
        return f"Tool execution failed: {e}"