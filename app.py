import asyncio
import logging

from bot import TelegramBot
from bot.responses import OK_RESPONSE

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
    if method == "POST" and event.get("body"):
        logger.info("Getting Message")
        tg_bot = TelegramBot()
        logger.info("Message received")
        body = event.get("body")
        response = asyncio.run(tg_bot.get_response(body), debug=True)
        logger.info("Message sent")
        logger.info(response)
    elif path == "/health-check" and method == "GET":
        logger.info("Health check")
        return OK_RESPONSE

    return OK_RESPONSE
