import os

api_id = 28088290
api_hash = os.environ.get("API_HASH", "6998f2c585fdce65ac72dfa23d02b6ec")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5850397219")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5850397219")
owner_users = [int(num) for num in osowner_users.split(",")]
