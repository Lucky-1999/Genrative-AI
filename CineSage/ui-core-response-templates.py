from dotenv import load_dotenv
import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()


# Model
model = ChatMistralAI(
    model="mistral-small-2506"
)


# Pydantic Model
class Movie(BaseModel):
    title: str
    release_year: Optional[int] = None
    genre: List[str]
    director: Optional[str] = None
    cast: List[str]
    rating: Optional[float] = None
    summary: str


# Pydantic Output Parser
parser = PydanticOutputParser(
    pydantic_object=Movie
)


# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a movie information extraction assistant.

Extract the movie information from the given paragraph.

{format_instructions}
"""
    ),
    (
        "human",
        "{paragraph}"
    )
])


# Streamlit Configuration
st.set_page_config(
    page_title="🎬 Movie Information Extractor",
    page_icon="🎬"
)


# UI
st.title("🎬 Movie Information Extractor")

paragraph = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Enter a movie paragraph here..."
)


if st.button("Extract Movie Information", type="primary"):

    if not paragraph.strip():
        st.warning("Please enter a movie paragraph.")

    else:

        # Create final prompt
        final_prompt = prompt.invoke({
            "paragraph": paragraph,
            "format_instructions": parser.get_format_instructions()
        })

        # Call LLM
        response = model.invoke(final_prompt)

        # Parse LLM response into Pydantic object
        movie = parser.parse(response.content)

        # Convert Pydantic object to JSON
        movie_json = movie.model_dump()

        # Display JSON
        st.subheader("Extracted Movie Information")

        st.json(movie_json)