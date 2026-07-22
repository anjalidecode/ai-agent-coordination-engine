import streamlit as st

from workflows.main_workflow import run_workflow

st.set_page_config(
    page_title="AI Agent Coordination Engine",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Agent Coordination Engine")

st.write(
    "Multi-Agent AI System built using LangChain and Gemini"
)

task = st.text_area(
    "Enter your task",
    placeholder="Example: Build a Hospital Management System"
)

if st.button("Generate"):

    if not task.strip():
        st.warning("Please enter a task.")
        st.stop()

    with st.spinner("Executing Workflow..."):

        result = run_workflow(task)

    if result["type"] == "tool":

        st.success(f"Tool Selected: {result['tool']}")

        st.subheader("🛠 Tool Output")
        st.write(result["result"])

    else:

        st.subheader("📋 Planner Agent")
        st.write(result["plan"])

        st.subheader("🔍 Research Agent")
        st.write(result["research"])

        st.subheader("✅ Decision Agent")
        st.write(result["decision"])