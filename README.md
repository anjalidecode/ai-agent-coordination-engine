# 🤖 AI Agent Coordination & Decision Engine

A multi-agent AI application developed using **Python**, **LangChain**, and **Google Gemini**.

This project demonstrates how multiple AI agents collaborate to solve complex tasks by intelligently coordinating specialized agents and custom enterprise tools. The system combines AI-powered reasoning with intelligent tool routing, enabling efficient workflow automation and decision support.

---

# 📌 Project Overview

Modern enterprise workflows often require multiple AI agents working together while interacting with external tools and APIs. This project implements an AI Agent Coordination & Decision Engine capable of:

- Coordinating multiple AI agents
- Selecting and executing appropriate tools
- Integrating with external APIs
- Supporting intelligent decision-making
- Providing modular and scalable workflow architecture

---

# 📌 Milestone 1 (Weeks 1–2)

## Objective

Establish the core AI agent framework and development environment.

### Completed Tasks

- Configured LangChain and required dependencies
- Developed foundational AI agents
- Implemented prompt templates
- Created agent interaction workflows
- Built a basic Streamlit testing interface

---

# 📌 Milestone 2 (Weeks 3–4)

## Objective

Enable AI agents to interact with enterprise tools and external APIs through intelligent tool selection and coordinated action execution.

### Completed Tasks

- Developed custom enterprise tools
- Integrated external REST APIs
- Implemented Tool Registry
- Built intelligent Tool Selector
- Developed Tool Executor
- Added exception handling
- Validated tool execution accuracy
- Created unit tests for workflow components

---

# 🏗️ System Architecture

```
                           User
                             │
                ┌────────────┴────────────┐
                │                         │
         Intelligent Tool Selector    AI Agent Workflow
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

## Planner Agent

- Breaks complex user requests into structured implementation plans.
- Organizes tasks into logical execution steps.

---

## Research Agent

- Analyses the generated plan.
- Suggests suitable technologies, APIs, frameworks, and best practices.

---

## Decision Agent

- Evaluates research findings.
- Produces the final recommendation with reasoning and implementation guidance.

---

# 🛠️ Enterprise Tools

## Calculator Tool

A custom enterprise tool that performs mathematical computations without invoking the LLM.

### Example

```
25 * 67
```

Output

```
1675
```

---

## Weather Information Tool

An external API-integrated tool that retrieves real-time weather information using the **Open-Meteo REST API**.

### Features

- Live weather information
- REST API integration
- Enterprise-style API connector
- Real-time temperature and wind speed

### Example

```
Weather in Bangalore
```

Output

```
Temperature: 26.4°C
Wind Speed: 12.5 km/h
```

---

# ⚙️ Intelligent Workflow

The application first determines whether the request requires an AI workflow or a specialized tool.

## Tool Execution Workflow

```
User Request
      │
      ▼
Tool Selector
      │
      ▼
Tool Registry
      │
      ▼
Tool Executor
      │
      ▼
Calculator / Weather Tool
      │
      ▼
Final Response
```

---

## AI Agent Workflow

```
User Request
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
│   ├── tool_registry.py
│   ├── tool_selector.py
│   └── tool_executor.py
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

# ✨ Features

- Multi-Agent Collaboration
- Planner Agent
- Research Agent
- Decision Agent
- Intelligent Tool Selection
- Enterprise Tool Registry
- Tool Executor
- Calculator Tool
- Weather API Integration
- Streamlit Web Interface
- Command-Line Interface
- Modular Architecture
- Unit Testing

---

# 🛠️ Technologies Used

- Python 3.12
- LangChain
- Google Gemini
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

---

## Create Virtual Environment

```bash
python3 -m venv .venv
```

---

## Activate Environment

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

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

# ▶️ Run the Application

## Terminal

```bash
python app.py
```

---

## Streamlit

```bash
streamlit run ui.py
```

---

# 🧪 Sample Inputs

## AI Agent Task

```
Build a Hospital Management System
```

---

## Calculator Tool

```
25 * 67
```

---

## Weather Tool

```
Weather in Bangalore
```

---

# ✅ Testing

Execute the following tests from the project root.

```bash
python -m tests.test_calculator
```

```bash
python -m tests.test_weather
```

```bash
python -m tests.test_selector
```

```bash
python -m tests.test_registry
```

```bash
python -m tests.test_executor
```

```bash
python -m tests.test_workflow
```

---

# 🚀 Future Enhancements

- Multi-Agent Coordinator
- Shared Memory Integration
- Long-Term Memory
- Vector Database Support
- FastAPI REST APIs
- Enterprise Database Integration
- Additional Enterprise Tools
- Workflow Automation Engine
- Authentication & User Management
- Multi-LLM Support
- Docker Deployment

---

# 👩‍💻 Author

**Anjali Sharma**

Bachelor of Engineering (Computer Science & Engineering)

Developed as part of the **Infosys Springboard Virtual Internship**.
