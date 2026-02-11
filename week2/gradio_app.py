"""Week 2 - Gradio Chat App with Google Gemini"""
import os
from dotenv import load_dotenv
import gradio as gr
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

system_message = "You are a helpful assistant that answers questions about LLM engineering."


def message_chat(message, history):
    contents = []
    for h in history:
        role = h.get("role", "user") if isinstance(h, dict) else getattr(h, "role", "user")
        content = h.get("content", "") if isinstance(h, dict) else getattr(h, "content", "")
        gemini_role = "model" if role == "assistant" else role
        if gemini_role != "system":
            contents.append(
                types.Content(
                    role=gemini_role,
                    parts=[types.Part.from_text(text=content or "")],
                )
            )
    user_content = message.get("content", message) if isinstance(message, dict) else (getattr(message, "content", None) or message)
    contents.append(
        types.Content(role="user", parts=[types.Part.from_text(text=user_content or "")])
    )
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(system_instruction=system_message),
    )
    for chunk in stream:
        if chunk.text:
            yield chunk.text


def run():
    view = gr.ChatInterface(fn=message_chat,type="messages")
    view.launch()




if __name__ == "__main__":
    run()