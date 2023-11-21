import os

API_ID = API_ID = 12606917

API_HASH = os.environ.get("API_HASH", "f25113b8c17dca6fa7abda53a86bd4f7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6705040975:AAF2JquHwnfwXb0Ks_YzsBtCnSNjVwqWY0o")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5318243282))

LOG = -1001699711548

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6462391456").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


