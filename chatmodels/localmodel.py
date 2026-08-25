from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"max_length": 512, "temperature": 0.7, "top_p": 0.9}
)

chat_model = ChatHuggingFace(llm = llm)
response = chat_model.invoke("What is data science?")

print(response.content)