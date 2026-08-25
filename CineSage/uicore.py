from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Information Extractor",
    page_icon="📝",
    layout="centered"
)


# -----------------------------
# Model
# -----------------------------
model = ChatMistralAI(
    model="mistral-small-2506"
)


# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an intelligent information extraction and summarization assistant.

Your task is to analyze the given paragraph and extract the most useful
and relevant information from it.

Follow these rules:

1. Extract only information explicitly mentioned in the paragraph.
2. Do not add facts from your own knowledge.
3. Identify important entities, facts, dates, people, places, organizations,
   categories, and relationships wherever applicable.
4. Organize the extracted information into clear sections.
5. If a particular category is not present in the paragraph, do not include it.
6. Keep the extracted information concise and easy to read.
7. After extracting the information, provide a quick summary in 2-3 sentences.
8. The summary should capture the main subject, important facts, and key message.
9. Do not repeat unnecessary information.

For example, if the paragraph is about a movie, consider extracting:
- Movie Name
- Release Date / Year
- Language
- Country
- Genre
- Director
- Producer
- Cast
- Main Characters
- Plot
- Themes
- Key Message
- Achievements / Reception

For other types of content, dynamically determine which categories
are useful instead of forcing the movie-specific categories.

Return the response in the following format:

## Extracted Information

**[Category]:** [Information]

**[Category]:** [Information]

...

## Quick Summary

[2-3 sentence summary]
"""
    ),
    (
        "human",
        """
Analyze and extract useful information from the following paragraph:

{paragraph}
"""
    )
])


# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🎬 Movie Information Extractor")
st.write("Extract useful information and generate a quick summary from a paragraph.")

st.divider()

paragraph = st.text_area(
    "Enter movie paragraph",
    height=250,
    placeholder="Paste your paragraph here..."
)

extract_button = st.button(
    "Extract Information",
    type="primary",
    use_container_width=True
)


# -----------------------------
# Generate Response
# -----------------------------
if extract_button:

    if not paragraph.strip():
        st.warning("Please enter a paragraph.")
    else:
        with st.spinner("Analyzing paragraph..."):

            final_prompt = prompt.invoke(
                {"paragraph": paragraph}
            )

            response = model.invoke(final_prompt)

        st.divider()

        st.subheader("Extracted Information")

        st.markdown(response.content)