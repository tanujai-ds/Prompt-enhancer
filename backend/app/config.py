"""Application Configuration"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

class Settings:
    """Application Settings"""
    GROQ_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODEL = "llama-3.3-70b-versatile"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost", "http://127.0.0.1"]
    API_VERSION = "v1"

settings = Settings()
