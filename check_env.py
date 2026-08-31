import os
from dotenv import load_dotenv

load_dotenv()

print("Current folder:", os.getcwd())
print("Key loaded:", os.getenv("GEMINI_API_KEY"))