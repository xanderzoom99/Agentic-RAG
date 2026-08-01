from langchain_community.vectorstores import FAISS
from .embeddings import embed
from .splitter import split

def vector_store():
    return FAISS.from_documents(documents=split(),embedding=embed())

vectore_db=vector_store()
