from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4.1")

# print(model)

response = model.invoke("Hello, how are you?")
print(response.content)