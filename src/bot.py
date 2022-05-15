import os

import requests
import telebot
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TELEGRAM_TOKEN"))

# remove previous webhook
bot.remove_webhook()

# configure the webhook for the bot
bot.set_webhook(
    "https://{}.herokuapp.com/{}".format(
        os.getenv("PROJECT_NAME"), os.getenv("TELEGRAM_TOKEN")
    )
)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    """
    handle triggered by the /start command
    """
    bot.reply_to(message, "hi there")


@bot.message_handler(commands=["random"])
def send_random_pic(message):
    """
    send a random picture
    """
    response = requests.get("https://source.unsplash.com/random")
    bot.send_photo(message.chat.id, response.content)


@bot.message_handler(commands=["4k"])
def send_random_4k_pic(message):
    """
    send random 4k unsplash picture
    """
    response = requests.get("https://source.unsplash.com/random/4096x2160")
    bot.send_photo(message.chat.id, response.content)
    bot.send_document(message.chat.id, response.content, caption="rename_to_jpeg")


@bot.message_handler(commands=["topic"])
def handle_text(message):
    """
    request the user to send the topics
    """
    chat_id = message.chat.id
    message_topics = bot.send_message(
        chat_id, "Type the topic(s) separated with commas"
    )
    bot.register_next_step_handler(message_topics, step_set_topics)


def step_set_topics(message):
    """
    get images according to topics
    """
    chat_id = message.chat.id
    topics = message.text
    response = requests.get("https://source.unsplash.com/random?{0}".format(topics))
    bot.send_photo(chat_id, response.content)
