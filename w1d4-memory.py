import os
from dotenv import load_dotenv

load_dotenv(override=True)

api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set")


