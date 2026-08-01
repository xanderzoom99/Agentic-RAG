# Agentic RAG with LangGraph

An Agentic Retrieval-Augmented Generation (RAG) application built using **LangGraph**, **LangChain**, **FastAPI**, and **FAISS**. The application retrieves relevant information from a PDF knowledge base and uses an LLM to generate accurate responses through tool calling.

## Features

- 📄 PDF document loading
- ✂️ Recursive text splitting
- 🔍 HuggingFace embeddings (BAAI/bge-small-en-v1.5)
- 🗂️ FAISS vector database
- 🤖 LangGraph agent with tool calling
- 🔎 Retrieval-Augmented Generation (RAG)
- ⚡ FastAPI REST API
- 📖 Interactive Swagger documentation

## Tech Stack

- Python
- LangChain
- LangGraph
- FastAPI
- FAISS
- HuggingFace Embeddings
- Groq
- Pydantic

## Project Structure

```text
src/
├── graph.py
├── state.py
├── tools.py
├── llm.py
├── retriever.py
├── vector_store.py
├── embeddings.py
├── splitter.py
├── loader.py
└── main.py
```

## Installation

```bash
git clone <https://github.com/xanderzoom99/Agentic-RAG/>
cd <Agentic-RAG>

uv sync
```

## Run the API

```bash
uv run uvicorn src.main:api --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

## API Endpoint

**POST** `/chat`

Example request:

```json
{
  "query": "How do I deploy FastAPI on AWS?"
}
```

Example response:

```json
{
  "answer": "..."
}
```

## Future Improvements

- Save and load the FAISS index
- Chat history and memory
- Streaming responses
- Docker support
- Cloud deployment (AWS/Render)

## License

This project is for learning and educational purposes.
