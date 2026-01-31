from langchain_groq import ChatGroq # type: ignore
from app.core.config import settings

def get_llm():
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0,
        model_kwargs={"response_format": {"type": "json_object"}} 
    )