from dotenv import load_dotenv
import os
from pathlib import Path

# Load variables from the .env in the project root
load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("✅ Key loaded:", api_key[:7] + "..." + str(len(api_key)) + " chars")
else:
    raise RuntimeError(
        "OPENAI_API_KEY not found. Add it to your .env like:\n"
        "OPENAI_API_KEY=sk-xxx"
    )
