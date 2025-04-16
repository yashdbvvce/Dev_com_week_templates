# Imports Required
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# A list to store messages
messages = [
    SystemMessage("You are helpful assistant")
]


# Update this function
def generate_response(user_input):
    # Your code goes here

    # Solution
    messages.append(HumanMessage(user_input))
    result = llm.invoke(messages)
    messages.append(AIMessage(result.content))
    return result.content