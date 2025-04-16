import os
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


# Define the persistent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "db_store", "chroma_db_romeo_juliet")

# Define the embedding model
embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001',)

# Load the existing vector store with the embedding function
db = Chroma(persist_directory=persistent_directory,embedding_function=embeddings)

# Define the user's question
query = "How did juliet Die ? Explain in detail ?"

# Retrieve relevant documents based on the query
retriever = db.as_retriever(search_type="similarity",search_kwargs={"k": 1})
relevant_docs = retriever.invoke(query)

# Display the relevant results with metadata
print("\n--- Relevant Documents ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")

# Combine the query and the relevant document contents
# Types this
# ========================================================
docs_combined = "\n\n".join([doc.page_content for doc in relevant_docs])
combined_input = (
    "Here are some documents that might help answer the question: "
    + query
    + "\n\nRelevant Documents:\n"
    + docs_combined
    + "\n\nPlease provide an answer based only on the provided documents. If the answer is not found in the documents, respond with 'I'm not sure'."
)
# ========================================================

# Create a ChatOpenAI model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define the messages for the model
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=combined_input),
]

# Invoke the model with the combined input
result = model.invoke(messages)

# Display the full result and content only
print("\n--- Generated Response ---")
print(result.content)