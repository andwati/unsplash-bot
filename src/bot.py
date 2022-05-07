from os import environ

import requests
import telebot

bot = telebot.TeleBot(environ["TELEGRAM_TOKEN"])


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """
    handle triggered by the /start command
    """
    bot.reply_to(message, "hi there")


# configure the webhook for the bot
bot.set_webhook(
    "https://{}.herokuapp.com/{}".format(
        environ["PROJECT_NAME"], environ["TELEGRAM_TOKEN"]
    )
)
