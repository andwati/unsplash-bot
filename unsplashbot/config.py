import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

BASE_URL = "https://api.unsplash.com"
