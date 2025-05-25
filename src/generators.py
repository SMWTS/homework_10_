from typing import Any, Generator, Iterator, Optional


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    for item in transactions:
        if item.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
            yield item

    filter_curr = filter_by_currency(transactions, "USD")
    print(next(filter_curr))


def transaction_descriptions(operation: list[dict[str, Any]]) -> Iterator[Optional[str]]:
    """Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
    count_transaction = len(operation)
    if count_transaction == 0:
        yield "Нет транзакций"
        return

    for dict_ in operation:
        if "description" not in dict_.keys() or count_transaction == 0:
            yield "Нет транзакции или описания транзакции!"
            return

        yield dict_.get("description")


# Вывод функции
transaction: list = []

count_transactions = len(transaction)
descriptions = transaction_descriptions(transaction)
for description in descriptions:
    print(description)


def card_number_generator(start: int, stop: int) -> Generator[Any, Any, None]:
    """Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    start_card_number = "0000000000000000"
    nums = (num for num in range(start, stop + 1))
    for num in nums:
        card_number = start_card_number[: -len(str(num))] + str(num)
        if len(card_number) > 16:
            raise ValueError("В номере карты не может быть больше 16 цифр")
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
