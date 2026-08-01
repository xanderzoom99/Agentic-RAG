from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm_model = ChatGroq(
    model_name="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2,
)