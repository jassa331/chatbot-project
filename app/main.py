from fastapi import FastAPI
from pydantic import BaseModel
from app.graph.chatbot_graph import app as chatbot_app
from fastapi.middleware.cors import CORSMiddleware


api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    question: str

@api.get("/jassa")
def jassa(question: str):

    result = chatbot_app.invoke({
        "question": question
    })

    return {
        "answer": result["answer"]
    }
    
@api.post("/chat")
def chat(request: ChatRequest):

    result = chatbot_app.invoke({
        "question": request.question
    })

    return {
        "answer": result["answer"]
    }