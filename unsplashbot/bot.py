import requests
import telebot
from config import ACCESS_TOKEN, BASE_URL, TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Hello, I'm a bot!")


@bot.message_handler(commands=["random"])
def get_random_photo(message):
    url = f"{BASE_URL}/photos/random"
    response = requests.get(
        url, timeout=10, headers={"Authorization": f"Client-ID {ACCESS_TOKEN}"}
    )
    data = response.json()
    image_url = data["links"]["download"]
    description = data["alt_description"]
    image_content = requests.get(image_url)

    bot.send_photo(message.chat.id, image_content.content, caption=description)


# send random 4k unsplash picture
@bot.message_handler(commands=["4k"])
def send_random_pic(message):
    response = requests.get("https://source.unsplash.com/random/4096x2160")
    bot.send_photo(message.chat.id, response.content)
    bot.send_document(message.chat.id, response.content, caption="rename_to_jpeg")


bot.infinity_polling()
