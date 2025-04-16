from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
        ("system","You are a comedian who tells jokes on the following {topic}."),
        ("human","Tell me {no_of_jokes} jokes")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

# Types this
# ========================================================
chain = prompt_template | llm | StrOutputParser()
result = chain.invoke({"topic":"RCB", "no_of_jokes":5})
print(result)
# ========================================================