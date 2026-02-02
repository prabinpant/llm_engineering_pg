import os
import json
from dotenv import load_dotenv
from IPython.display import display, Markdown, update_display
from scraper import fetch_website_links, fetch_website_contents
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/", api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    print("Hello from w1d4-brochure-generator!")

    website_links = fetch_website_links("https://www.carelogix.com.au")
    print(website_links)

    website_contents = fetch_website_contents("https://www.carelogix.com.au")
    print(website_contents)

if __name__ == "__main__":
    main()