from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
import os
from dotenv import load_dotenv
load_dotenv()


dir_name = os.path.dirname(__file__)
file_path = os.path.join(dir_name, 'books','romeo_and_juliet.txt')
persistant_directory = os.path.join(dir_name, 'db_store','chroma_db_romeo_juliet')

if not os.path.exists(persistant_directory):

    # Path checking
    if not os.path.exists(file_path):
        raise FileExistsError("No file found")

    # Load data from document - (Single Chunk)
    loader = TextLoader(file_path)
    document_data = loader.load()

    # Split text in chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000,chunk_overlap=0)
    docs = text_splitter.split_documents(document_data)

    # Display information about the split documents
    print("\n--- Document Chunks Information ---")
    print(f"Number of document chunks: {len(docs)}")
    print(f"Sample chunk:\n{docs[0].page_content}\n")

    # Create embeddings function
    embeddings = GoogleGenerativeAIEmbeddings(
        model='models/embedding-001',
    )

    # Create and save a vector store
    db = Chroma.from_documents(docs, embeddings, persist_directory=persistant_directory)
    print("Vector store created successfully")

else:
    print("Vector Store already exists")
