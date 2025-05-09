import os
from dotenv import load_dotenv

from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.tools import DuckDuckGoSearchRun
import uvicorn

load_dotenv()

app = FastAPI()

# Define input structure
class Query(BaseModel):
    question: str

# Build agent
llm = ChatOpenAI(temperature=0)
search = DuckDuckGoSearchRun()
tools = [Tool(name="Search", func=search.run, description="Search for current events")]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

@app.post("/ask")
def ask_agent(query: Query):
    result = agent.run(query.question)
    return {"response": result}

# Optional: test route
@app.get("/")
def read_root():
    return {"message": "Agent is live. POST to /ask"}

# Only needed for local runs (won't be used by Fly)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
