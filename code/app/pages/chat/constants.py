import os

from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.environ.get("OPEN_AI_API_KEY", "API_KEY")