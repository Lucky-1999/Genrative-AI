from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimensions = 64
)

vector = embeddings.embed_query("What is data science?")
print(vector)