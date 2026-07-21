def calculator(expression: str):
    """
    Evaluate a mathematical expression.

    Example:
    25 * 67
    """

    try:
        result = eval(expression)

        return f"Result: {result}"

    except Exception as e:

        return f"Error: {e}"