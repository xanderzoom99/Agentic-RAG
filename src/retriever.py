from .vector_store import vectore_db

def retriever():
    return vectore_db.as_retriever()
retriever_db=retriever()
