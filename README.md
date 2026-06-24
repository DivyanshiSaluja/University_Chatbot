# University Chatbot

A multi-agent AI chatbot for university query resolution, built using **LangGraph** and **Ollama (local LLM)**. The bot intelligently routes student queries to specialized agents based on the topic — admissions, academics, hostel, placement, or personal memory.

---

# Architecture Overview

```
User Input
    ↓
extractor_profile   →   Extracts student name & registration number
    ↓
classify_query      →   Classifies query into a category
    ↓
agent_router        →   Conditional routing via LangGraph
    ↓
┌──────────────────────────────────────────┐
│  academic_agent  │  Routes academic queries (syllabus, exams)     │
│  admission_agent │  Routes admission queries (fees, eligibility)  │
│  hostel_agent    │  Routes hostel queries (rooms, mess, wifi)      │
│  placement_agent │  Routes placement queries (packages, companies) │
│  memory_agent    │  Recalls student-specific info from memory      │
└──────────────────────────────────────────┘
    ↓
Structured Response to User
```

---

# Project Structure

```
university_chatbot/
│
├── agents/
│   ├── academic_agent.py       # Handles academic queries
│   ├── admission_agent.py      # Handles admission queries
│   ├── hostel_agent.py         # Handles hostel queries
│   ├── placement_agent.py      # Handles placement queries
│   └── memory_agent.py         # Recalls student profile info
│
├── graph/
│   ├── University_state.py     # LangGraph shared state definition
│   ├── router.py               # Conditional edge routing function
│   └── workflow.py             # Full LangGraph graph construction
│
├── knowledge_base/
│   ├── academic_kb.py          # Static academic knowledge base
│   ├── admission_kb.py         # Static admission knowledge base
│   ├── hostel_kb.py            # Static hostel knowledge base
│   └── placement_kb.py         # Static placement knowledge base
│
├── memory/
│   └── checkpoint.py           # SQLite-based memory/checkpointing
│
├── nodes/
│   ├── classifier.py           # Keyword-based query classifier node
│   └── extractor_profile.py    # Extracts student name & reg no
│
├── utils/
│   └── llm.py                  # Ollama LLM initialisation
│
├── app.py                      # Entry point — runs the chatbot
├── requirements.txt            # Python dependencies
└── README.md
```

---

# Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | [LangGraph](https://github.com/langchain-ai/langgraph) |
| LLM | [Ollama](https://ollama.com) (local, no API key needed) |
| Memory | SQLite via `langgraph-checkpoint-sqlite` |
| Language | Python 3.10+ |

---

# Getting Started

# 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/university_chatbot.git
cd university_chatbot
```

# 2. Install dependencies
```bash
pip install -r requirements.txt
```

# 3. Pull the Ollama model
```bash
ollama pull llama3
```
> Make sure [Ollama](https://ollama.com/download) is installed and running locally.

# 4. Run the chatbot
```bash
python app.py
```

---

# Example Queries

| Query | Routed To |
|---|---|
| *"What is the B.Tech fee?"* | `admission_agent` |
| *"Tell me about hostel facilities"* | `hostel_agent` |
| *"What companies visit for placement?"* | `placement_agent` |
| *"What is my name?"* | `memory_agent` |
| *"When is the end semester exam?"* | `academic_agent` |

---

# Key Design Decisions

- **LangGraph StateGraph** is used for deterministic, inspectable agent routing
- **Keyword-based classifier** keeps the MVP lightweight without requiring an LLM call for routing
- **SQLite checkpointing** gives the bot session memory across turns
- **Modular agents** make it easy to extend — add a new agent by adding a node and an edge

---

# Future Improvements

- [ ] Replace keyword classifier with LLM-based intent detection
- [ ] Add web search tool for real-time university data
- [ ] Expose as REST API with FastAPI
- [ ] Add WhatsApp/Telegram integration
- [ ] Role-based access (student vs staff)

---

# Author

Built as a portfolio project to demonstrate multi-agent AI orchestration using LangGraph.
