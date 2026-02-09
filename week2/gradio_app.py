"""Week 2 - Gradio Chat App with Google Gemini"""
import os
from dotenv import load_dotenv
import gradio as gr
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def chat(message, history):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=message,
    )
    return response.text


def run():
    demo = gr.ChatInterface(
        fn=chat,
        title="Gemini Chat",
        description="Chat with Google Gemini",
    )
    demo.launch()


if __name__ == "__main__":
    run()