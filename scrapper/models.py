import re
from dataclasses import dataclass
from decimal import ROUND_HALF_EVEN, Decimal
from typing import Optional

from scrapper.exceptions import NotValidAmount


@dataclass
class PriceCalculator:
    currency_price: Decimal | str

    def __post_init__(self):
        if type(self.currency_price) == str:
            self.currency_price = self.validate_amounts([self.currency_price])[
                0
            ]

    def validate_amounts(self, amounts: list[str]):
        decimal_pattern = re.compile(r"^\d+(\.\d+)?$")
        decimal_amounts = []
        for amount in amounts:
            amount = amount.replace(",", ".")
            if not decimal_pattern.match(amount):
                raise NotValidAmount(amount)
            decimal_amounts.append(Decimal(amount))
        return decimal_amounts

    def sum_amounts(self, amounts: list):
        return sum(self.validate_amounts(amounts))

    def from_usd_to_bs(self, amounts: list[str]):
        amounts_parsed = self.validate_amounts(amounts)
        return sum(amounts_parsed) * self.currency_price

    def from_bs_to_usd(self, amounts: list[str]):
        amounts_parsed = self.validate_amounts(amounts)
        return self.round(
            Decimal(sum(amounts_parsed)) / self.currency_price  # type: ignore
        )

    def round(self, amount: Decimal, decimals: Optional[int] = None):
        decimals = decimals or 3
        return amount.quantize(
            Decimal(f"1e-{decimals}"), rounding=ROUND_HALF_EVEN
        )
