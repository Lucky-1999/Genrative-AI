from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatMistralAI(
    model_name="mistral-small-2506",temperature=0.7)

print("----------------- Welcome type 0 to exit the application ----------------- ")

message = [
    SystemMessage(content="You are a funny AI agent."),
]
while True:
    prompt = input("You: ")
    message.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot: ", response.content)

print(message)
print("----------------- Thank you for using the application ----------------- ")

