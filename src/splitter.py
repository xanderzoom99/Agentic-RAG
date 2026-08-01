from langchain_text_splitters import RecursiveCharacterTextSplitter
from .loader import load

def split():
    docs = load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    return splitter.split_documents(docs)