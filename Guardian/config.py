import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN") or os.environ.get("BOT_TOKEN")

try:
    OWNER_ID = int(os.environ.get("OWNER_ID")) if os.environ.get("OWNER_ID") else 0
except (ValueError, TypeError):
    OWNER_ID = 0

try:
    SUDO_ID = list(map(int, os.environ.get("SUDO_ID", "").split())) if os.environ.get("SUDO_ID") else []
except (ValueError, TypeError):
    SUDO_ID = []

MONGO_URI = os.environ.get("MONGO_URI") or os.environ.get("MONGO_URL")
DB_NAME = os.environ.get("DB_NAME", "Guardian")
LOGGER = os.environ.get("LOGGER", "True") == "True"
BOT_NAME = os.environ.get("BOT_NAME", "Security & Edit Guardian Bot")
SIGHTENGINE_USER = os.environ.get("SIGHTENGINE_USER", "")
SIGHTENGINE_SECRET = os.environ.get("SIGHTENGINE_SECRET", "")

SUPPORT_ID = (
    os.environ.get("SUPPORT_ID") or 
    os.environ.get("LOGGER_ID") or 
    os.environ.get("OTHER_LOGS")
)
if SUPPORT_ID:
    SUPPORT_ID = SUPPORT_ID.strip().strip('"').strip("'")
    if SUPPORT_ID.startswith("https://t.me/"):
        SUPPORT_ID = "@" + SUPPORT_ID[len("https://t.me/"):]
    elif SUPPORT_ID.startswith("t.me/"):
        SUPPORT_ID = "@" + SUPPORT_ID[len("t.me/"):]
    
    try:
        if SUPPORT_ID.lstrip('-').isdigit():
            SUPPORT_ID = int(SUPPORT_ID)
    except (ValueError, TypeError):
        pass
else:
    SUPPORT_ID = None
