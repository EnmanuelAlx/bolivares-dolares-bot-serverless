import json
import logging

import telegram

from bot import init_bot
from bot.responses import ERROR_RESPONSE, OK_RESPONSE

# Logging is cool!
logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
logging.basicConfig(level=logging.INFO)


def webhook(event, context):
    """
    Runs the Telegram webhook.
    """

    bot = init_bot()
    logger.info("Event: {}".format(event))

    if event.get("httpMethod") == "POST" and event.get("body"):
        logger.info("Message received")
        update = telegram.Update.de_json(json.loads(event.get("body")), bot)
        chat_id = update.message.chat.id
        text = update.message.text

        if text == "/start":
            text = """Hello, human! I am an echo bot, built with Python and the Serverless Framework.
            You can take a look at my source code here: https://github.com/jonatasbaldin/serverless-telegram-bot.
            If you have any issues, please drop a tweet to my creator: https://twitter.com/jonatsbaldin. Happy botting!"""

        bot.sendMessage(chat_id=chat_id, text=text)
        logger.info("Message sent")

        return OK_RESPONSE

    return ERROR_RESPONSE


def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info("Event: {}".format(event))
    bot = init_bot()
    url = "https://{}/{}/".format(
        event.get("headers").get("Host"),
        event.get("requestContext").get("stage"),
    )
    webhook = bot.set_webhook(url)

    if webhook:
        return OK_RESPONSE

    return ERROR_RESPONSE


def health_check(self, _):
    return OK_RESPONSE
