def select_tool(task: str):
    """
    Select the appropriate tool based on the user's request.
    """

    operators = ["+", "-", "*", "/"]

    if any(op in task for op in operators):
        return "calculator"

    return None