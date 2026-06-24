from fastapi import FastAPI
from pydantic import BaseModel

from app.document_loader import load_document, chunk_text
from app.vector_store import add_documents
from app.rag_pipeline import answer_question

app = FastAPI(title="Enterprise RAG Assistant")


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Enterprise RAG Assistant is running"}


@app.post("/index")
def index_documents():
    text = load_document("data/company_policy.txt")
    chunks = chunk_text(text)
    add_documents(chunks)
    return {"message": "Documents indexed successfully", "chunks": len(chunks)}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = answer_question(request.question)
    return {"question": request.question, "answer": answer}
