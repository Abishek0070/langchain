from langchain_openai import ChatOpenAI

# LangChain will synchronously look for the OPENAI_API_KEY environment variable.
llm = ChatOpenAI(model="gpt-3.5-turbo")

# This synchronous method is now fine.
response = llm.invoke("write me a essay with 500 words with introduction, body, conlusion on large cybersecurity and tools ")
print(response.content)




