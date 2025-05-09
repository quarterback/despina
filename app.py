import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.tools import DuckDuckGoSearchRun

load_dotenv()

llm = ChatOpenAI(temperature=0)
search = DuckDuckGoSearchRun()
tools = [Tool(name="Search", func=search.run, description="Search for current events")]
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

result = agent.run("What is the latest update on AI policy from the White House?")
print(result)
