from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str

# passing usery query to agent
from agent import (
    run_agent, 
    create_state
    )

app = FastAPI()

@app.post("/chat")
def chat(request: ChatRequest):
    return run_agent(request.question)
