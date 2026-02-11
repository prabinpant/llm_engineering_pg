"""Week 2 - Gradio Chat App with Google Gemini (OpenAI client)"""
import json
import os
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

load_dotenv()

MODEL = "gemini-2.5-flash"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=GEMINI_BASE_URL,
)

system_message = "You are a helpful assistant for an Airline called FlightAI. Give short, courteous answers, no more than 1 sentence. Always be accurate. If you dont know the answer, say so."

ticket_prices = {"New York": 200, "Los Angeles": 300, "Chicago": 250, "Houston": 225, "Miami": 350}


def get_ticket_price(city):
    print(f"Getting ticket price for {city}")
    return ticket_prices.get(city, "Unknown city")


price_function = {
    "name": "get_ticket_price",
    "description": "Get the ticket price for a given city",
    "parameters": {
        "type": "object",
        "properties": {
            "destination_city": {"type": "string", "description": "The city to get the ticket price for"}
        },
        "required": ["destination_city"],
        "additionalProperties": False,
    },
}

tools = [{"type": "function", "function": price_function}]


def handle_tool_call(message):
    tool_call = message.tool_calls[0]
    if tool_call.function.name == "get_ticket_price":
        arguments = json.loads(tool_call.function.arguments)
        city = arguments.get('destination_city')
        price_details = get_ticket_price(city)
        response = {
            "role": "tool",
            "content": price_details,
            "tool_call_id": tool_call.id
        }
    return response


def message_chat(message, history):
    print(f"Message: {message}")
    history = [{"role":h["role"], "content":h["content"]} for h in history]
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    response = client.chat.completions.create(model=MODEL, messages=messages, tools=tools)
    
    print(f"Messages: {messages}")
    
    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        response = client.chat.completions.create(model=MODEL, messages=messages)

    return response.choices[0].message.content


def run():
    view = gr.ChatInterface(fn=message_chat)
    view.launch()



if __name__ == "__main__":
    run()