from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Working test
def test_final_value_card_number_generator() -> None:
    """Код проверяет, что генератор выдает ожидаемые значения, и затем проверяет, что после них действительно возникает StopIteration"""
    generator_card = card_number_generator(1, 2)
    assert next(generator_card) == "0000 0000 0000 0001"
    assert next(generator_card) == "0000 0000 0000 0002"
    with pytest.raises(StopIteration):
        next(generator_card)


# Working test
@pytest.mark.parametrize(
    "start, end, result",
    [(1, 5, "0000 0000 0000 0001"), (10, 12, "0000 0000 0000 0010"), (1012, 1015, "0000 0000 0000 1012")],
)
def test_card_number_generator_1(start: int, end: int, result: str) -> None:
    gen = card_number_generator(start, end)
    # Проверяем первый результат
    assert next(gen) == result


# Working test
@pytest.mark.parametrize(
    "start, end, first_card, end_card",
    {
        (1, 4, "0000 0000 0000 0001", "0000 0000 0000 0004"),
        (15, 30, "0000 0000 0000 0015", "0000 0000 0000 0030"),
        (5956132884514579, 5956132884514589, "5956 1328 8451 4579", "5956 1328 8451 4589"),
    },
)
def test_card_number_generator_2(start: int, end: int, first_card: str, end_card: str) -> None:
    result = list(card_number_generator(start, end))
    assert result[0] == first_card
    assert result[-1] == end_card
    assert len(result) == end - start + 1


# Working test
def test_without_code(sample_filter_without_code: list) -> None:
    result = list(filter_by_currency(sample_filter_without_code, "USD"))
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    assert result == expected


# Working test
def test_missing_currency(sample_filter_without_code: list[dict]) -> None:
    result = list(filter_by_currency(sample_filter_without_code, "USD"))
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    assert result == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        ([], ["Нет транзакций"]),  # пустой список
        ([{"description": "Перевод организации"}], ["Перевод организации"]),
        (
            [{"description": "Перевод с карты на счет"}, {"description": "Перевод организации"}],
            ["Перевод с карты на счет", "Перевод организации"],
        ),
    ],
)
def test_transaction_descriptions(transactions: list[dict[str, Any]], expected: str) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == expected
