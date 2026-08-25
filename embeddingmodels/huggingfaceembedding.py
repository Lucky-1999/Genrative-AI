from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = [
    "What is data science?",
    "What is machine learning?"
]
vectors = embeddings.embed_documents(text)
print(vectors)