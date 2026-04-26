from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
from config import GROQ_API_KEY
from prompts import build_system_prompt

app = FastAPI()

# Add CORS middleware to allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=GROQ_API_KEY)


@app.get("/")
def root():
    return {"status": "Backend is running", "endpoint": "/improve"}


@app.get("/improve")
def improve(prompt: str, techniques: str = ""):
    try:
        system_prompt = build_system_prompt(techniques)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        return {"result": response.choices[0].message.content}
    
    except Exception as e:
        return {"error": str(e)}