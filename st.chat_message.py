import streamlit as st

# title of the app
st.title("Streamlit new chat elements")

with st.chat_message("user"):
    st.write("Hello 👋")

with st.chat_message("assistant"):
    st.write("Hello 👋 I'm assistant")
