"""
LiteLLM Example - Calling models through a unified interface
"""
import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()


def run():
    """Main function to run this practice module"""
    response = completion(
        model="gemini/gemini-2.5-flash",
        messages=[
            {"role": "user", "content": "Explain advanced prompting techniques in LLMs."}
        ],
    )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    run()