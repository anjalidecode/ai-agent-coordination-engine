import streamlit as st

from agents.planner import create_plan
from agents.researcher import research_plan
from agents.decision import make_decision

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

    with st.spinner("Planner Agent Working..."):
        plan = create_plan(task)

    st.subheader("📋 Planner Agent")
    st.write(plan)

    with st.spinner("Research Agent Working..."):
        research = research_plan(plan)

    st.subheader("🔍 Research Agent")
    st.write(research)

    with st.spinner("Decision Agent Working..."):
        decision = make_decision(research)

    st.subheader("✅ Decision Agent")
    st.write(decision)