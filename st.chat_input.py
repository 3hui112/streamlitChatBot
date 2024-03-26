import streamlit as st

# title of the app
st.title("Streamlit new chat elements")

prompt = st.chat_input(placeholder = "Input here")
if prompt:
    st.markdown(f"Echo is working: {prompt}")
