import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6130457410:AAG8jDlWwyFQv1-u8XYnpDhtXaliPo3YrEY")

API_ID = int(os.environ.get("API_ID", "29616312"))

API_HASH = os.environ.get("API_HASH", "dd1a05ab4c47a5a037cc067cf4bded27")

PICS = os.environ.get("PICS", "https://telegra.ph/file/34fd203eb89fd747ffb57.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5190902724').split()]

DB_URL = os.environ.get("DB_URL", "mongodb+srv://ronoxe1308:nulcnaRvqNC5uty@rename-telegram-bot-log.clbv64f.mongodb.net/?retryWrites=true&w=majority")

DB_NAME = os.environ.get("DB_NAME", "tg-multi-bot")

RemoveBG_API = os.environ.get("RemoveBG_API", "sFvSnp6KmgGi7pWDNp4sfn5P")

FORCE_SUB = os.environ.get("FORCE_SUB", -1001785446911)           

HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "a9c33765-4ce7-406a-9ce4-82c5eb502a90")
 
log_channel = environ.get("LOG_CHANNEL" , default="-1001924268233")

LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None

LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""












