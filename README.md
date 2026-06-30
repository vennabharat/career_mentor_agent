# Career Mentor Agent

An AI-powered Career Mentor Agent that provides personalized AI engineering career guidance using Retrieval-Augmented Generation (RAG), user memory, state management, configurable LLM providers, and pluggable embedding models.

This project is part of my AI Engineer learning journey, where the goal is to understand how production-style AI applications are designed using clean software engineering principles rather than relying on a single LLM call.

---

# Features

- Modular AI Agent architecture
- State-driven execution pipeline
- User memory management
- Retrieval-Augmented Generation (RAG)
- ChromaDB vector database
- Configurable LLM providers
- Configurable embedding providers
- Factory Pattern implementation
- Loose coupling between components
- PDF, TXT and JSON knowledge ingestion
- Easily extendable architecture

---

# Tech Stack

- Python
- FastAPI
- Google Gemini
- Hugging Face
- Sentence Transformers
- ChromaDB
- python-dotenv
- PyPDF
- JSON

---

# Architecture

```
                     User
                       │
                       ▼
                 FastAPI Endpoint
                       │
                       ▼
                  Agent Runner
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
  Initialize State             Load Memory
         │                           │
         └─────────────┬─────────────┘
                       ▼
              Recall User Details
                       │
                       ▼
            Missing Skill Analysis
                       │
                       ▼
          Retrieve Relevant Documents
             (ChromaDB + Embeddings)
                       │
                       ▼
                Prompt Builder
                       │
                       ▼
               LLM Provider Factory
                       │
                       ▼
              Gemini / HuggingFace
                       │
                       ▼
                Personalized Answer
```

---

# Project Structure

```
career_mentor_agent/
│
├── app.py
├── agent.py
├── configuration.py
├── prompt.py
├── tools.py
├── state.py
├── memory.py
│
├── llm/
│   ├── base.py
│   ├── factory.py
│   ├── gemini_provider.py
│   └── huggingface_provider.py
│
├── embedding/
│   ├── base.py
│   ├── factory.py
│   ├── gemini_embedding.py
│   └── sentence_transformer_embedding.py
│
├── rag.py
├── embeddings.py
├── documents_loader.py
├── file_loader.py
│
├── knowledge_base/
│
├── chromaDB/
│
├── requirements.txt
└── README.md
```

---

# Agent Workflow

## 1. User submits a question

Example:

```
How can I become an AI Engineer?
```

---

## 2. Initialize Agent State

A fresh state object is created.

The state contains:

- Memory
- Career goal
- Existing skills
- Missing skills
- Retrieved documents
- User question
- Learning plan

---

## 3. Recall User Memory

The agent loads previously stored information such as:

- Goal
- Skills
- User profile

---

## 4. Skill Gap Analysis

The current skills are compared against the required AI Engineering skill set.

Example

Current Skills

```
Python
SQL
```

Missing Skills

```
FastAPI
Docker
RAG
ChromaDB
Memory
```

---

## 5. Retrieve Relevant Knowledge

The user's question is converted into an embedding.

Depending on the configuration, the embedding model can be:

- Sentence Transformers
- Gemini Embeddings

The generated embedding is searched against ChromaDB to retrieve the most relevant knowledge.

---

## 6. Prompt Construction

The prompt builder combines

- User goal
- Skills
- Missing skills
- Retrieved documents
- User question

into a single prompt sent to the LLM.

---

## 7. Response Generation

The prompt is passed to the configured LLM provider.

Supported providers include:

- Gemini
- Hugging Face

Switching providers requires only a configuration change.

---

# Factory Pattern

The project uses the Factory Pattern to decouple the application from specific AI providers.

## LLM Factory

```
get_llm("gemini")

get_llm("huggingface")
```

Both providers implement a common interface.

```
BaseLLM
    │
    ├── GeminiLLM
    └── HuggingFaceLLM
```

---

## Embedding Factory

```
get_embedding("sentence-transformers")

get_embedding("gemini")
```

Both embedding models expose the same interface.

```
BaseEmbedding
      │
      ├── GeminiEmbedding
      └── SentenceTransformerEmbedding
```

This allows changing embedding providers without modifying the RAG pipeline.

---

# Software Engineering Concepts Used

- Factory Pattern
- Dependency Inversion
- Interface-based design
- Loose Coupling
- High Cohesion
- Modular Architecture
- Configuration-driven provider selection

---

# Configuration

LLM provider

```python
llm = get_llm("gemini")
```

Embedding provider

```python
embedding_generator = get_embedding("sentence-transformers")
```

Changing providers requires modifying only the configuration file.

---

# Knowledge Base

The agent retrieves information from multiple document formats.

Supported formats

- PDF
- TXT
- JSON

Documents are embedded and stored in ChromaDB for semantic retrieval.

---

# Future Improvements

- Long-term conversational memory
- Persistent user profiles
- LangGraph integration
- Streaming responses
- Multi-agent architecture
- Tool calling
- Conversation history
- User authentication
- REST API deployment
- Docker support
- Cloud deployment
- Observability and logging

---

# Learning Outcomes

This project demonstrates practical implementation of:

- AI Agents
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Embedding Models
- LLM Provider Abstraction
- Factory Design Pattern
- State Management
- Memory Management
- Semantic Search
- Clean Software Architecture

---

# Author

**Bharat Venna**

AI Engineer | Building AI Agents, RAG Systems, and Production-ready LLM Applications.

GitHub:
https://github.com/vennabharat

LinkedIn:
https://www.linkedin.com/vennabharat/