# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "27114060"))
API_HASH = getenv("API_HASH", "9c25bf87849e886ef437d94f8f3f956f")
BOT_TOKEN = getenv("BOT_TOKEN", "7278911043:AAFkhKG2lL7UUbxP1-1EnIGxsnQtgu7w0zM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6169288210").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://wiki:wiki@cluster0.17fai.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
