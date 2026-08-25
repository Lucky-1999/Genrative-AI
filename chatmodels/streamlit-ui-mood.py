import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# -----------------------------
# Model
# -----------------------------
model = ChatMistralAI(
    model_name="mistral-small-2506",
    temperature=0.7
)


# -----------------------------
# AI Modes
# -----------------------------
MODES = {
    "😡 Angry AI Agent": (
        "You are an Angry AI agent. "
        "Your responses should be angry and aggressive."
    ),

    "😂 Funny AI Agent": (
        "You are a Funny AI agent. "
        "Your responses should be humorous and entertaining."
    ),

    "😢 Sad AI Agent": (
        "You are a Sad AI agent. "
        "Your responses should be empathetic and understanding."
    )
}


# -----------------------------
# Initialize session state
# -----------------------------
if "selected_mode" not in st.session_state:
    st.session_state.selected_mode = "😂 Funny AI Agent"

if "message" not in st.session_state:
    st.session_state.message = [
        SystemMessage(
            content=MODES[st.session_state.selected_mode]
        )
    ]


# -----------------------------
# Function to change AI mode
# -----------------------------
def change_mode():
    selected_mode = st.session_state.mode_selector

    st.session_state.selected_mode = selected_mode

    # Completely reset conversation
    st.session_state.message = [
        SystemMessage(
            content=MODES[selected_mode]
        )
    ]


# -----------------------------
# UI
# -----------------------------
st.title("AI Agent")

st.write("Choose Your AI Mode")
st.write("Choose AI personality and start chatting")


choice = st.radio(
    "Select your AI mode:",
    list(MODES.keys()),
    horizontal=True,
    key="mode_selector",
    on_change=change_mode
)


# -----------------------------
# Display conversation
# -----------------------------
for msg in st.session_state.message:

    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)

    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)




# -----------------------------
# Chat input
# -----------------------------
prompt = st.chat_input("You:")


if prompt:

    if prompt == "0":

        st.write(
            "----------------- Thank you for using the application -----------------"
        )

    else:

        # Add user message
        st.session_state.message.append(
            HumanMessage(content=prompt)
        )

        # Display user message
        st.chat_message("user").write(prompt)

        # Invoke model
        response = model.invoke(
            st.session_state.message
        )

        # Add AI response
        st.session_state.message.append(
            AIMessage(content=response.content)
        )

        # Display AI response
        st.chat_message("assistant").write(
            response.content
        )