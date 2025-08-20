# Default config; can be overridden via file or env vars
AI_PROVIDER = 'xai'  # Or 'openai', etc.
API_KEY = None  # Set via env var for security
DEFAULT_PROMPT = "Generate a concise Git commit message for these changes: {diff}"
MAX_MESSAGE_LENGTH = 72  # Conventional commit style