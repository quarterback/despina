import streamlit as st
import requests

st.set_page_config(page_title="Neptune Agent Demo")

st.title("🧠 Neptune Agent Interface")

question = st.text_input("Ask a question for the agent:", "")

if st.button("Run Agent") and question:
    with st.spinner("Thinking..."):
        response = requests.post(
            "http://localhost:8080/ask",
            json={"question": question}
        )
        if response.status_code == 200:
            st.success(response.json()["response"])
        else:
            st.error("Error calling the agent.")
