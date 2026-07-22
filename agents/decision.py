from config import llm
from prompts.decision_prompt import DECISION_PROMPT

from workflows.tool_selector import select_tool
from workflows.tool_executor import execute_tool


def make_decision(task: str, research: str):
    """
    Make a decision based on research.
    If a suitable tool exists, execute it.
    Otherwise, use the LLM.
    """

    tool_name = select_tool(task)

    if tool_name:
        return execute_tool(tool_name, task)

    prompt = DECISION_PROMPT.format(
        research=research
    )

    response = llm.invoke(prompt)


    if isinstance(response.content, list):
     return response.content[0]["text"]

    return response.content

