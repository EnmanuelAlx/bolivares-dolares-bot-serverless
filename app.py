import asyncio
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
    path = event.get("requestPath") or event.get("resource")
    method = event.get("httpMethod") or event.get("method")
    logger.info("El path es: {} y el method es {}".format(path, method))
    if path == "/set_webhook" and method == "POST":
        logger.info("Setting webhook")
        return set_webhook(event)
    elif method == "POST" and event.get("body"):
        logger.info("Getting Message")
        tg_bot = TelegramBot()
        logger.info("Message received")
        body = event.get("body")
        response = asyncio.run(tg_bot.get_response(body))
        logger.info("Message sent")
        logger.info(response)
    elif path == "/health-check" and method == "GET":
        logger.info("Health check")
        return OK_RESPONSE

    return OK_RESPONSE


def set_webhook(event):
    """
    Sets the Telegram bot webhook.
    """

    logger.info("Event: {}".format(event))
    bot = TelegramBot()
    url = "https://{}/{}/".format(
        event.get("headers").get("Host"),
        event.get("stage"),
    )
    webhook = asyncio.run(bot.set_webhook(url))
    logger.info("webhook: {}".format(webhook))
    if webhook:
        return OK_RESPONSE

    return ERROR_RESPONSE
