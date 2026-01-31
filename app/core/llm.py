from langchain_google_genai import ChatGoogleGenerativeAI
from app.core.config import settings

def get_llm():
    """
    Initialize and return the Gemini LLM model.
    """
    return ChatGoogleGenerativeAI(
        model=settings.MODEL_NAME,
        google_api_key=settings.GEMINI_API_KEY,
        temperature=0.2  # Low temperature for more factual and consistent analysis
    )