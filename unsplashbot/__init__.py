from flask import Flask

from unsplashbot.config import TELEGRAM_TOKEN

app = Flask(__name__)

WEBHOOK_URL_PATH = "/{}".format(TELEGRAM_TOKEN)
