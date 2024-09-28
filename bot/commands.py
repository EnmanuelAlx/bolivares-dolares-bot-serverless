from abc import ABC, abstractmethod

from scrapper import BCVScrapper
from scrapper.models import PriceCalculator


class AbstractCommand(ABC):

    @abstractmethod
    def command(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def help_text(self) -> str:
        raise NotImplementedError

    @abstractmethod
    async def execute(self, arguments: list) -> str:
        raise NotImplementedError


class DefaultCommand(AbstractCommand):

    def command(self) -> str:
        return ""

    def help_text(self) -> str:
        return "A command that is not found"

    async def execute(self, _) -> str:
        return "Command not found"


class StartCommand(AbstractCommand):

    def command(self) -> str:
        return "/start"

    def help_text(self) -> str:
        return f"""
{self.command()}: Comando de inicio del bot
Ejemplo: {self.command()}
"""

    async def execute(self, _) -> str:
        return """
Hola, soy un bot que te ayuda a calcular el precio del dolar en Bs.
Para ver los comandos disponibles usa /help
"""


class BCVCommand(AbstractCommand):

    def command(self) -> str:
        return "/bcv"

    def help_text(self) -> str:
        return f"""
{self.command()}: Comando para obtener el precio del dólar en bolívares a tasa del Banco Central de Venezuela .
Ejemplo: {self.command()} 10 20 30
"""

    async def execute(self, arguments: list) -> str:
        scrapper = BCVScrapper()
        price = scrapper.get_dollar_price()
        calculator = PriceCalculator(currency_price=price)
        rate_change = calculator.from_usd_to_bs(arguments)
        message = ""
        if len(arguments) > 1:
            sum_amounts = calculator.sum_amounts(arguments)
            message = f"La suma de tus montos es: {sum_amounts}$ \n"
        message += f"El precio del dolar es: {price} \nAl cambio sería: Bs.{rate_change}"
        return message


class BSCommand(AbstractCommand):

    def command(self) -> str:
        return "/bs"

    def help_text(self) -> str:
        return f"""
{self.command()}: Comando para transformar el precio de bolivares a dolares a tasa del Banco Central de Venezuela .
Ejemplo: {self.command()} 365 423 342
"""

    async def execute(self, arguments: list) -> str:
        scrapper = BCVScrapper()
        price = scrapper.get_dollar_price()
        calculator = PriceCalculator(currency_price=price)
        rate_change = calculator.from_bs_to_usd(arguments)
        message = ""
        if len(arguments) > 1:
            sum_amounts = calculator.sum_amounts(arguments)
            message = f"La suma de tus montos es: {sum_amounts}$ \n"
        message += f"El precio del dolar es: {price} \nAl cambio sería: ${rate_change}"
        return message


class ManualCommand(AbstractCommand):

    def command(self) -> str:
        return "/manual"

    def help_text(self) -> str:
        return f"""
{self.command()}: Comando para calcular el precio del dólar en bolívares con una tasa elegida por el usuario.
Ejemplo: {self.command()} 40 10 15, donde el 40 es la tasa de cambio
"""

    async def execute(self, arguments: list) -> str:
        rate, *amounts = arguments
        calculator = PriceCalculator(currency_price=rate)
        rate_change = calculator.from_usd_to_bs(amounts)
        message = ""
        if len(amounts) > 1:
            sum_amounts = calculator.sum_amounts(amounts)
            message = f"La suma de tus montos es: {sum_amounts}$ \n"
        message += f"Tu precio del dólar es: {rate} \nAl cambio sería: {rate_change} Bs"
        return message


class HelpCommand(AbstractCommand):

    def command(self) -> str:
        return "/help"

    def format_commands(self, commands: list[AbstractCommand]) -> str:
        formatted_commands = []
        for command in commands:
            # Remove the leading dash and space
            formatted_command = command.help_text().lstrip("- ").strip()
            formatted_commands.append(formatted_command)
        return "\n\n".join(formatted_commands)

    def help_text(self) -> str:
        return "Los comandos disponibles son:"

    async def execute(self, _) -> str:
        commands = [BCVCommand(), BSCommand(), ManualCommand(), StartCommand()]
        return f"""
{self.help_text()}

{self.format_commands(commands)}
"""


command_list = [
    StartCommand(),
    BCVCommand(),
    BSCommand(),
    HelpCommand(),
    ManualCommand(),
]
