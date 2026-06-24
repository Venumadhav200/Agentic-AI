from fastapi import FastAPI
from pydantic import BaseModel
from backend.manager_agent import smart_manager

app = FastAPI()


class AgentRequest(BaseModel):
    question: str
    document: str | None = None


@app.post("/agent")
def run_agent(request: AgentRequest):

    result = smart_manager(request.question, request.document)

    return {"result": result}