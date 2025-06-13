from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()  # Load from .env

import os
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
db = Chroma(embedding_function=embedding, persist_directory="./chroma_db")

def add_to_db(title, text):
    doc = Document(page_content=text, metadata={"title": title})
    db.add_documents([doc])
    db.persist()

def get_similar_articles(query, k=3):
    return db.similarity_search(query, k=k)
