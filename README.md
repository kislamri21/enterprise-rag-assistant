# Enterprise RAG Assistant

An AI-powered enterprise assistant that answers questions from internal company documents using Retrieval-Augmented Generation.

## Features

- FastAPI backend
- Document ingestion
- Text chunking
- Vector search with ChromaDB
- OpenAI-powered answer generation
- REST API endpoints
- GitHub-ready deployment

## Tech Stack

- Python
- FastAPI
- ChromaDB
- OpenAI API
- Uvicorn
- Render

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
