from typing import Callable

import telegram

from bot import commands
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
            "/start": commands.start,
            "/bcv": commands.bcv,
        }

    def _get_commands(self, command: str) -> Callable:
        return self.commands.get(command, commands.default_command)

    async def get_response(self, json) -> str:
        try:
            update = telegram.Update.de_json(json, self.bot)
            message = update.message.text
            command, *arguments = message.split(" ")
            chat_id = update.message.chat.id
            response = await self._get_commands(command)(arguments)
            await self.bot.send_message(chat_id=chat_id, text=response)
        except Exception as e:
            response = str(e)
        return response

    async def set_webhook(self, url: str) -> bool:
        return await self.bot.set_webhook(url)
