import logging
from dataclasses import dataclass
from datetime import datetime
from decimal import ROUND_HALF_EVEN, Decimal

import requests
from bs4 import BeautifulSoup

from scrapper.constants import BCV_URL
from scrapper.exceptions import CurrencyNotFoundException

log = logging.getLogger(__name__)


@dataclass
class Scrapper:
    url: str

    def __post_init__(self):
        self.update_soup()

    def update_soup(self):
        response = requests.get(self.url)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.content, "html.parser")


@dataclass
class BCVScrapper(Scrapper):
    def __init__(self, *args, **kwargs):
        self.url = BCV_URL
        super().__init__(url=self.url)

    def __process_currency(self, currency: str):
        text_currency = currency.strip()
        text = text_currency.replace(",", ".")
        decimal_number = Decimal(text)
        return decimal_number.quantize(
            Decimal("0.001"), rounding=ROUND_HALF_EVEN
        )

    def __get_currency_by_id(self, currency) -> Decimal:
        currency = self.soup.find(id=currency)
        if not currency:
            raise CurrencyNotFoundException(currency)
        currency = currency.strong.get_text()  # type: ignore
        return self.__process_currency(currency)

    def get_dollar_price(self):
        return self.__get_currency_by_id("dolar")
