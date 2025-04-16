from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')


# You code goes here
TEMPLATE = ""
prompt_template = ""


# Gives out a messages array
prompt = prompt_template.invoke({"topic":"Cats"})
print(prompt)
response = llm.invoke(prompt)
print(response.content)