# LangSmith Tracing with Groq

## Overview

This project demonstrates how to integrate Groq LLMs with LangSmith for tracing and observability.

The application:

1. Accepts a user question.
2. Calls a tool function (`get_context`) to retrieve contextual information.
3. Sends the context and user question to a Groq-hosted LLM.
4. Returns the generated response.
5. Logs the complete execution flow in LangSmith.

The project helps developers understand:

* LLM application tracing
* LangSmith observability
* Tool execution tracking
* Groq API integration
* Prompt construction
* Parent-child trace relationships

---

# Project Architecture

```text
User Question
      │
      ▼
assistant()
      │
      ├── get_context() [Tool]
      │
      ▼
call_groq() [LLM]
      │
      ▼
Groq API
      │
      ▼
Llama Model
      │
      ▼
Response
      │
      ▼
User
```

---

# Technologies Used

* Python
* Groq API
* LangSmith
* python-dotenv

---

# Installation

## Clone Project

```bash
git clone <repository-url>
cd langsmith-tracing-project
```

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install groq
pip install langsmith
pip install python-dotenv
```

or

```bash
pip install groq langsmith python-dotenv
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

LANGSMITH_API_KEY=your_langsmith_api_key

LANGSMITH_TRACING=true

LANGSMITH_PROJECT=Groq-Tracing
```

---

# Getting API Keys

## Groq API Key

1. Create an account on Groq.
2. Open the API Keys section.
3. Generate a new API key.
4. Copy it to the `.env` file.

## LangSmith API Key

1. Create a LangSmith account.
2. Open Settings.
3. Navigate to API Keys.
4. Create a new key.
5. Add it to the `.env` file.

---

# Project Structure

```text
langsmith-tracing-project/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
└── venv/
```

---

# Core Components

## 1. LangSmith Tracing

The `@traceable` decorator records function execution details.

Example:

```python
@traceable
def assistant(question):
    ...
```

LangSmith tracks:

* Inputs
* Outputs
* Execution time
* Errors
* Nested calls

---

## 2. Tool Function

```python
@traceable(run_type="tool")
def get_context(question):
```

Purpose:

* Simulates a tool call.
* Returns contextual information.
* Appears as a Tool span in LangSmith.

In production this could:

* Query a database
* Search documents
* Retrieve vector embeddings
* Call external APIs

---

## 3. LLM Function

```python
@traceable(run_type="llm")
def call_groq(messages):
```

Purpose:

* Sends prompts to Groq.
* Receives model output.
* Appears as an LLM span in LangSmith.

---

## 4. Assistant Function

```python
@traceable
def assistant(question):
```

Purpose:

* Orchestrates the complete workflow.
* Calls tools.
* Builds prompts.
* Invokes the LLM.

Acts as the root trace.

---

# Running the Application

Start the application:

```bash
python app.py
```

Example:

```text
You: What is Python?

Assistant:
Python is a high-level programming language...
```

Exit:

```text
You: exit
```

---

# LangSmith Trace Visualization

Each user request generates a trace.

Example trace hierarchy:

```text
assistant
│
├── get_context (tool)
│
└── call_groq (llm)
```

The trace captures:

* User input
* Tool output
* Prompt sent to the model
* Model response
* Latency
* Errors

---

# Benefits of LangSmith

* Debug prompt issues
* Monitor application performance
* Inspect tool execution
* Analyze model outputs
* Track latency
* Understand application workflows

---

# Future Enhancements

This project can be extended with:

## RAG Pipeline

* PDF ingestion
* Text chunking
* Embeddings
* Vector databases
* Retrieval-augmented generation

## Multi-Tool Agents

* Search tools
* Calculator tools
* Database tools
* Web APIs

## LangGraph

* Stateful workflows
* Multi-agent systems
* Human-in-the-loop applications

## Production Monitoring

* Prompt analytics
* Latency tracking
* Cost tracking
* Error monitoring

---

# Learning Outcomes

After completing this project, you should understand:

* How LangSmith tracing works
* How decorators capture execution data
* How Groq APIs are integrated
* How prompts are structured
* How tools and LLMs interact
* How to debug AI applications using traces

This project serves as a foundation for building production-grade AI applications with observability and monitoring.
