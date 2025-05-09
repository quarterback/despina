import os
os.environ["STREAMLIT_SERVER_PORT"] = "8080"
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.tools import DuckDuckGoSearchRun

load_dotenv()

st.set_page_config(page_title="Despina", page_icon="🧠")
st.title("🧠 Despina: Agent Experience Demo")
st.markdown("Ask a question to observe how an AI agent reasons, uses tools, and produces output in monitored environments.")

question = st.text_input("What do you want to ask the agent?", "")
if st.button("Run Agent") and question:
    with st.spinner("Agent thinking..."):
        try:
            llm = ChatOpenAI(temperature=0)
            search = DuckDuckGoSearchRun()
            tools = [Tool(name="Search", func=search.run, description="Search for current events")]
            agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
            result = agent.run(question)
            st.success(result)
            st.markdown("🔍 [View LangSmith Traces](https://smith.langchain.com/o/projects)")
        except Exception as e:
            st.error(f"Agent failed: {e}")
