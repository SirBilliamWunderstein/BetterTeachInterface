
from dotenv import load_dotenv
import os

from google import genai

load_dotenv()  # Loads variables from .env

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

