import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


START_STRING = """Hola, soy un bot que te ayuda a calcular el precio del dolar en Bs.
Para ver los comandos disponibles usa /help
"""

HELP_STRING = """
Los comandos disponibles son:
- /bcv <monto1> <monto2> ... <montoN>
- /help
"""
