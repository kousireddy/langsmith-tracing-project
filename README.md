# LangSmith Tracing and Evaluation with Groq

## Overview

This project demonstrates how to integrate **LangSmith** with **Groq LLMs** to perform:

* End-to-end tracing of AI applications
* Tool execution monitoring
* LLM call tracking
* Application observability
* Automated evaluation of model responses

The application uses a simple knowledge base tool and a Groq-powered LLM to answer user questions while capturing complete execution traces in LangSmith.

---

## Features

* LangSmith tracing integration
* Custom tool tracing
* Groq LLM integration
* Interactive chatbot interface
* Dataset-based evaluation
* Custom correctness evaluator
* Experiment tracking in LangSmith

---

## Project Structure

```text
langsmith-tracing-project/
│
├── .env
├── requirements.txt
├── README.md
│
├── app.py
├── evaluate.py
│
├── tools/
│   └── context_tool.py
│
├── llm/
│   └── groq_client.py
│
├── datasets/
│   └── evaluation_data.py
│
└── utils/
    └── config.py
```

---

## Tech Stack

* Python
* Groq API
* LangSmith
* Python Dotenv

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd langsmith-tracing-project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=LangSmith-Project1
```

---

## Running the Chatbot

```bash
python app.py
```

Example:

```text
You: What is Python?

Assistant: Python is a high-level programming language.
```

---

## LangSmith Tracing

Each request creates a trace:

```text
assistant
│
├── get_context (tool)
│
└── call_groq (llm)
```

The trace includes:

* User input
* Tool calls
* LLM requests
* LLM responses
* Execution metadata

---

## Running Evaluations

Create a dataset in LangSmith containing:

### Example 1

Input:

```json
{
  "question": "How long are LangSmith traces stored?"
}
```

Reference Output:

```json
{
  "expected": "14 days"
}
```

### Example 2

Input:

```json
{
  "question": "What is Python?"
}
```

Reference Output:

```json
{
  "expected": "programming language"
}
```

Run evaluation:

```bash
python evaluate.py
```

---

## Custom Evaluator

```python
def correctness(inputs, outputs, reference_outputs):

    answer = outputs["output"].lower()
    expected = reference_outputs["expected"].lower()

    return {
        "key": "correctness",
        "score": int(expected in answer)
    }
```

The evaluator checks whether the expected answer appears in the model response.

---

## Sample Trace Flow

```text
User Question
      ↓
assistant()
      ↓
get_context()
      ↓
call_groq()
      ↓
Groq Response
      ↓
LangSmith Trace
```

---

## Learning Outcomes

This project demonstrates:

* LLM Observability
* Prompt Monitoring
* Tool Tracing
* AI Application Debugging
* LangSmith Experiments
* Dataset Management
* Automated Evaluation
* Production AI Monitoring

---

## Future Enhancements

* RAG with PDF documents
* Vector Databases
* LangChain Integration
* LangGraph Agents
* Multi-tool Agents
* Advanced LLM Evaluators
* Hallucination Detection
* Response Relevance Scoring

---

## Author

Built as a hands-on learning project for understanding LangSmith Tracing, Evaluation, and Groq-powered AI applications.
