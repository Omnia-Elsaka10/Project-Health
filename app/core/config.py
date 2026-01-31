import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    # Get API key from environment variables
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
    # Using Gemini 1.5 Flash for speed and efficiency
    MODEL_NAME: str = "gemini-1.5-flash"

settings = Settings()