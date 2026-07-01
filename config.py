aiogram==3.4.1
python-dotenv==1.0.1


import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
