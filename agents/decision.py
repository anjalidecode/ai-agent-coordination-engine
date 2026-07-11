from config import llm
from prompts.decision_prompt import DECISION_PROMPT


def make_decision(research: str) -> str:
    """
    Analyze the research report and provide
    the best technical recommendation.
    """

    prompt = DECISION_PROMPT.format(research=research)

    response = llm.invoke(prompt)

    if isinstance(response.content, list):
        return response.content[0]["text"]

    return response.content
