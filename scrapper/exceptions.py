class CurrencyNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        message = f"Currency not found: {args}"
        super().__init__(message)


class NotValidAmount(Exception):
    def __init__(self, *args: object) -> None:
        message = f"Amounts must be a valid number: {args}"
        super().__init__(message)
