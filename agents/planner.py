from langchain_google_genai import ChatGoogleGenerativeAI
from prompts.planner_prompt import PLANNER_PROMPT
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Create the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

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