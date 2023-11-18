import os

API_ID = API_ID = 28031075

API_HASH = os.environ.get("API_HASH", "6443392317:6a309d42eda281416f798a554360e6a8")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443392317:AAFrtUcMDsuoFK4p1_JMkJgebF4m9hTILHI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5829511291))

LOG = -1002140062103

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6462391456").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


