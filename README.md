# ✍️ AI Blog Generation – End-to-End Agentic Workflow  

## 📌 Overview
**AI Blog Generator** is an end-to-end **agentic AI application** that automates blog creation.  
It uses **LangChain** for LLM orchestration, **LangGraph** for workflow management, and **FastAPI** for serving results via APIs.  

The system is powered by two collaborative AI agents:
1. **Title Agent** → Generates catchy, SEO-friendly blog titles.  
2. **Content Agent** → Expands the title into a full-length blog post with structured sections.  

This makes it easy to generate professional blogs in seconds.

---

## 🚀 Features
- 📰 **Automated Blog Writing** – From idea to full article.  
- ✨ **Two-Agent Collaboration**:  
  - **Title Agent** → Creates engaging titles.  
  - **Content Agent** → Generates well-structured blogs.  
- 🔗 **LangGraph Workflow** – Manages multi-agent pipeline seamlessly.  
- ⚡ **FastAPI Backend** – RESTful API for blog generation.  
- 📑 **JSON & Markdown Outputs** – Blogs available in multiple formats.  

---

## 🏗️ Architecture
1. **User Request** → Send blog topic via FastAPI endpoint.  
2. **Title Agent** → Suggests best possible blog titles.  
3. **Content Agent** → Writes blog based on chosen title.  
4. **LangGraph Orchestration** → Ensures smooth multi-step execution.  
5. **Response** → Returns final blog in structured format.  

---

## 📂 Project Structure
blog-generation/
│── .env # Environment variables (API keys, configs)
│── .gitignore
│── app.py # FastAPI entry point
│── main.py # Alternative entry / test runner
│── pyproject.toml
│── requirements.txt
│── request.json # Sample request body
│── README.md
│── uv.lock
│
├── src/ # Core project source code
│ ├── graphs/ # LangGraph workflow definitions
│ │ ├── init.py
│ │ └── graph_builder.py
│ │
│ ├── llms/ # LLM integrations
│ │ ├── init.py
│ │ └── groqlm.py
│ │
│ ├── nodes/ # Agent node definitions
│ │ ├── init.py
│ │ └── blog_node.py
│ │
│ └── states/ # Workflow states
│ ├── init.py
│ └── blogstate.py
│
├── .venv/ # Virtual environment
└── pycache/ # Cache files

---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone https://github.com/hero0p/ai-blog-generator.git
cd ai-blog-generator

### 2. Create Virtual Environment

python -m venv .venv

source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run FastAPI Server

uvicorn main:app --reload