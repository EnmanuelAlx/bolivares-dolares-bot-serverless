from scrapper import BCVScrapper
from scrapper.models import PriceCalculator


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