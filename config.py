import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "JANEMAN")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/c887aa840fa0380159a2e.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/c887aa840fa0380159a2e.jpg")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/c887aa840fa0380159a2e.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/c887aa840fa0380159a2e.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c887aa840fa0380159a2e.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "@JANEMAN_OPX_BOT)
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "JANEMAN_ASSISTANT")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "INDIAN_NETWORK_OP)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "INDIAN_NETWORK_OFFICIAL)
OWNER_NAME = getenv("OWNER_NAME", "MR_X_OP_BOLTE) # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
