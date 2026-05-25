import os

import google.generativeai as genai

from dotenv import load_dotenv

from app.prompts import SYSTEM_PROMPT

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_response(user_message, history):

    prompt = SYSTEM_PROMPT + "\n\n"

    for msg in history:
        prompt += f"{msg['role']}: {msg['content']}\n"

    prompt += f"user: {user_message}"

    response = model.generate_content(
        prompt
    )

    return response.text