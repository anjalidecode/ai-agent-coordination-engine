from config import llm
from prompts.research_prompt import RESEARCH_PROMPT


def research_plan(plan: str) -> str:
    """
    Analyze the project plan and recommend technologies,
    tools, libraries, and best practices.
    """

    prompt = RESEARCH_PROMPT.format(plan=plan)

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content