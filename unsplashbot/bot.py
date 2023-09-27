import requests
import telebot
from config import ACCESS_TOKEN, BASE_URL, TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Hello, I'm a bot!")


@bot.message_handler(commands=["random"])
def get_random_photo(message):
    url = "https://api.unsplash.com/photos/random"
    response = requests.get(
        url, timeout=10, headers={"Authorization": f"Client-ID {ACCESS_TOKEN}"}
    )
    data = response.json()
    image_url = data["urls"]["regular"]
    description = data["alt_description"]
    image_content = requests.get(image_url)

    bot.send_photo(message.chat.id, image_content.content, caption=description)


bot.infinity_polling()
