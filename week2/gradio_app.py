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

system_message = "You are a helpful assistant that answers questions about LLM engineering."


def message_chat(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            system_instruction=system_message,
        ),
    )
    return response.text

def shout(text):
    print(f"Shout has been called with input: {text}")
    return text.upper()

def run():
    print(shout('test'))
    
    gr.Interface(fn=shout, inputs="textbox", outputs="textbox", flagging_mode="never").launch()
    # result = message_chat("What are some best practices for prompt engineering?")
    # print(result)
 


if __name__ == "__main__":
    run()