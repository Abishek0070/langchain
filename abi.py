from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

response = llm.invoke("write me a essay with 500 words with introduction, body, conlusion on large cybersecurity and tools ")
print(response.content)




