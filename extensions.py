import requests
import json
from config import keys


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote, base, amount):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote.casefold()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base.casefold()]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={quote_ticker} &from={base_ticker} &amount = {amount}"
        headers = {"apikey": "5748HRIEOVAwbd40Axw1JX7ya96DGrmL"}
        response = requests.request("GET", url, headers=headers)
        r = json.loads(response.text)
        text = f"Стоимость {amount} {base} в {quote} - {r['result']}"
        return text
