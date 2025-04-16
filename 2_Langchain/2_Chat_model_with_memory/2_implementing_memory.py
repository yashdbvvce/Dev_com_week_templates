from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
    HumanMessage("Hey! My Name is Yash D B? How are you?"),
]

while True:
    user_input = input("Type your message: ")
    # Your code goes below

    result = llm.invoke(messages)
    # Your code goes below

    print(result.content)