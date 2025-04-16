from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Type this ===============================================
TEMPLATE = "Tell me a joke on {topic}"
prompt_template = ChatPromptTemplate.from_template(TEMPLATE)
# Type this ===============================================

# Gives out a messages array
prompt = prompt_template.invoke({"topic":"CSK"})
print(prompt)
response = llm.invoke(prompt)
print(response.content)