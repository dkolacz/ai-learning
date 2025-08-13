from dotenv import load_dotenv
from pathlib import Path
import os

def load_env():
    """Load environment variables from the project root .env file."""
    root = Path(__file__).resolve().parents[1]  # project root
    load_dotenv(dotenv_path=root / ".env")

def require(name: str) -> str:
    """Get an env var or raise an error if it's missing."""
    load_env()
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}. Set it in .env")
    return value
