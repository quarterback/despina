import streamlit as st
import requests

st.set_page_config(page_title="Despina", page_icon="🧠")

st.title("🧠 Despina: Agent Experience Demo")
st.markdown("This prototype monitors how agents reason, interact, and break. It sends each prompt to a deployed LangChain agent running with real-time observability in [LangSmith](https://smith.langchain.com).")

st.markdown("---")

question = st.text_input("Enter a prompt for the agent:")
run_button = st.button("Send to Agent")

if run_button and question:
    with st.spinner("Agent thinking..."):
        try:
            response = requests.post(
                "http://localhost:8080/ask",  # Internal to container
                json={"question": question},
                timeout=20
            )
            if response.status_code == 200:
                agent_reply = response.json().get("response", "")
                st.success(agent_reply)

                # Placeholder trace link (manual for now)
                st.markdown("🔍 View trace in [LangSmith](https://smith.langchain.com/o/projects)")
            else:
                st.error(f"Agent failed with status code {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")
