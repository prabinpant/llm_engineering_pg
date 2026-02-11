"""Week 2 - Gradio Chat App with Google Gemini (OpenAI-compatible client)"""

import json
import os
from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI

# -------------------- Setup --------------------

load_dotenv()

MODEL = "gemini-2.5-flash"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url=GEMINI_BASE_URL,
)

system_message = (
    "You are a helpful assistant for an Airline called FlightAI. "
    "Give short, courteous answers, no more than 1 sentence. "
    "If you dont know the answer, say so. "
    "You have access to the tool get_ticket_price. "
    "Use it to return the ticket price for a city directly."
)

# -------------------- Data --------------------

ticket_prices = {
    "New York": 200,
    "Los Angeles": 300,
    "Chicago": 250,
    "Houston": 225,
    "Miami": 350,
}

# -------------------- Tool --------------------

def get_ticket_price(city: str):
    print(f"[TOOL] Getting ticket price for {city}")
    return ticket_prices.get(city, "Unknown city")

price_function = {
    "name": "get_ticket_price",
    "description": "Get the ticket price for a given city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string"}
        },
        "required": ["city"],
        "additionalProperties": False,
    },
}

tools = [{"type": "function", "function": price_function}]

# -------------------- Tool Executor --------------------

def handle_tool_calls(msg):
    responses = []

    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments)
        result = get_ticket_price(args["city"])

        responses.append({
            "role": "tool",
            "tool_call_id": tc.id,
            "content": str(result),
        })

    return responses

# -------------------- Chat Handler --------------------

def message_chat(message, history):
    messages = [{"role": "system", "content": system_message}]

    # ✅ SAFE history handling (works for all Gradio versions)
    for h in history or []:
        if isinstance(h, (list, tuple)) and len(h) == 2:
            messages.append({"role": "user", "content": h[0]})
            messages.append({"role": "assistant", "content": h[1]})
        elif isinstance(h, dict):
            messages.append({
                "role": h.get("role", "user"),
                "content": h.get("content", "")
            })

    messages.append({"role": "user", "content": message})

    # First LLM call
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    choice = response.choices[0]

    # Tool call path
    if choice.finish_reason == "tool_calls":
        messages.append({
            "role": "assistant",
            "tool_calls": choice.message.tool_calls,
        })

        messages.extend(handle_tool_calls(choice.message))

        # Second LLM call (tool results)
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
        )

    return response.choices[0].message.content

# -------------------- UI --------------------

def run():
    gr.ChatInterface(
        fn=message_chat,
        title="✈️ FlightAI",
        description="Ask for ticket prices by city",
    ).launch()

if __name__ == "__main__":
    run()
