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
st.markdown("This prototype lets you observe agent behavior and trust integrity, with LangSmith traces in the background.")

question = st.text_input("Ask the agent anything:", "")
run_button = st.button("Run Agent")

if run_button and question:
    with st.spinner("Thinking..."):
        llm = ChatOpenAI(temperature=0)
        search = DuckDuckGoSearchRun()
        tools = [Tool(name="Search", func=search.run, description="Search for current events")]
        agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
        result = agent.run(question)
        st.success(result)
        st.markdown("🔍 [View LangSmith Traces](https://smith.langchain.com/o/projects)")
