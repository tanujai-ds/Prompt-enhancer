# Configuration settings
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from parent directory
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(env_path)

GROQ_API_KEY = os.getenv("OPENAI_API_KEY")