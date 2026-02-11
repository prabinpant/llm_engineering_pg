"""Week 2 - Gradio Chat App with Google Gemini"""
import os
from dotenv import load_dotenv
import gradio as gr
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

system_message = "You are a helpful assistant for an Airline clled FlightAI. Give short, courteous answers, no more than 1 sentence. Always be accurate. If you dont know the answer, say so."

ticket_prices = {"New York": 200, "Los Angeles": 300, "Chicago": 250, "Houston": 225, "Miami": 350}

def get_ticket_price(city):
    print(f"Getting ticket price for {city}")
    return ticket_prices.get(city, "Unknown city")

price_function = {
    "name" : "get_ticket_price",
    "description" : "Get the ticket price for a given city",
    "parameters" : {
        "type" : "object",
        "properties" : {
            "destination_city" : {"type": "string", "description": "The city to get the ticket price for"}
        },
        "required" : ["destination_city"],
        "additionalProperties" : False,
    }
}

tools = [{"type": "function", "function": price_function}]


def message_chat(message, history):
    history = history or []
    contents = []
    for h in history:
        role = h.get("role", "user") if isinstance(h, dict) else getattr(h, "role", "user")
        content = h.get("content", "") if isinstance(h, dict) else getattr(h, "content", "")
        gemini_role = "model" if role == "assistant" else role
        if gemini_role != "system":
            contents.append(types.Content(role=gemini_role, parts=[types.Part.from_text(text=content or "")]))
    contents.append(types.Content(role="user", parts=[types.Part.from_text(text=message or "")]))
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_message,
            response_mime_type="text/plain",
        ),
    )
    for chunk in stream:
        text = getattr(chunk, "text", None)
        if text:
            yield text


def run():
    view = gr.ChatInterface(fn=message_chat, type="messages")
    view.launch()



if __name__ == "__main__":
    run()