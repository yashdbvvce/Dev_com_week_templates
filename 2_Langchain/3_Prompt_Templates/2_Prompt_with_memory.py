from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Your code goes here
messages = []

prompt_template = ChatPromptTemplate.from_messages(messages)

# Gives out a messages array
prompt = prompt_template.invoke({"topic":"Cats","no_of_jokes":5})
print(prompt)
response = llm.invoke(prompt)
print(response.content)