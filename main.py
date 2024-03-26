import streamlit as st

st.title("Streamlit Conversation App")

# this should have two containers (one for user and one for assistant)
# and a input box for user

# initialize the session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# iterate through the messages in the session state
# and display them in the chat message container
# message["role"] is used because we need to identify user and bot
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# check if user made a chat input 
prompt = st.chat_input("What is up?")
if prompt:
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # add message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        st.markdown(response)

    # add the echo message to chat history
    st.session_state.messages.append({"role":"assistant","content":response})
