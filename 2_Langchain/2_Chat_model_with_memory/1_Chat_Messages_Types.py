from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Your code goes here
messages = []

result = llm.invoke(messages)
messages.append(AIMessage(result.content))
print(result.content)