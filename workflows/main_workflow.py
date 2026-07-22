from workflows.tool_selector import select_tool
from workflows.tool_executor import execute_tool

from agents.planner import create_plan
from agents.researcher import research_plan
from agents.decision import make_decision


def run_workflow(task: str):
    """
    Execute the complete AI workflow.
    Returns a dictionary containing the results.
    """

    tool = select_tool(task)

    if tool:
        result = execute_tool(tool, task)

        return {
            "type": "tool",
            "tool": tool,
            "result": result
        }

    plan = create_plan(task)

    research = research_plan(plan)

    decision = make_decision(task, research)

    return {
        "type": "agent",
        "plan": plan,
        "research": research,
        "decision": decision
    }