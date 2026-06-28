# Career Mentor Agent

An AI-powered Career Mentor Agent built using **FastAPI**, **Google Gemini**, **ChromaDB**, and **Retrieval-Augmented Generation (RAG)**. The agent maintains user memory, retrieves relevant information from a knowledge base, analyzes missing skills, and generates personalized career guidance.

This project was built as part of my **AI Engineer Learning Journey** to understand how modern AI agents are designed by combining memory, state management, tools, vector databases, embeddings, and Large Language Models.

---

# Project Objective

Build a stateful AI agent capable of:

* Remembering user information
* Maintaining state throughout execution
* Retrieving relevant knowledge using RAG
* Identifying missing skills based on career goals
* Generating personalized learning recommendations using Gemini

---

# Tech Stack

* Python
* FastAPI
* Google Gemini 2.5 Flash
* Gemini Embedding Model
* ChromaDB
* PyPDF
* python-dotenv

---

# Project Architecture

```text
                  User
                    │
                    ▼
             FastAPI Endpoint
                    │
                    ▼
               Agent Runner
                    │
                    ▼
              Initialize State
                    │
                    ▼
             Recall User Memory
                    │
                    ▼
          Identify Missing Skills
                    │
                    ▼
      Retrieve Relevant Documents
           (ChromaDB + RAG)
                    │
                    ▼
          Generate Gemini Response
                    │
                    ▼
             Final Career Advice
```

---

# Project Structure

```text
career_mentor_agent/
│
├── app.py                  # FastAPI application
├── agent.py                # Agent orchestration
├── tools.py                # Agent tools
├── rag.py                  # ChromaDB operations
├── embeddings.py           # Gemini embeddings
├── documents_loader.py     # Reads knowledge base files
├── file_loader.py          # TXT, PDF and JSON loaders
├── memory.py               # User memory
├── state.py                # Agent state
│
├── knowledge_base/         # Documents used for RAG
├── chromaDB/               # Persistent vector database
├── .env.example            # API key
├── .gitignore              # Used for keeping API key locally
└── README.md
```

---

# Agent Workflow

### Step 1 — Receive User Question

The user sends a question through the FastAPI endpoint.

Example:

```text
What skills should I learn to become an AI Engineer?
```

---

### Step 2 — Initialize State

A fresh state object is created for the current request.

The state stores information such as:

* User memory
* Career goal
* Current skills
* Missing skills
* Retrieved documents
* User question

---

### Step 3 — Recall User Memory

The agent retrieves previously stored information including:

* Name
* Career Goal
* Existing Skills

---

### Step 4 — Skill Gap Analysis

The agent compares the user's existing skills with a predefined list of required AI Engineering skills and identifies missing skills.

Example:

Current Skills

* Python
* SQL

Missing Skills

* FastAPI
* ChromaDB
* RAG
* Docker
* Memory Management

---

### Step 5 — Retrieval-Augmented Generation (RAG)

The user's question is converted into an embedding using Gemini Embeddings.

The embedding is searched against the ChromaDB vector database.

The most relevant documents are retrieved and added to the agent's state.

---

### Step 6 — Generate Final Response

The agent sends the following context to Gemini:

* User Goal
* Current Skills
* Missing Skills
* Retrieved Knowledge

Gemini generates a personalized response using both the retrieved knowledge and the user's context.

---

# Features

* User memory management
* Shared agent state
* Skill gap analysis
* Document ingestion
* PDF, TXT and JSON support
* Gemini embeddings
* Persistent ChromaDB vector database
* Retrieval-Augmented Generation (RAG)
* Personalized AI career guidance

---

# Knowledge Base

The project supports multiple document formats:

* TXT
* PDF
* JSON

Documents are converted into embeddings and stored in ChromaDB for semantic search.

---

# Concepts Learned

This project combines several AI Engineering concepts into a single application:

* FastAPI
* State Management
* Memory
* AI Agent Architecture
* Tool-Based Design
* Embeddings
* Vector Databases
* ChromaDB
* Semantic Search
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Google Gemini API

---

# Challenges Solved

During development, the following engineering challenges were identified and resolved:

* Circular imports between modules
* Persistent ChromaDB collection management
* Embedding format conversion for ChromaDB
* Unique document ID generation
* State propagation across multiple tools
* Separation of tools and utility functions

These improvements resulted in a cleaner and more maintainable architecture.

---

# Future Improvements

* LLM Function Calling
* Dynamic tool selection
* Tool chaining
* Conversation history
* Long-term memory
* Multi-user support
* Planner-based agent workflow
* Docker deployment
* Cloud deployment
* Authentication and user profiles

---

# Sample Questions

* What skills am I missing to become an AI Engineer?
* Create a learning roadmap for me.
* Explain Retrieval-Augmented Generation (RAG).
* How should I prepare for AI Engineer interviews?
* What is ChromaDB?
* Recommend my next learning topics.

---

# Learning Outcome

This project helped me understand how an AI agent combines multiple AI engineering components into a complete workflow. Instead of calling an LLM directly, the agent retrieves user information, maintains state, searches a vector database for relevant context, and then generates grounded responses using Gemini.

This project represents my transition from building individual AI components to designing an integrated AI agent architecture.
