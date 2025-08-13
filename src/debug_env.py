from utils.env import load_env, require
import os

# Load the .env and print where it came from
path = load_env(verbose=True)

# Check if the key is loaded into the environment
print("Has OPENAI_API_KEY?", "OPENAI_API_KEY" in os.environ)

# Show the first few characters of the key (safety: not full key)
print("Key preview:", require("OPENAI_API_KEY")[:8] + "...")
