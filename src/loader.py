from pathlib import Path
path=Path("data/FastAPI.pdf")
print(path.exists())
print(path.name)
from langchain_community.document_loaders import PyPDFLoader

def load():
    loader=PyPDFLoader(str(path))
    return loader.load()
