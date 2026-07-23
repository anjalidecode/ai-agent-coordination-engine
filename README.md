# 🤖 AI Agent Coordination & Decision Engine

A multi-agent AI application developed using **Python**, **LangChain**, and **Google Gemini** as part of the **Infosys Springboard Virtual Internship**.

This project demonstrates how multiple AI agents collaborate to solve a user's task by intelligently deciding whether the request should be handled by AI agents or specialized tools. The system supports AI-powered planning and reasoning along with custom tools such as a Calculator and a Weather service.

---

# 📌 Milestone 1

## Objectives Completed

- Configure LangChain and required dependencies
- Develop foundational AI agents
- Implement prompt templates
- Create agent interaction workflow
- Build a basic testing interface using Streamlit

---

# 📌 Milestone 2

## Objectives Completed

- Developed intelligent Tool Selection mechanism
- Implemented Tool Registry for scalable tool management
- Built Tool Executor for dynamic tool execution
- Added Calculator Tool
- Integrated Weather Tool using Open-Meteo API
- Combined AI Agents and Tool Routing into a unified workflow
- Created modular testing framework
- Improved application architecture for future scalability

---

# 🏗️ Project Architecture

```
                           User
                             │
                ┌────────────┴────────────┐
                │                         │
         Tool Selector              AI Agent Workflow
                │                         │
      ┌─────────┴──────────┐              │
      │                    │              │
Calculator Tool      Weather Tool     Planner Agent
      │                    │              │
      └──────────┬─────────┘              ▼
                 │                 Research Agent
                 │                      │
                 │                      ▼
                 │                 Decision Agent
                 └──────────────► Final Response
```

---

# 🤖 AI Agents

## 1. Planner Agent

- Breaks user requirements into logical steps.
- Creates a structured implementation plan.

## 2. Research Agent

- Analyzes the generated plan.
- Suggests suitable technologies, frameworks, APIs, and best practices.

## 3. Decision Agent

- Reviews research findings.
- Produces the final recommendation and implementation strategy.

---

# 🛠️ Custom Tools

## Calculator Tool

- Evaluates mathematical expressions.
- Provides instant computation without invoking the LLM.

### Example

```
25 * 67
```

Output

```
1675
```

---

## Weather Tool

- Retrieves live weather information.
- Uses the Open-Meteo REST API.
- Demonstrates integration with external APIs.

### Example

```
Weather in Bangalore
```

Output

```
Temperature: 26.3°C
Wind Speed: 11.5 km/h
```

---

# ⚙️ Intelligent Workflow

The application first determines whether the request requires a tool or AI reasoning.

### Tool Workflow

```
User
   │
   ▼
Tool Selector
   │
   ▼
Tool Executor
   │
   ▼
Calculator / Weather Tool
   │
   ▼
Result
```

### AI Workflow

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

# 📂 Project Structure

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
├── tests/
│   ├── test_calculator.py
│   ├── test_weather.py
│   ├── test_selector.py
│   ├── test_executor.py
│   ├── test_registry.py
│   └── test_workflow.py
│
├── tools/
│   ├── calculator.py
│   └── weather.py
│
├── workflows/
│   ├── main_workflow.py
│   ├── tool_selector.py
│   ├── tool_executor.py
│   └── tool_registry.py
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

# 🛠️ Technologies Used

- Python 3.12
- LangChain
- Google Gemini API
- Streamlit
- Requests
- Open-Meteo API
- python-dotenv

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-agent-coordination-engine.git

cd ai-agent-coordination-engine
```

## Create a Virtual Environment

```bash
python3 -m venv .venv
```

## Activate the Virtual Environment

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# ▶️ Run the Project

## Terminal Interface

```bash
python app.py
```

## Streamlit Interface

```bash
streamlit run ui.py
```

---

# 🧪 Sample Inputs

### AI Task

```
Build a Hospital Management System
```

### Calculator

```
25 * 67
```

### Weather

```
Weather in Bangalore
```

---

# ✅ Testing

The project includes dedicated unit tests for major components.

```
python -m tests.test_calculator

python -m tests.test_weather

python -m tests.test_selector

python -m tests.test_executor

python -m tests.test_registry

python -m tests.test_workflow
```

---

# 🚀 Future Enhancements

- Multi-Agent Coordinator
- Memory Integration
- Vector Database Support
- Additional Enterprise Tools
- FastAPI REST Services
- Docker Deployment
- Authentication & User Management
- Multi-LLM Support

---

# 👩‍💻 Author

**Anjali Sharma**

Bachelor of Engineering (Computer Science & Engineering)

Infosys Springboard Virtual Internship Project
