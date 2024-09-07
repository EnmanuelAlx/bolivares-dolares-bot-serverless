import logging
import os
import telegram

logger = logging.getLogger()


def init_bot():
    """
    Configures the bot with a Telegram Token.

    Returns a bot instance.
    """

    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    if not TELEGRAM_TOKEN:
        logger.error("The TELEGRAM_TOKEN must be set")
        raise NotImplementedError

    return telegram.Bot(TELEGRAM_TOKEN)
