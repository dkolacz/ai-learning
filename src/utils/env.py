from __future__ import annotations
from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path

def load_env(verbose: bool = False) -> str:
    env_path = find_dotenv(filename=".env", usecwd=True)
    if not env_path:
        raise RuntimeError("Couldn't find a .env file. Create one in the project root.")
    load_dotenv(env_path, override=True)
    if verbose:
        print(f"Loaded .env from: {Path(env_path).resolve()}")
    return env_path

def require(name: str) -> str:
    load_env()
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}. Set it in .env")
    return value

