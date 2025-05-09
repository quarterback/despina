import os
os.environ["LANGSMITH_PROJECT"] = "despina"


import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain_community.tools import DuckDuckGoSearchRun

# Streamlit setup
st.set_page_config(page_title="Despina", page_icon="🧠")
st.title("🧠 Despina")
st.caption("An agent observability prototype using LangChain + LangSmith")

st.markdown("Ask the agent a question and see how it reasons using real-time tool use and LLM prompts.")

# Input
question = st.text_input("Enter a question for the agent:")

# Run agent
if st.button("Run Agent") and question:
    with st.spinner("Thinking..."):
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
