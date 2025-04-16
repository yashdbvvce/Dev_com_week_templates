from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
    SystemMessage("You are a professional chef"),
]



def generate_response(food_dish):
    # Type this ===============================================
    # Write your prompt here
    prompt_template = """
    Give me only the ingredients for this food this
    {food_dish}
    """
    prompt_template_ = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt_template_.invoke({"food_dish": food_dish})
    messages.extend(prompt.to_messages())
    result = llm.invoke(messages)
    return result.content
    # Type this ===============================================