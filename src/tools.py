from langchain_core.tools import tool
from .retriever import retriever_db

@tool
def rag_tool(query: str) -> str:
    """Retrieve relevant documents."""
    docs = retriever_db.invoke(query)
    return "\n\n".join(doc.page_content for doc in docs)

tools = [rag_tool]