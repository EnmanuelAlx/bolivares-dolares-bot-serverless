from typing import Callable

import telegram

from bot.commands import bcv
from bot.constants import TELEGRAM_TOKEN


class TelegramBot:
    def __init__(self) -> None:
        print(TELEGRAM_TOKEN)
        assert TELEGRAM_TOKEN, "The TELEGRAM_TOKEN must be set"
        self.bot = telegram.Bot(TELEGRAM_TOKEN)
        self.command = None
        self.arguments = []
        self.commands = self.__set_commands()

    def __set_commands(self) -> dict[str, Callable]:
        return {
            "/start": lambda _: "Hola, soy un bot que te ayuda a calcular el precio del dolar en Bs",
            "/bcv": bcv,
        }

    def _get_commands(self, command: str) -> Callable:
        return self.commands.get(command, lambda _: "Command not found")

    async def get_response(self, json) -> str:
        update = telegram.Update.de_json(json, self.bot)
        message = update.message.text
        command, *arguments = message.split(" ")
        chat_id = update.message.chat.id
        response = self._get_commands(command)(arguments)
        await self.bot.send_message(chat_id=chat_id, text=response)
        return response

    def set_webhook(self, url: str) -> None:
        self.bot.set_webhook(url)