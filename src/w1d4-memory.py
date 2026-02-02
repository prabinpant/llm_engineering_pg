import os
from dotenv import load_dotenv
from google import genai

load_dotenv(override=True)

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the capital of France?",
    config=genai.types.GenerateContentConfig(
        system_instruction="You are a helpful assistant that can answer questions and help with tasks.",
    ),
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What was my last message?",
    config=genai.types.GenerateContentConfig(
        system_instruction="You are a helpful assistant that can answer questions and help with tasks.",
    ),
)


print(response.text) 