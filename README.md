# 🏥 Project Health AI Service

An intelligent microservice built with **FastAPI** and **LangChain** to analyze project health status using LLM reasoning (Groq/Llama 3.1).

---

## 🚀 Features
* **AI-Driven Audit**: Analyzes project tasks, goals, and comments to detect risks.
* **Smart Status Classification**: Automatically assigns (Green, Yellow, Red) status based on custom hard rules.
* **Technical Blocker Detection**: Identifies bottlenecks like missing documentation or resource constraints from unstructured text.
* **FastAPI Backend**: High-performance API with automatic Swagger documentation.

## 🛠️ Tech Stack
* **Framework**: FastAPI
* **AI Orchestration**: LangChain
* **LLM Provider**: Groq (Llama-3.1-8b-instant)
* **Environment**: Python 3.13 / Miniconda

## 📦 Installation & Setup

1. **Clone the project**:
   ```bash
   git clone <your-repo-url>
   cd Project-Health

 2. **-Setup Environment**:
 Create a .env file in the root directory and add your Groq API Key:
      ```bash
      GROQ_API_KEY=your_api_key_here
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Run the Server**:
   ```bash
   uvicorn app.main:app --reload
---

## 🚥 API Endpoints

### `POST /api/v1/analyze-health`
Sends project metadata for AI analysis.

 **Sample Request Body:**
```json
{
  "project_name": "AI App",
  "main_goals": "Finish prototype",
  "tasks": [
    {
      "title": "API Integration",
      "status": "Overdue",
      "assigned_to": "Ahmed",
      "comments": "Blocked by missing docs"
    }
  ]
}
```
**Sample Successful Response (200 OK):**
```json
{
  "project_name": "AI App",
  "status": "Yellow",
  "progress": {
    "completed_tasks": 0,
    "total_tasks": 1
  },
  "schedule_risk": {
    "overdue_tasks": 1,
    "final_deadline_impact": "Medium"
  },
  "quality_check": {
    "technical_blockers": ["Missing documentation"]
  }
}
```
## 🧠 Logic Implementation

* **Consistency**: Uses a **Zero-Temperature** LLM configuration to ensure deterministic and stable project health assessments.
* **Robust Parsing**: Implements a **Regex cleaning layer** to extract valid JSON even if the model includes extra conversational text or Markdown formatting.
* **Reliability**: Uses synchronous execution for deep reasoning tasks to maintain stable response delivery within the FastAPI request-response cycle.

---
*Generated for Graduation Project - 2026*
