from fastapi import FastAPI
from pydantic import BaseModel
from .graph import app
from langchain_core.messages import HumanMessage
from pprint import pprint

api=FastAPI()

class ChatRequest(BaseModel):
    query: str

@api.get("/")
def home():
    return {"message":"Agentic RAG running"}


@api.post("/chat")
def chat(request:ChatRequest):
    response = app.invoke(
            {
                "messages": [
                    HumanMessage(content=request.query)
                ]
            }
        )
    return {"answer":pprint(response["messages"][-1].content)}
