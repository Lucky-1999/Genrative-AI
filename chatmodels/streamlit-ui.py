import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


model = ChatMistralAI(
    model_name="mistral-small-2506",
    temperature=0.7
)


st.title("Sad AI Agent")

# Initialize messages
if "message" not in st.session_state:
    st.session_state.message = [
        SystemMessage(content="You are a Sad AI agent.")
    ]

# Display previous conversation
for msg in st.session_state.message:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)

    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)


prompt = st.chat_input("You:")

if prompt:
    if prompt == "0":
        st.write("Thank you for using the application")
    else:
        # Add user message
        st.session_state.message.append(
            HumanMessage(content=prompt)
        )

        # Display user message
        st.chat_message("user").write(prompt)

        # Get response
        response = model.invoke(st.session_state.message)

        # Add AI response
        st.session_state.message.append(
            AIMessage(content=response.content)
        )

        # Display AI response
        st.chat_message("assistant").write(response.content)