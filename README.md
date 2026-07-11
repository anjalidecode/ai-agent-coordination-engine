# 🤖 AI Agent Coordination & Decision Engine

A multi-agent AI application developed using **Python**, **LangChain**, and **Google Gemini** as part of the **Infosys Springboard Virtual Internship**.

This project demonstrates how multiple AI agents collaborate to solve a user's task by dividing responsibilities among specialized agents.

---

## 📌 Milestone 1

### Objectives Completed

- Configure LangChain and required dependencies
- Develop foundational AI agents
- Implement prompt templates
- Create agent interaction workflow
- Build a basic testing interface using Streamlit

---

## 🏗️ Project Architecture

```
User
  │
  ▼
Planner Agent
  │
  ▼
Research Agent
  │
  ▼
Decision Agent
  │
  ▼
Final Recommendation
```

---

## 🤖 AI Agents

### 1. Planner Agent

- Breaks the user's task into logical and actionable steps.
- Creates a structured project plan.

### 2. Research Agent

- Analyzes the generated plan.
- Recommends technologies, frameworks, libraries, and best practices.

### 3. Decision Agent

- Reviews the research report.
- Suggests the most suitable solution with reasoning and recommendations.

---

## 📂 Project Structure

```
agent-engine/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   ├── decision.py
│   └── __init__.py
│
├── prompts/
│   ├── planner_prompt.py
│   ├── research_prompt.py
│   └── decision_prompt.py
│
├── app.py
├── ui.py
├── config.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

## 🛠️ Technologies Used

- Python 3.12
- LangChain
- Google Gemini API
- Streamlit
- python-dotenv

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/ai-agent-coordination-engine.git

cd ai-agent-coordination-engine
```

### Create a virtual environment

```bash
python3 -m venv .venv
```

### Activate the virtual environment

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run the Project

### Command Line Interface

```bash
python app.py
```

### Streamlit Interface

```bash
streamlit run ui.py
```

---

## 📸 Example Workflow

**Input**

```
Build a Hospital Management System
```

**Workflow**

```
User Input
      │
      ▼
Planner Agent
      │
      ▼
Research Agent
      │
      ▼
Decision Agent
      │
      ▼
Final Recommendation
```

---

## 🚀 Future Enhancements

- Agent Coordinator
- Shared Memory
- External API Integration
- Long-Term Memory
- Enterprise Workflow Automation
- REST API using FastAPI

---

## 👩‍💻 Author

**Anjali Sharma**

Bachelor of Engineering (Computer Science & Engineering)

Infosys Springboard Virtual Internship Project
