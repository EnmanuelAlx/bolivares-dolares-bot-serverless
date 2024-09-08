from bot.constants import HELP_STRING, START_STRING
from scrapper import BCVScrapper
from scrapper.models import PriceCalculator


async def default_command(_) -> str:
    return "Command not found"


async def start(arguments: list) -> str:
    return START_STRING


async def help(_) -> str:
    return HELP_STRING


async def bcv(arguments: list) -> str:
    scrapper = BCVScrapper()
    price = scrapper.get_dollar_price()
    calculator = PriceCalculator(currency_price=price)
    rate_change = calculator.calculate_price(arguments)
    message = ""
    if len(arguments) > 1:
        sum_amounts = calculator.sum_amounts(arguments)
        message = f"La suma de tus montos es: {sum_amounts}$ \n"
    message += (
        f"El precio del dolar es: {price} \nAl cambio sería: {rate_change} Bs"
    )
    return message
