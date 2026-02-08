import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display

load_dotenv()

def run():

    print("Running advanced prompting techniques practice...")
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is not set")
    
    gemini = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=api_key
    )
    
    response = gemini.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain advanced prompting techniques in LLMs."}
        ]
    )
    
    content = response.choices[0].message.content

    try:
        display(Markdown(content))
    except Exception:
        pass

    print("\n--- Response ---\n")
    print(content)

if __name__ == "__main__":
    run()