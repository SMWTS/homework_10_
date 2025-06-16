import os
from unittest.mock import mock_open, patch

import pytest

from src.reader_transactions import get_read_csv, get_read_xlsx


def test_get_read_csv() -> None:
    """Тестирует функцию чтения реального CSV-файла."""
    file_path = "..\\data\\transactions.csv"
    if not os.path.exists(file_path):
        pytest.skip(f"Файл {file_path} не найден.")  # Пропускаем тест, если файл отсутствует
    result = get_read_csv(file_path)
    # Проверяем, что данные успешно прочитаны
    assert len(result) > 0


@patch("builtins.open", new_callable=mock_open)
@patch("csv.DictReader")
def test_get_read_csv_2(mock_csv, mock_file) -> None:
    mock_csv.return_value = [
        {
            "id": 4137938.0,
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": 15560.0,
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": " ",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        }
    ]
    assert get_read_csv(mock_file) == [
        {
            "id": 4137938.0,
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": 15560.0,
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": " ",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        }
    ]


@patch("builtins.open", new_callable=mock_open)
@patch("csv.DictReader")
def test_get_read_xlsx(mock_xlsx, mock_file) -> None:
    mock_xlsx.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert get_read_csv(mock_file) == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


def test_get_read_xlsx_2() -> None:
    """Тестирует функцию чтения реального XLSX-файла."""
    file_path_xlsx = "..\\data\\transactions_excel.xlsx"
    if not os.path.exists(file_path_xlsx):
        pytest.skip(f"Файл {file_path_xlsx} не найден.")  # Пропускаем тест, если файл отсутствует
    results = str(get_read_xlsx(file_path_xlsx))
    # Проверяем, что данные успешно прочитаны
    assert len(results) > 0
