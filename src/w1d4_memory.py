"""
Week 1 Day 4 - Memory Practice
Working with conversation memory using Google Gemini
"""
import os
from dotenv import load_dotenv
from google import genai


def run():
    """Main function to run this practice module"""
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


if __name__ == "__main__":
    run() 