def select_tool(task: str):
    """
    Select the appropriate tool based on the user's task.
    """

    task = task.lower()

    # Calculator Tool
    operators = ["+", "-", "*", "/"]

    if any(op in task for op in operators):
        return "calculator"

    # Weather Tool
    weather_keywords = [
        "weather",
        "temperature",
        "forecast",
        "climate",
    ]

    if any(keyword in task for keyword in weather_keywords):
        return "weather"

    return None