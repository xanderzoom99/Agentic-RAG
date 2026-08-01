from langchain_huggingface import HuggingFaceEmbeddings

model_name="BAAI/bge-small-en-v1.5"

def embed():
    return HuggingFaceEmbeddings(model_name=model_name) 