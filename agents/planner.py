from prompts.planner_prompt import PLANNER_PROMPT
from config import llm

def create_plan(task: str) -> str:
    """
    Generate a step-by-step plan for the given task.
    """

    prompt = PLANNER_PROMPT.format(task=task)

    response = llm.invoke(prompt)

    # Handle both string and content-block responses
    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content