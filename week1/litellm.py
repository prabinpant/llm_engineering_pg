import os
from dotenv import load_dotenv
from litellm import completion

response = completion(
    model="gemini/gemini-2.5-flash",
    prompt="Explain advanced prompting techniques in LLMs."
)