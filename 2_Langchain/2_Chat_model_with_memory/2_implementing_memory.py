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
    # Type this ===============================================
    messages.append(HumanMessage(user_input))
    # Type this ===============================================
    result = llm.invoke(messages)
    # Type this ===============================================
    messages.append(AIMessage(result.content))
    # Type this ===============================================
    print(result.content)