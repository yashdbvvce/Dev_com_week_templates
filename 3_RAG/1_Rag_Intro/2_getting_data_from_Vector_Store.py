from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv
load_dotenv()


# Required Directories
current_dir = os.path.dirname(__file__)
persistant_directory = os.path.join(current_dir, "db_store","chroma_db_romeo_juliet")

# Get the embedding function
embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')

# Get the stored Vector db
db = Chroma(
    persist_directory=persistant_directory,
    embedding_function=embeddings
)

# Query the user
# Change this line
query = "How did juliet die ?"

# Set up the retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)
relevant_docs = retriever.invoke(query)

doc_content = []

print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
    doc_content.append(f"\n{doc.page_content}\n")
print('\n'.join(doc_content))