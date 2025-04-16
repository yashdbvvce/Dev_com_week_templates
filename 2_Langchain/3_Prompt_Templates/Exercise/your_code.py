from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import lorem

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
    SystemMessage("You are a professional chef"),
]




def generate_response(food_dish):
    # Your code goes here
    # Your code goes gere
    # Write your prompt here
    prompt_template = """
    {food_dish}
    """

    return lorem.paragraph()
