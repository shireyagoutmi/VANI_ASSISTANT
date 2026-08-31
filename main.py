from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
print("Current folder:", os.getcwd())
print("Key loaded:", os.getenv("GEMINI_API_KEY"))



GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
app = FastAPI()
class AskRequest(BaseModel):
    message: str

@app.post("/ask")
def ask(request: AskRequest):
    reply = get_ai_response(request.message)
    return {"reply": reply}

@app.get("/hello")
def hello():
    return {"message": "Hello from VANI!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello {name} from VANI!"}

def get_ai_response(user_message: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_message
    )
    return response.text
