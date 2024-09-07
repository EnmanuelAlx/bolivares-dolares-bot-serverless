import asyncio
import json
import logging

from bot import TelegramBot
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

    tg_bot = TelegramBot()
    logger.info("Message received")
    body = event.get("body")
    response = asyncio.run(tg_bot.get_response(body))
    logger.info("Message sent")
    logger.info(response)

    return OK_RESPONSE


def set_webhook(event, context):
    """
    Sets the Telegram bot webhook.
    """

    logger.info("Event: {}".format(event))
    bot = TelegramBot()
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
