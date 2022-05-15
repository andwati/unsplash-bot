import flask
import telebot

from .bot import bot

app = flask.Flask(__name__)

WEBHOOK_URL_PATH = "/{}".format(bot.token)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Index page</h1>"


@app.route(WEBHOOK_URL_PATH, methods=["POST"])
def webhook():
    """
    sets the bot webhook
    """
    if flask.request.headers.get("content-type") == "application/json":
        json_string = flask.request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)

        bot.process_new_updates([update])
        return ""
    else:
        flask.abort(403)
