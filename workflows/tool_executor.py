from workflows.tool_registry import TOOLS


def execute_tool(tool_name: str, tool_input: str):
    """
    Execute the selected tool with the appropriate input.
    """

    if tool_name not in TOOLS:
        return f"Tool '{tool_name}' not found."

    tool = TOOLS[tool_name]

    try:

        if tool_name == "calculator":
            return tool.invoke({"expression": tool_input})

        elif tool_name == "weather":

            task = tool_input.lower()

            # Remove common prefixes
            prefixes = [
                "weather in",
                "temperature in",
                "forecast for",
                "forecast in",
            ]

            city = task

            for prefix in prefixes:
                if task.startswith(prefix):
                    city = task.replace(prefix, "").strip()
                    break

            return tool.invoke({"city": city})

        return "Unsupported tool."

    except Exception as e:
        return f"Tool execution failed: {e}"