import os
from typing import Any

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()
# импортируем API_KEY из .env-файла
API_KEY = os.getenv("API_KEY")


def get_the_transaction_amount(transaction: dict) -> Any:
    """Функция принимает транзакцию и возвращает ее сумму. Если в транзакции валюта не является рублями,
    то функция конвертирует ее в рубли"""
    # получение суммы транзакции по ключу "amount"
    amount = transaction["operationAmount"]["amount"]
    # получение кода валюты по ключу "code"
    currency = transaction["operationAmount"]["currency"]["code"]
    # валюта в которую будет производиться конвертация - рубли
    currency_rub = "RUB"

    # ели код транзакции не рубль то обращаемся к конвертации валюты в рубли
    if currency != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_rub}&from={currency}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.request("GET", url, headers=headers)
        status_code = response.status_code
        result = response.json()
        if status_code == 200:
            return result["result"]
        else:
            return f"Запрос не был успешным.\nКод ошибки: {status_code}.\nОписание ошибки: {result}."
    else:
        return amount


def get_currency_usd_or_euro(transaction: dict) -> str | None | Any:


    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        rub = "RUB"
        amounts = float(transaction["operationAmount"]["amount"])
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={currency}&amount={amounts}"

        payload = {}
        headers = {
            "apikey": API_KEY
            }
        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        if status_code == 200:
            try:
                result = response.json()
                return result["result"]
            except requests.exceptions.RequestException as e:
                return f'Проблема с сервером{e}'
        return None
    except Exception as e:
        return f"Произошла ошибка с подключением"





def convert_to_rub(transaction: dict) -> float | None:
    if not isinstance(transaction, dict):
        print("Ошибка: transaction не является словарем.")
        return None

    if not transaction:
        print("Словарь пуст.")
        return None

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return transaction["operationAmount"]["amount"]
    else:
        return get_currency_usd_or_euro(transaction)