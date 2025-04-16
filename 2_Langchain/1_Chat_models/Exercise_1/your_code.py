# Imports Required
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

# Update this function
def generate_response(user_input):
    # Your code goes here
    # Type this ===============================================
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
    result = llm.invoke("Hello How are you ?")
    return result.content
    # Type this ===============================================