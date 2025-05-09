import os
os.environ["STREAMLIT_SERVER_PORT"] = "8080"
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
os.environ["STREAMLIT_SERVER_ADDRESS"] = "0.0.0.0"

import streamlit as st

st.title("Hello, Streamlit!")
