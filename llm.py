from langchain_openai import ChatOpenAI  
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Initialize the model using ChatOpenAI
chat = ChatOpenAI(
    # 1. OpenRouter API Endpoint
    openai_api_base="https://openrouter.ai/api/v1",  
    model_name= "openrouter/auto",
    temperature= 0.7,#
    max_tokens= 500

)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is the capital of France?"),
    AIMessage(content="The capital of France is Paris."),
    HumanMessage(content="give me tips to learn GO programming language"),
]

response = chat.invoke(messages)
print(response.content)