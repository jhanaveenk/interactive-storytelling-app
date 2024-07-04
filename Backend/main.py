from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os
from pydantic import BaseModel

class Prompt(BaseModel):
    prompt: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.post("/generate")
async def generate(prompt: Prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt.prompt,
        max_tokens=150
    )

    story_part = response.choices[0].text.strip()
    return {"story": story_part}
