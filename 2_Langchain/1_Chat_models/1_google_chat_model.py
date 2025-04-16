# Type this ===============================================
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Sample
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
result = llm.invoke("Hello How are you ?")
print(result.content)
# Type this ===============================================