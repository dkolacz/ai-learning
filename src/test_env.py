from utils.env import require

OPENAI_API_KEY = require("OPENAI_API_KEY")
print("✅ Loaded key:", OPENAI_API_KEY[:8] + "...")
