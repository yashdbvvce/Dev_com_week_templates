from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
        ("system","You are a comedien who tells jokes on the following {topic}."),
        ("human","Tell ne {no_of_jokes} jokes")
]

prompt = ChatPromptTemplate.from_messages(messages)

# Types this
# ========================================================
to_upper = ""
word_count = ""
# ========================================================

chain = prompt | llm | StrOutputParser() | to_upper | word_count
result = chain.invoke({"topic":"cats","no_of_jokes":5})
print(result)