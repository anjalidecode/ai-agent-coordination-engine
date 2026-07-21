from langchain_core.tools import tool

@tool
def calculator(expression: str) -> str:
    """
    Perform mathematical calculations.

    Input should be a valid mathematical expression.
    Example:
    25 * 67
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Error: {e}"