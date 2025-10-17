# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "26342348"))
API_HASH = getenv("API_HASH", "aac8f8c983c97a08db79ece3eee2b9be"")
BOT_TOKEN = getenv("BOT_TOKEN", "8435242917:AAEzdr_7i00nxdNqBj6azNLOX91EocFIPiM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1365883451").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Ansh089:Ansh089@cluster0.y8tpouc.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-4975202471")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1003077530022"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
