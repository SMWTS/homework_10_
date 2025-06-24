from src.process_bank import filter_operations_by_description, process_bank_operations

# Пример данных для тестирования
sample_data = [
    {"description": "Перевод с карты на карту", "amount": "130 USD", "status": "EXECUTED"},
    {"description": "Открытие вклада", "amount": "40542 руб.", "status": "EXECUTED"},
    {"description": "Перевод организации", "amount": "8390 руб.", "status": "CANCELED"},
    {"description": "Перевод со счета на счет", "amount": "8200 EUR", "status": "PENDING"},
]

categories = ["перевод", "вклад", "организация"]


def test_filter_operations_by_description_found()-> None:
    result = filter_operations_by_description(sample_data, "перевод")
    assert len(result) == 3
    for op in result:
        assert "перевод" in op["description"].lower()


def test_filter_operations_by_description_not_found() -> None:
    result = filter_operations_by_description(sample_data, "несуществующее слово")
    assert result == []


def test_filter_operations_by_description_case_insensitive()-> None:
    result_upper = filter_operations_by_description(sample_data, "ПЕРЕВОД")
    result_mixed = filter_operations_by_description(sample_data, "ПерЕвОд")
    assert len(result_upper) == len(result_mixed) == 3


def test_process_bank_operations_counts()-> None:
    result = process_bank_operations(sample_data, categories)
    # Проверяем, что категории подсчитаны правильно
    assert result["перевод"] == 3
    assert result["вклад"] == 1


def test_process_bank_operations_no_matches()-> None:
    # Категории, которых нет в описаниях
    result = process_bank_operations(sample_data, ["несуществующая категория"])
    assert result == {"несуществующая категория": 0} or result == {}


def test_process_bank_operations_partial_match()-> None:
    # Проверка, что только совпадающие категории считаются
    categories_test = ["перевод", "вклад"]
    result = process_bank_operations(sample_data, categories_test)
    assert result["перевод"] == 3
    assert result["вклад"] == 1
